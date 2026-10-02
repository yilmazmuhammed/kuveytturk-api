"""Bilgi servisleri (şube, ATM, parametre sorguları...) uç noktaları (``kt.information``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Resource, merge

__all__ = ["AsyncInformation", "Information"]


class Information(Resource):
    """Bilgi servisleri (şube, ATM, parametre sorguları...) - ``kt.information``."""

    def central_notification(
        self,
        *,
        template_code: str,
        parameters: Sequence[Any] | None = None,
        request_json: str | None = None,
        request_type: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Central Notification.

        ``POST /v1/notification/sendInfEng``

        Kapsam: ``public`` · Akış: client credentials

        Sends a notification by using the provided template code, parameter list, request JSON,
        and request type. The response returns the notification operation identifier and
        operation result.

        Args:
            template_code: (``templateCode``, gövde, zorunlu) Template code used to generate and
                send the notification.
            parameters: (gövde) List of key-value parameters to be used in the notification
                template.
            request_json: (``requestJson``, gövde) JSON request content related to the
                notification operation.
            request_type: (``requestType``, gövde) Request type information used to classify or
                process the notification request.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "templateCode": template_code,
                "parameters": parameters,
                "requestJson": request_json,
                "requestType": request_type,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/notification/sendInfEng",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncInformation(AsyncResource):
    """Bilgi servisleri (şube, ATM, parametre sorguları...) (asenkron) - ``kt.information``."""

    async def central_notification(
        self,
        *,
        template_code: str,
        parameters: Sequence[Any] | None = None,
        request_json: str | None = None,
        request_type: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Central Notification.

        ``POST /v1/notification/sendInfEng``

        Kapsam: ``public`` · Akış: client credentials

        Sends a notification by using the provided template code, parameter list, request JSON,
        and request type. The response returns the notification operation identifier and
        operation result.

        Args:
            template_code: (``templateCode``, gövde, zorunlu) Template code used to generate and
                send the notification.
            parameters: (gövde) List of key-value parameters to be used in the notification
                template.
            request_json: (``requestJson``, gövde) JSON request content related to the
                notification operation.
            request_type: (``requestType``, gövde) Request type information used to classify or
                process the notification request.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "templateCode": template_code,
                "parameters": parameters,
                "requestJson": request_json,
                "requestType": request_type,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/notification/sendInfEng",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
