"""Kuveyt Türk API Market ortamları (sandbox / production)."""

from __future__ import annotations

from dataclasses import dataclass

from .exceptions import ConfigurationError

__all__ = ["PRODUCTION", "SANDBOX", "Environment", "resolve_environment"]


@dataclass(frozen=True)
class Environment:
    """Bir ortamın identity (OAuth2) ve gateway (API) adresleri.

    Hazır ortamlar yetmezse kendi adreslerinizle bir ``Environment`` oluşturup
    istemciye verebilirsiniz::

        env = Environment("ozel", identity_url="https://...", gateway_url="https://...")
        kt = KuveytTurk(..., environment=env)
    """

    name: str
    identity_url: str
    gateway_url: str

    def __post_init__(self) -> None:
        object.__setattr__(self, "identity_url", self.identity_url.rstrip("/"))
        object.__setattr__(self, "gateway_url", self.gateway_url.rstrip("/"))

    @property
    def authorize_url(self) -> str:
        return f"{self.identity_url}/connect/authorize"

    @property
    def token_url(self) -> str:
        return f"{self.identity_url}/connect/token"


#: Test ortamı. Geliştirici portalında oluşturulan uygulamalar önce burada çalışır.
SANDBOX = Environment(
    name="sandbox",
    identity_url="https://prep-identity.kuveytturk.com.tr",
    gateway_url="https://prep-gateway.kuveytturk.com.tr",
)

#: Canlı ortam. Go-Live süreci onaylanmış uygulamalar içindir.
PRODUCTION = Environment(
    name="production",
    identity_url="https://identity.kuveytturk.com.tr",
    gateway_url="https://gateway.kuveytturk.com.tr",
)

_BY_NAME = {
    "sandbox": SANDBOX,
    "test": SANDBOX,
    "prep": SANDBOX,
    "production": PRODUCTION,
    "prod": PRODUCTION,
    "live": PRODUCTION,
}


def resolve_environment(environment: str | Environment) -> Environment:
    """``"sandbox"`` / ``"production"`` gibi bir adı ya da hazır bir nesneyi ``Environment``'a çevirir."""
    if isinstance(environment, Environment):
        return environment
    try:
        return _BY_NAME[environment.strip().lower()]
    except (KeyError, AttributeError):
        raise ConfigurationError(
            f"Bilinmeyen ortam: {environment!r}. 'sandbox', 'production' ya da bir Environment nesnesi verin."
        ) from None
