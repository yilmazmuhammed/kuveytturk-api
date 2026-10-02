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

    def hgs_product_information(
        self,
        *,
        plate_no: str,
        barcodeno: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """HGS Product Information.

        ``POST /v1/hgs/product-info``

        Kapsam: ``public`` · Akış: client credentials

        This API takes plate number and HGS barcode number as request parameters and returns the
        product details of the related HGS barcode. The response includes barcode number, plate
        number, balance, product status, cancellation date, sales date, vehicle class, and
        payment type information.

        Args:
            plate_no: (``plateNo``, gövde, zorunlu) Represents the plate number of the vehicle.
            barcodeno: (gövde, zorunlu) Represents the HGS barcode number.

        Yanıt alanları: barcodeNo, plateNo, balance, productStatusDescription, cancelDate,
        salesDate, vehicleClass, paymentType

        Doküman: https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-product-information
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
            "/v1/hgs/product-info",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def hgs_usage_transactions(
        self,
        *,
        plate_no: str,
        barcode_no: str,
        start: str,
        end: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """HGS Usage Transactions.

        ``POST /v1/hgs/usage-transactions``

        Kapsam: ``public`` · Akış: client credentials

        This API returns HGS usage transaction information for the customer. It takes plate
        number, HGS barcode number, start date, and end date as request parameters. The response
        includes order number, entry and exit date/time, entry and exit locations, description,
        and amount information.

        Args:
            plate_no: (``plateNo``, gövde, zorunlu) Represents the plate number of the vehicle.
            barcode_no: (``barcodeNo``, gövde, zorunlu) Represents the HGS barcode number.
            start: (gövde, zorunlu) Represents the start date for querying HGS usage
                transactions.
            end: (gövde, zorunlu) Represents the end date for querying HGS usage transactions.

        Yanıt alanları: OrderNo, entryDateTime, exitDateTime, entryLocation, exitLocation,
        description, amount

        Doküman: https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-usage-transactions
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "plateNo": plate_no,
                "barcodeNo": barcode_no,
                "start": start,
                "end": end,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/hgs/usage-transactions",
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

    async def hgs_product_information(
        self,
        *,
        plate_no: str,
        barcodeno: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """HGS Product Information.

        ``POST /v1/hgs/product-info``

        Kapsam: ``public`` · Akış: client credentials

        This API takes plate number and HGS barcode number as request parameters and returns the
        product details of the related HGS barcode. The response includes barcode number, plate
        number, balance, product status, cancellation date, sales date, vehicle class, and
        payment type information.

        Args:
            plate_no: (``plateNo``, gövde, zorunlu) Represents the plate number of the vehicle.
            barcodeno: (gövde, zorunlu) Represents the HGS barcode number.

        Yanıt alanları: barcodeNo, plateNo, balance, productStatusDescription, cancelDate,
        salesDate, vehicleClass, paymentType

        Doküman: https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-product-information
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
            "/v1/hgs/product-info",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def hgs_usage_transactions(
        self,
        *,
        plate_no: str,
        barcode_no: str,
        start: str,
        end: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """HGS Usage Transactions.

        ``POST /v1/hgs/usage-transactions``

        Kapsam: ``public`` · Akış: client credentials

        This API returns HGS usage transaction information for the customer. It takes plate
        number, HGS barcode number, start date, and end date as request parameters. The response
        includes order number, entry and exit date/time, entry and exit locations, description,
        and amount information.

        Args:
            plate_no: (``plateNo``, gövde, zorunlu) Represents the plate number of the vehicle.
            barcode_no: (``barcodeNo``, gövde, zorunlu) Represents the HGS barcode number.
            start: (gövde, zorunlu) Represents the start date for querying HGS usage
                transactions.
            end: (gövde, zorunlu) Represents the end date for querying HGS usage transactions.

        Yanıt alanları: OrderNo, entryDateTime, exitDateTime, entryLocation, exitLocation,
        description, amount

        Doküman: https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-usage-transactions
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "plateNo": plate_no,
                "barcodeNo": barcode_no,
                "start": start,
                "end": end,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/hgs/usage-transactions",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
