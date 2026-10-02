"""Kuveyt Türk API Market için gayriresmî Python istemcisi.

Hızlı başlangıç::

    from kuveytturk_api import KuveytTurk

    kt = KuveytTurk(
        client_id="...",
        client_secret="...",
        private_key="private_key.pem",
        environment="sandbox",
    )
    print(kt.request("GET", "/v1/fx/rates", scope="public").value)

Asenkron kullanım için :class:`AsyncKuveytTurk`. İstek ve yanıtları görmek için
:func:`enable_logging` ya da ``KUVEYTTURK_LOG=debug`` ortam değişkeni.
"""

from ._base import DEFAULT_USER, Flow, RequestOptions
from ._logging import enable_from_environment as _enable_logging_from_environment
from ._logging import enable_logging
from ._version import __version__
from .async_client import AsyncAuth, AsyncKuveytTurk
from .client import Auth, KuveytTurk
from .environments import PRODUCTION, SANDBOX, Environment
from .exceptions import (
    APIError,
    AuthenticationError,
    AuthorizationRequiredError,
    BadRequestError,
    BusinessError,
    ConfigurationError,
    ForbiddenError,
    KuveytTurkError,
    NotFoundError,
    RateLimitError,
    ServerError,
    SignatureError,
    TransportError,
    UnauthorizedError,
)
from .response import APIResponse, ResultItem
from .signature import Signer, generate_key_pair
from .tokens import FileTokenStore, MemoryTokenStore, Token, TokenStore

__all__ = [
    "DEFAULT_USER",
    "PRODUCTION",
    "SANDBOX",
    "APIError",
    "APIResponse",
    "AsyncAuth",
    "AsyncKuveytTurk",
    "Auth",
    "AuthenticationError",
    "AuthorizationRequiredError",
    "BadRequestError",
    "BusinessError",
    "ConfigurationError",
    "Environment",
    "FileTokenStore",
    "Flow",
    "ForbiddenError",
    "KuveytTurk",
    "KuveytTurkError",
    "MemoryTokenStore",
    "NotFoundError",
    "RateLimitError",
    "RequestOptions",
    "ResultItem",
    "ServerError",
    "SignatureError",
    "Signer",
    "Token",
    "TokenStore",
    "TransportError",
    "UnauthorizedError",
    "__version__",
    "enable_logging",
    "generate_key_pair",
]

# KUVEYTTURK_LOG=debug (ya da info) verilmişse logları kod değiştirmeden açar.
_enable_logging_from_environment()
