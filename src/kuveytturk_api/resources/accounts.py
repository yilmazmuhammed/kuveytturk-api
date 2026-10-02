"""Hesap yönetimi (kurumun kendi hesapları) uç noktaları (``kt.accounts``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(Resource):
    """Hesap yönetimi (kurumun kendi hesapları) - ``kt.accounts``."""

    def account_activity_list(
        self,
        *,
        begin_date: DateLike,
        end_date: DateLike,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Activity List.

        ``POST /v1/accountActivities``

        Kapsam: ``account_activities`` · Akış: client credentials

        Retrieves the account activities within the specified date range for the client making
        the request.

        Args:
            begin_date: (``BeginDate``, gövde, zorunlu) Specifies after which date the account
                activities will be retrieved.
            end_date: (``EndDate``, gövde, zorunlu) Specifies before which date the account
                activities will be retrieved.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/account-activity-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "BeginDate": begin_date,
                "EndDate": end_date,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/accountActivities",
            scope="account_activities",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def account_list_v3(
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
        """Account List V3.

        ``GET /v3/accounts``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve the account list of the customer associated with the
        authorization context. The response includes account details such as account suffix,
        balance, available balance, currency information, IBAN, account type, branch
        information, customer name, maturity dates and account status. The account list can be
        filtered by account suffix and optional account status or balance filters.

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

        Yanıt alanları: executionReferenceId, accountList, name, suffix, balance,
        avaibleBalance, fxId, iban, type, openDate, branchName, branchId, withHoldingAmount,
        customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-v3
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
            "/v3/accounts",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def account_list_with_suffix_v3(
        self,
        *,
        suffix: int,
        only_has_available_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account List With Suffix v3.

        ``GET /v3/accounts/{suffix}``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve account information for the specified account suffix of the
        customer associated with the authorization context. The response includes account
        details such as account suffix, balance, available balance, currency information, IBAN,
        account type, branch information, customer name, maturity dates and account status.
        Additional filters can be used to narrow the account list by balance, account status,
        current account type and shared account signature type.

        Args:
            suffix: (yol, zorunlu) Account suffix used to retrieve a specific account. This
                value is sent as a route parameter.
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

        Yanıt alanları: executionReferenceId, accountList, name, suffix, balance,
        avaibleBalance, fxId, iban, type, openDate, branchName, branchId, withHoldingAmount,
        customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-with-suffix-v3
        """
        _query = merge(
            {
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
            "/v3/accounts/{suffix}",
            scope="accounts",
            flow="client_credentials",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    def account_transactions_v3(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Transactions V3.

        ``GET /v3/accounts/{suffix}/transactions``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve account transaction history for the specified account
        suffix of the customer associated with the authorization context. The transaction list
        can be filtered by item count, begin date and end date. The response includes
        transaction details such as transaction date, description, amount, balance, transaction
        reference, currency code, resource code, IBAN and request number.

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
        amount, balance, transactionReference, fxCode, resourceCode, iban, reqNum

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v3
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
            "/v3/accounts/{suffix}/transactions",
            scope="accounts",
            flow="client_credentials",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    def account_transactions_v4_detail(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Transactions V4 - Detail.

        ``GET /v4/accounts/{suffix}/transactions``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve account transaction history for the specified account
        suffix of the customer associated with the authorization context. The transaction list
        can be filtered by item count, begin date and end date. The response includes
        transaction details such as transaction date, description, amount, balance, transaction
        reference, currency code, resource code and IBAN.

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
        amount, balance, transactionReference, fxCode, resourceCode, iban

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v4-detail
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
            "/v4/accounts/{suffix}/transactions",
            scope="accounts",
            flow="client_credentials",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    def account_verification_v2(
        self,
        *,
        correlation_identifier: str,
        context: str,
        uetr: str,
        creditor_account: str,
        creditor_name: str,
        creditor_address: Mapping[str, Any] | None = None,
        creditor_organisation_identification: Mapping[str, Any] | None = None,
        creditor_agent: Mapping[str, Any] | None = None,
        creditor_agent_branch_identification: str | None = None,
        x_bic: str | None = None,
        subject_dn: str | None = None,
        institution: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Prevalidation Data Provider.

        ``POST /v2/accounts/verification``

        Kapsam: ``accounts`` · Akış: client credentials

        This API verifies beneficiary account information before processing a payment or
        transfer. The verification is performed using creditor account, creditor name, creditor
        address, creditor organisation identification and creditor agent information.

        Args:
            correlation_identifier: (gövde, zorunlu) Unique correlation identifier used to track
                the verification request.
            context: (gövde, zorunlu) Context information related to the verification request.
            uetr: (gövde, zorunlu) Unique end_to_end Transaction Reference associated with the
                transaction.
            creditor_account: (gövde, zorunlu) Creditor account number or account identifier to
                be verified.
            creditor_name: (gövde, zorunlu) Name of the creditor to be verified.
            creditor_address: (gövde) Address information of the creditor.
            creditor_organisation_identification: (gövde) Organisation identification
                information of the creditor.
            creditor_agent: (gövde) Financial institution or agent information of the creditor.
            creditor_agent_branch_identification: (gövde) Branch identification of the creditor
                agent.
            x_bic: (``x-bic``, gövde) BIC value provided in the request context.
            subject_dn: (``SubjectDN``, gövde) Subject distinguished name information used for
                certificate or institution identification.
            institution: (``Institution``, gövde) Institution information associated with the
                verification request.

        Yanıt alanları: correlation_identifier, response, account_validation_status,
        creditor_account_match, creditor_name_match, creditor_address_match,
        creditor_organisation_identification_match

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/prevalidation-data-provider
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "correlation_identifier": correlation_identifier,
                "context": context,
                "uetr": uetr,
                "creditor_account": creditor_account,
                "creditor_name": creditor_name,
                "creditor_address": creditor_address,
                "creditor_organisation_identification": creditor_organisation_identification,
                "creditor_agent": creditor_agent,
                "creditor_agent_branch_identification": creditor_agent_branch_identification,
                "x-bic": x_bic,
                "SubjectDN": subject_dn,
                "Institution": institution,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/accounts/verification",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pdf_receipt_v3(
        self,
        *,
        execution_reference_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PDF Receipt V3.

        ``POST /v3/accounts/transactions/pdfReceipts``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve PDF receipt data for a transaction. The customer account
        number is retrieved from the authorization context, and the transaction is identified by
        the executionReferenceId value sent in the request body. The response returns the
        receipt PDF content in Base64 format.

        Args:
            execution_reference_id: (``executionReferenceId``, gövde, zorunlu) Reference ID of
                the transaction for which the PDF receipt data will be retrieved.

        Yanıt alanları: contract, pdfData

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/pdf-receipt-v3
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "executionReferenceId": execution_reference_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v3/accounts/transactions/pdfReceipts",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def receipt_v3(
        self,
        *,
        transaction_reference: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dekont V3.

        ``POST /v3/accounts/transactions/receipts``

        Kapsam: ``accounts`` · Akış: client credentials

        Bu API, transactionReference değeri ile tanımlanan bir transaction için receipt
        bilgilerini almak amacıyla kullanılır. Servis; title, description, amount, currency
        bilgisi ve slip list, left header, right header, body ve footer bölümlerini içeren
        receipt detaylarını döndürür.

        Args:
            transaction_reference: (``transactionReference``, gövde, zorunlu) Receipt bilgisi
                alınacak şifrelenmiş transaction reference değeridir.

        Yanıt alanları: executionReferenceId, title, description, amount, fecName, slipList,
        key, leftHeader, rightHeader, body, footer

        Doküman: https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-hesaplariniz/dekont-v3
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
            "/v3/accounts/transactions/receipts",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncAccounts(AsyncResource):
    """Hesap yönetimi (kurumun kendi hesapları) (asenkron) - ``kt.accounts``."""

    async def account_activity_list(
        self,
        *,
        begin_date: DateLike,
        end_date: DateLike,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Activity List.

        ``POST /v1/accountActivities``

        Kapsam: ``account_activities`` · Akış: client credentials

        Retrieves the account activities within the specified date range for the client making
        the request.

        Args:
            begin_date: (``BeginDate``, gövde, zorunlu) Specifies after which date the account
                activities will be retrieved.
            end_date: (``EndDate``, gövde, zorunlu) Specifies before which date the account
                activities will be retrieved.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/account-activity-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "BeginDate": begin_date,
                "EndDate": end_date,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/accountActivities",
            scope="account_activities",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def account_list_v3(
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
        """Account List V3.

        ``GET /v3/accounts``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve the account list of the customer associated with the
        authorization context. The response includes account details such as account suffix,
        balance, available balance, currency information, IBAN, account type, branch
        information, customer name, maturity dates and account status. The account list can be
        filtered by account suffix and optional account status or balance filters.

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

        Yanıt alanları: executionReferenceId, accountList, name, suffix, balance,
        avaibleBalance, fxId, iban, type, openDate, branchName, branchId, withHoldingAmount,
        customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-v3
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
            "/v3/accounts",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def account_list_with_suffix_v3(
        self,
        *,
        suffix: int,
        only_has_available_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account List With Suffix v3.

        ``GET /v3/accounts/{suffix}``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve account information for the specified account suffix of the
        customer associated with the authorization context. The response includes account
        details such as account suffix, balance, available balance, currency information, IBAN,
        account type, branch information, customer name, maturity dates and account status.
        Additional filters can be used to narrow the account list by balance, account status,
        current account type and shared account signature type.

        Args:
            suffix: (yol, zorunlu) Account suffix used to retrieve a specific account. This
                value is sent as a route parameter.
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

        Yanıt alanları: executionReferenceId, accountList, name, suffix, balance,
        avaibleBalance, fxId, iban, type, openDate, branchName, branchId, withHoldingAmount,
        customerName, maturityBeginDate, maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-with-suffix-v3
        """
        _query = merge(
            {
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
            "/v3/accounts/{suffix}",
            scope="accounts",
            flow="client_credentials",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    async def account_transactions_v3(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Transactions V3.

        ``GET /v3/accounts/{suffix}/transactions``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve account transaction history for the specified account
        suffix of the customer associated with the authorization context. The transaction list
        can be filtered by item count, begin date and end date. The response includes
        transaction details such as transaction date, description, amount, balance, transaction
        reference, currency code, resource code, IBAN and request number.

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
        amount, balance, transactionReference, fxCode, resourceCode, iban, reqNum

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v3
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
            "/v3/accounts/{suffix}/transactions",
            scope="accounts",
            flow="client_credentials",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    async def account_transactions_v4_detail(
        self,
        *,
        suffix: int,
        item_count: int | None = None,
        begin_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Transactions V4 - Detail.

        ``GET /v4/accounts/{suffix}/transactions``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve account transaction history for the specified account
        suffix of the customer associated with the authorization context. The transaction list
        can be filtered by item count, begin date and end date. The response includes
        transaction details such as transaction date, description, amount, balance, transaction
        reference, currency code, resource code and IBAN.

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
        amount, balance, transactionReference, fxCode, resourceCode, iban

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v4-detail
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
            "/v4/accounts/{suffix}/transactions",
            scope="accounts",
            flow="client_credentials",
            path_params={"suffix": suffix},
            query=_query,
            options=request_options,
        )

    async def account_verification_v2(
        self,
        *,
        correlation_identifier: str,
        context: str,
        uetr: str,
        creditor_account: str,
        creditor_name: str,
        creditor_address: Mapping[str, Any] | None = None,
        creditor_organisation_identification: Mapping[str, Any] | None = None,
        creditor_agent: Mapping[str, Any] | None = None,
        creditor_agent_branch_identification: str | None = None,
        x_bic: str | None = None,
        subject_dn: str | None = None,
        institution: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Prevalidation Data Provider.

        ``POST /v2/accounts/verification``

        Kapsam: ``accounts`` · Akış: client credentials

        This API verifies beneficiary account information before processing a payment or
        transfer. The verification is performed using creditor account, creditor name, creditor
        address, creditor organisation identification and creditor agent information.

        Args:
            correlation_identifier: (gövde, zorunlu) Unique correlation identifier used to track
                the verification request.
            context: (gövde, zorunlu) Context information related to the verification request.
            uetr: (gövde, zorunlu) Unique end_to_end Transaction Reference associated with the
                transaction.
            creditor_account: (gövde, zorunlu) Creditor account number or account identifier to
                be verified.
            creditor_name: (gövde, zorunlu) Name of the creditor to be verified.
            creditor_address: (gövde) Address information of the creditor.
            creditor_organisation_identification: (gövde) Organisation identification
                information of the creditor.
            creditor_agent: (gövde) Financial institution or agent information of the creditor.
            creditor_agent_branch_identification: (gövde) Branch identification of the creditor
                agent.
            x_bic: (``x-bic``, gövde) BIC value provided in the request context.
            subject_dn: (``SubjectDN``, gövde) Subject distinguished name information used for
                certificate or institution identification.
            institution: (``Institution``, gövde) Institution information associated with the
                verification request.

        Yanıt alanları: correlation_identifier, response, account_validation_status,
        creditor_account_match, creditor_name_match, creditor_address_match,
        creditor_organisation_identification_match

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/prevalidation-data-provider
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "correlation_identifier": correlation_identifier,
                "context": context,
                "uetr": uetr,
                "creditor_account": creditor_account,
                "creditor_name": creditor_name,
                "creditor_address": creditor_address,
                "creditor_organisation_identification": creditor_organisation_identification,
                "creditor_agent": creditor_agent,
                "creditor_agent_branch_identification": creditor_agent_branch_identification,
                "x-bic": x_bic,
                "SubjectDN": subject_dn,
                "Institution": institution,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/accounts/verification",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pdf_receipt_v3(
        self,
        *,
        execution_reference_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PDF Receipt V3.

        ``POST /v3/accounts/transactions/pdfReceipts``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve PDF receipt data for a transaction. The customer account
        number is retrieved from the authorization context, and the transaction is identified by
        the executionReferenceId value sent in the request body. The response returns the
        receipt PDF content in Base64 format.

        Args:
            execution_reference_id: (``executionReferenceId``, gövde, zorunlu) Reference ID of
                the transaction for which the PDF receipt data will be retrieved.

        Yanıt alanları: contract, pdfData

        Doküman: https://developer.kuveytturk.com.tr/documentation/account-management-own/pdf-receipt-v3
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "executionReferenceId": execution_reference_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v3/accounts/transactions/pdfReceipts",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def receipt_v3(
        self,
        *,
        transaction_reference: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dekont V3.

        ``POST /v3/accounts/transactions/receipts``

        Kapsam: ``accounts`` · Akış: client credentials

        Bu API, transactionReference değeri ile tanımlanan bir transaction için receipt
        bilgilerini almak amacıyla kullanılır. Servis; title, description, amount, currency
        bilgisi ve slip list, left header, right header, body ve footer bölümlerini içeren
        receipt detaylarını döndürür.

        Args:
            transaction_reference: (``transactionReference``, gövde, zorunlu) Receipt bilgisi
                alınacak şifrelenmiş transaction reference değeridir.

        Yanıt alanları: executionReferenceId, title, description, amount, fecName, slipList,
        key, leftHeader, rightHeader, body, footer

        Doküman: https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-hesaplariniz/dekont-v3
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
            "/v3/accounts/transactions/receipts",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
