"""Uç nokta gruplarının (kaynakların) tabanı. Üretilen modüller bunu kullanır."""

from __future__ import annotations

import datetime as _dt
from collections.abc import Mapping
from decimal import Decimal
from typing import TYPE_CHECKING, Any, TypeVar, Union

if TYPE_CHECKING:
    from ..async_client import AsyncKuveytTurk
    from ..client import KuveytTurk

__all__ = ["AsyncResource", "DateLike", "Number", "Resource", "ResourceHost", "merge"]

R = TypeVar("R")

#: Parasal ve sayısal alanlar. ``Decimal`` JSON'a sayı olarak yazılır.
Number = Union[int, float, Decimal]
#: Tarih alanları: ``date``/``datetime`` ISO 8601'e çevrilir; hazır metin olduğu gibi gönderilir.
DateLike = Union[_dt.datetime, _dt.date, str]


class Resource:
    """Senkron istemciye bağlı uç nokta grubu."""

    def __init__(self, client: KuveytTurk) -> None:
        self._client = client


class AsyncResource:
    """Asenkron istemciye bağlı uç nokta grubu."""

    def __init__(self, client: AsyncKuveytTurk) -> None:
        self._client = client


class ResourceHost:
    """İstemcilerin kaynak nesnelerini ilk erişimde oluşturup saklamasını sağlar."""

    def _resource(self, name: str, factory: type[R]) -> R:
        cache: dict[str, Any] = self.__dict__.setdefault("_resource_cache", {})
        if name not in cache:
            cache[name] = factory(self)  # type: ignore[call-arg]
        resource: R = cache[name]
        return resource


def merge(params: Mapping[str, Any], extra: Mapping[str, Any] | None) -> dict[str, Any]:
    """Verilmeyen (``None``) parametreleri atar ve ``extra_*`` ile gelenleri ekler."""
    merged = {key: value for key, value in params.items() if value is not None}
    if extra:
        merged.update(extra)
    return merged
