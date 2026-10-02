"""examples/web_app: müşteri girişi akışının web uygulamasındaki uçtan uca davranışı."""

from __future__ import annotations

import importlib.util
import sys
import time
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest

from conftest import IDENTITY, Recorder, envelope, token_response
from kuveytturk_api import KuveytTurk, Token

pytest.importorskip("flask")

APP_PATH = Path(__file__).resolve().parent.parent / "examples" / "web_app" / "app.py"

ACCOUNTS = {
    "accountList": [
        {
            "accountNumber": 123456,
            "name": "Maaş Hesabı",
            "suffix": 1,
            "balance": 1500.5,
            "availableBalance": 1400.0,
            "fxCode": "TL",
            "iban": "TR00TEST0001",
            "type": "Cari Hesap",
        }
    ]
}
ACTIVITIES = {
    "accountActivities": [
        {
            "date": "2026-09-23T23:17:05.327",
            "description": "<b>Market</b>",
            "amount": -42.5,
            "fxCode": "TL",
        }
    ]
}
RATES = {
    "rateList": [{"fxName": "Amerikan Doları", "fxCode": "USD", "buyRate": 45.7, "sellRate": 44.7}]
}


def api(request: httpx.Request) -> httpx.Response:
    path = request.url.path
    if path == "/v2/accounts":
        return envelope(ACCOUNTS)
    if path == "/v2/accounts/1/transactions":
        return envelope(ACTIVITIES)
    if path == "/v2/fx/rates":
        return envelope(RATES)
    return httpx.Response(404, json={"code": 404, "message": "Path not found"})


def tokens(request: httpx.Request) -> httpx.Response:
    form = dict(httpx.QueryParams(request.content.decode()))
    if form["grant_type"] == "authorization_code":
        return token_response(
            f"musteri-{form['code']}", refresh_token="ref", scope="accounts offline_access"
        )
    return token_response("uygulama-tok", scope=form.get("scope", ""))


@pytest.fixture
def recorder() -> Recorder:
    return Recorder(api=api, token=tokens)


