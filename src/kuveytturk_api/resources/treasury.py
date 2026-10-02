"""Hazine servisleri (kıymetli maden, kur) uç noktaları (``kt.treasury``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncTreasury", "Treasury"]


class Treasury(Resource):
    """Hazine servisleri (kıymetli maden, kur) - ``kt.treasury``."""

    def fx_and_precious_metal_rates(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX and Precious Metal Rates.

        ``GET /v1/fx/rates``

        Kapsam: ``public`` · Akış: client credentials

        This API retrieves the current foreign exchange rates, including currency information,
        buy/sell rates and parity rates. Foreign exchange rates represent the bank's rates at
        the time the request is sent.

        Yanıt alanları: name, fxCode, fxId, buyRate, sellRate, parityBuyRate, paritySellRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metal-rates
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/fx/rates",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def fx_and_precious_metals_transaction_history(
        self,
        *,
        sender_account_suffix: int,
        receiver_account_number: int,
        receiver_account_suffix: int,
        money_transfer_description: str,
        money_transfer_amount: Number,
        transfer_type: int,
        cm_customer_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX and Precious Metals Transaction History.

        ``POST /v1/fx/fxtransactions``

        Kapsam: ``public`` · Akış: client credentials

        It carries out precious metal sales transactions.

        Args:
            cm_customer_id: (``cm:CustomerId``, gövde)
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Sender account
                suffix for the account from which the amount will be transferred.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Receiver
                account number to which the amount will be transferred.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Receiver
                account suffix for the target account.
            money_transfer_description: (``moneyTransferDescription``, gövde, zorunlu)
                Description of the money transfer transaction.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Amount to be
                transferred.
            transfer_type: (``transferType``, gövde, zorunlu) Transfer type value that
                identifies the transaction type.

        Gövde alanları istekte ``request`` -> ``moneyTransferContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metals-transaction-history
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cm:CustomerId": cm_customer_id,
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

    def precious_metal_buy(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        corporate_web_user_name: str,
        buy_rate: Number,
        exchange_amount: Number,
        cm_customer_id: int | None = None,
        cm_language_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Precious Metal Buy.

        ``POST /v1/preciousmetal/buy``

        Kapsam: ``public`` · Akış: client credentials

        Performs precious metal purchasing transactions. The request includes the source
        account, target precious metal account, corporate web user name, buy rate and precious
        metal amount. The response returns the transaction amount, currency amount, exchange
        rate and tax information for the completed transaction.

        Args:
            cm_customer_id: (``cm:CustomerId``, gövde)
            cm_language_id: (``cm:LanguageId``, gövde)
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Additional number of
                the account from which the precious metal purchase amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Additional number of the
                account to which the purchased precious metal will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde, zorunlu) Corporate web
                user name of the account owner performing the precious metal purchase transaction.
            buy_rate: (``BuyRate``, gövde, zorunlu) Exchange rate at which the precious metal
                will be purchased. This value is obtained from the exchange rate API.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of precious metal to be
                purchased.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate, TaxFecCode, TaxAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-buy
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cm:CustomerId": cm_customer_id,
                "cm:LanguageId": cm_language_id,
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "BuyRate": buy_rate,
                "ExchangeAmount": exchange_amount,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/preciousmetal/buy",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def precious_metal_rates(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Precious Metal Rates.

        ``GET /v1/preciousmetal/rates``

        Kapsam: ``public`` · Akış: client credentials

        A service for querying many common precious metal rates. Precious metal rates represent
        the bank's rates at the time the request is sent.

        Yanıt alanları: FxName, FxCode, BuyRate, SellRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-rates
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/preciousmetal/rates",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def precious_metal_sell(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        corporate_web_user_name: str,
        sell_rate: Number,
        exchange_amount: Number,
        cm_customer_id: int | None = None,
        cm_language_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Precious Metal Sell.

        ``POST /v1/preciousmetal/sell``

        Kapsam: ``public`` · Akış: client credentials

        Performs precious metal sales transactions. The request includes the source precious
        metal account, target account, corporate web user name, sell rate and precious metal
        amount. The response returns the transaction amount, currency amount and exchange rate
        for the completed transaction.

        Args:
            cm_customer_id: (``cm:CustomerId``, gövde)
            cm_language_id: (``cm:LanguageId``, gövde)
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Additional number of
                the account from which the precious metal amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Additional number of the
                account to which the sale amount will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde, zorunlu) Corporate web
                user name of the account owner performing the precious metal sale transaction.
            sell_rate: (``SellRate``, gövde, zorunlu) Exchange rate at which the precious metal
                will be sold. This value is obtained from the exchange rate API.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of precious metal to be
                sold.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-sell
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cm:CustomerId": cm_customer_id,
                "cm:LanguageId": cm_language_id,
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "SellRate": sell_rate,
                "ExchangeAmount": exchange_amount,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/preciousmetal/sell",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncTreasury(AsyncResource):
    """Hazine servisleri (kıymetli maden, kur) (asenkron) - ``kt.treasury``."""

    async def fx_and_precious_metal_rates(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX and Precious Metal Rates.

        ``GET /v1/fx/rates``

        Kapsam: ``public`` · Akış: client credentials

        This API retrieves the current foreign exchange rates, including currency information,
        buy/sell rates and parity rates. Foreign exchange rates represent the bank's rates at
        the time the request is sent.

        Yanıt alanları: name, fxCode, fxId, buyRate, sellRate, parityBuyRate, paritySellRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metal-rates
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/fx/rates",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def fx_and_precious_metals_transaction_history(
        self,
        *,
        sender_account_suffix: int,
        receiver_account_number: int,
        receiver_account_suffix: int,
        money_transfer_description: str,
        money_transfer_amount: Number,
        transfer_type: int,
        cm_customer_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """FX and Precious Metals Transaction History.

        ``POST /v1/fx/fxtransactions``

        Kapsam: ``public`` · Akış: client credentials

        It carries out precious metal sales transactions.

        Args:
            cm_customer_id: (``cm:CustomerId``, gövde)
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Sender account
                suffix for the account from which the amount will be transferred.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Receiver
                account number to which the amount will be transferred.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Receiver
                account suffix for the target account.
            money_transfer_description: (``moneyTransferDescription``, gövde, zorunlu)
                Description of the money transfer transaction.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Amount to be
                transferred.
            transfer_type: (``transferType``, gövde, zorunlu) Transfer type value that
                identifies the transaction type.

        Gövde alanları istekte ``request`` -> ``moneyTransferContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metals-transaction-history
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cm:CustomerId": cm_customer_id,
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

    async def precious_metal_buy(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        corporate_web_user_name: str,
        buy_rate: Number,
        exchange_amount: Number,
        cm_customer_id: int | None = None,
        cm_language_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Precious Metal Buy.

        ``POST /v1/preciousmetal/buy``

        Kapsam: ``public`` · Akış: client credentials

        Performs precious metal purchasing transactions. The request includes the source
        account, target precious metal account, corporate web user name, buy rate and precious
        metal amount. The response returns the transaction amount, currency amount, exchange
        rate and tax information for the completed transaction.

        Args:
            cm_customer_id: (``cm:CustomerId``, gövde)
            cm_language_id: (``cm:LanguageId``, gövde)
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Additional number of
                the account from which the precious metal purchase amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Additional number of the
                account to which the purchased precious metal will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde, zorunlu) Corporate web
                user name of the account owner performing the precious metal purchase transaction.
            buy_rate: (``BuyRate``, gövde, zorunlu) Exchange rate at which the precious metal
                will be purchased. This value is obtained from the exchange rate API.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of precious metal to be
                purchased.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate, TaxFecCode, TaxAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-buy
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cm:CustomerId": cm_customer_id,
                "cm:LanguageId": cm_language_id,
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "BuyRate": buy_rate,
                "ExchangeAmount": exchange_amount,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/preciousmetal/buy",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def precious_metal_rates(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Precious Metal Rates.

        ``GET /v1/preciousmetal/rates``

        Kapsam: ``public`` · Akış: client credentials

        A service for querying many common precious metal rates. Precious metal rates represent
        the bank's rates at the time the request is sent.

        Yanıt alanları: FxName, FxCode, BuyRate, SellRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-rates
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/preciousmetal/rates",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def precious_metal_sell(
        self,
        *,
        account_suffix_from: int,
        account_suffix_to: int,
        corporate_web_user_name: str,
        sell_rate: Number,
        exchange_amount: Number,
        cm_customer_id: int | None = None,
        cm_language_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Precious Metal Sell.

        ``POST /v1/preciousmetal/sell``

        Kapsam: ``public`` · Akış: client credentials

        Performs precious metal sales transactions. The request includes the source precious
        metal account, target account, corporate web user name, sell rate and precious metal
        amount. The response returns the transaction amount, currency amount and exchange rate
        for the completed transaction.

        Args:
            cm_customer_id: (``cm:CustomerId``, gövde)
            cm_language_id: (``cm:LanguageId``, gövde)
            account_suffix_from: (``AccountSuffixFrom``, gövde, zorunlu) Additional number of
                the account from which the precious metal amount will be withdrawn.
            account_suffix_to: (``AccountSuffixTo``, gövde, zorunlu) Additional number of the
                account to which the sale amount will be deposited.
            corporate_web_user_name: (``CorporateWebUserName``, gövde, zorunlu) Corporate web
                user name of the account owner performing the precious metal sale transaction.
            sell_rate: (``SellRate``, gövde, zorunlu) Exchange rate at which the precious metal
                will be sold. This value is obtained from the exchange rate API.
            exchange_amount: (``ExchangeAmount``, gövde, zorunlu) Amount of precious metal to be
                sold.

        Yanıt alanları: ExecutionReferenceId, FromFec, ToFec, TransactionAmount, CurrencyAmount,
        FxRate

        Doküman: https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-sell
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cm:CustomerId": cm_customer_id,
                "cm:LanguageId": cm_language_id,
                "AccountSuffixFrom": account_suffix_from,
                "AccountSuffixTo": account_suffix_to,
                "CorporateWebUserName": corporate_web_user_name,
                "SellRate": sell_rate,
                "ExchangeAmount": exchange_amount,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/preciousmetal/sell",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
