"""Para transferleri uç noktaları (``kt.transfers``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Number, Resource, merge

__all__ = ["AsyncTransfers", "Transfers"]


class Transfers(Resource):
    """Para transferleri - ``kt.transfers``."""

    def customer_iban_info_for_money_transfer(
        self,
        *,
        iban: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Iban Info for Money Transfer.

        ``GET /v1/moneytransfer/{iban}/customeribaninfo``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to retrieve customer account information associated with a given IBAN.
        The service returns masked customer name, bank name, bank ID and FEC information for the
        queried IBAN.

        Args:
            iban: (yol, zorunlu) IBAN number for which customer account information will be
                retrieved. This value is sent as a route parameter.

        Yanıt alanları: customerName, bankName, bankId, fec

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/customer-iban-info-for-money-transfer
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/moneytransfer/{iban}/customeribaninfo",
            scope="transfers",
            flow="client_credentials",
            path_params={"iban": iban},
            query=_query,
            options=request_options,
        )

    def internal_money_transfer(
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
        """Money Transfer (Veeraman).

        ``POST /v1/moneytransfer/interbankmoneytransfer``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to initiate an internal account-to-account money transfer transaction.
        The sender account number is retrieved from the customer information in the
        authorization context, and the request includes sender suffix, receiver account
        information, transfer amount, description and transfer type.

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

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-veeraman
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
            "/v1/moneytransfer/interbankmoneytransfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def money_transfer_payment_type(
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
        """Money Transfer Payment Type.

        ``POST /v1/moneytransfer/paymenttype``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to initiate an internal money transfer transaction based on the
        customer account number from the authorization context. The request includes sender
        account suffix, receiver account information, transfer amount, transfer description and
        transfer type. The response returns the transaction execution reference and the created
        money transfer transaction ID.

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

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-payment-type
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
            "/v1/moneytransfer/paymenttype",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def money_transfer_state(
        self,
        *,
        transfer_type: str,
        out_going_id: str | None = None,
        virman_key: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Money Transfer State.

        ``GET /v1/moneytransfer-state``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to check the current state of a money transfer transaction. The
        transaction can be queried by outGoingId for outgoing transfer types or by virmanKey for
        VIRMAN transactions. The transferType parameter determines which transaction type will
        be checked.

        Args:
            out_going_id: (``outGoingId``, sorgu) Outgoing money transfer ID used to query the
                transfer state. Required for transfer types other than VIRMAN.
            virman_key: (``virmanKey``, sorgu) Encrypted business key used to query VIRMAN
                transaction state. Required when transferType is VIRMAN.
            transfer_type: (``transferType``, sorgu, zorunlu) Money transfer type to be queried.
                Possible values include VIRMAN, HAVALE, FAST, POS and PÖS - EFT.

        Yanıt alanları: transferType, state, stateDescription

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-state
        """
        _query = merge(
            {
                "outGoingId": out_going_id,
                "virmanKey": virman_key,
                "transferType": transfer_type,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/moneytransfer-state",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def outgoing_money_transfer(
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
        """Para Transferi (Havale & EFT & FAST & Virman).

        ``POST /v1/moneytransfer/outgoingmoneytransfer``

        Kapsam: ``transfers`` · Akış: client credentials

        Bu API, authorization context ile ilişkili müşteri hesabından money transfer işlemi
        başlatmak için kullanılır. Servis; sender account bilgilerini, receiver account
        bilgilerini, transfer amount ve transfer type değerlerini doğrular, ardından ilgili
        money transfer transaction kaydını oluşturur.

        Args:
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Money transfer
                tutarının çekileceği sender account suffix numarasıdır.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Money transfer
                gönderilecek receiver customer account number değeridir.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Money transfer
                gönderilecek receiver account suffix numarasıdır.
            money_transfer_description: (``moneyTransferDescription``, gövde) Money transfer
                transaction için eklenen açıklama veya comment bilgisidir.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Transfer edilecek
                tutardır.
            transfer_type: (``transferType``, gövde, zorunlu) Transfer senaryosunu belirlemek
                için kullanılan money transfer type değeridir.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/para-transferleri/para-transferi-havale-eft-fast-virman
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
            "/v1/moneytransfer/outgoingmoneytransfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def outgoing_money_transfer_v2(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Outgoing Money Transfer V2.

        ``POST /v2/moneytransfer/outgoingmoneytransfer``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve account transaction statement information based on the
        customer account number from the authorization context. The request can be filtered by
        account suffix, item count, begin date and end date. The response returns account
        activity records including transaction date, description, amount, balance, currency
        code, transaction reference and transaction code information.

        Args:
            suffix: (gövde, zorunlu) Account suffix for which transaction records will be
                retrieved.
            item_count: (``itemCount``, gövde) Maximum number of account activity records to be
                returned.
            begin_date: (``beginDate``, gövde) Start date from which account activity records
                will be retrieved.
            end_date: (``endDate``, gövde) End date until which account activity records will be
                retrieved.

        Yanıt alanları: executionReferenceId, accountActivities, suffix, date, description,
        amount, balance, transactionReference, fxCode, transactionCode,
        transactionCodeDescription, senderIdentityNumber, transactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/outgoing-money-transfer-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "suffix": suffix,
                "itemCount": item_count,
                "beginDate": begin_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/moneytransfer/outgoingmoneytransfer",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def transaction_validation_list(
        self,
        *,
        transaction_guid: str | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Transaction Validation List.

        ``GET /v1/transactionvalidation/transactionlist``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve the transaction list used in transaction validation
        processes. The service returns transaction validation records filtered by transaction
        GUID and date range. It also returns the total transaction amount and total transaction
        count for the retrieved transaction list.

        Args:
            transaction_guid: (``transactionGuid``, sorgu) Unique transaction GUID used to
                filter transaction validation records.
            begin_date: (``beginDate``, sorgu) Start date from which transaction validation
                records will be retrieved.
            end_date: (``endDate``, sorgu) End date until which transaction validation records
                will be retrieved.

        Yanıt alanları: transactionContract, totalAmount, totalTransactionCount,
        transactionList, transactionGuid, executionReferenceId, amount, tranDate,
        transactionDescription

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/transaction-validation-list
        """
        _query = merge(
            {
                "transactionGuid": transaction_guid,
                "beginDate": begin_date,
                "endDate": end_date,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/transactionvalidation/transactionlist",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )


class AsyncTransfers(AsyncResource):
    """Para transferleri (asenkron) - ``kt.transfers``."""

    async def customer_iban_info_for_money_transfer(
        self,
        *,
        iban: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Iban Info for Money Transfer.

        ``GET /v1/moneytransfer/{iban}/customeribaninfo``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to retrieve customer account information associated with a given IBAN.
        The service returns masked customer name, bank name, bank ID and FEC information for the
        queried IBAN.

        Args:
            iban: (yol, zorunlu) IBAN number for which customer account information will be
                retrieved. This value is sent as a route parameter.

        Yanıt alanları: customerName, bankName, bankId, fec

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/customer-iban-info-for-money-transfer
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/moneytransfer/{iban}/customeribaninfo",
            scope="transfers",
            flow="client_credentials",
            path_params={"iban": iban},
            query=_query,
            options=request_options,
        )

    async def internal_money_transfer(
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
        """Money Transfer (Veeraman).

        ``POST /v1/moneytransfer/interbankmoneytransfer``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to initiate an internal account-to-account money transfer transaction.
        The sender account number is retrieved from the customer information in the
        authorization context, and the request includes sender suffix, receiver account
        information, transfer amount, description and transfer type.

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

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-veeraman
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
            "/v1/moneytransfer/interbankmoneytransfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def money_transfer_payment_type(
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
        """Money Transfer Payment Type.

        ``POST /v1/moneytransfer/paymenttype``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to initiate an internal money transfer transaction based on the
        customer account number from the authorization context. The request includes sender
        account suffix, receiver account information, transfer amount, transfer description and
        transfer type. The response returns the transaction execution reference and the created
        money transfer transaction ID.

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

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-payment-type
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
            "/v1/moneytransfer/paymenttype",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def money_transfer_state(
        self,
        *,
        transfer_type: str,
        out_going_id: str | None = None,
        virman_key: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Money Transfer State.

        ``GET /v1/moneytransfer-state``

        Kapsam: ``transfers`` · Akış: client credentials

        This API is used to check the current state of a money transfer transaction. The
        transaction can be queried by outGoingId for outgoing transfer types or by virmanKey for
        VIRMAN transactions. The transferType parameter determines which transaction type will
        be checked.

        Args:
            out_going_id: (``outGoingId``, sorgu) Outgoing money transfer ID used to query the
                transfer state. Required for transfer types other than VIRMAN.
            virman_key: (``virmanKey``, sorgu) Encrypted business key used to query VIRMAN
                transaction state. Required when transferType is VIRMAN.
            transfer_type: (``transferType``, sorgu, zorunlu) Money transfer type to be queried.
                Possible values include VIRMAN, HAVALE, FAST, POS and PÖS - EFT.

        Yanıt alanları: transferType, state, stateDescription

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-state
        """
        _query = merge(
            {
                "outGoingId": out_going_id,
                "virmanKey": virman_key,
                "transferType": transfer_type,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/moneytransfer-state",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def outgoing_money_transfer(
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
        """Para Transferi (Havale & EFT & FAST & Virman).

        ``POST /v1/moneytransfer/outgoingmoneytransfer``

        Kapsam: ``transfers`` · Akış: client credentials

        Bu API, authorization context ile ilişkili müşteri hesabından money transfer işlemi
        başlatmak için kullanılır. Servis; sender account bilgilerini, receiver account
        bilgilerini, transfer amount ve transfer type değerlerini doğrular, ardından ilgili
        money transfer transaction kaydını oluşturur.

        Args:
            sender_account_suffix: (``senderAccountSuffix``, gövde, zorunlu) Money transfer
                tutarının çekileceği sender account suffix numarasıdır.
            receiver_account_number: (``receiverAccountNumber``, gövde, zorunlu) Money transfer
                gönderilecek receiver customer account number değeridir.
            receiver_account_suffix: (``receiverAccountSuffix``, gövde, zorunlu) Money transfer
                gönderilecek receiver account suffix numarasıdır.
            money_transfer_description: (``moneyTransferDescription``, gövde) Money transfer
                transaction için eklenen açıklama veya comment bilgisidir.
            money_transfer_amount: (``moneyTransferAmount``, gövde, zorunlu) Transfer edilecek
                tutardır.
            transfer_type: (``transferType``, gövde, zorunlu) Transfer senaryosunu belirlemek
                için kullanılan money transfer type değeridir.

        Yanıt alanları: executionReferenceId, moneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/para-transferleri/para-transferi-havale-eft-fast-virman
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
            "/v1/moneytransfer/outgoingmoneytransfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def outgoing_money_transfer_v2(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Outgoing Money Transfer V2.

        ``POST /v2/moneytransfer/outgoingmoneytransfer``

        Kapsam: ``transfers`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve account transaction statement information based on the
        customer account number from the authorization context. The request can be filtered by
        account suffix, item count, begin date and end date. The response returns account
        activity records including transaction date, description, amount, balance, currency
        code, transaction reference and transaction code information.

        Args:
            suffix: (gövde, zorunlu) Account suffix for which transaction records will be
                retrieved.
            item_count: (``itemCount``, gövde) Maximum number of account activity records to be
                returned.
            begin_date: (``beginDate``, gövde) Start date from which account activity records
                will be retrieved.
            end_date: (``endDate``, gövde) End date until which account activity records will be
                retrieved.

        Yanıt alanları: executionReferenceId, accountActivities, suffix, date, description,
        amount, balance, transactionReference, fxCode, transactionCode,
        transactionCodeDescription, senderIdentityNumber, transactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/outgoing-money-transfer-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "suffix": suffix,
                "itemCount": item_count,
                "beginDate": begin_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/moneytransfer/outgoingmoneytransfer",
            scope="transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def transaction_validation_list(
        self,
        *,
        transaction_guid: str | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Transaction Validation List.

        ``GET /v1/transactionvalidation/transactionlist``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve the transaction list used in transaction validation
        processes. The service returns transaction validation records filtered by transaction
        GUID and date range. It also returns the total transaction amount and total transaction
        count for the retrieved transaction list.

        Args:
            transaction_guid: (``transactionGuid``, sorgu) Unique transaction GUID used to
                filter transaction validation records.
            begin_date: (``beginDate``, sorgu) Start date from which transaction validation
                records will be retrieved.
            end_date: (``endDate``, sorgu) End date until which transaction validation records
                will be retrieved.

        Yanıt alanları: transactionContract, totalAmount, totalTransactionCount,
        transactionList, transactionGuid, executionReferenceId, amount, tranDate,
        transactionDescription

        Doküman: https://developer.kuveytturk.com.tr/documentation/money-transfers/transaction-validation-list
        """
        _query = merge(
            {
                "transactionGuid": transaction_guid,
                "beginDate": begin_date,
                "endDate": end_date,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/transactionvalidation/transactionlist",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )
