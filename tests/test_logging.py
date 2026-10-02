"""İstek/yanıt logları: neyin yazıldığı ve neyin asla yazılmadığı."""

from __future__ import annotations

import io
import logging

import httpx
import pytest

import kuveytturk_api
from conftest import Recorder, envelope, token_response
from kuveytturk_api import NotFoundError, Token, TransportError, _logging

SECRET_TOKEN = "eyJ-cok-gizli-access-token"


@pytest.fixture(autouse=True)
def restore_logger():
    logger = logging.getLogger("kuveytturk_api")
    state = (logger.level, logger.propagate, list(logger.handlers))
    yield
    logger.setLevel(state[0])
    logger.propagate = state[1]
    logger.handlers[:] = state[2]


def assert_no_secrets(text: str, signature: str | None = None) -> None:
    assert SECRET_TOKEN not in text
    assert "client-secret" not in text
    assert "Y2xpZW50LWlk" not in text  # Basic başlığındaki base64(client-id:...)
    if signature:
        assert signature not in text


def test_info_level_is_a_one_line_summary_without_query_or_bodies(make_client, caplog):
    recorder = Recorder(
        api=lambda r: httpx.Response(404, text="yok"),
        token=lambda r: token_response(SECRET_TOKEN),
    )
    with caplog.at_level(logging.INFO, logger="kuveytturk_api"), pytest.raises(NotFoundError):
        make_client(recorder).get("/v1/x", scope="public", query={"iban": "TR00MUSTERI"})

    token_line, request_line = caplog.messages
    assert token_line.startswith("POST /connect/token -> 200 (")
    assert request_line.startswith("GET /v1/x -> 404 (") and request_line.endswith(" sn)")
    assert "TR00MUSTERI" not in caplog.text and "yok" not in caplog.text
    assert_no_secrets(caplog.text)


def test_debug_level_shows_full_request_and_response_with_masked_secrets(make_client, caplog):
    recorder = Recorder(
        api=lambda r: envelope({"accountList": [{"iban": "TR99HESAP"}]}),
        token=lambda r: token_response(SECRET_TOKEN, scope="accounts"),
    )
    with caplog.at_level(logging.DEBUG, logger="kuveytturk_api"):
        make_client(recorder, language_id=1).post(
            "/v1/things",
            scope="accounts",
            query={"page": 2},
            body={"açıklama": "Kira", "amount": 5},
        )

    token_out, token_in, request, response = caplog.messages
    assert token_out.startswith("→ POST https://prep-identity.kuveytturk.com.tr/connect/token")
    assert "grant_type=client_credentials" in token_out and "scope=accounts" in token_out
    assert "access_token=<gizlendi" in token_in and "expires_in=3600" in token_in

    lines = request.splitlines()
    assert lines[0] == "→ POST https://prep-gateway.kuveytturk.com.tr/v1/things?page=2"
    assert f"    Authorization: Bearer <gizlendi, {len(SECRET_TOKEN)} karakter>" in lines
    assert any(line.startswith("    Signature: <gizlendi, ") for line in lines)
    assert "    LanguageId: 1" in lines and "    Content-Type: application/json" in lines
    assert lines[-1] == '    gövde: {"açıklama":"Kira","amount":5}'

    assert response.startswith("← POST /v1/things -> 200 (")
    assert '"iban":"TR99HESAP"' in response.replace(" ", "")
    assert_no_secrets(caplog.text, signature=recorder.last.headers["Signature"])


def test_debug_log_for_get_has_no_body_line_and_marks_retries(make_client, caplog):
    responses = iter([httpx.Response(503, text="meşgul"), envelope({"ok": 1})])
    recorder = Recorder(api=lambda r: next(responses))
    with caplog.at_level(logging.DEBUG, logger="kuveytturk_api"):
        make_client(recorder).get("/v1/x", scope="public")

    first, _, second, _ = caplog.messages[2:]
    assert "gövde" not in first
    assert first.splitlines()[0].endswith("/v1/x")
    assert second.splitlines()[0].endswith("/v1/x (deneme 2)")
    assert "-> 503" in caplog.messages[3] and "meşgul" in caplog.messages[3]
    assert caplog.messages[5].splitlines()[0].endswith("(deneme 2)")


def test_long_bodies_are_truncated(make_client, caplog):
    recorder = Recorder(
        api=lambda r: httpx.Response(200, text="x" * (_logging.MAX_BODY_CHARS + 25))
    )
    with caplog.at_level(logging.DEBUG, logger="kuveytturk_api"):
        make_client(recorder).get("/v1/x", options={"token": "t"})
    assert caplog.messages[-1].endswith("x… (+25 karakter)")


