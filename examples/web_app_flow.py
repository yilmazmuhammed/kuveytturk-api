"""Web uygulamasında müşteri girişi (authorization code) — çatıdan bağımsız iskelet.

Çalıştırılacak bir betik değildir; kendi rotalarınıza (Django, FastAPI, Flask...) uyarlayın.
``login`` kullanıcıyı bankaya yönlendirir, ``callback`` bankadan dönen kodu token'a çevirir.
Her müşterinin token'ı kendi anahtarıyla saklanır ve ``kt.as_user(...)`` ile kullanılır.
"""

from __future__ import annotations

from typing import Any

from kuveytturk_api import AuthorizationRequiredError, KuveytTurk

# Uygulama boyunca tek bir istemci yeterlidir. Birden çok süreç/sunucu varsa token'ları
# paylaşmak için token_store= ile kendi deponuzu (Redis, veritabanı...) verin.
kt = KuveytTurk.from_env(".env")


def login(session: dict[str, Any]) -> str:
    """Kullanıcıyı yönlendireceğiniz adresi döndürür."""
    session["kt_state"] = kt.auth.new_state()  # CSRF koruması
    return kt.auth.authorization_url(["accounts", "offline_access"], state=session["kt_state"])


def callback(session: dict[str, Any], callback_url: str, user_id: str) -> None:
    """Redirect URI'nize gelen isteği işler (``callback_url``: isteğin tam adresi)."""
    code = kt.auth.parse_callback(callback_url, state=session.pop("kt_state"))
    kt.auth.exchange_code(code, user=user_id)


def list_accounts(user_id: str) -> list[dict[str, Any]] | None:
    """Müşterinin hesapları; yeniden giriş gerekiyorsa ``None``."""
    try:
        response = kt.as_user(user_id).tpp_accounts.account_list_v2()
    except AuthorizationRequiredError:
        # Token yok ya da refresh token'ın süresi (24 saat) dolmuş: kullanıcıyı login'e gönderin.
        return None
    accounts: list[dict[str, Any]] = response["accountList"]
    return accounts
