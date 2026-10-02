"""MoneyGram uç noktaları (``kt.moneygram``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncMoneygram", "Moneygram"]


class Moneygram(Resource):
    """MoneyGram - ``kt.moneygram``."""

    def money_gram_country_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Country List.

        ``GET /v1/moneygram/countrylist``

        Kapsam: ``public`` · Akış: client credentials

        &lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and
        response models may change over time. &lt;/div&gt; Returns the list of countries within
        MoneyGram Payment System.

        Yanıt alanları: countryCode, countryName, countryNameTR, baseReceiveCurrency

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-country-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/moneygram/countrylist",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def money_gram_currency_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Currency List.

        ``GET /v1/moneygram/currencylist``

        Kapsam: ``public`` · Akış: client credentials

        &lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and
        response models may change over time. &lt;/div&gt; Returns the list of currencies of
        interested countries within Moneygram Payment System.

        Yanıt alanları: currencyCode, currencyName, currencyNameTR

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-currency-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/moneygram/currencylist",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def money_gram_get_fee(
        self,
        *,
        receive_country: str,
        send_currency: str,
        amount: Number,
        choice_type: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Get Fee.

        ``POST /v1/moneygram/getfee``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        Get fee results. Countries can pay only with allowed currencies. In order to proceed the
        transfer, sender must select payment type accordibg these results. The parameters sent
        include receiveCountry, amount, and choiceType.

        Args:
            receive_country: (``receiveCountry``, gövde, zorunlu) Indicates receive country code
                info.
            send_currency: (``sendCurrency``, gövde, zorunlu) Indicates send currency code info.
            amount: (gövde, zorunlu) Amount that will be sent.
            choice_type: (``choiceType``, gövde, zorunlu) Fee type according to send amount.

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-get-fee
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "receiveCountry": receive_country,
                "sendCurrency": send_currency,
                "amount": amount,
                "choiceType": choice_type,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/moneygram/getfee",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def money_gram_query_fee(
        self,
        *,
        receive_country: str,
        amount: Number,
        choice_type: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Query Fee.

        ``GET /v1/moneygram/queryfee``

        Kapsam: ``transfers`` · Akış: client credentials

        Get fee results. Countries can pay only with allowed currencies. In order to proceed the
        transfer, sender must select payment type accordibg these results. The parameters sent
        include receiveCountry, amount, and choiceType.

        Args:
            receive_country: (``receiveCountry``, sorgu, zorunlu) Indicates receive country code
                info.
            amount: (sorgu, zorunlu) Amount that will be sent.
            choice_type: (``choiceType``, sorgu, zorunlu) Fee type according to send amount.

        Yanıt alanları: sendAmount, feeAmount, sendCurrency, totalAmount, validReceiveAmount,
        validReceiveCurrency, validExchangeRate, receiveCountryName, deliveryOption,
        deliveryOptionNameTR

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-fee
        """
        _query = merge(
            {
                "receiveCountry": receive_country,
                "amount": amount,
                "choiceType": choice_type,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/moneygram/queryfee",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def money_gram_query_reference(
        self,
        *,
        reference_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Query Reference.

        ``POST /v1/moneygram/queryreference``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        According the reference number, returns detail informations about the money transfer.

        Args:
            reference_number: (``referenceNumber``, gövde, zorunlu) Transaction reference
                number.

        Yanıt alanları: ReferenceNumber, TransactionStatusTR, SenderFirstName, SenderLastName,
        ReceiverFirstName, ReceiverLastName, DateTimeSent, ReceiveAmount, ReceiveCurrency,
        SenderCountry, DeliveryOption, SenderHomePhone, SenderAddress, OriginalSendFee,
        OriginalExchangeRate, SenderCity, ReceiverCountry

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-reference
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumber": reference_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/moneygram/queryreference",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def money_gram_send(
        self,
        *,
        transaction_contract: Mapping[str, Any] | None = None,
        sender_customer: Mapping[str, Any] | None = None,
        receiver_customer: Mapping[str, Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Send.

        ``POST /v1/moneygram/send``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        According the customer information, sender person can send money to countries which
        moneygram payment system allows.In order to proceed the transfer, Kuveyt Turk sends a
        one-time-password via SMS to the customer and gives a transaction id to the developer,
        the customer enters the code to the third party app, and the third party app sends the
        id and the SMS code to Kuveyt Turk via “Moneygram Send” API.If the id and the sms codes
        match, then Kuveyt Turk authenticates the transaction.

        Args:
            transaction_contract: (``TransactionContract``, gövde)
            sender_customer: (``SenderCustomer``, gövde)
            receiver_customer: (``ReceiverCustomer``, gövde)

        Gövde alanları istekte ``MoneyGramTranContract`` -> ``SendMoneygramContract`` nesnesinin
        içine yerleştirilir.

        Yanıt alanları: ReferenceNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-send
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionContract": transaction_contract,
                "SenderCustomer": sender_customer,
                "ReceiverCustomer": receiver_customer,
            },
            extra_body,
        )
        _body = {"SendMoneygramContract": _body}
        _body = {"MoneyGramTranContract": _body}
        return self._client.request(
            "POST",
            "/v1/moneygram/send",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncMoneygram(AsyncResource):
    """MoneyGram (asenkron) - ``kt.moneygram``."""

    async def money_gram_country_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Country List.

        ``GET /v1/moneygram/countrylist``

        Kapsam: ``public`` · Akış: client credentials

        &lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and
        response models may change over time. &lt;/div&gt; Returns the list of countries within
        MoneyGram Payment System.

        Yanıt alanları: countryCode, countryName, countryNameTR, baseReceiveCurrency

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-country-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/moneygram/countrylist",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def money_gram_currency_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Currency List.

        ``GET /v1/moneygram/currencylist``

        Kapsam: ``public`` · Akış: client credentials

        &lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and
        response models may change over time. &lt;/div&gt; Returns the list of currencies of
        interested countries within Moneygram Payment System.

        Yanıt alanları: currencyCode, currencyName, currencyNameTR

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-currency-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/moneygram/currencylist",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def money_gram_get_fee(
        self,
        *,
        receive_country: str,
        send_currency: str,
        amount: Number,
        choice_type: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Get Fee.

        ``POST /v1/moneygram/getfee``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        Get fee results. Countries can pay only with allowed currencies. In order to proceed the
        transfer, sender must select payment type accordibg these results. The parameters sent
        include receiveCountry, amount, and choiceType.

        Args:
            receive_country: (``receiveCountry``, gövde, zorunlu) Indicates receive country code
                info.
            send_currency: (``sendCurrency``, gövde, zorunlu) Indicates send currency code info.
            amount: (gövde, zorunlu) Amount that will be sent.
            choice_type: (``choiceType``, gövde, zorunlu) Fee type according to send amount.

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-get-fee
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "receiveCountry": receive_country,
                "sendCurrency": send_currency,
                "amount": amount,
                "choiceType": choice_type,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/moneygram/getfee",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def money_gram_query_fee(
        self,
        *,
        receive_country: str,
        amount: Number,
        choice_type: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Query Fee.

        ``GET /v1/moneygram/queryfee``

        Kapsam: ``transfers`` · Akış: client credentials

        Get fee results. Countries can pay only with allowed currencies. In order to proceed the
        transfer, sender must select payment type accordibg these results. The parameters sent
        include receiveCountry, amount, and choiceType.

        Args:
            receive_country: (``receiveCountry``, sorgu, zorunlu) Indicates receive country code
                info.
            amount: (sorgu, zorunlu) Amount that will be sent.
            choice_type: (``choiceType``, sorgu, zorunlu) Fee type according to send amount.

        Yanıt alanları: sendAmount, feeAmount, sendCurrency, totalAmount, validReceiveAmount,
        validReceiveCurrency, validExchangeRate, receiveCountryName, deliveryOption,
        deliveryOptionNameTR

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-fee
        """
        _query = merge(
            {
                "receiveCountry": receive_country,
                "amount": amount,
                "choiceType": choice_type,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/moneygram/queryfee",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def money_gram_query_reference(
        self,
        *,
        reference_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Query Reference.

        ``POST /v1/moneygram/queryreference``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        According the reference number, returns detail informations about the money transfer.

        Args:
            reference_number: (``referenceNumber``, gövde, zorunlu) Transaction reference
                number.

        Yanıt alanları: ReferenceNumber, TransactionStatusTR, SenderFirstName, SenderLastName,
        ReceiverFirstName, ReceiverLastName, DateTimeSent, ReceiveAmount, ReceiveCurrency,
        SenderCountry, DeliveryOption, SenderHomePhone, SenderAddress, OriginalSendFee,
        OriginalExchangeRate, SenderCity, ReceiverCountry

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-reference
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumber": reference_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/moneygram/queryreference",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def money_gram_send(
        self,
        *,
        transaction_contract: Mapping[str, Any] | None = None,
        sender_customer: Mapping[str, Any] | None = None,
        receiver_customer: Mapping[str, Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """MoneyGram Send.

        ``POST /v1/moneygram/send``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        According the customer information, sender person can send money to countries which
        moneygram payment system allows.In order to proceed the transfer, Kuveyt Turk sends a
        one-time-password via SMS to the customer and gives a transaction id to the developer,
        the customer enters the code to the third party app, and the third party app sends the
        id and the SMS code to Kuveyt Turk via “Moneygram Send” API.If the id and the sms codes
        match, then Kuveyt Turk authenticates the transaction.

        Args:
            transaction_contract: (``TransactionContract``, gövde)
            sender_customer: (``SenderCustomer``, gövde)
            receiver_customer: (``ReceiverCustomer``, gövde)

        Gövde alanları istekte ``MoneyGramTranContract`` -> ``SendMoneygramContract`` nesnesinin
        içine yerleştirilir.

        Yanıt alanları: ReferenceNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-send
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionContract": transaction_contract,
                "SenderCustomer": sender_customer,
                "ReceiverCustomer": receiver_customer,
            },
            extra_body,
        )
        _body = {"SendMoneygramContract": _body}
        _body = {"MoneyGramTranContract": _body}
        return await self._client.request(
            "POST",
            "/v1/moneygram/send",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )
