"""Döviz işlemleri uç noktaları (``kt.fx``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncFx", "Fx"]


class Fx(Resource):
    """Döviz işlemleri - ``kt.fx``."""

    def fx_currency_buy(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        buy_rate: Number,
        exchange_amount: Number,
        corporate_web_user_name: str | None = None,
        tl_amount: Number | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency Buy.

        ``POST /v1/fx/buy``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to perform a foreign exchange buy transaction. The customer account
        number and language information are retrieved from the authorization context. The
        request includes source account suffix, target account suffix, corporate web user name,
        buy rate, foreign currency amount and TL amount. The response returns transaction
        amount, currency amount, applied FX rate, tax information and execution reference
        information.

        Args:
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Source account suffix
                from which the TL amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Target account suffix where
                the purchased foreign currency will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde) Corporate web user name
                used to perform the transaction.
            buy_rate: (``BuyRate``, gövde, zorunlu) Foreign exchange buy rate used for the
                transaction.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of foreign currency to
                be purchased.
            tl_amount: (``TLAmount``, gövde) TL amount of the transaction.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate, TaxFecCode, TaxAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-buy
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "BuyRate": buy_rate,
                "ExchangeAmount": exchange_amount,
                "TLAmount": tl_amount,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/fx/buy",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def fx_currency_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency List.

        ``GET /v1/data/fecs``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve currency information. The response returns currency details
        such as ISO code, international code, FEC name, FEC code, FEC group and FEC ID.

        Yanıt alanları: isoCode, internationalCode, name, code, group, id

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/data/fecs",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def fx_currency_rates(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency Rates.

        ``GET /v2/fx/rates``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve foreign exchange rates for the customer account associated
        with the client configuration. The response returns currency name, currency code, buy
        rate, sell rate and spread status information.

        Yanıt alanları: name, fxCode, buyRate, sellRate, isSpreadApplied

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-rates
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v2/fx/rates",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def fx_currency_sell(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        sell_rate: Number,
        exchange_amount: Number,
        corporate_web_user_name: str | None = None,
        tl_amount: Number | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency Sell.

        ``POST /v1/fx/sell``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to perform a foreign exchange sell transaction. The customer account
        number and language information are retrieved from the authorization context. The
        request includes source account suffix, target account suffix, corporate web user name,
        sell rate, foreign currency amount and TL amount. The response returns transaction
        amount, currency amount, applied FX rate and execution reference information.

        Args:
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Source foreign currency
                account suffix from which the exchange amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Target account suffix where
                the TL amount will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde) Corporate web user name
                used to perform the transaction.
            sell_rate: (``SellRate``, gövde, zorunlu) Foreign exchange sell rate used for the
                transaction.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of foreign currency to
                be sold.
            tl_amount: (``TLAmount``, gövde) TL amount of the transaction.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-sell
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "SellRate": sell_rate,
                "ExchangeAmount": exchange_amount,
                "TLAmount": tl_amount,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/fx/sell",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def fx_transaction_history(
        self,
        *,
        sender_account_suffix: int,
        receiver_account_number: int,
        receiver_account_suffix: int,
        money_transfer_amount: Number,
        transfer_type: int,
        money_transfer_description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Transaction History.

        ``POST /v1/fx/fxtransactions``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to initiate an internal money transfer transaction based on the
        customer account number from the authorization context. The request contains money
        transfer contract information including sender account suffix, receiver account
        information, transfer amount, transfer description and transfer type. The response
        returns the transaction execution reference and the created money transfer transaction
        ID.

        Args:
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Sender account
                suffix number from which the money transfer amount will be withdrawn.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Receiver
                customer account number to which the money transfer will be sent.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Receiver
                account suffix number to which the money transfer will be sent.
            money_transfer_description: (``moneyTransferDescription``, gövde) Description or
                comment added to the money transfer transaction.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Amount that will be
                transferred.
            transfer_type: (``transferType``, gövde, zorunlu) Money transfer type used to
                identify the transfer scenario.

        Gövde alanları istekte ``request`` -> ``moneyTransferContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-transaction-history
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "senderAccountSuffix": sender_account_suffix,
                "receiverAccountNumber": receiver_account_number,
                "receiverAccountSuffix": receiver_account_suffix,
                "moneyTransferDescription": money_transfer_description,
                "moneyTransferAmount": money_transfer_amount,
                "transferType": transfer_type,
            },
            extra_body,
        )
        _body = {"moneyTransferContract": _body}
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/fx/fxtransactions",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncFx(AsyncResource):
    """Döviz işlemleri (asenkron) - ``kt.fx``."""

    async def fx_currency_buy(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        buy_rate: Number,
        exchange_amount: Number,
        corporate_web_user_name: str | None = None,
        tl_amount: Number | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency Buy.

        ``POST /v1/fx/buy``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to perform a foreign exchange buy transaction. The customer account
        number and language information are retrieved from the authorization context. The
        request includes source account suffix, target account suffix, corporate web user name,
        buy rate, foreign currency amount and TL amount. The response returns transaction
        amount, currency amount, applied FX rate, tax information and execution reference
        information.

        Args:
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Source account suffix
                from which the TL amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Target account suffix where
                the purchased foreign currency will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde) Corporate web user name
                used to perform the transaction.
            buy_rate: (``BuyRate``, gövde, zorunlu) Foreign exchange buy rate used for the
                transaction.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of foreign currency to
                be purchased.
            tl_amount: (``TLAmount``, gövde) TL amount of the transaction.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate, TaxFecCode, TaxAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-buy
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "BuyRate": buy_rate,
                "ExchangeAmount": exchange_amount,
                "TLAmount": tl_amount,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/fx/buy",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def fx_currency_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency List.

        ``GET /v1/data/fecs``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve currency information. The response returns currency details
        such as ISO code, international code, FEC name, FEC code, FEC group and FEC ID.

        Yanıt alanları: isoCode, internationalCode, name, code, group, id

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/data/fecs",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def fx_currency_rates(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency Rates.

        ``GET /v2/fx/rates``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve foreign exchange rates for the customer account associated
        with the client configuration. The response returns currency name, currency code, buy
        rate, sell rate and spread status information.

        Yanıt alanları: name, fxCode, buyRate, sellRate, isSpreadApplied

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-rates
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v2/fx/rates",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def fx_currency_sell(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        sell_rate: Number,
        exchange_amount: Number,
        corporate_web_user_name: str | None = None,
        tl_amount: Number | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Currency Sell.

        ``POST /v1/fx/sell``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to perform a foreign exchange sell transaction. The customer account
        number and language information are retrieved from the authorization context. The
        request includes source account suffix, target account suffix, corporate web user name,
        sell rate, foreign currency amount and TL amount. The response returns transaction
        amount, currency amount, applied FX rate and execution reference information.

        Args:
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Source foreign currency
                account suffix from which the exchange amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Target account suffix where
                the TL amount will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde) Corporate web user name
                used to perform the transaction.
            sell_rate: (``SellRate``, gövde, zorunlu) Foreign exchange sell rate used for the
                transaction.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of foreign currency to
                be sold.
            tl_amount: (``TLAmount``, gövde) TL amount of the transaction.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-sell
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "SellRate": sell_rate,
                "ExchangeAmount": exchange_amount,
                "TLAmount": tl_amount,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/fx/sell",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def fx_transaction_history(
        self,
        *,
        sender_account_suffix: int,
        receiver_account_number: int,
        receiver_account_suffix: int,
        money_transfer_amount: Number,
        transfer_type: int,
        money_transfer_description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX Transaction History.

        ``POST /v1/fx/fxtransactions``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to initiate an internal money transfer transaction based on the
        customer account number from the authorization context. The request contains money
        transfer contract information including sender account suffix, receiver account
        information, transfer amount, transfer description and transfer type. The response
        returns the transaction execution reference and the created money transfer transaction
        ID.

        Args:
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Sender account
                suffix number from which the money transfer amount will be withdrawn.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Receiver
                customer account number to which the money transfer will be sent.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Receiver
                account suffix number to which the money transfer will be sent.
            money_transfer_description: (``moneyTransferDescription``, gövde) Description or
                comment added to the money transfer transaction.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Amount that will be
                transferred.
            transfer_type: (``transferType``, gövde, zorunlu) Money transfer type used to
                identify the transfer scenario.

        Gövde alanları istekte ``request`` -> ``moneyTransferContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-transaction-history
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "senderAccountSuffix": sender_account_suffix,
                "receiverAccountNumber": receiver_account_number,
                "receiverAccountSuffix": receiver_account_suffix,
                "moneyTransferDescription": money_transfer_description,
                "moneyTransferAmount": money_transfer_amount,
                "transferType": transfer_type,
            },
            extra_body,
        )
        _body = {"moneyTransferContract": _body}
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/fx/fxtransactions",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
