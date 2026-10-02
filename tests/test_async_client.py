from __future__ import annotations

import asyncio
import time

import httpx
import pytest

from conftest import Recorder, body_json, envelope, token_response
from kuveytturk_api import (
    AsyncKuveytTurk,
    AuthorizationRequiredError,
    BusinessError,
    ServerError,
    Token,
    UnauthorizedError,
)


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    async def instant(seconds: float) -> None:
        return None

    monkeypatch.setattr("kuveytturk_api.async_client.asyncio.sleep", instant)


async def test_get_and_post_are_signed_like_the_sync_client(make_async_client, verify):
    recorder = Recorder(api=lambda r: envelope({"ok": True}))
    async with make_async_client(recorder) as kt:
        response = await kt.get(
            "/v3/accounts/{suffix}",
            scope="accounts",
            path_params={"suffix": 2},
            query={"onlyOpen": True},
        )
        await kt.post("/v1/transfers", scope="transfers", body={"amount": 5})

    assert response.value == {"ok": True}
    get_request, post_request = recorder.api_requests
    assert get_request.url.raw_path == b"/v3/accounts/2?onlyOpen=true"
    verify(get_request.headers["Signature"], b"tok-1?onlyOpen=true")
    assert body_json(post_request) == {"amount": 5}
    verify(post_request.headers["Signature"], b'tok-1{"amount":5}')


async def test_concurrent_calls_share_one_token_request(make_async_client):
    recorder = Recorder()
    async with make_async_client(recorder) as kt:
        await asyncio.gather(*(kt.get("/v1/x", scope="public") for _ in range(5)))
    assert len(recorder.token_requests) == 1
    assert len(recorder.api_requests) == 5


async def test_user_flow_refresh_and_as_user(make_async_client):
    recorder = Recorder(token=lambda r: token_response("fresh", scope="accounts"))
    async with make_async_client(recorder) as kt:
        with pytest.raises(AuthorizationRequiredError):
            await kt.get("/v2/accounts", scope="accounts", flow="authorization_code")

        kt.auth.set_user_token(
            Token(
                access_token="stale",
                expires_at=time.time() - 5,
                refresh_token="ref",
                scope="accounts",
            ),
            user="ali",
        )
        await kt.as_user("ali").get("/v2/accounts", scope="accounts", flow="authorization_code")

    assert recorder.token_form() == {"grant_type": "refresh_token", "refresh_token": "ref"}
    assert recorder.last.headers["Authorization"] == "Bearer fresh"


async def test_exchange_code_and_invalid_grant(make_async_client):
    recorder = Recorder(token=lambda r: token_response("u", refresh_token="ref", scope="accounts"))
    async with make_async_client(recorder) as kt:
        token = await kt.auth.exchange_code("code-1")
        assert kt.auth.get_user_token() == token
        assert recorder.token_form()["grant_type"] == "authorization_code"

        recorder.token = lambda r: httpx.Response(400, json={"error": "invalid_grant"})
        with pytest.raises(AuthorizationRequiredError):
            await kt.auth.refresh()
        assert kt.auth.get_user_token() is None


async def test_retries_and_errors(make_async_client):
    responses = iter([httpx.Response(502), envelope({"ok": 1})])
    recorder = Recorder(api=lambda r: next(responses))
    async with make_async_client(recorder) as kt:
        assert (await kt.get("/v1/x", scope="public")).value == {"ok": 1}

    failing = Recorder(api=lambda r: httpx.Response(500))
    async with make_async_client(failing) as kt:
        with pytest.raises(ServerError):
            await kt.post("/v1/x", scope="public", body={})
    assert len(failing.api_requests) == 1

    business = Recorder(api=lambda r: envelope(None, success=False))
    async with make_async_client(business) as kt:
        with pytest.raises(BusinessError):
            await kt.get("/v1/x", scope="public")


async def test_unauthorized_refetches_token_once(make_async_client):
    tokens = iter(["old", "new", "newer"])
    recorder = Recorder(
        api=lambda r: (
            envelope({}) if r.headers["Authorization"] == "Bearer new" else httpx.Response(401)
        ),
        token=lambda r: token_response(next(tokens)),
    )
    async with make_async_client(recorder) as kt:
        await kt.get("/v1/x", scope="public")
        assert len(recorder.api_requests) == 2
        with pytest.raises(UnauthorizedError):
            await kt.get("/v1/x", options={"token": "explicit"})


async def test_login_flow(make_async_client, monkeypatch):
    from urllib.parse import parse_qs, urlsplit

    recorder = Recorder(token=lambda r: token_response("user-tok"))
    opened: list[str] = []
    monkeypatch.setattr("webbrowser.open", lambda url: opened.append(url) or True)

    def fake_wait(redirect_uri: str, *, timeout: float) -> str:
        state = parse_qs(urlsplit(opened[0]).query)["state"][0]
        return f"{redirect_uri}?code=c&state={state}"

    monkeypatch.setattr("kuveytturk_api.async_client.wait_for_callback", fake_wait)
    async with make_async_client(recorder) as kt:
        token = await kt.auth.login("accounts")
    assert token.access_token == "user-tok"


async def test_aclose_only_closes_owned_client(private_pem):
    kt = AsyncKuveytTurk("id", "secret", private_pem)
    http = kt._shared.http
    await kt.aclose()
    assert http.is_closed
    assert "sandbox" in repr(kt)
