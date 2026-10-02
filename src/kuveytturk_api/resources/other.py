"""Diğer uç noktaları (``kt.other``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Number, Resource, merge

__all__ = ["AsyncOther", "Other"]


class Other(Resource):
    """Diğer - ``kt.other``."""

    def money_transfer_report_for_kuveyt_turk_investment_securities_inc(
        self,
        *,
        language_id: int,
        transaction_date: DateLike,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Money Transfer Report For Kuveyt Türk Investment Securities Inc..

        ``POST /v1/investment/report-for-account-activities``

        Kapsam: ``transfers`` · Akış: client credentials

        Retrieves the account activities report for Kuveyt Türk Investment Securities Inc.
        according to the provided language and transaction date. The response includes money
        transfer and account activity details such as transaction identifier, transfer type,
        amount, intermediary account number, currency, comment, and system date.

        Args:
            language_id: (``languageId``, gövde, zorunlu) Language identifier used for report
                content and descriptions.
            transaction_date: (``transactionDate``, gövde, zorunlu) Transaction date used to
                retrieve account activities.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: accountActivities, bankMoneyTransferId, transactionId, transferType,
        transferAmount, intermediaryAccountNumber, currency, comment, systemDate

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/money-transfer-report-for-kuveyt-turk-investment-securities-inc
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "languageId": language_id,
                "transactionDate": transaction_date,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/investment/report-for-account-activities",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def virtual_card_limit_update(
        self,
        *,
        credit_card_number: str,
        limit: Number,
        customer_id: int,
        language_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual Card Limit Update.

        ``POST /v1/cards/virtualcardlimitupdate``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This API updates the limit of a virtual credit card for the authenticated customer. >
        This API is in beta stage. Request and response models may change over time.

        Args:
            credit_card_number: (``CreditCardNumber``, gövde, zorunlu) Virtual credit card
                number whose limit will be updated.
            limit: (``Limit``, gövde, zorunlu) New limit amount to be assigned to the virtual
                credit card.
            customer_id: (``CustomerId``, gövde, zorunlu) Unique customer identifier.
            language_id: (``LanguageId``, gövde, zorunlu) Language identifier used for localized
                messages and responses.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/virtual-card-limit-update
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "CreditCardNumber": credit_card_number,
                "Limit": limit,
                "CustomerId": customer_id,
                "LanguageId": language_id,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/cards/virtualcardlimitupdate",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncOther(AsyncResource):
    """Diğer (asenkron) - ``kt.other``."""

    async def money_transfer_report_for_kuveyt_turk_investment_securities_inc(
        self,
        *,
        language_id: int,
        transaction_date: DateLike,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Money Transfer Report For Kuveyt Türk Investment Securities Inc..

        ``POST /v1/investment/report-for-account-activities``

        Kapsam: ``transfers`` · Akış: client credentials

        Retrieves the account activities report for Kuveyt Türk Investment Securities Inc.
        according to the provided language and transaction date. The response includes money
        transfer and account activity details such as transaction identifier, transfer type,
        amount, intermediary account number, currency, comment, and system date.

        Args:
            language_id: (``languageId``, gövde, zorunlu) Language identifier used for report
                content and descriptions.
            transaction_date: (``transactionDate``, gövde, zorunlu) Transaction date used to
                retrieve account activities.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: accountActivities, bankMoneyTransferId, transactionId, transferType,
        transferAmount, intermediaryAccountNumber, currency, comment, systemDate

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/money-transfer-report-for-kuveyt-turk-investment-securities-inc
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "languageId": language_id,
                "transactionDate": transaction_date,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/investment/report-for-account-activities",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def virtual_card_limit_update(
        self,
        *,
        credit_card_number: str,
        limit: Number,
        customer_id: int,
        language_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual Card Limit Update.

        ``POST /v1/cards/virtualcardlimitupdate``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This API updates the limit of a virtual credit card for the authenticated customer. >
        This API is in beta stage. Request and response models may change over time.

        Args:
            credit_card_number: (``CreditCardNumber``, gövde, zorunlu) Virtual credit card
                number whose limit will be updated.
            limit: (``Limit``, gövde, zorunlu) New limit amount to be assigned to the virtual
                credit card.
            customer_id: (``CustomerId``, gövde, zorunlu) Unique customer identifier.
            language_id: (``LanguageId``, gövde, zorunlu) Language identifier used for localized
                messages and responses.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/virtual-card-limit-update
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "CreditCardNumber": credit_card_number,
                "Limit": limit,
                "CustomerId": customer_id,
                "LanguageId": language_id,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/cards/virtualcardlimitupdate",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )
