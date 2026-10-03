"""Kuveyt Türk ile müşteri girişi yapan örnek web uygulaması (Flask).

Authorization code akışının bir web uygulamasında nasıl kurulduğunu gösterir:

1. Ziyaretçi "Kuveyt Türk ile bağlan"a basar; ``/login`` onu bankanın giriş sayfasına yollar.
2. Müşteri bankada giriş yapıp izin verir; banka tarayıcıyı Redirect URI'ye geri yollar.
3. Callback rotası dönen ``code`` değerini token'a çevirir ve o ziyaretçi için saklar.
4. Sonraki sayfalar (hesaplar, hareketler) o ziyaretçinin token'ıyla API'yi çağırır.

Çalıştırma (proje kökünden)::

    pip install flask
    python examples/web_app/app.py

Uygulama, ``.env`` içindeki ``KUVEYTTURK_REDIRECT_URI`` adresinin portunda açılır ve callback'i
o adresin yolunda karşılar; bu adres portaldaki uygulamanızın Redirect URI'siyle aynı olmalıdır.
"""

from __future__ import annotations

import datetime as dt
import os
import secrets
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from flask import Flask, flash, redirect, render_template, request, session, url_for
from werkzeug.wrappers import Response

from kuveytturk_api import (
    APIError,
    AuthenticationError,
    AuthorizationRequiredError,
    FileTokenStore,
    KuveytTurk,
    KuveytTurkError,
)

ROOT = Path(__file__).resolve().parents[2]

#: Müşteriden istenen izinler. ``offline_access`` refresh token verilmesini sağlar; böylece
#: access token'ın bir saatlik süresi dolunca müşteri yeniden giriş yapmak zorunda kalmaz.
SCOPES = ["accounts", "offline_access"]


def create_client() -> KuveytTurk:
    """Uygulama boyunca kullanılacak tek istemci.

    Token'lar dosyada saklanır ki uygulama yeniden başlayınca girişler kaybolmasın. Gerçek bir
    uygulamada bunun yerine veritabanı/Redis kullanan kendi ``TokenStore``'unuzu verin.
    """
    return KuveytTurk.from_env(
        ROOT / ".env",
        token_store=FileTokenStore(ROOT / ".kuveytturk" / "web_tokens.json"),
    )


