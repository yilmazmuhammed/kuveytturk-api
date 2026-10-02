from __future__ import annotations

import base64
import json
from collections.abc import Callable
from typing import Any

import httpx
import pytest
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from kuveytturk_api import AsyncKuveytTurk, KuveytTurk

IDENTITY = "https://prep-identity.kuveytturk.com.tr"
GATEWAY = "https://prep-gateway.kuveytturk.com.tr"

Handler = Callable[[httpx.Request], httpx.Response]


@pytest.fixture(scope="session")
def private_key() -> rsa.RSAPrivateKey:
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


@pytest.fixture(scope="session")
def private_pem(private_key: rsa.RSAPrivateKey) -> str:
    return private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    ).decode()


@pytest.fixture(scope="session")
def verify(private_key: rsa.RSAPrivateKey) -> Callable[[str, bytes], None]:
    """İmzanın verilen baytlara ait olduğunu public key ile doğrular (değilse hata fırlatır)."""
    public_key = private_key.public_key()

    def _verify(signature: str, signed: bytes) -> None:
        public_key.verify(base64.b64decode(signature), signed, padding.PKCS1v15(), hashes.SHA256())

    return _verify


def token_response(access_token: str = "tok-1", **extra: Any) -> httpx.Response:
    payload = {"access_token": access_token, "token_type": "Bearer", "expires_in": 3600}
    payload.update(extra)
    return httpx.Response(200, json=payload)


def envelope(value: Any = None, *, success: bool = True, results: Any = None) -> httpx.Response:
    return httpx.Response(200, json={"value": value, "success": success, "results": results or []})


class Recorder:
    """Sahte sunucu: token isteklerini yanıtlar, API isteklerini ``api`` işleyicisine verir."""

    def __init__(self, api: Handler | None = None, token: Handler | None = None) -> None:
        self.api = api or (lambda request: envelope({}))
        self.token = token or (lambda request: token_response())
        self.token_requests: list[httpx.Request] = []
        self.api_requests: list[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        if request.url.host == httpx.URL(IDENTITY).host:
            self.token_requests.append(request)
            return self.token(request)
        self.api_requests.append(request)
        return self.api(request)

    @property
    def last(self) -> httpx.Request:
        return self.api_requests[-1]

    def token_form(self, index: int = -1) -> dict[str, str]:
        return dict(httpx.QueryParams(self.token_requests[index].content.decode()))


@pytest.fixture
def make_client(private_pem: str, monkeypatch: pytest.MonkeyPatch) -> Callable[..., KuveytTurk]:
    monkeypatch.setattr("time.sleep", lambda seconds: None)

    def _make(recorder: Recorder, **kwargs: Any) -> KuveytTurk:
        kwargs.setdefault("redirect_uri", "http://localhost:8000/callback")
        return KuveytTurk(
            "client-id",
            "client-secret",
            private_pem,
            http_client=httpx.Client(transport=httpx.MockTransport(recorder)),
            **kwargs,
        )

    return _make


@pytest.fixture
def make_async_client(private_pem: str) -> Callable[..., AsyncKuveytTurk]:
    def _make(recorder: Recorder, **kwargs: Any) -> AsyncKuveytTurk:
        kwargs.setdefault("redirect_uri", "http://localhost:8000/callback")
        return AsyncKuveytTurk(
            "client-id",
            "client-secret",
            private_pem,
            http_client=httpx.AsyncClient(transport=httpx.MockTransport(recorder)),
            **kwargs,
        )

    return _make


def body_json(request: httpx.Request) -> Any:
    return json.loads(request.content)
