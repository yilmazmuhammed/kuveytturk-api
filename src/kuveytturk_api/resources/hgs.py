"""HGS servisleri uç noktaları (``kt.hgs``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Resource, merge

__all__ = ["AsyncHgs", "Hgs"]


class Hgs(Resource):
    """HGS servisleri - ``kt.hgs``."""

    def hgs_balance_information(
        self,
        *,
        plate_no: str,
        barcodeno: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """HGS Balance Information.

        ``POST /v1/hgs/balance-info``

        Kapsam: ``public`` · Akış: client credentials

        This API takes plate and HGS barcode numbers as request parameters and returns the HGS
        balance information in detail. The response includes barcode number, balance, system
        date, and transaction status information.

        Args:
            plate_no: (``plateNo``, gövde, zorunlu) Represents the plate number of the vehicle.
            barcodeno: (gövde, zorunlu) Represents the HGS barcode number.

        Yanıt alanları: barcodeNo, Status, balance, systemDate

        Doküman: https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-balance-information
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "plateNo": plate_no,
                "barcodeno": barcodeno,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/hgs/balance-info",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncHgs(AsyncResource):
    """HGS servisleri (asenkron) - ``kt.hgs``."""

    async def hgs_balance_information(
        self,
        *,
        plate_no: str,
        barcodeno: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """HGS Balance Information.

        ``POST /v1/hgs/balance-info``

        Kapsam: ``public`` · Akış: client credentials

        This API takes plate and HGS barcode numbers as request parameters and returns the HGS
        balance information in detail. The response includes barcode number, balance, system
        date, and transaction status information.

        Args:
            plate_no: (``plateNo``, gövde, zorunlu) Represents the plate number of the vehicle.
            barcodeno: (gövde, zorunlu) Represents the HGS barcode number.

        Yanıt alanları: barcodeNo, Status, balance, systemDate

        Doküman: https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-balance-information
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "plateNo": plate_no,
                "barcodeno": barcodeno,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/hgs/balance-info",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
