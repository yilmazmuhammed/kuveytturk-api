from __future__ import annotations

import datetime as dt
import time
from decimal import Decimal

import httpx
import pytest

from conftest import GATEWAY, Recorder, envelope, token_response
from kuveytturk_api import (
    APIError,
    AuthorizationRequiredError,
    BadRequestError,
    BusinessError,
    ConfigurationError,
    ForbiddenError,
    KuveytTurk,
    NotFoundError,
    RateLimitError,
    ServerError,
    Token,
    TransportError,
    UnauthorizedError,
)


def raw_target(request: httpx.Request) -> str:
    return request.url.raw_path.decode()


# ----------------------------------------------------------------- imza ve istek biçimi


def test_get_signs_token_plus_query_string(make_client, verify):
    recorder = Recorder()
    kt = make_client(recorder)
    kt.get(
        "/v4/accounts/{suffix}/transactions",
        scope="accounts",
        path_params={"suffix": 1},
        query={"beginDate": dt.date(2025, 1, 1), "itemCount": 10, "onlyOpen": True, "skip": None},
    )

    request = recorder.last
    assert request.method == "GET"
    assert raw_target(request) == (
        "/v4/accounts/1/transactions?beginDate=2025-01-01&itemCount=10&onlyOpen=true"
    )
    assert request.headers["Authorization"] == "Bearer tok-1"
    assert request.content == b""
    assert "Content-Type" not in request.headers
    verify(
        request.headers["Signature"],
        b"tok-1?beginDate=2025-01-01&itemCount=10&onlyOpen=true",
    )


def test_get_without_query_signs_only_the_token(make_client, verify):
    recorder = Recorder()
    make_client(recorder).get("/v1/data/branches", scope="public")
    assert raw_target(recorder.last) == "/v1/data/branches"
    verify(recorder.last.headers["Signature"], b"tok-1")


def test_signed_query_is_exactly_what_goes_on_the_wire(make_client, verify):
    recorder = Recorder()
    make_client(recorder).get(
        "/v1/x",
        scope="public",
        query={"q": "Şişli & co/1", "when": dt.datetime(2025, 1, 2, 3, 4, 5), "ids": [1, 2]},
    )
    sent_query = raw_target(recorder.last).partition("?")[2]
    assert sent_query == (
        "q=%C5%9Ei%C5%9Fli%20%26%20co%2F1&when=2025-01-02T03%3A04%3A05&ids=1&ids=2"
    )
    verify(recorder.last.headers["Signature"], b"tok-1?" + sent_query.encode())


def test_post_signs_token_plus_exact_body_bytes(make_client, verify):
    recorder = Recorder()
    make_client(recorder).post(
        "/v1/transfers",
        scope="transfers",
        body={"amount": Decimal("12.50"), "açıklama": "Kira", "date": dt.date(2025, 1, 1)},
    )
    request = recorder.last
    assert request.content == '{"amount":12.5,"açıklama":"Kira","date":"2025-01-01"}'.encode()
    assert request.headers["Content-Type"] == "application/json"
    verify(request.headers["Signature"], b"tok-1" + request.content)


def test_post_without_body_sends_empty_object(make_client, verify):
    recorder = Recorder()
    make_client(recorder).post("/v1/x", scope="public")
    assert recorder.last.content == b"{}"
    verify(recorder.last.headers["Signature"], b"tok-1{}")


def test_path_params_are_escaped_and_validated(make_client):
    recorder = Recorder()
    kt = make_client(recorder)
    kt.get("/v1/items/{id}", scope="public", path_params={"id": "a/b c"})
    assert raw_target(recorder.last) == "/v1/items/a%2Fb%20c"
    with pytest.raises(ConfigurationError, match="yer tutucusu"):
        kt.get("/v1/items", scope="public", path_params={"id": 1})
    with pytest.raises(ConfigurationError, match="boş olamaz"):
        kt.get("/v1/items/{id}", scope="public", path_params={"id": None})


def test_get_with_body_is_rejected(make_client):
    with pytest.raises(ConfigurationError, match="gövde"):
        make_client(Recorder()).request("GET", "/v1/x", scope="public", body={"a": 1})


