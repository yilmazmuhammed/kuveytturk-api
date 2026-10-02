"""Hesap yönetimi (TPP - müşteri adına) uç noktaları (``kt.tpp_accounts``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["AsyncTppAccounts", "TppAccounts"]


class TppAccounts(Resource):
    """Hesap yönetimi (TPP - müşteri adına) - ``kt.tpp_accounts``."""

    def account_list_v2(
        self,
        *,
        suffix: int | None = None,
        only_has_available_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account List V2.

        ``GET /v2/accounts``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve the account list of the customer associated with the
        authorization context. The response includes account details such as account number,
        account suffix, balance, available balance, currency information, IBAN, account type,
        branch information, customer name, maturity dates and account status. The account list
        can be filtered by account suffix and optional account status or balance filters.

        Args:
            suffix: (sorgu) Account suffix used to retrieve a specific account.
            only_has_available_balance: (``onlyHasAvailableBalance``, sorgu) Indicates whether
                only accounts with available balance should be returned.
            only_open: (``onlyOpen``, sorgu) Indicates whether only open accounts should be
                returned.
            only_with_no_balance: (``onlyWithNoBalance``, sorgu) Indicates whether only accounts
                with no balance should be returned.
            only_current: (``onlyCurrent``, sorgu) Indicates whether only current accounts
                should be returned.
            shared_with_multi_signature: (``sharedWithMultiSignature``, sorgu) Indicates whether
                shared accounts requiring multiple signatures should be included.

        Yanıt alanları: executionReferenceId, accountList, accountNumber, name, suffix, balance,
        availableBalance, fxId, fxCode, iban, type, openDate, branchName, branchId,
        withHoldingAmount, customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-list-v2
        """
        _query = merge(
            {
                "suffix": suffix,
                "onlyHasAvailableBalance": only_has_available_balance,
                "onlyOpen": only_open,
                "onlyWithNoBalance": only_with_no_balance,
                "onlyCurrent": only_current,
                "sharedWithMultiSignature": shared_with_multi_signature,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/accounts",
            scope="accounts",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    def account_list_with_suffix_v2(
        self,
        *,
        suffix: int,
        customer_id: int,
        language_id: int | None = None,
        only_has_available_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account List V2 (withouth suffix).

        ``GET /v2/accounts/{suffix}``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        Retrieves the account information for the authenticated customer by account suffix. The
        response includes account details such as balance, available balance, currency, IBAN,
        account type, branch information, maturity dates and account status.

        Args:
            suffix: (yol, zorunlu) Account suffix used to retrieve a specific account.
            customer_id: (``CustomerId``, sorgu, zorunlu) Customer number used to retrieve the
                account list.
            language_id: (``LanguageId``, sorgu) Language identifier used for localized account
                information.
            only_has_available_balance: (``onlyHasAvailableBalance``, sorgu) Indicates whether
                only accounts with available balance should be returned.
            only_open: (``onlyOpen``, sorgu) Indicates whether only open accounts should be
                returned.
            only_with_no_balance: (``onlyWithNoBalance``, sorgu) Indicates whether only accounts
                with no balance should be returned.
            only_current: (``onlyCurrent``, sorgu) Indicates whether only current accounts
                should be returned.
            shared_with_multi_signature: (``sharedWithMultiSignature``, sorgu) Indicates whether
                accounts shared with multi-signature authorization should be included.

        Yanıt alanları: executionReferenceId, accountList, accountNumber, name, suffix,
        availableBalance, fxId, fxCode, iban, type, openDate, branchName, branchId,
        withHoldingAmount, customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/account-list-v2-withouth-suffix
        """
        _query = merge(
            {
                "CustomerId": customer_id,
                "LanguageId": language_id,
                "onlyHasAvailableBalance": only_has_available_balance,
                "onlyOpen": only_open,
                "onlyWithNoBalance": only_with_no_balance,
                "onlyCurrent": only_current,
                "sharedWithMultiSignature": shared_with_multi_signature,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/accounts/{suffix}",
            scope="accounts",
            flow="authorization_code",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    def account_transactions_v2(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Transactions V2.

        ``GET /v2/accounts/{suffix}/transactions``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve account transaction history for the specified account
        suffix of the customer associated with the authorization context. The transaction list
        can be filtered by item count, begin date and end date. The response includes
        transaction details such as transaction date, description, amount, balance, transaction
        reference, transaction ID, currency code, transaction code, sequence number,
        sender/receiver identity information and resource code.

        Args:
            suffix: (yol, zorunlu) Account suffix for which transaction records will be
                retrieved. This value is sent as a route parameter.
            item_count: (``itemCount``, sorgu) Maximum number of account activity records to be
                returned.
            begin_date: (``beginDate``, sorgu) Start date from which account activity records
                will be retrieved.
            end_date: (``endDate``, sorgu) End date until which account activity records will be
                retrieved.

        Yanıt alanları: executionReferenceId, accountActivities, suffix, date, description,
        amount, balance, transactionReference, transactionId, fxCode, transactionCode, seqNum,
        receiverTCKNorVKN, senderTCKNorVKN, resourceCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-transactions-v2
        """
        _query = merge(
            {
                "itemCount": item_count,
                "beginDate": begin_date,
                "endDate": end_date,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/accounts/{suffix}/transactions",
            scope="accounts",
            flow="authorization_code",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    def receipt_v1(
        self,
        *,
        suffix: str,
        business_key: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Receipt.

        ``GET /v1/accounts/{suffix}/transactions/{businessKey}``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        Returns the receipt values of the transaction that is given by the businesskey. The API
        response is divided into four parts in order to help visualize the receipt: "leftHeader,
        rightHeader, body, footer". The entire data in these properties is also available in the
        slipList property.

        Args:
            suffix: (yol, zorunlu)
            business_key: (``businessKey``, yol, zorunlu)

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/receipt
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/accounts/{suffix}/transactions/{businessKey}",
            scope="accounts",
            flow="authorization_code",
            path_params={"suffix": suffix, "businessKey": business_key},
            query=_query,
            options=request_options,
        )

    def receipt_v2(
        self,
        *,
        transaction_reference: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Receipt V2.

        ``POST /v2/accounts/transactions/receipts``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve receipt information for a transaction identified by the
        transactionReference value. The service returns receipt details such as title,
        description, amount, currency information and receipt sections including slip list, left
        header, right header, body and footer.

        Args:
            transaction_reference: (``transactionReference``, gövde, zorunlu) Encrypted
                transaction reference value for which receipt information will be retrieved.

        Yanıt alanları: executionReferenceId, title, description, amount, fecName, slipList,
        key, leftHeader, rightHeader, body, footer

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-tpp/receipt-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionReference": transaction_reference,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/accounts/transactions/receipts",
            scope="accounts",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncTppAccounts(AsyncResource):
    """Hesap yönetimi (TPP - müşteri adına) (asenkron) - ``kt.tpp_accounts``."""

    async def account_list_v2(
        self,
        *,
        suffix: int | None = None,
        only_has_available_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account List V2.

        ``GET /v2/accounts``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve the account list of the customer associated with the
        authorization context. The response includes account details such as account number,
        account suffix, balance, available balance, currency information, IBAN, account type,
        branch information, customer name, maturity dates and account status. The account list
        can be filtered by account suffix and optional account status or balance filters.

        Args:
            suffix: (sorgu) Account suffix used to retrieve a specific account.
            only_has_available_balance: (``onlyHasAvailableBalance``, sorgu) Indicates whether
                only accounts with available balance should be returned.
            only_open: (``onlyOpen``, sorgu) Indicates whether only open accounts should be
                returned.
            only_with_no_balance: (``onlyWithNoBalance``, sorgu) Indicates whether only accounts
                with no balance should be returned.
            only_current: (``onlyCurrent``, sorgu) Indicates whether only current accounts
                should be returned.
            shared_with_multi_signature: (``sharedWithMultiSignature``, sorgu) Indicates whether
                shared accounts requiring multiple signatures should be included.

        Yanıt alanları: executionReferenceId, accountList, accountNumber, name, suffix, balance,
        availableBalance, fxId, fxCode, iban, type, openDate, branchName, branchId,
        withHoldingAmount, customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-list-v2
        """
        _query = merge(
            {
                "suffix": suffix,
                "onlyHasAvailableBalance": only_has_available_balance,
                "onlyOpen": only_open,
                "onlyWithNoBalance": only_with_no_balance,
                "onlyCurrent": only_current,
                "sharedWithMultiSignature": shared_with_multi_signature,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/accounts",
            scope="accounts",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    async def account_list_with_suffix_v2(
        self,
        *,
        suffix: int,
        customer_id: int,
        language_id: int | None = None,
        only_has_available_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account List V2 (withouth suffix).

        ``GET /v2/accounts/{suffix}``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        Retrieves the account information for the authenticated customer by account suffix. The
        response includes account details such as balance, available balance, currency, IBAN,
        account type, branch information, maturity dates and account status.

        Args:
            suffix: (yol, zorunlu) Account suffix used to retrieve a specific account.
            customer_id: (``CustomerId``, sorgu, zorunlu) Customer number used to retrieve the
                account list.
            language_id: (``LanguageId``, sorgu) Language identifier used for localized account
                information.
            only_has_available_balance: (``onlyHasAvailableBalance``, sorgu) Indicates whether
                only accounts with available balance should be returned.
            only_open: (``onlyOpen``, sorgu) Indicates whether only open accounts should be
                returned.
            only_with_no_balance: (``onlyWithNoBalance``, sorgu) Indicates whether only accounts
                with no balance should be returned.
            only_current: (``onlyCurrent``, sorgu) Indicates whether only current accounts
                should be returned.
            shared_with_multi_signature: (``sharedWithMultiSignature``, sorgu) Indicates whether
                accounts shared with multi-signature authorization should be included.

        Yanıt alanları: executionReferenceId, accountList, accountNumber, name, suffix,
        availableBalance, fxId, fxCode, iban, type, openDate, branchName, branchId,
        withHoldingAmount, customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/account-list-v2-withouth-suffix
        """
        _query = merge(
            {
                "CustomerId": customer_id,
                "LanguageId": language_id,
                "onlyHasAvailableBalance": only_has_available_balance,
                "onlyOpen": only_open,
                "onlyWithNoBalance": only_with_no_balance,
                "onlyCurrent": only_current,
                "sharedWithMultiSignature": shared_with_multi_signature,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/accounts/{suffix}",
            scope="accounts",
            flow="authorization_code",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    async def account_transactions_v2(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Transactions V2.

        ``GET /v2/accounts/{suffix}/transactions``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve account transaction history for the specified account
        suffix of the customer associated with the authorization context. The transaction list
        can be filtered by item count, begin date and end date. The response includes
        transaction details such as transaction date, description, amount, balance, transaction
        reference, transaction ID, currency code, transaction code, sequence number,
        sender/receiver identity information and resource code.

        Args:
            suffix: (yol, zorunlu) Account suffix for which transaction records will be
                retrieved. This value is sent as a route parameter.
            item_count: (``itemCount``, sorgu) Maximum number of account activity records to be
                returned.
            begin_date: (``beginDate``, sorgu) Start date from which account activity records
                will be retrieved.
            end_date: (``endDate``, sorgu) End date until which account activity records will be
                retrieved.

        Yanıt alanları: executionReferenceId, accountActivities, suffix, date, description,
        amount, balance, transactionReference, transactionId, fxCode, transactionCode, seqNum,
        receiverTCKNorVKN, senderTCKNorVKN, resourceCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-transactions-v2
        """
        _query = merge(
            {
                "itemCount": item_count,
                "beginDate": begin_date,
                "endDate": end_date,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/accounts/{suffix}/transactions",
            scope="accounts",
            flow="authorization_code",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    async def receipt_v1(
        self,
        *,
        suffix: str,
        business_key: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Receipt.

        ``GET /v1/accounts/{suffix}/transactions/{businessKey}``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        Returns the receipt values of the transaction that is given by the businesskey. The API
        response is divided into four parts in order to help visualize the receipt: "leftHeader,
        rightHeader, body, footer". The entire data in these properties is also available in the
        slipList property.

        Args:
            suffix: (yol, zorunlu)
            business_key: (``businessKey``, yol, zorunlu)

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/receipt
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/accounts/{suffix}/transactions/{businessKey}",
            scope="accounts",
            flow="authorization_code",
            path_params={"suffix": suffix, "businessKey": business_key},
            query=_query,
            options=request_options,
        )

    async def receipt_v2(
        self,
        *,
        transaction_reference: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Receipt V2.

        ``POST /v2/accounts/transactions/receipts``

        Kapsam: ``accounts`` · Akış: authorization code (müşteri girişi gerekir)

        This API is used to retrieve receipt information for a transaction identified by the
        transactionReference value. The service returns receipt details such as title,
        description, amount, currency information and receipt sections including slip list, left
        header, right header, body and footer.

        Args:
            transaction_reference: (``transactionReference``, gövde, zorunlu) Encrypted
                transaction reference value for which receipt information will be retrieved.

        Yanıt alanları: executionReferenceId, title, description, amount, fecName, slipList,
        key, leftHeader, rightHeader, body, footer

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-tpp/receipt-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionReference": transaction_reference,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/accounts/transactions/receipts",
            scope="accounts",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )
