"""Kredi kartı işlemleri uç noktaları (``kt.cards``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncCards", "Cards"]


class Cards(Resource):
    """Kredi kartı işlemleri - ``kt.cards``."""

    def credit_card_list_v3(
        self,
        *,
        customer_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Credit Card List V3.

        ``GET /v3/creditcard/cardlist``

        Kapsam: ``cards`` · Akış: client credentials

        This API is used to retrieve the credit card list for the customer. The response returns
        card information such as masked card number, shadow card number, expiration date, card
        holder name, card type and supplementary card type.

        Args:
            customer_number: (``customerNumber``, sorgu) Customer number for which the credit
                card list will be retrieved.

        Yanıt alanları: cardList, maskedCardNumber, shadowCardNumber, expireDate, ownerName,
        cardType, supplementaryCardType

        Doküman: https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-list-v3
        """
        _query = merge(
            {
                "customerNumber": customer_number,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v3/creditcard/cardlist",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def credit_card_money_transfer(
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
        """Credit Card Money Transfer.

        ``POST /v1/moneytransfer/creditcardmoneytransfer``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to initiate a money transfer transaction from a customer account to a
        credit card. The customer account number is retrieved from the authorization context.
        The request includes sender account suffix, receiver account information, transfer
        amount, transfer description and transfer type. The response returns the transaction
        execution reference and the created money transfer transaction ID.

        Args:
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Sender account
                suffix number from which the money transfer amount will be withdrawn.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Receiver
                account number associated with the credit card money transfer.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Receiver
                account suffix associated with the credit card money transfer.
            money_transfer_description: (``moneyTransferDescription``, gövde) Description or
                comment added to the money transfer transaction.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Amount that will be
                transferred.
            transfer_type: (``transferType``, gövde, zorunlu) Money transfer type used to
                identify the transfer scenario.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-money-transfer
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
        return self._client.request(
            "POST",
            "/v1/moneytransfer/creditcardmoneytransfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def credit_card_transactions_list_v3(
        self,
        *,
        cardnumber: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Credit Card Transactions List V3.

        ``GET /v3/creditcard/{cardnumber}/transactions``

        Kapsam: ``cards`` · Akış: client credentials

        This API is used to retrieve credit card transaction information for the specified card
        number. The response includes pending provision transactions and current credit card
        transactions.

        Args:
            cardnumber: (yol, zorunlu) Credit card number for which transaction information will
                be retrieved. This value is sent as a route parameter.

        Yanıt alanları: cardPendingProvisionInfoResponseModel,
        creditCardStatementTransactionType, amount, message, transactionDate, transactionHour,
        fecCode, domesticAmount, originalAmount, mccGroupCode,
        currentTransactionInfoResponseModel, transactionId, category, currencyDef,
        earnedGoldPoint, installmentNumber, isTransactionRefund, isTrnIncludeInstallment,
        mechantName, shadowCardNumber, transactionAmount, transactionTime, bkmUniqueMerchantId,
        totalInstallmentAmount, provisionNumber, errors, executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-transactions-list-v3
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v3/creditcard/{cardnumber}/transactions",
            scope="cards",
            flow="client_credentials",
            path_params={"cardnumber": cardnumber},
            query=_query,
            options=request_options,
        )


class AsyncCards(AsyncResource):
    """Kredi kartı işlemleri (asenkron) - ``kt.cards``."""

    async def credit_card_list_v3(
        self,
        *,
        customer_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Credit Card List V3.

        ``GET /v3/creditcard/cardlist``

        Kapsam: ``cards`` · Akış: client credentials

        This API is used to retrieve the credit card list for the customer. The response returns
        card information such as masked card number, shadow card number, expiration date, card
        holder name, card type and supplementary card type.

        Args:
            customer_number: (``customerNumber``, sorgu) Customer number for which the credit
                card list will be retrieved.

        Yanıt alanları: cardList, maskedCardNumber, shadowCardNumber, expireDate, ownerName,
        cardType, supplementaryCardType

        Doküman: https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-list-v3
        """
        _query = merge(
            {
                "customerNumber": customer_number,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v3/creditcard/cardlist",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def credit_card_money_transfer(
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
        """Credit Card Money Transfer.

        ``POST /v1/moneytransfer/creditcardmoneytransfer``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to initiate a money transfer transaction from a customer account to a
        credit card. The customer account number is retrieved from the authorization context.
        The request includes sender account suffix, receiver account information, transfer
        amount, transfer description and transfer type. The response returns the transaction
        execution reference and the created money transfer transaction ID.

        Args:
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Sender account
                suffix number from which the money transfer amount will be withdrawn.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Receiver
                account number associated with the credit card money transfer.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Receiver
                account suffix associated with the credit card money transfer.
            money_transfer_description: (``moneyTransferDescription``, gövde) Description or
                comment added to the money transfer transaction.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Amount that will be
                transferred.
            transfer_type: (``transferType``, gövde, zorunlu) Money transfer type used to
                identify the transfer scenario.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-money-transfer
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
        return await self._client.request(
            "POST",
            "/v1/moneytransfer/creditcardmoneytransfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def credit_card_transactions_list_v3(
        self,
        *,
        cardnumber: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Credit Card Transactions List V3.

        ``GET /v3/creditcard/{cardnumber}/transactions``

        Kapsam: ``cards`` · Akış: client credentials

        This API is used to retrieve credit card transaction information for the specified card
        number. The response includes pending provision transactions and current credit card
        transactions.

        Args:
            cardnumber: (yol, zorunlu) Credit card number for which transaction information will
                be retrieved. This value is sent as a route parameter.

        Yanıt alanları: cardPendingProvisionInfoResponseModel,
        creditCardStatementTransactionType, amount, message, transactionDate, transactionHour,
        fecCode, domesticAmount, originalAmount, mccGroupCode,
        currentTransactionInfoResponseModel, transactionId, category, currencyDef,
        earnedGoldPoint, installmentNumber, isTransactionRefund, isTrnIncludeInstallment,
        mechantName, shadowCardNumber, transactionAmount, transactionTime, bkmUniqueMerchantId,
        totalInstallmentAmount, provisionNumber, errors, executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-transactions-list-v3
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v3/creditcard/{cardnumber}/transactions",
            scope="cards",
            flow="client_credentials",
            path_params={"cardnumber": cardnumber},
            query=_query,
            options=request_options,
        )