@pytest.fixture
def app(recorder: Recorder, private_pem: str) -> Any:
    spec = importlib.util.spec_from_file_location("kt_example_web_app", APP_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    kt = KuveytTurk(
        "client-id",
        "client-secret",
        private_pem,
        redirect_uri="http://localhost:8000/callback",
        http_client=httpx.Client(transport=httpx.MockTransport(recorder)),
    )
    flask_app = module.create_app(kt)
    flask_app.config.update(TESTING=True)
    flask_app.kt = kt  # testlerin token deposuna bakabilmesi için
    return flask_app


def start_login(browser: Any) -> str:
    """/login'e gider ve bankaya gönderilen state değerini döndürür."""
    response = browser.get("/login")
    assert response.status_code == 302
    target = urlsplit(response.headers["Location"])
    assert f"{target.scheme}://{target.netloc}{target.path}" == f"{IDENTITY}/connect/authorize"
    query = parse_qs(target.query)
    assert query["scope"] == ["accounts offline_access"]
    assert query["redirect_uri"] == ["http://localhost:8000/callback"]
    assert query["response_type"] == ["code"] and query["client_id"] == ["client-id"]
    return query["state"][0]


def connect(browser: Any, code: str = "kod-1") -> None:
    state = start_login(browser)
    response = browser.get(f"/callback?code={code}&state={state}")
    assert response.status_code == 302 and response.headers["Location"] == "/accounts"


def test_home_page_offers_to_connect(app):
    page = app.test_client().get("/").get_data(as_text=True)
    assert "Kuveyt Türk ile bağlan" in page and 'href="/login"' in page
    assert "Hesaplarım" not in page


def test_full_login_flow_then_accounts_and_transactions(app, recorder):
    browser = app.test_client()
    connect(browser)
    assert recorder.token_form() == {
        "grant_type": "authorization_code",
        "code": "kod-1",
        "redirect_uri": "http://localhost:8000/callback",
    }

    accounts = browser.get("/accounts").get_data(as_text=True)
    assert "Hesabınız bağlandı." in accounts
    assert "Maaş Hesabı" in accounts and "1,500.50" in accounts and "TR00TEST0001" in accounts
    assert recorder.last.headers["Authorization"] == "Bearer musteri-kod-1"

    listing = browser.get("/accounts/1/transactions?days=7").get_data(as_text=True)
    assert "son 7 gün" in listing and "-42.50" in listing and "2026-09-23 23:17" in listing
    assert "&lt;b&gt;Market&lt;/b&gt;" in listing and "<b>Market</b>" not in listing  # kaçışlanır
    assert recorder.last.url.params["itemCount"] == "50"

    home = browser.get("/").get_data(as_text=True)
    assert "hesabınız bağlı" in home and "Bağlantıyı kaldır" in home


def test_tokens_never_reach_the_browser(app):
    browser = app.test_client()
    connect(browser)
    for path in ("/", "/accounts", "/accounts/1/transactions"):
        response = browser.get(path)
        text = response.get_data(as_text=True) + str(response.headers)
        assert "musteri-kod-1" not in text and "ref" not in response.headers.get("Set-Cookie", "")
    with browser.session_transaction() as session:
        assert set(session) <= {"visitor", "_flashes"}


def test_callback_rejects_a_forged_state(app, recorder):
    browser = app.test_client()
    start_login(browser)
    response = browser.get("/callback?code=kod-1&state=sahte")
    assert response.status_code == 400
    assert "state" in response.get_data(as_text=True)
    assert recorder.token_requests == []
    # Aynı state ikinci kez kullanılamaz: oturumdan silindi.
    assert browser.get("/callback?code=kod-1&state=sahte").status_code == 400


def test_callback_without_a_started_login_is_rejected(app, recorder):
    response = app.test_client().get("/callback?code=kod-1&state=herhangi")
    assert response.status_code == 400
    assert "bu tarayıcıdan başlatılmadı" in response.get_data(as_text=True)
    assert recorder.token_requests == []


def test_callback_reports_denied_consent_and_rejected_code(app, recorder):
    browser = app.test_client()
    state = start_login(browser)
    denied = browser.get(f"/callback?error=access_denied&state={state}")
    assert denied.status_code == 400 and "access_denied" in denied.get_data(as_text=True)

    recorder.token = lambda r: httpx.Response(400, json={"error": "invalid_grant"})
    state = start_login(browser)
    rejected = browser.get(f"/callback?code=eski&state={state}")
    assert rejected.status_code == 400 and "invalid_grant" in rejected.get_data(as_text=True)
    assert browser.get("/accounts").status_code == 302  # bağlantı kurulmadı


def test_customer_pages_require_a_connection(app, recorder):
    browser = app.test_client()
    response = browser.get("/accounts")
    assert response.status_code == 302 and response.headers["Location"] == "/"
    assert "hesabınızı bağlayın" in browser.get("/").get_data(as_text=True)
    assert recorder.api_requests == []


def test_expired_login_sends_the_visitor_back_to_connect(app):
    browser = app.test_client()
    connect(browser)
    with browser.session_transaction() as session:
        visitor = session["visitor"]
    app.kt.auth.set_user_token(
        Token(access_token="eski", expires_at=time.time() - 60), user=visitor
    )

    response = browser.get("/accounts")
    assert response.status_code == 302 and response.headers["Location"] == "/"
    assert app.kt.auth.get_user_token(user=visitor) is None
    assert "Kuveyt Türk ile bağlan" in browser.get("/").get_data(as_text=True)


def test_each_browser_gets_its_own_customer_token(app, recorder):
    first, second = app.test_client(), app.test_client()
    connect(first, "ali")
    connect(second, "veli")
    first.get("/accounts")
    assert recorder.last.headers["Authorization"] == "Bearer musteri-ali"
    second.get("/accounts")
    assert recorder.last.headers["Authorization"] == "Bearer musteri-veli"
    assert app.test_client().get("/accounts").status_code == 302  # üçüncü tarayıcı bağlı değil


def test_logout_requires_post_and_forgets_the_token(app):
    browser = app.test_client()
    connect(browser)
    with browser.session_transaction() as session:
        visitor = session["visitor"]
    assert browser.get("/logout").status_code == 405
    response = browser.post("/logout")
    assert response.status_code == 302
    assert app.kt.auth.get_user_token(user=visitor) is None
    assert browser.get("/accounts").status_code == 302


def test_rates_page_works_without_login(app, recorder):
    page = app.test_client().get("/rates")
    assert page.status_code == 200 and "Amerikan Doları" in page.get_data(as_text=True)
    assert recorder.last.headers["Authorization"] == "Bearer uygulama-tok"


def test_api_errors_render_an_error_page(app, recorder):
    browser = app.test_client()
    connect(browser)
    recorder.api = lambda r: httpx.Response(
        403, json={"results": [{"errorCode": "X", "errorMessage": "Bu işlem için yetkiniz yok"}]}
    )
    response = browser.get("/accounts")
    assert response.status_code == 502
    assert "Bu işlem için yetkiniz yok" in response.get_data(as_text=True)


def test_days_parameter_is_clamped(app):
    browser = app.test_client()
    connect(browser)
    assert "son 365 gün" in browser.get("/accounts/1/transactions?days=99999").get_data(
        as_text=True
    )
    assert "son 1 gün" in browser.get("/accounts/1/transactions?days=-3").get_data(as_text=True)
    assert "son 30 gün" in browser.get("/accounts/1/transactions?days=abc").get_data(as_text=True)


def test_app_refuses_to_start_without_a_redirect_uri(private_pem):
    spec = importlib.util.spec_from_file_location("kt_example_web_app_2", APP_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    with pytest.raises(RuntimeError, match="KUVEYTTURK_REDIRECT_URI"):
        module.create_app(KuveytTurk("id", "secret", private_pem))