def test_optional_headers(make_client):
    recorder = Recorder()
    kt = make_client(recorder, language_id=1, device_id="dev-1")
    kt.get("/v1/x", scope="public", options={"headers": {"X-Trace": "abc"}})
    headers = recorder.last.headers
    assert headers["LanguageId"] == "1"
    assert headers["DeviceId"] == "dev-1"
    assert headers["X-Trace"] == "abc"
    assert headers["User-Agent"].startswith("kuveytturk-api-python/")
    with pytest.raises(ConfigurationError, match=r"(?i)signature"):
        kt.get("/v1/x", scope="public", options={"headers": {"signature": "x"}})


def test_base_url_follows_environment(make_client):
    recorder = Recorder()
    make_client(recorder).get("/v1/x", scope="public")
    assert str(recorder.last.url) == f"{GATEWAY}/v1/x"

    prod = Recorder(token=lambda r: token_response())
    prod_client = make_client(prod, environment="production")
    # Recorder yalnızca sandbox identity adresini token isteği sayar; production'da
    # token isteği de "api" listesine düşer ve adresi oradan doğrulanır.
    prod.api = lambda r: token_response() if "connect/token" in str(r.url) else envelope({})
    prod_client.get("/v1/x", scope="public")
    assert [str(r.url) for r in prod.api_requests] == [
        "https://identity.kuveytturk.com.tr/connect/token",
        "https://gateway.kuveytturk.com.tr/v1/x",
    ]


# ----------------------------------------------------------------- token seçimi


def test_client_credentials_token_is_reused_per_scope(make_client):
    recorder = Recorder()
    kt = make_client(recorder)
    kt.get("/v1/a", scope="accounts")
    kt.get("/v1/b", scope="accounts")
    kt.get("/v1/c", scope="public")
    assert [recorder.token_form(i)["scope"] for i in range(2)] == ["accounts", "public"]


def test_authorization_code_flow_uses_the_user_token(make_client):
    recorder = Recorder()
    kt = make_client(recorder)
    with pytest.raises(AuthorizationRequiredError):
        kt.get("/v2/accounts", scope="accounts", flow="authorization_code")
    assert recorder.api_requests == []

    kt.auth.set_user_token(Token(access_token="ali-tok", scope="accounts"), user="ali")
    kt.as_user("ali").get("/v2/accounts", scope="accounts", flow="authorization_code")
    kt.get("/v2/accounts", scope="accounts", flow="authorization_code", options={"user": "ali"})
    assert [r.headers["Authorization"] for r in recorder.api_requests] == ["Bearer ali-tok"] * 2
    assert recorder.token_requests == []


def test_as_user_shares_state_but_not_identity(make_client):
    kt = make_client(Recorder())
    ali = kt.as_user("ali")
    assert ali is not kt
    assert ali._shared is kt._shared
    assert "ali" in repr(ali)
    assert kt._user is None
    with pytest.raises(ConfigurationError):
        kt.as_user("")


def test_explicit_token_bypasses_token_management(make_client, verify):
    recorder = Recorder()
    kt = make_client(recorder)
    kt.get("/v1/x", options={"token": "given"})
    kt.get("/v1/x", options={"token": Token(access_token="given-2")})
    assert recorder.token_requests == []
    assert [r.headers["Authorization"] for r in recorder.api_requests] == [
        "Bearer given",
        "Bearer given-2",
    ]
    verify(recorder.api_requests[0].headers["Signature"], b"given")


def test_flow_and_scope_can_be_overridden_per_call(make_client):
    recorder = Recorder()
    kt = make_client(recorder)
    kt.get(
        "/v2/accounts",
        scope="accounts",
        flow="authorization_code",
        options={"flow": "client_credentials", "scope": "public"},
    )
    assert recorder.token_form()["scope"] == "public"
    with pytest.raises(ConfigurationError, match="scope"):
        kt.get("/v1/x")
    with pytest.raises(ConfigurationError, match="akış"):
        kt.get("/v1/x", scope="public", flow="implicit")  # type: ignore[arg-type]


# ----------------------------------------------------------------- yanıtlar ve hatalar


