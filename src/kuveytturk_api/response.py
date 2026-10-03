"""API yanıtlarının sarmalayıcısı.

Kuveyt Türk API'leri yanıtlarını çoğunlukla şu zarf içinde döndürür:

```json
{"value": {...}, "success": true, "results": [{"errorCode": "...", "errorMessage": "..."}]}
```

``APIResponse`` bu zarfı çözer; zarf kullanılmayan uç noktalarda da ham veriye
``APIResponse.data`` üzerinden erişilebilir.
"""

from __future__ import annotations

from collections.abc import Iterator, Mapping
from dataclasses import dataclass
from typing import Any

__all__ = ["APIResponse", "ResultItem"]


@dataclass(frozen=True)
class ResultItem:
    """Yanıtın ``results`` listesindeki bir kayıt (hata, uyarı ya da bilgi)."""

    error_code: str | None
    error_message: str | None
    raw: Mapping[str, Any]

    @classmethod
    def from_dict(cls, item: Mapping[str, Any]) -> ResultItem:
        code = item.get("errorCode", item.get("ErrorCode"))
        message = item.get("errorMessage", item.get("ErrorMessage"))
        return cls(
            error_code=None if code is None else str(code),
            error_message=None if message is None else str(message),
            raw=item,
        )

    def __str__(self) -> str:
        if self.error_code and self.error_message:
            return f"{self.error_code}: {self.error_message}"
        return self.error_message or self.error_code or ""


def parse_results(data: Any) -> list[ResultItem]:
    """Yanıt gövdesindeki ``results`` listesini (varsa) çözümler."""
    if not isinstance(data, Mapping):
        return []
    results = data.get("results", data.get("Results"))
    if not isinstance(results, list):
        return []
    return [ResultItem.from_dict(item) for item in results if isinstance(item, Mapping)]


class APIResponse:
    """Başarılı bir API çağrısının sonucu.

    Attributes:
        status_code: HTTP durum kodu.
        headers: Yanıt başlıkları.
        data: Çözümlenmiş gövdenin tamamı (JSON değilse metin, boşsa ``None``).

    Zarfın içindeki asıl veriye ``value`` ile ulaşılır. ``value`` bir sözlükse
    kısayol olarak ``response["alan"]``, ``"alan" in response`` ve
    ``response.get("alan")`` da kullanılabilir.
    """

    __slots__ = ("data", "headers", "status_code")

    def __init__(self, *, status_code: int, headers: Mapping[str, str], data: Any) -> None:
        self.status_code = status_code
        self.headers = headers
        self.data = data

    @property
    def value(self) -> Any:
        """Zarfın ``value`` alanı; zarf yoksa gövdenin kendisi."""
        if isinstance(self.data, Mapping) and "value" in self.data:
            return self.data["value"]
        return self.data

    @property
    def success(self) -> bool:
        """Zarfın ``success`` alanı; alan yoksa ``True`` (HTTP başarılı olduğu için)."""
        if isinstance(self.data, Mapping) and isinstance(self.data.get("success"), bool):
            return bool(self.data["success"])
        return True

    @property
    def results(self) -> list[ResultItem]:
        """Zarfın ``results`` listesi (uyarı/bilgi mesajları); yoksa boş liste."""
        return parse_results(self.data)

    @property
    def execution_reference_id(self) -> str | None:
        """Çağrıyı tekil olarak tanımlayan referans (yanıtta varsa)."""
        for container in (self.value, self.data):
            if isinstance(container, Mapping) and container.get("executionReferenceId") is not None:
                return str(container["executionReferenceId"])
        return None

    def __getitem__(self, key: Any) -> Any:
        return self.value[key]

    def __contains__(self, key: object) -> bool:
        value = self.value
        return isinstance(value, (Mapping, list)) and key in value

    def __iter__(self) -> Iterator[Any]:
        return iter(self.value)

    def get(self, key: str, default: Any = None) -> Any:
        value = self.value
        return value.get(key, default) if isinstance(value, Mapping) else default

    def __repr__(self) -> str:
        return f"<APIResponse [{self.status_code}] success={self.success}>"
