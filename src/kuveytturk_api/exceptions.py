"""Kütüphanenin fırlattığı tüm istisnalar.

Hiyerarşi::

    KuveytTurkError
    ├── ConfigurationError          eksik/hatalı yapılandırma
    ├── SignatureError              private key okunamadı / imza üretilemedi
    ├── TransportError              ağ hatası, zaman aşımı
    ├── AuthenticationError         token uç noktası hata döndü
    ├── AuthorizationRequiredError  kullanıcı girişi (authorization code) gerekiyor
    └── APIError                    API hata yanıtı döndü
        ├── BadRequestError         400 (imza hataları da 400 döner)
        ├── UnauthorizedError       401
        ├── ForbiddenError          403
        ├── NotFoundError           404
        ├── RateLimitError          429
        ├── ServerError             5xx
        └── BusinessError           HTTP 2xx ama ``success: false``
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .response import ResultItem

__all__ = [
    "APIError",
    "AuthenticationError",
    "AuthorizationRequiredError",
    "BadRequestError",
    "BusinessError",
    "ConfigurationError",
    "ForbiddenError",
    "KuveytTurkError",
    "NotFoundError",
    "RateLimitError",
    "ServerError",
    "SignatureError",
    "TransportError",
    "UnauthorizedError",
]


class KuveytTurkError(Exception):
    """Kütüphanedeki tüm istisnaların tabanı."""


class ConfigurationError(KuveytTurkError):
    """Eksik ya da hatalı yapılandırma (client_id, private key, redirect_uri...)."""


class SignatureError(KuveytTurkError):
    """Private key yüklenemedi ya da imza üretilemedi."""


class TransportError(KuveytTurkError):
    """İstek sunucuya ulaşamadı (bağlantı hatası, zaman aşımı...)."""


class AuthenticationError(KuveytTurkError):
    """Identity sunucusu token vermeyi reddetti.

    Attributes:
        error: OAuth2 hata kodu (ör. ``invalid_client``, ``invalid_grant``).
        error_description: Sunucunun verdiği açıklama (varsa).
        status_code: HTTP durum kodu.
    """

    def __init__(
        self,
        message: str,
        *,
        error: str | None = None,
        error_description: str | None = None,
        status_code: int | None = None,
    ) -> None:
        super().__init__(message)
        self.error = error
        self.error_description = error_description
        self.status_code = status_code


class AuthorizationRequiredError(KuveytTurkError):
    """Uç nokta müşteri girişi (authorization code) istiyor ama geçerli kullanıcı token'ı yok."""

    def __init__(self, message: str, *, scope: str | None = None, user: str | None = None) -> None:
        super().__init__(message)
        self.scope = scope
        self.user = user


class APIError(KuveytTurkError):
    """API bir hata yanıtı döndürdü.

    Attributes:
        status_code: HTTP durum kodu.
        error_code: Yanıttaki ilk ``errorCode`` (varsa).
        error_message: Yanıttaki ilk ``errorMessage`` (varsa).
        results: Yanıtın ``results`` listesindeki tüm kayıtlar.
        body: Çözümlenmiş yanıt gövdesi (JSON değilse ham metin).
        method / url: Hataya yol açan istek.
    """

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        method: str,
        url: str,
        body: Any = None,
        results: list[ResultItem] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.method = method
        self.url = url
        self.body = body
        self.results: list[ResultItem] = results or []

    @property
    def error_code(self) -> str | None:
        return self.results[0].error_code if self.results else None

    @property
    def error_message(self) -> str | None:
        return self.results[0].error_message if self.results else None


class BadRequestError(APIError):
    """HTTP 400 — istek parametreleri hatalı ya da imza doğrulanamadı.

    Gateway imza hatalarını da 400 ile bildirir (``"Client signature validation error"``);
    bu durumda private key'in karşılığı olan public key'in portaldaki uygulamada kayıtlı
    olduğunu kontrol edin.
    """


class UnauthorizedError(APIError):
    """HTTP 401 — token geçersiz/süresi dolmuş ya da uç nokta başka bir akış istiyor.

    Müşteri girişi isteyen bir uç nokta client credentials token'ıyla çağrılırsa gateway
    ``"Invalid grant type. Authorization Code is required."`` mesajıyla 401 döner.
    """


class ForbiddenError(APIError):
    """HTTP 403 — token'ın kapsamı uç noktaya uymuyor (``"Invalid Scope"``) ya da yetki yok."""


class NotFoundError(APIError):
    """HTTP 404 — uç nokta (``"Path not found"``) ya da kaynak bulunamadı."""


class RateLimitError(APIError):
    """HTTP 429 — istek limiti aşıldı."""


class ServerError(APIError):
    """HTTP 5xx — Kuveyt Türk tarafında hata."""


class BusinessError(APIError):
    """HTTP başarılı ama yanıt zarfında ``success: false`` döndü."""