def test_response_envelope(make_client):
    recorder = Recorder(
        api=lambda r: httpx.Response(
            200,
            json={
                "value": {"executionReferenceId": "ref-1", "accountList": [{"suffix": 1}]},
                "success": True,
                "results": [{"errorCode": "Info", "errorMessage": "bilgi"}],
            },
        )
    )
    response = make_client(recorder).get("/v3/accounts", scope="accounts")
    assert response.status_code == 200
    assert response.success is True
    assert response.value["accountList"] == [{"suffix": 1}]
    assert response["accountList"][0]["suffix"] == 1
    assert "accountList" in response
    assert response.get("yok", 5) == 5
    assert response.execution_reference_id == "ref-1"
    assert str(response.results[0]) == "Info: bilgi"
    assert "200" in repr(response)


def test_response_without_envelope_or_body(make_client):
    plain = Recorder(api=lambda r: httpx.Response(200, json=[1, 2]))
    response = make_client(plain).get("/v1/x", scope="public")
    assert response.value == [1, 2]
    assert list(response) == [1, 2]
    assert response.success is True and response.results == []

    empty = Recorder(api=lambda r: httpx.Response(204))
    assert make_client(empty).get("/v1/x", scope="public").value is None

    text = Recorder(api=lambda r: httpx.Response(200, text="tamam"))
    assert make_client(text).get("/v1/x", scope="public").data == "tamam"


