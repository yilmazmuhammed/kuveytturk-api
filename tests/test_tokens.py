from __future__ import annotations

import os
import stat
from pathlib import Path

import pytest

from kuveytturk_api import FileTokenStore, MemoryTokenStore, Token, TokenStore
from kuveytturk_api.tokens import normalize_scopes


def test_from_response_computes_expiry_times():
    token = Token.from_response(
        {"access_token": "a", "expires_in": 3600, "refresh_token": "r", "scope": "accounts"},
        now=1000.0,
    )
    assert token.expires_at == 4600.0
    assert token.refresh_expires_at == 1000.0 + 24 * 3600
    assert token.scopes == ("accounts",)


def test_expiry_uses_leeway():
    token = Token(access_token="a", expires_at=1000.0)
    assert not token.is_expired(now=900.0)
    assert token.is_expired(now=950.0)  # 60 sn'lik pay içinde
    assert not token.is_expired(now=950.0, leeway=0)
    assert not Token(access_token="a").is_expired()  # bitişi bilinmeyen token


def test_can_refresh():
    assert not Token(access_token="a").can_refresh()
    token = Token(access_token="a", refresh_token="r", refresh_expires_at=1000.0)
    assert token.can_refresh(now=999.0)
    assert not token.can_refresh(now=1000.0)


def test_has_scope_is_case_insensitive_and_lenient_when_unknown():
    token = Token(access_token="a", scope="accounts Loans offline_access")
    assert token.has_scope("loans")
    assert token.has_scope(["accounts", "LOANS"])
    assert not token.has_scope("transfers")
    assert Token(access_token="a").has_scope("transfers")


def test_normalize_scopes():
    assert normalize_scopes("b  A a") == ("a", "b")
    assert normalize_scopes(["accounts transfers", "Accounts"]) == ("accounts", "transfers")
    assert normalize_scopes(None) == ()


def test_repr_hides_secrets():
    text = repr(Token(access_token="SECRET-A", refresh_token="SECRET-R"))
    assert "SECRET" not in text


@pytest.fixture(params=["memory", "file"])
def store(request, tmp_path: Path) -> TokenStore:
    if request.param == "memory":
        return MemoryTokenStore()
    return FileTokenStore(tmp_path / "nested" / "tokens.json")


def test_store_roundtrip(store: TokenStore):
    token = Token(access_token="a", expires_at=10.0, refresh_token="r", scope="accounts")
    assert store.get("user:x") is None
    store.set("user:x", token)
    store.set("client:public", Token(access_token="b"))
    assert store.get("user:x") == token
    store.delete("user:x")
    store.delete("user:x")  # olmayan anahtarı silmek hata değil
    assert store.get("user:x") is None
    assert store.get("client:public") == Token(access_token="b")
    assert isinstance(store, TokenStore)


def test_file_store_persists_with_private_permissions(tmp_path: Path):
    path = tmp_path / "tokens.json"
    FileTokenStore(path).set("user:x", Token(access_token="a"))
    assert FileTokenStore(path).get("user:x") == Token(access_token="a")
    if os.name == "posix":
        assert stat.S_IMODE(path.stat().st_mode) == 0o600
    assert [p.name for p in tmp_path.iterdir()] == ["tokens.json"]  # geçici dosya kalmadı


def test_file_store_tolerates_corrupt_file(tmp_path: Path):
    path = tmp_path / "tokens.json"
    path.write_text("{bozuk")
    store = FileTokenStore(path)
    assert store.get("user:x") is None
    store.set("user:x", Token(access_token="a"))
    assert store.get("user:x") == Token(access_token="a")
