"""SGK uç noktaları (``kt.sgk``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncSgk", "Sgk"]


class Sgk(Resource):
    """SGK - ``kt.sgk``."""

    def consume_insurance_queue(
        self,
        *,
        unique_id: str,
        business_key: Number,
        base64_data: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Consume Insurance Queue.

        ``POST /v1/insurance/consumeQueue``

        Kapsam: ``public`` · Akış: client credentials

        Consumes an insurance queue message by using the provided unique identifier, business
        key, and Base64 encoded data. The response indicates whether the queue consumption
        operation was completed successfully.

        Args:
            unique_id: (``UniqueId``, gövde, zorunlu) Unique identifier of the queue message.
            business_key: (``BusinessKey``, gövde, zorunlu) Business key associated with the
                queue message.
            base64_data: (``Base64Data``, gövde, zorunlu) Base64 encoded content of the queue
                message.

        Gövde alanları istekte ``QueueMessage`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sgk/consume-insurance-queue
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "UniqueId": unique_id,
                "BusinessKey": business_key,
                "Base64Data": base64_data,
            },
            extra_body,
        )
        _body = {"QueueMessage": _body}
        return self._client.request(
            "POST",
            "/v1/insurance/consumeQueue",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncSgk(AsyncResource):
    """SGK (asenkron) - ``kt.sgk``."""

    async def consume_insurance_queue(
        self,
        *,
        unique_id: str,
        business_key: Number,
        base64_data: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Consume Insurance Queue.

        ``POST /v1/insurance/consumeQueue``

        Kapsam: ``public`` · Akış: client credentials

        Consumes an insurance queue message by using the provided unique identifier, business
        key, and Base64 encoded data. The response indicates whether the queue consumption
        operation was completed successfully.

        Args:
            unique_id: (``UniqueId``, gövde, zorunlu) Unique identifier of the queue message.
            business_key: (``BusinessKey``, gövde, zorunlu) Business key associated with the
                queue message.
            base64_data: (``Base64Data``, gövde, zorunlu) Base64 encoded content of the queue
                message.

        Gövde alanları istekte ``QueueMessage`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sgk/consume-insurance-queue
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "UniqueId": unique_id,
                "BusinessKey": business_key,
                "Base64Data": base64_data,
            },
            extra_body,
        )
        _body = {"QueueMessage": _body}
        return await self._client.request(
            "POST",
            "/v1/insurance/consumeQueue",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