@pytest.mark.parametrize(
    ("status", "error_cls"),
    [
        (400, BadRequestError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (418, APIError),
        (429, RateLimitError),
        (503, ServerError),
    ],
)
def test_http_errors_map_to_exception_classes(make_client, status, error_cls):
    payload = {
        "success": False,
        "results": [{"errorCode": "ValidationError", "errorMessage": "Alıcı hesap boş olamaz."}],
    }
    recorder = Recorder(api=lambda r: httpx.Response(status, json=payload))
    with pytest.raises(error_cls) as info:
        make_client(recorder).post("/v1/transfers", scope="transfers", body={})
    error = info.value
    assert type(error) is error_cls
    assert error.status_code == status
    assert error.error_code == "ValidationError"
    assert error.error_message == "Alıcı hesap boş olamaz."
    assert error.body == payload
    assert error.method == "POST"
    assert "Alıcı hesap boş olamaz." in str(error)


def test_error_message_does_not_leak_query_string(make_client):
    recorder = Recorder(api=lambda r: httpx.Response(400, text="bad"))
    with pytest.raises(BadRequestError) as info:
        make_client(recorder).get("/v1/x", scope="public", query={"iban": "TR00SECRET"})
    assert "TR00SECRET" not in str(info.value)
    assert "TR00SECRET" in info.value.url  # ayrıntı isteyen için nitelikte duruyor


def test_success_false_raises_business_error_unless_disabled(make_client):
    failure = envelope(
        None, success=False, results=[{"errorCode": "E1", "errorMessage": "yetersiz bakiye"}]
    )
    recorder = Recorder(api=lambda r: failure)
    kt = make_client(recorder)
    with pytest.raises(BusinessError, match="yetersiz bakiye") as info:
        kt.post("/v1/transfers", scope="transfers", body={})
    assert info.value.status_code == 200
    assert info.value.error_code == "E1"

    response = kt.post(
        "/v1/transfers", scope="transfers", body={}, options={"raise_on_failure": False}
    )
    assert response.success is False
    assert (
        make_client(recorder, raise_on_failure=False).post("/v1/t", scope="transfers").success
        is False
    )


# ----------------------------------------------------------------- yeniden deneme


def test_get_is_retried_on_server_errors(make_client):
    responses = iter([httpx.Response(500), httpx.Response(503), envelope({"ok": 1})])
    recorder = Recorder(api=lambda r: next(responses))
    assert make_client(recorder).get("/v1/x", scope="public").value == {"ok": 1}
    assert len(recorder.api_requests) == 3


def test_get_gives_up_after_max_retries(make_client):
    recorder = Recorder(api=lambda r: httpx.Response(500, text="patladı"))
    with pytest.raises(ServerError):
        make_client(recorder, max_retries=1).get("/v1/x", scope="public")
    assert len(recorder.api_requests) == 2


def test_post_is_never_retried(make_client):
    recorder = Recorder(api=lambda r: httpx.Response(500))
    with pytest.raises(ServerError):
        make_client(recorder).post("/v1/transfers", scope="transfers", body={"amount": 1})
    assert len(recorder.api_requests) == 1

    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("zaman aşımı")

    timeouts = Recorder(api=boom)
    with pytest.raises(TransportError):
        make_client(timeouts).post("/v1/transfers", scope="transfers", body={"amount": 1})
    assert len(timeouts.api_requests) == 1


def test_network_errors_are_retried_for_get(make_client):
    calls = {"n": 0}

    def flaky(request: httpx.Request) -> httpx.Response:
        calls["n"] += 1
        if calls["n"] < 3:
            raise httpx.ConnectError("bağlantı yok")
        return envelope({"ok": 1})

    assert make_client(Recorder(api=flaky)).get("/v1/x", scope="public").value == {"ok": 1}

    calls["n"] = -10
    with pytest.raises(TransportError, match="gönderilemedi"):
        make_client(Recorder(api=flaky)).get("/v1/x", scope="public")


def test_unauthorized_refetches_client_token_once(make_client):
    tokens = iter(["old", "new"])
    recorder = Recorder(
        api=lambda r: (
            envelope({}) if r.headers["Authorization"] == "Bearer new" else httpx.Response(401)
        ),
        token=lambda r: token_response(next(tokens)),
    )
    make_client(recorder).post("/v1/x", scope="public", body={"a": 1})
    assert [r.headers["Authorization"] for r in recorder.api_requests] == [
        "Bearer old",
        "Bearer new",
    ]


def test_unauthorized_is_raised_when_new_token_also_fails(make_client):
    recorder = Recorder(api=lambda r: httpx.Response(401, json={"message": "imza geçersiz"}))
    with pytest.raises(UnauthorizedError, match="imza geçersiz"):
        make_client(recorder).get("/v1/x", scope="public")
    assert len(recorder.api_requests) == 2
    assert len(recorder.token_requests) == 2


def test_unauthorized_refreshes_user_token_once(make_client):
    recorder = Recorder(
        api=lambda r: (
            envelope({}) if r.headers["Authorization"] == "Bearer fresh" else httpx.Response(401)
        ),
        token=lambda r: token_response("fresh", scope="accounts"),
    )
    kt = make_client(recorder)
    kt.auth.set_user_token(
        Token(
            access_token="revoked",
            expires_at=time.time() + 3000,
            refresh_token="r",
            scope="accounts",
        )
    )
    kt.get("/v2/accounts", scope="accounts", flow="authorization_code")
    assert recorder.token_form()["grant_type"] == "refresh_token"
    assert len(recorder.api_requests) == 2


def test_unauthorized_is_not_retried_without_a_way_to_renew(make_client):
    recorder = Recorder(api=lambda r: httpx.Response(401))
    kt = make_client(recorder)
    kt.auth.set_user_token(Token(access_token="no-refresh", scope="accounts"))
    with pytest.raises(UnauthorizedError):
        kt.get("/v2/accounts", scope="accounts", flow="authorization_code")
    with pytest.raises(UnauthorizedError):
        kt.get("/v1/x", options={"token": "explicit"})
    assert len(recorder.api_requests) == 2


# ----------------------------------------------------------------- yapılandırma


def test_missing_configuration_is_reported(private_pem):
    with pytest.raises(ConfigurationError, match="client_secret, private_key"):
        KuveytTurk("id")
    with pytest.raises(ConfigurationError, match="Bilinmeyen ortam"):
        KuveytTurk("id", "secret", private_pem, environment="staging")
    with pytest.raises(ConfigurationError, match="max_retries"):
        KuveytTurk("id", "secret", private_pem, max_retries=-1)


def test_context_manager_closes_owned_http_client(private_pem):
    with KuveytTurk("id", "secret", private_pem) as kt:
        http = kt._shared.http
        assert "sandbox" in repr(kt)
    assert http.is_closed

    external = httpx.Client()
    with KuveytTurk("id", "secret", private_pem, http_client=external):
        pass
    assert not external.is_closed
    external.close()


def test_requests_are_logged_without_secrets(make_client, caplog):
    recorder = Recorder(api=lambda r: httpx.Response(404, text="yok"))
    with caplog.at_level("DEBUG", logger="kuveytturk_api"), pytest.raises(NotFoundError):
        make_client(recorder).get("/v1/x", scope="public", query={"iban": "TR00SECRET"})
    assert caplog.messages == ["GET /v1/x -> HTTP 404 (deneme 1)"]