def create_app(kt: KuveytTurk | None = None) -> Flask:
    app = Flask(__name__)
    # Oturum çerezini imzalayan anahtar. Sabit bir değer verilmezse her başlatmada yenilenir
    # ve açık oturumlar düşer; canlıda FLASK_SECRET_KEY ile sabit ve gizli bir değer verin.
    app.secret_key = os.environ.get("FLASK_SECRET_KEY") or secrets.token_hex(32)
    app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax")

    client = kt if kt is not None else create_client()
    if not client.redirect_uri:
        raise RuntimeError("KUVEYTTURK_REDIRECT_URI tanımlı değil (.env dosyasına ekleyin).")
    callback_path = urlsplit(client.redirect_uri).path or "/"

    def visitor() -> str:
        """Bu tarayıcıyı tanıyan anahtar; müşterinin token'ı bu anahtarla saklanır.

        Kendi üyelik sisteminiz varsa burada rastgele bir değer yerine kullanıcı kimliğinizi
        kullanın. Token'ın kendisi asla tarayıcıya gönderilmez; çerezde yalnızca bu anahtar durur.
        """
        if "visitor" not in session:
            session["visitor"] = secrets.token_urlsafe(16)
        return str(session["visitor"])

    def connected() -> bool:
        return client.auth.get_user_token(user=visitor()) is not None

    @app.context_processor
    def inject() -> dict[str, Any]:
        return {"connected": connected(), "environment": client.environment.name}

    # ------------------------------------------------------------------ giriş akışı

    @app.get("/")
    def index() -> str:
        return render_template("index.html", scopes=SCOPES)

    @app.get("/login")
    def login() -> Response:
        # state: callback'in gerçekten bizim başlattığımız girişe ait olduğunu doğrular (CSRF).
        session["oauth_state"] = client.auth.new_state()
        return redirect(client.auth.authorization_url(SCOPES, state=session["oauth_state"]))

    @app.get(callback_path, endpoint="callback")
    def callback() -> Response | tuple[str, int]:
        expected_state = session.pop("oauth_state", None)
        if expected_state is None:
            return render_template(
                "error.html", message="Bu giriş isteği bu tarayıcıdan başlatılmadı."
            ), 400
        try:
            code = client.auth.parse_callback(request.url, state=expected_state)
            client.auth.exchange_code(code, user=visitor())
        except AuthenticationError as exc:
            # Müşteri izni reddetti, state uyuşmadı ya da kod geçersiz/süresi dolmuş.
            return render_template("error.html", message=str(exc)), 400
        flash("Hesabınız bağlandı.")
        return redirect(url_for("accounts"))

    @app.post("/logout")
    def logout() -> Response:
        client.auth.forget_user(user=visitor())
        session.clear()
        flash("Bağlantı kaldırıldı.")
        return redirect(url_for("index"))

    # ------------------------------------------------------------------ müşteri sayfaları

    @app.get("/accounts")
    def accounts() -> str:
        response = client.as_user(visitor()).tpp_accounts.account_list_v2()
        return render_template("accounts.html", accounts=response.get("accountList") or [])

    @app.get("/accounts/<int:suffix>/transactions")
    def transactions(suffix: int) -> str:
        days = max(1, min(request.args.get("days", default=30, type=int), 365))
        end = dt.date.today()
        begin = end - dt.timedelta(days=days)
        response = client.as_user(visitor()).tpp_accounts.account_transactions_v2(
            suffix=suffix, begin_date=begin, end_date=end, item_count=50
        )
        # Banka tarih filtresini her zaman uygulamadığı için aralık burada da uygulanır.
        activities = [
            activity
            for activity in response.get("accountActivities") or []
            if begin.isoformat() <= str(activity.get("date") or "")[:10] <= end.isoformat()
        ]
        return render_template(
            "transactions.html",
            suffix=suffix,
            days=days,
            activities=activities,
        )

    # ------------------------------------------------------------------ giriş gerektirmeyen sayfa

    @app.get("/rates")
    def rates() -> str:
        # Client credentials: müşteri girişi gerekmez, token'ı kütüphane kendisi alır.
        response = client.fx.fx_currency_rates()
        return render_template("rates.html", rates=response.get("rateList") or [])

    # ------------------------------------------------------------------ hatalar

    @app.errorhandler(AuthorizationRequiredError)
    def needs_login(error: AuthorizationRequiredError) -> Response:
        # Token yok, refresh token'ın süresi dolmuş ya da izin eksik: yeniden bağlanmalı.
        client.auth.forget_user(user=visitor())
        flash("Devam etmek için Kuveyt Türk hesabınızı bağlayın.")
        return redirect(url_for("index"))

    @app.errorhandler(APIError)
    def api_error(error: APIError) -> tuple[str, int]:
        detail = error.error_message or f"HTTP {error.status_code}"
        return render_template("error.html", message=f"Banka isteği reddetti: {detail}"), 502

    @app.errorhandler(KuveytTurkError)
    def library_error(error: KuveytTurkError) -> tuple[str, int]:
        return render_template("error.html", message=str(error)), 502

    @app.template_filter("money")
    def money(value: Any) -> str:
        return f"{value:,.2f}" if isinstance(value, (int, float)) else str(value or "")

    return app


def main() -> None:
    kt = create_client()
    app = create_app(kt)
    # Banka müşteriyi Redirect URI'ye geri yollayacağı için uygulama o adresin portunda dinler.
    port = urlsplit(kt.redirect_uri or "").port or 8000
    print(f"Uygulama http://localhost:{port}/ adresinde ({kt.environment.name} ortamı).")
    app.run(host="127.0.0.1", port=port, debug=False)


if __name__ == "__main__":
    main()
