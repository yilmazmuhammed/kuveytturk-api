from __future__ import annotations

import base64
import time
from urllib.parse import parse_qs, urlsplit

import httpx
import pytest

from conftest import IDENTITY, Recorder, envelope, token_response
from kuveytturk_api import (
    AuthenticationError,
    AuthorizationRequiredError,
    ConfigurationError,
    Token,
    TransportError,
)


def test_authorization_url(make_client):
    kt = make_client(Recorder())
    url = kt.auth.authorization_url(["accounts", "offline_access"], state="s t/1", ui_locales="tr")
    parts = urlsplit(url)
    assert f"{parts.scheme}://{parts.netloc}{parts.path}" == f"{IDENTITY}/connect/authorize"
    assert parse_qs(parts.query) == {
        "response_type": ["code"],
        "client_id": ["client-id"],
        "redirect_uri": ["http://localhost:8000/callback"],
        "scope": ["accounts offline_access"],
        "state": ["s t/1"],
        "ui_locales": ["tr"],
    }
    assert "+" not in parts.query  # boşluklar %20 olarak kodlanır


def test_authorization_url_requires_redirect_uri_and_scope(make_client):
    with pytest.raises(ConfigurationError, match="redirect_uri"):
        make_client(Recorder(), redirect_uri=None).auth.authorization_url("accounts")
    with pytest.raises(ConfigurationError, match="scope"):
        make_client(Recorder()).auth.authorization_url([])


def test_parse_callback(make_client):
    auth = make_client(Recorder()).auth
    assert (
        auth.parse_callback("http://localhost:8000/callback?code=abc&state=s", state="s") == "abc"
    )
    assert auth.parse_callback("code=abc&state=s") == "abc"
    with pytest.raises(AuthenticationError, match="access_denied") as denied:
        auth.parse_callback("http://localhost:8000/callback?error=access_denied&state=s")
    assert denied.value.error == "access_denied"
    with pytest.raises(AuthenticationError, match="state"):
        auth.parse_callback("http://localhost:8000/callback?code=abc&state=other", state="s")
    with pytest.raises(AuthenticationError, match="code"):
        auth.parse_callback("http://localhost:8000/callback?state=s", state="s")


def test_new_state_is_random(make_client):
    auth = make_client(Recorder()).auth
    assert auth.new_state() != auth.new_state()
    assert len(auth.new_state()) >= 32


def test_client_token_request_and_cache(make_client):
    recorder = Recorder()
    kt = make_client(recorder)

    assert kt.auth.client_token("accounts").access_token == "tok-1"
    kt.auth.client_token("accounts")
    kt.auth.client_token("Accounts")  # aynı kapsam, farklı yazım
    assert len(recorder.token_requests) == 1

    request = recorder.token_requests[0]
    assert str(request.url) == f"{IDENTITY}/connect/token"
    expected = base64.b64encode(b"client-id:client-secret").decode()
    assert request.headers["Authorization"] == f"Basic {expected}"
    assert request.headers["Content-Type"] == "application/x-www-form-urlencoded"
    assert recorder.token_form() == {"grant_type": "client_credentials", "scope": "accounts"}

    kt.auth.client_token("public")  # farklı kapsam ayrı token ister
    kt.auth.client_token("accounts", force=True)
    assert len(recorder.token_requests) == 3


def test_expired_client_token_is_fetched_again(make_client):
    recorder = Recorder(token=lambda r: token_response(expires_in=30))  # 60 sn'lik payın altında
    kt = make_client(recorder)
    kt.auth.client_token("public")
    kt.auth.client_token("public")
    assert len(recorder.token_requests) == 2


def test_token_endpoint_error(make_client):
    recorder = Recorder(
        token=lambda r: httpx.Response(
            400, json={"error": "invalid_client", "error_description": "kötü sır"}
        )
    )
    with pytest.raises(AuthenticationError, match="invalid_client") as info:
        make_client(recorder).auth.client_token("public")
    assert info.value.error == "invalid_client"
    assert info.value.error_description == "kötü sır"
    assert info.value.status_code == 400


def test_token_endpoint_non_json_and_network_errors(make_client):
    html = Recorder(token=lambda r: httpx.Response(502, text="<html>Bad Gateway</html>"))
    with pytest.raises(AuthenticationError, match="502"):
        make_client(html).auth.client_token("public")

    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("bağlantı yok")

    with pytest.raises(TransportError):
        make_client(Recorder(token=boom)).auth.client_token("public")


