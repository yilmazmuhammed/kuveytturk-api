from __future__ import annotations

import threading
import time
from pathlib import Path

import httpx
import pytest

from kuveytturk_api import (
    PRODUCTION,
    SANDBOX,
    AuthenticationError,
    ConfigurationError,
    Environment,
    KuveytTurk,
)
from kuveytturk_api._base import read_env_file
from kuveytturk_api.callback_server import wait_for_callback
from kuveytturk_api.environments import resolve_environment

ENV_VARS = (
    "CLIENT_ID",
    "CLIENT_SECRET",
    "PRIVATE_KEY",
    "PRIVATE_KEY_PASSWORD",
    "REDIRECT_URI",
    "ENVIRONMENT",
    "LANGUAGE_ID",
    "DEVICE_ID",
)


@pytest.fixture(autouse=True)
def clean_env(monkeypatch):
    for name in ENV_VARS:
        monkeypatch.delenv(f"KUVEYTTURK_{name}", raising=False)


def test_environments():
    assert SANDBOX.token_url == "https://prep-identity.kuveytturk.com.tr/connect/token"
    assert PRODUCTION.authorize_url == "https://identity.kuveytturk.com.tr/connect/authorize"
    assert resolve_environment(" Production ") is PRODUCTION
    custom = Environment("ozel", "https://id.example/", "https://gw.example/")
    assert custom.gateway_url == "https://gw.example"
    assert resolve_environment(custom) is custom


def test_read_env_file(tmp_path: Path):
    path = tmp_path / ".env"
    path.write_text(
        "# yorum\n\nKUVEYTTURK_CLIENT_ID=abc\nexport KUVEYTTURK_CLIENT_SECRET='s=1'\n"
        'KUVEYTTURK_REDIRECT_URI="http://localhost:8000/cb"\nbozuk satır\n'
    )
    assert read_env_file(path) == {
        "KUVEYTTURK_CLIENT_ID": "abc",
        "KUVEYTTURK_CLIENT_SECRET": "s=1",
        "KUVEYTTURK_REDIRECT_URI": "http://localhost:8000/cb",
    }
    assert read_env_file(tmp_path / "yok") == {}


def test_from_env_file_resolves_key_relative_to_the_file(tmp_path: Path, private_pem, monkeypatch):
    (tmp_path / "keys").mkdir()
    (tmp_path / "keys" / "private.pem").write_text(private_pem)
    (tmp_path / ".env").write_text(
        "KUVEYTTURK_CLIENT_ID=file-id\nKUVEYTTURK_CLIENT_SECRET=file-secret\n"
        "KUVEYTTURK_PRIVATE_KEY=keys/private.pem\nKUVEYTTURK_ENVIRONMENT=production\n"
        "KUVEYTTURK_LANGUAGE_ID=1\nKUVEYTTURK_REDIRECT_URI=http://localhost:9/cb\n"
    )
    monkeypatch.chdir(tmp_path.parent)  # çalışma dizini farklı olsa da anahtar bulunmalı

    kt = KuveytTurk.from_env(tmp_path / ".env")
    config = kt._shared.config
    assert (config.client_id, config.client_secret) == ("file-id", "file-secret")
    assert config.environment is PRODUCTION
    assert config.language_id == 1
    assert config.redirect_uri == "http://localhost:9/cb"


def test_real_environment_wins_over_file_and_overrides_win_over_both(
    tmp_path: Path, private_pem, monkeypatch
):
    (tmp_path / ".env").write_text("KUVEYTTURK_CLIENT_ID=file-id\nKUVEYTTURK_CLIENT_SECRET=file\n")
    monkeypatch.setenv("KUVEYTTURK_CLIENT_ID", "env-id")
    monkeypatch.setenv("KUVEYTTURK_PRIVATE_KEY", private_pem.replace("\n", "\\n"))

    kt = KuveytTurk.from_env(tmp_path / ".env", client_secret="override", timeout=5)
    config = kt._shared.config
    assert (config.client_id, config.client_secret, config.timeout) == ("env-id", "override", 5)


def test_from_env_reports_what_is_missing():
    with pytest.raises(ConfigurationError, match="client_id, client_secret, private_key"):
        KuveytTurk.from_env()


def _free_port() -> int:
    import socket

    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def test_callback_server_captures_the_redirect():
    port = _free_port()
    redirect_uri = f"http://localhost:{port}/callback"
    result: dict[str, str] = {}
    thread = threading.Thread(
        target=lambda: result.update(url=wait_for_callback(redirect_uri, timeout=10))
    )
    thread.start()

    base = f"http://127.0.0.1:{port}"
    deadline = time.time() + 5
    while True:
        try:
            assert httpx.get(f"{base}/favicon.ico").status_code == 404  # başka yollar yok sayılır
            break
        except httpx.TransportError:
            assert time.time() < deadline, "callback sunucusu açılmadı"
            time.sleep(0.05)
    page = httpx.get(f"{base}/callback?code=abc&state=xyz")
    thread.join(timeout=5)

    assert page.status_code == 200
    assert "Giriş tamamlandı" in page.text
    assert result["url"] == f"http://localhost:{port}/callback?code=abc&state=xyz"


def test_callback_server_times_out_and_validates_redirect_uri():
    with pytest.raises(AuthenticationError, match="saniye içinde"):
        wait_for_callback(f"http://localhost:{_free_port()}/callback", timeout=0.2)
    for bad in ("https://localhost:8000/cb", "http://example.com/cb"):
        with pytest.raises(ConfigurationError, match="localhost"):
            wait_for_callback(bad)