def test_authorization_code_and_refresh_token_are_masked(make_client, caplog):
    recorder = Recorder(
        token=lambda r: token_response(
            SECRET_TOKEN, refresh_token="gizli-refresh", scope="accounts"
        )
    )
    kt = make_client(recorder)
    with caplog.at_level(logging.DEBUG, logger="kuveytturk_api"):
        kt.auth.exchange_code("gizli-auth-code")
        kt.auth.refresh()
    assert "grant_type=authorization_code" in caplog.text
    assert "redirect_uri=http://localhost:8000/callback" in caplog.text
    for secret in ("gizli-auth-code", "gizli-refresh"):
        assert secret not in caplog.text
    assert_no_secrets(caplog.text)


def test_token_endpoint_errors_are_shown(make_client, caplog):
    recorder = Recorder(token=lambda r: httpx.Response(400, json={"error": "invalid_scope"}))
    with caplog.at_level(logging.DEBUG, logger="kuveytturk_api"), pytest.raises(Exception):  # noqa: B017
        make_client(recorder).get("/v1/x", scope="loans")
    assert "-> 400" in caplog.text and "error=invalid_scope" in caplog.text


def test_network_failures_are_logged_as_warnings(make_client, caplog):
    def boom(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("bağlantı reddedildi")

    with caplog.at_level(logging.WARNING, logger="kuveytturk_api"), pytest.raises(TransportError):
        make_client(Recorder(api=boom), max_retries=1).get("/v1/x", options={"token": "t"})
    assert [r.levelname for r in caplog.records] == ["WARNING", "WARNING"]
    assert "ağ hatası" in caplog.messages[0] and "bağlantı reddedildi" in caplog.messages[0]
    assert caplog.messages[1].count("(deneme 2)") == 1


def test_nothing_is_formatted_when_logging_is_off(make_client, caplog, monkeypatch):
    monkeypatch.setattr(
        _logging, "_body_text", lambda content: pytest.fail("gövde biçimlendirildi")
    )
    with caplog.at_level(logging.WARNING, logger="kuveytturk_api"):
        make_client(Recorder()).post("/v1/x", scope="public", body={"a": 1})
    assert caplog.messages == []


async def test_async_client_logs_the_same_way(make_async_client, caplog):
    recorder = Recorder(
        api=lambda r: envelope({"ok": 1}), token=lambda r: token_response(SECRET_TOKEN)
    )
    with caplog.at_level(logging.DEBUG, logger="kuveytturk_api"):
        async with make_async_client(recorder) as kt:
            kt.auth.set_user_token(Token(access_token="kullanici-tok"))
            await kt.post("/v1/x", scope="public", body={"a": 1})
    assert [m.split()[0] for m in caplog.messages] == ["→", "←", "→", "←"]
    assert caplog.messages[2].splitlines()[-1] == '    gövde: {"a":1}'
    assert_no_secrets(caplog.text)


def test_enable_logging_writes_to_the_given_stream_and_is_idempotent(make_client):
    stream = io.StringIO()
    kuveytturk_api.enable_logging("info", stream=io.StringIO())
    kuveytturk_api.enable_logging("debug", stream=stream)
    logger = logging.getLogger("kuveytturk_api")
    assert logger.level == logging.DEBUG and logger.propagate is False
    assert sum(getattr(h, "_kuveytturk_api_handler", False) for h in logger.handlers) == 1

    make_client(Recorder()).get("/v1/x", scope="public")
    output = stream.getvalue()
    assert "kuveytturk_api DEBUG → GET https://prep-gateway.kuveytturk.com.tr/v1/x" in output
    assert "<gizlendi" in output and "tok-1" not in output

    with pytest.raises(ValueError, match="Bilinmeyen log düzeyi"):
        kuveytturk_api.enable_logging("verbose")


@pytest.mark.parametrize(("value", "expected"), [("debug", logging.DEBUG), ("INFO", logging.INFO)])
def test_environment_variable_enables_logging(monkeypatch, value, expected):
    monkeypatch.setenv("KUVEYTTURK_LOG", value)
    _logging.enable_from_environment()
    assert logging.getLogger("kuveytturk_api").level == expected


def test_environment_variable_is_ignored_when_unset_or_unknown(monkeypatch):
    logger = logging.getLogger("kuveytturk_api")
    before = (logger.level, list(logger.handlers))
    for value in ("", "0", "yes"):
        monkeypatch.setenv("KUVEYTTURK_LOG", value)
        _logging.enable_from_environment()
    assert (logger.level, list(logger.handlers)) == before