def test_exchange_code_stores_user_token(make_client):
    recorder = Recorder(
        token=lambda r: token_response("user-tok", refresh_token="ref-1", scope="accounts")
    )
    kt = make_client(recorder)
    token = kt.auth.exchange_code("the-code", user="ali")

    assert recorder.token_form() == {
        "grant_type": "authorization_code",
        "code": "the-code",
        "redirect_uri": "http://localhost:8000/callback",
    }
    assert token.refresh_token == "ref-1"
    assert kt.auth.get_user_token(user="ali") == token
    assert kt.auth.get_user_token() is None  # varsayılan kullanıcı ayrı tutulur
    assert kt.as_user("ali").auth.user_token(scope="accounts") == token


def test_user_token_is_refreshed_when_expired(make_client):
    recorder = Recorder(token=lambda r: token_response("fresh", scope="accounts"))
    kt = make_client(recorder)
    stale = Token(
        access_token="stale",
        expires_at=time.time() - 10,
        refresh_token="ref-1",
        refresh_expires_at=time.time() + 1000,
        scope="accounts",
    )
    kt.auth.set_user_token(stale)

    token = kt.auth.user_token(scope="accounts")
    assert token.access_token == "fresh"
    assert recorder.token_form() == {"grant_type": "refresh_token", "refresh_token": "ref-1"}
    # Sunucu yeni refresh token dönmediyse eskisi korunur.
    assert token.refresh_token == "ref-1"
    assert token.refresh_expires_at == stale.refresh_expires_at
    assert kt.auth.get_user_token() == token


def test_user_token_errors(make_client):
    kt = make_client(Recorder())
    with pytest.raises(AuthorizationRequiredError, match="token'ı yok") as info:
        kt.auth.user_token(scope="accounts")
    assert info.value.scope == "accounts"
    assert info.value.user == "default"

    kt.auth.set_user_token(Token(access_token="a", expires_at=time.time() - 10))
    with pytest.raises(AuthorizationRequiredError, match="offline_access"):
        kt.auth.user_token()

    kt.auth.set_user_token(Token(access_token="a", scope="accounts"))
    with pytest.raises(AuthorizationRequiredError, match="transfers"):
        kt.auth.user_token(scope="transfers")

    kt.auth.forget_user()
    assert kt.auth.get_user_token() is None


def test_refresh_with_invalid_grant_forgets_token(make_client):
    recorder = Recorder(token=lambda r: httpx.Response(400, json={"error": "invalid_grant"}))
    kt = make_client(recorder)
    kt.auth.set_user_token(Token(access_token="a", refresh_token="dead"))
    with pytest.raises(AuthorizationRequiredError, match="yeniden giriş"):
        kt.auth.refresh()
    assert kt.auth.get_user_token() is None


def test_refresh_without_refresh_token(make_client):
    kt = make_client(Recorder())
    kt.auth.set_user_token(Token(access_token="a"))
    with pytest.raises(AuthorizationRequiredError, match="refresh token yok"):
        kt.auth.refresh()


def test_login_runs_full_browser_flow(make_client, monkeypatch):
    recorder = Recorder(
        api=lambda r: envelope({"ok": True}),
        token=lambda r: token_response("user-tok", scope="accounts"),
    )
    kt = make_client(recorder)
    opened: list[str] = []

    def fake_wait(redirect_uri: str, *, timeout: float) -> str:
        state = parse_qs(urlsplit(opened[0]).query)["state"][0]
        return f"{redirect_uri}?code=the-code&state={state}"

    monkeypatch.setattr("webbrowser.open", lambda url: opened.append(url) or True)
    monkeypatch.setattr("kuveytturk_api.client.wait_for_callback", fake_wait)

    token = kt.auth.login(["accounts"])
    assert token.access_token == "user-tok"
    assert recorder.token_form()["code"] == "the-code"
    assert kt.auth.get_user_token() == token


def test_login_rejects_forged_state(make_client, monkeypatch):
    kt = make_client(Recorder())
    monkeypatch.setattr("webbrowser.open", lambda url: True)
    monkeypatch.setattr(
        "kuveytturk_api.client.wait_for_callback",
        lambda redirect_uri, *, timeout: f"{redirect_uri}?code=x&state=sahte",
    )
    with pytest.raises(AuthenticationError, match="state"):
        kt.auth.login("accounts")


def test_invalid_scope_error_names_the_missing_scope(make_client):
    recorder = Recorder(token=lambda r: httpx.Response(400, json={"error": "invalid_scope"}))
    with pytest.raises(AuthenticationError, match="'loans' kapsamı için yetkili değil") as info:
        make_client(recorder).get("/v1/data/loans", scope="Loans")
    assert info.value.error == "invalid_scope"
    assert info.value.status_code == 400
