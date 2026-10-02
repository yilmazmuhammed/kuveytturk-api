"""Erişim token'ı modeli ve token saklama katmanı."""

from __future__ import annotations

import contextlib
import json
import os
import tempfile
import threading
import time
from collections.abc import Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from .exceptions import ConfigurationError

__all__ = ["FileTokenStore", "MemoryTokenStore", "Token", "TokenStore", "normalize_scopes"]

#: Kuveyt Türk refresh token'ları 24 saat geçerlidir (Authorization Guide).
REFRESH_TOKEN_LIFETIME = 24 * 60 * 60

#: Token'ı süresi dolmadan bu kadar saniye önce "dolmuş" say; istek yoldayken dolmasın.
DEFAULT_LEEWAY = 60.0


def normalize_scopes(scopes: str | Iterable[str] | None) -> tuple[str, ...]:
    """Kapsamları (boşlukla ayrılmış metin ya da liste) sıralı, tekil ve küçük harfli hale getirir."""
    if scopes is None:
        return ()
    parts = scopes.split() if isinstance(scopes, str) else [p for s in scopes for p in s.split()]
    return tuple(sorted({p.strip().lower() for p in parts if p.strip()}))


@dataclass(frozen=True)
class Token:
    """Identity sunucusundan alınan bir OAuth2 token'ı.

    Attributes:
        access_token: API çağrılarında kullanılan token.
        expires_at: Geçerliliğin bittiği an (epoch saniyesi); bilinmiyorsa ``None``.
        refresh_token: Yalnızca authorization code akışında (``offline_access`` ile) gelir.
        refresh_expires_at: Refresh token'ın tahmini bitiş anı (alındıktan 24 saat sonra).
        scope: Verilen kapsamlar (boşlukla ayrılmış).
    """

    access_token: str = field(repr=False)
    token_type: str = "Bearer"
    expires_at: float | None = None
    refresh_token: str | None = field(default=None, repr=False)
    refresh_expires_at: float | None = None
    scope: str = ""

    @classmethod
    def from_response(cls, data: Mapping[str, Any], *, now: float | None = None) -> Token:
        """Token uç noktasının JSON yanıtından ``Token`` üretir."""
        now = time.time() if now is None else now
        expires_in = data.get("expires_in")
        refresh_token = data.get("refresh_token")
        return cls(
            access_token=str(data["access_token"]),
            token_type=str(data.get("token_type") or "Bearer"),
            expires_at=now + float(expires_in) if expires_in is not None else None,
            refresh_token=str(refresh_token) if refresh_token else None,
            refresh_expires_at=now + REFRESH_TOKEN_LIFETIME if refresh_token else None,
            scope=str(data.get("scope") or ""),
        )

    @property
    def scopes(self) -> tuple[str, ...]:
        return normalize_scopes(self.scope)

    def is_expired(self, *, leeway: float = DEFAULT_LEEWAY, now: float | None = None) -> bool:
        """Access token'ın süresi dolmuş (ya da ``leeway`` saniye içinde dolacak) mı?"""
        if self.expires_at is None:
            return False
        return (time.time() if now is None else now) >= self.expires_at - leeway

    def can_refresh(self, *, now: float | None = None) -> bool:
        """Kullanılabilir bir refresh token var mı?"""
        if not self.refresh_token:
            return False
        if self.refresh_expires_at is None:
            return True
        return (time.time() if now is None else now) < self.refresh_expires_at

    def has_scope(self, scope: str | Iterable[str]) -> bool:
        """Token istenen kapsam(lar)ın hepsini içeriyor mu? Kapsamı bilinmeyen token ``True`` döner."""
        granted = self.scopes
        if not granted:
            return True
        return set(normalize_scopes(scope)) <= set(granted)

    def to_dict(self) -> dict[str, Any]:
        return {
            "access_token": self.access_token,
            "token_type": self.token_type,
            "expires_at": self.expires_at,
            "refresh_token": self.refresh_token,
            "refresh_expires_at": self.refresh_expires_at,
            "scope": self.scope,
        }

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> Token:
        return cls(
            access_token=str(data["access_token"]),
            token_type=str(data.get("token_type") or "Bearer"),
            expires_at=data.get("expires_at"),
            refresh_token=data.get("refresh_token"),
            refresh_expires_at=data.get("refresh_expires_at"),
            scope=str(data.get("scope") or ""),
        )


@runtime_checkable
class TokenStore(Protocol):
    """Token'ların saklandığı yer.

    Kendi deponuzu (Redis, veritabanı...) yazmak için bu üç metodu sağlamanız yeterli.
    Anahtarlar ``"client:<kapsamlar>"`` (uygulama token'ları) ve ``"user:<kullanıcı>"``
    (müşteri token'ları) biçimindedir. Metotlar asenkron istemciden de senkron çağrılır;
    bu yüzden hızlı olmaları gerekir.
    """

    def get(self, key: str) -> Token | None: ...

    def set(self, key: str, token: Token) -> None: ...

    def delete(self, key: str) -> None: ...


class MemoryTokenStore:
    """Token'ları yalnızca süreç belleğinde tutar (varsayılan)."""

    def __init__(self) -> None:
        self._tokens: dict[str, Token] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> Token | None:
        with self._lock:
            return self._tokens.get(key)

    def set(self, key: str, token: Token) -> None:
        with self._lock:
            self._tokens[key] = token

    def delete(self, key: str) -> None:
        with self._lock:
            self._tokens.pop(key, None)


class FileTokenStore:
    """Token'ları bir JSON dosyasında saklar; betikler ve CLI araçları için uygundur.

    Dosya yalnızca sahibinin okuyabileceği izinlerle (``0600``) ve atomik olarak yazılır.
    İçinde access/refresh token bulunduğu için bu dosyayı sürüm kontrolüne eklemeyin.
    """

    def __init__(self, path: str | os.PathLike[str]) -> None:
        self.path = Path(os.fspath(path)).expanduser()
        self._lock = threading.Lock()

    def _read(self) -> dict[str, Any]:
        try:
            raw = self.path.read_text(encoding="utf-8")
        except FileNotFoundError:
            return {}
        except OSError as exc:
            raise ConfigurationError(f"Token dosyası okunamadı: {self.path} ({exc})") from exc
        try:
            data = json.loads(raw) if raw.strip() else {}
        except json.JSONDecodeError:
            return {}
        return data if isinstance(data, dict) else {}

    def _write(self, data: Mapping[str, Any]) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(self.path.parent), prefix=".kt-token-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                json.dump(data, fh, indent=2)
            os.chmod(tmp, 0o600)
            os.replace(tmp, self.path)
        except BaseException:
            with contextlib.suppress(OSError):
                os.unlink(tmp)
            raise

    def get(self, key: str) -> Token | None:
        with self._lock:
            item = self._read().get(key)
        if not isinstance(item, dict) or "access_token" not in item:
            return None
        return Token.from_dict(item)

    def set(self, key: str, token: Token) -> None:
        with self._lock:
            data = self._read()
            data[key] = token.to_dict()
            self._write(data)

    def delete(self, key: str) -> None:
        with self._lock:
            data = self._read()
            if key in data:
                del data[key]
                self._write(data)
