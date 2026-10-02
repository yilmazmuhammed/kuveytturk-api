"""SMS / OTP uç noktaları (``kt.sms_otp``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Resource, merge

__all__ = ["AsyncSmsOtp", "SmsOtp"]


class SmsOtp(Resource):
    """SMS / OTP - ``kt.sms_otp``."""

    def pr_customer_validation(
        self,
        *,
        iban: str,
        title: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Customer Validation.

        ``POST /v1/paymentrequest/customerValidation``

        Kapsam: ``public`` · Akış: client credentials

        Validates customer information for payment request operations by using the provided IBAN
        and title. The response includes customer, IBAN, title match, payment request
        permission, customer status, language, FAST limit, customer type, and result details.

        Args:
            iban: (gövde, zorunlu) IBAN used to validate the customer for payment request
                operations.
            title: (gövde, zorunlu) Customer title used to validate title matching for the
                provided IBAN.

        Yanıt alanları: customerId, isIbanFound, isIbanActive, isTitleMatch,
        isPaymentRequestAllowed, isCustomerActive, languageId, fastLimit, customerType

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-customer-validation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "iban": iban,
                "title": title,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/paymentrequest/customerValidation",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pr_get_account_details_by_iban(
        self,
        *,
        i_ban: str,
        account_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Get Account Details By IBAN.

        ``POST /v1/paymentrequest/getAccountByIban``

        Kapsam: ``accounts`` · Akış: client credentials

        Retrieves account balance information for payment request operations by using the
        provided IBAN and account number. The response includes balance and blocked balance
        details for the related account.

        Args:
            i_ban: (``iBAN``, gövde, zorunlu) IBAN used to retrieve account balance details.
            account_number: (``accountNumber``, gövde, zorunlu) Account number used together
                with the IBAN to retrieve account balance details.

        Yanıt alanları: balance, blockedBalance

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-account-details-by-iban
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "iBAN": i_ban,
                "accountNumber": account_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/paymentrequest/getAccountByIban",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pr_get_fast_result(
        self,
        *,
        oi_reference: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Get FAST Result.

        ``GET /v1/paymentrequest/getFastResult``

        Kapsam: ``public`` · Akış: client credentials

        Retrieves the FAST transaction result for payment request operations by using the
        provided OI reference number. The response includes the transfer completion date and
        result code of the related FAST transaction.

        Args:
            oi_reference: (``oiReference``, sorgu, zorunlu) OI reference number used to retrieve
                the FAST transaction result.

        Yanıt alanları: transferCompleteDate, resultCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-fast-result
        """
        _query = merge(
            {
                "oiReference": oi_reference,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/paymentrequest/getFastResult",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def pr_payment_request_control(
        self,
        *,
        request_payment_reference: str,
        request_payment_flow_type: str,
        creditor_identity_value: str,
        creditor_title: str,
        creditor_iban: str,
        amount: str,
        payment_intent: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Payment Request Control.

        ``POST /v1/paymentrequest/paymentControl``

        Kapsam: ``public`` · Akış: client credentials

        Checks and validates a payment request by using the provided payment reference, flow
        type, creditor identity, creditor title, creditor IBAN, amount, and payment intent
        information. The response returns the payment request control result, return code, and
        validation result details.

        Args:
            request_payment_reference: (``requestPaymentReference``, gövde, zorunlu) Payment
                request reference number used to identify the payment request.
            request_payment_flow_type: (``requestPaymentFlowType``, gövde, zorunlu) Flow type of
                the payment request.
            creditor_identity_value: (``creditorIdentityValue``, gövde, zorunlu) Identity value
                of the creditor.
            creditor_title: (``creditorTitle``, gövde, zorunlu) Title or name of the creditor.
            creditor_iban: (``creditorIBAN``, gövde, zorunlu) IBAN of the creditor account.
            amount: (gövde, zorunlu) Payment request amount.
            payment_intent: (``paymentIntent``, gövde, zorunlu) Payment intent or purpose
                information of the payment request.

        Yanıt alanları: isSuccess, returnCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-request-control
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "requestPaymentReference": request_payment_reference,
                "requestPaymentFlowType": request_payment_flow_type,
                "creditorIdentityValue": creditor_identity_value,
                "creditorTitle": creditor_title,
                "creditorIBAN": creditor_iban,
                "amount": amount,
                "paymentIntent": payment_intent,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/paymentrequest/paymentControl",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pr_payment_transaction(
        self,
        *,
        account_number: int,
        language_id: int,
        account_suffix: int | None = None,
        only_has_avaible_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Payment Transaction.

        ``POST /v1/paymentrequest/transfer``

        Kapsam: ``transfers`` · Akış: client credentials

        Retrieves the account list for payment request transfer operations according to the
        provided customer, language, account suffix, balance, account status, current account,
        and multi-signature sharing filters. The response includes account details such as
        account name, suffix, balance, available balance, currency, IBAN, product type, opening
        date, branch information, customer name, maturity dates, and active status.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) Customer account number used to
                retrieve the account list.
            language_id: (``languageId``, gövde, zorunlu) Language identifier used for account
                information and descriptions.
            account_suffix: (``accountSuffix``, gövde) Account suffix used to filter the account
                list.
            only_has_avaible_balance: (``onlyHasAvaibleBalance``, gövde) Indicates whether only
                accounts with available balance should be returned.
            only_open: (``onlyOpen``, gövde) Indicates whether only open accounts should be
                returned.
            only_with_no_balance: (``onlyWithNoBalance``, gövde) Indicates whether only accounts
                with no balance should be returned.
            only_current: (``onlyCurrent``, gövde) Indicates whether only current accounts
                should be returned.
            shared_with_multi_signature: (``sharedWithMultiSignature``, gövde) Indicates whether
                accounts shared with multi-signature authorization should be included.

        Yanıt alanları: executionReferenceId, accountList, name, suffix, fxId, iban, type,
        openDate, branchName, branchId, withHoldingAmount, customerName, maturityBeginDate,
        maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-transaction
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumber": account_number,
                "languageId": language_id,
                "accountSuffix": account_suffix,
                "onlyHasAvaibleBalance": only_has_avaible_balance,
                "onlyOpen": only_open,
                "onlyWithNoBalance": only_with_no_balance,
                "onlyCurrent": only_current,
                "sharedWithMultiSignature": shared_with_multi_signature,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/paymentrequest/transfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncSmsOtp(AsyncResource):
    """SMS / OTP (asenkron) - ``kt.sms_otp``."""

    async def pr_customer_validation(
        self,
        *,
        iban: str,
        title: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Customer Validation.

        ``POST /v1/paymentrequest/customerValidation``

        Kapsam: ``public`` · Akış: client credentials

        Validates customer information for payment request operations by using the provided IBAN
        and title. The response includes customer, IBAN, title match, payment request
        permission, customer status, language, FAST limit, customer type, and result details.

        Args:
            iban: (gövde, zorunlu) IBAN used to validate the customer for payment request
                operations.
            title: (gövde, zorunlu) Customer title used to validate title matching for the
                provided IBAN.

        Yanıt alanları: customerId, isIbanFound, isIbanActive, isTitleMatch,
        isPaymentRequestAllowed, isCustomerActive, languageId, fastLimit, customerType

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-customer-validation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "iban": iban,
                "title": title,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/paymentrequest/customerValidation",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pr_get_account_details_by_iban(
        self,
        *,
        i_ban: str,
        account_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Get Account Details By IBAN.

        ``POST /v1/paymentrequest/getAccountByIban``

        Kapsam: ``accounts`` · Akış: client credentials

        Retrieves account balance information for payment request operations by using the
        provided IBAN and account number. The response includes balance and blocked balance
        details for the related account.

        Args:
            i_ban: (``iBAN``, gövde, zorunlu) IBAN used to retrieve account balance details.
            account_number: (``accountNumber``, gövde, zorunlu) Account number used together
                with the IBAN to retrieve account balance details.

        Yanıt alanları: balance, blockedBalance

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-account-details-by-iban
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "iBAN": i_ban,
                "accountNumber": account_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/paymentrequest/getAccountByIban",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pr_get_fast_result(
        self,
        *,
        oi_reference: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Get FAST Result.

        ``GET /v1/paymentrequest/getFastResult``

        Kapsam: ``public`` · Akış: client credentials

        Retrieves the FAST transaction result for payment request operations by using the
        provided OI reference number. The response includes the transfer completion date and
        result code of the related FAST transaction.

        Args:
            oi_reference: (``oiReference``, sorgu, zorunlu) OI reference number used to retrieve
                the FAST transaction result.

        Yanıt alanları: transferCompleteDate, resultCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-fast-result
        """
        _query = merge(
            {
                "oiReference": oi_reference,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/paymentrequest/getFastResult",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def pr_payment_request_control(
        self,
        *,
        request_payment_reference: str,
        request_payment_flow_type: str,
        creditor_identity_value: str,
        creditor_title: str,
        creditor_iban: str,
        amount: str,
        payment_intent: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Payment Request Control.

        ``POST /v1/paymentrequest/paymentControl``

        Kapsam: ``public`` · Akış: client credentials

        Checks and validates a payment request by using the provided payment reference, flow
        type, creditor identity, creditor title, creditor IBAN, amount, and payment intent
        information. The response returns the payment request control result, return code, and
        validation result details.

        Args:
            request_payment_reference: (``requestPaymentReference``, gövde, zorunlu) Payment
                request reference number used to identify the payment request.
            request_payment_flow_type: (``requestPaymentFlowType``, gövde, zorunlu) Flow type of
                the payment request.
            creditor_identity_value: (``creditorIdentityValue``, gövde, zorunlu) Identity value
                of the creditor.
            creditor_title: (``creditorTitle``, gövde, zorunlu) Title or name of the creditor.
            creditor_iban: (``creditorIBAN``, gövde, zorunlu) IBAN of the creditor account.
            amount: (gövde, zorunlu) Payment request amount.
            payment_intent: (``paymentIntent``, gövde, zorunlu) Payment intent or purpose
                information of the payment request.

        Yanıt alanları: isSuccess, returnCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-request-control
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "requestPaymentReference": request_payment_reference,
                "requestPaymentFlowType": request_payment_flow_type,
                "creditorIdentityValue": creditor_identity_value,
                "creditorTitle": creditor_title,
                "creditorIBAN": creditor_iban,
                "amount": amount,
                "paymentIntent": payment_intent,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/paymentrequest/paymentControl",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pr_payment_transaction(
        self,
        *,
        account_number: int,
        language_id: int,
        account_suffix: int | None = None,
        only_has_avaible_balance: bool | None = None,
        only_open: bool | None = None,
        only_with_no_balance: bool | None = None,
        only_current: bool | None = None,
        shared_with_multi_signature: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """PR - Payment Transaction.

        ``POST /v1/paymentrequest/transfer``

        Kapsam: ``transfers`` · Akış: client credentials

        Retrieves the account list for payment request transfer operations according to the
        provided customer, language, account suffix, balance, account status, current account,
        and multi-signature sharing filters. The response includes account details such as
        account name, suffix, balance, available balance, currency, IBAN, product type, opening
        date, branch information, customer name, maturity dates, and active status.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) Customer account number used to
                retrieve the account list.
            language_id: (``languageId``, gövde, zorunlu) Language identifier used for account
                information and descriptions.
            account_suffix: (``accountSuffix``, gövde) Account suffix used to filter the account
                list.
            only_has_avaible_balance: (``onlyHasAvaibleBalance``, gövde) Indicates whether only
                accounts with available balance should be returned.
            only_open: (``onlyOpen``, gövde) Indicates whether only open accounts should be
                returned.
            only_with_no_balance: (``onlyWithNoBalance``, gövde) Indicates whether only accounts
                with no balance should be returned.
            only_current: (``onlyCurrent``, gövde) Indicates whether only current accounts
                should be returned.
            shared_with_multi_signature: (``sharedWithMultiSignature``, gövde) Indicates whether
                accounts shared with multi-signature authorization should be included.

        Yanıt alanları: executionReferenceId, accountList, name, suffix, fxId, iban, type,
        openDate, branchName, branchId, withHoldingAmount, customerName, maturityBeginDate,
        maturityEndDate, isActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-transaction
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumber": account_number,
                "languageId": language_id,
                "accountSuffix": account_suffix,
                "onlyHasAvaibleBalance": only_has_avaible_balance,
                "onlyOpen": only_open,
                "onlyWithNoBalance": only_with_no_balance,
                "onlyCurrent": only_current,
                "sharedWithMultiSignature": shared_with_multi_signature,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/paymentrequest/transfer",
            scope="transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
