"""E-ticaret uç noktaları (``kt.ecommerce``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncEcommerce", "Ecommerce"]


class Ecommerce(Resource):
    """E-ticaret - ``kt.ecommerce``."""

    def ecommerce_application_refund_v1(
        self,
        *,
        application_id: str,
        reference_id: str,
        refund_type: str,
        refund_amount: Number,
        order_date: int,
        order_id: str,
        promotion_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Application Refund.

        ``POST /v1/lendings/{applicationId}/refund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Allows partial or full refund of funding.

        Args:
            application_id: (``applicationId``, yol, zorunlu)
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            refund_type: (``refundType``, gövde, zorunlu) Full or partial refund. Enum: [ FULL,
                PARTIAL ].
            refund_amount: (``refundAmount``, gövde, zorunlu) Refund amount.
            order_date: (``orderDate``, gövde, zorunlu) Date of the returned order
            order_id: (``orderId``, gövde, zorunlu) Id of the returned order.
            promotion_id: (``promotionId``, gövde) Preset id for applied promotion

        Yanıt alanları: isSuccess, responseCode, responseMessage, bankReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "refundType": refund_type,
                "refundAmount": refund_amount,
                "orderDate": order_date,
                "orderId": order_id,
                "promotionId": promotion_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/lendings/{applicationId}/refund",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_application_refund_v1_2(
        self,
        *,
        application_id: str,
        x_company_id: str,
        x_sub_company_id: int,
        reference_id: str,
        refund_type: str,
        refund_amount: Number,
        order_date: int,
        order_id: str,
        application_id_: str | None = None,
        promotion_id: str | None = None,
        invoice_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Application Refund.

        ``POST /v1/lendings/{applicationId}/refund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API performs a refund transaction for a lending application. The refund is
        processed using the specified application id, company information, reference information
        and refund details.

        Args:
            application_id: (``applicationId``, yol, zorunlu) Unique lending application
                identifier for which the refund will be processed.
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the refund request.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the refund request.
            application_id_: (``applicationId``, gövde)
            reference_id: (``referenceId``, gövde, zorunlu) Reference identifier of the refund
                transaction.
            refund_type: (``refundType``, gövde, zorunlu) Type of the refund transaction.
            refund_amount: (``refundAmount``, gövde, zorunlu) Amount to be refunded.
            order_date: (``orderDate``, gövde, zorunlu) Order date related to the refund
                transaction.
            order_id: (``orderId``, gövde, zorunlu) Order identifier related to the refund
                transaction.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the refund
                transaction.
            invoice_number: (``invoiceNumber``, gövde) Invoice number related to the refund
                transaction.

        Yanıt alanları: isSuccess, responseCode, responseMessage, bankReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "applicationId": application_id_,
                "referenceId": reference_id,
                "refundType": refund_type,
                "refundAmount": refund_amount,
                "orderDate": order_date,
                "orderId": order_id,
                "promotionId": promotion_id,
                "invoiceNumber": invoice_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/lendings/{applicationId}/refund",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_get_lending_information_v1(
        self,
        *,
        application_id: str,
        applicaction_id: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Get Lending Information.

        ``GET /v1/lendings/{applicationId}``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Its purpose is to question the details of the loan applied for.

        Args:
            application_id: (``applicationId``, yol, zorunlu)
            applicaction_id: (``applicactionId``, sorgu, zorunlu) Application Number

        Yanıt alanları: applicationId, isApproved, applicationDate, responseCode,
        responseMessage, type, allocationInformation, isSuccess, allocationDate,
        totalRefundAmount, refundHistory, referenceId, bankReferenceId, refundDate, refundType,
        refundAmount, paymentPlan, lendingAmount, interestRate, term, totalPaymentAmount,
        annualEffectiveInterestRate, monthlyPayments, amount, dueDate, isPaid, paymentDate,
        details, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information
        """
        _query = merge(
            {
                "applicactionId": applicaction_id,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/lendings/{applicationId}",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            options=request_options,
        )

    def ecommerce_get_lending_information_v1_2(
        self,
        *,
        application_id: str,
        client_id: str,
        x_sub_company_id: int,
        date: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Get Lending Information.

        ``GET /v1/lendings/{applicationId}``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API retrieves the details of a lending application by application id. The response
        includes application status, invoice information, allocation information, refund
        history, payment plan and digital onboarding information.

        Args:
            application_id: (``applicationId``, yol, zorunlu) Unique lending application
                identifier to be queried.
            client_id: (sorgu, zorunlu) Client identifier used to determine the company
                initiating the request.
            x_sub_company_id: (``x-sub-company-id``, sorgu, zorunlu) Sub-company identifier used
                to determine the related sub-company for the request.
            date: (sorgu, zorunlu) Date parameter used to query the lending application details.

        Yanıt alanları: applicationId, isApproved, isInvoiceApproved, applicationDate,
        responseCode, responseMessage, type, isActiveCustomer, isDigitalChannelCustomer,
        allocationInformation, isSuccess, allocationDate, refundInformation, totalRefundAmount,
        refundHistory, referenceId, bankReferenceId, refundDate, refundType, refundAmount,
        invoiceInformation, invoiceStatus, invoiceDescription, paymentPlan, lendingAmount,
        interestRate, totalPaymentAmount, annualEffectiveInterestRate,
        monthlyEffectiveInterestRate, term, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information
        """
        _query = merge(
            {
                "client_id": client_id,
                "x-sub-company-id": x_sub_company_id,
                "date": date,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/lendings/{applicationId}",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            options=request_options,
        )

    def ecommerce_lendings_v1(
        self,
        *,
        reference_id: str,
        pre_approved_application_id: str,
        national_identity_number: str,
        gsm_number: str,
        total_term: int,
        type: str,
        time_to_live: int,
        order_id: str,
        cart: Mapping[str, Any],
        callback_url: str | None = None,
        birthdate: str | None = None,
        promotion_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Lendings.

        ``POST /v1/lendings``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Allows you to apply for funding.

        Args:
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            pre_approved_application_id: (``preApprovedApplicationId``, gövde, zorunlu)
                Pre-approved funding application number.
            callback_url: (``callbackUrl``, gövde) URL to return after financing disbursement
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) National
                identification number.
            birthdate: (gövde)
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's confirmed mobile phone
                number.
            total_term: (``totalTerm``, gövde, zorunlu) Total term.
            type: (gövde, zorunlu) Selected financing type.
            time_to_live: (``timeToLive``, gövde, zorunlu) The lifetime of the basket. It should
                be used and returned within this period.
            order_id: (``orderId``, gövde, zorunlu) Order number.
            promotion_id: (``promotionId``, gövde) Predetermined id for the promotion to be
                applied
            cart: (gövde, zorunlu) Contains price and cart product information.

        Yanıt alanları: applicationId, isApproved, applicationDate, responseCode,
        responseMessage, bankRedirectionUrl, timeToLive, paymentPlan, lendingAmount,
        interestRate, term, totalPaymentAmount, annualEffectiveInterestRate, monthlyPayments,
        amount, dueDate, details, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "preApprovedApplicationId": pre_approved_application_id,
                "callbackUrl": callback_url,
                "nationalIdentityNumber": national_identity_number,
                "birthdate": birthdate,
                "gsmNumber": gsm_number,
                "totalTerm": total_term,
                "type": type,
                "timeToLive": time_to_live,
                "orderId": order_id,
                "promotionId": promotion_id,
                "cart": cart,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/lendings",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_lendings_v1_2(
        self,
        *,
        x_company_id: str,
        x_sub_company_id: int,
        reference_id: str,
        pre_approved_application_id: str,
        callback_url: str,
        failcallback_url: str,
        national_identity_number: str,
        birth_date: str,
        gsm_number: str,
        total_term: int,
        type: str,
        time_to_live: int,
        order_id: str,
        company_code: str,
        cart: Mapping[str, Any],
        promotion_id: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Lendings.

        ``POST /v1/lendings``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API creates a lending application using the customer's pre-approved application
        information, selected term, order details, callback URLs and cart content. The response
        includes the application result, bank redirection URL and payment plan details.

        Args:
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the lending application.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the lending application.
            reference_id: (``referenceId``, gövde, zorunlu) Unique reference identifier of the
                lending application request.
            pre_approved_application_id: (``preApprovedApplicationId``, gövde, zorunlu)
                Pre-approved application identifier obtained from the pre-approved monthly payments
                query.
            callback_url: (``callbackUrl``, gövde, zorunlu) URL to which the customer will be
                redirected after a successful lending application flow.
            failcallback_url: (``failcallbackUrl``, gövde, zorunlu) URL to which the customer
                will be redirected if the lending application flow fails.
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) Customer's
                national identity number.
            birth_date: (``birthDate``, gövde, zorunlu) Customer's birth date.
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's mobile phone number.
            total_term: (``totalTerm``, gövde, zorunlu) Total term selected for the lending
                application.
            type: (gövde, zorunlu) Type of the selected lending/payment option.
            time_to_live: (``timeToLive``, gövde, zorunlu) Validity duration of the lending
                application flow.
            order_id: (``orderId``, gövde, zorunlu) Order identifier related to the lending
                application.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the lending
                application.
            company_code: (``companyCode``, gövde, zorunlu) Company code associated with the
                lending application.
            cart: (gövde, zorunlu) Cart information containing price and item details.

        Yanıt alanları: applicationId, isApproved, applicationDate, responseCode,
        responseMessage, bankRedirectionUrl, timeToLive, paymentPlan, lendingAmount,
        interestRate, totalPaymentAmount, annualEffectiveInterestRate,
        monthlyEffectiveInterestRate, term, monthlyPayments, amount, type, dueDate, details,
        name

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "referenceId": reference_id,
                "preApprovedApplicationId": pre_approved_application_id,
                "callbackUrl": callback_url,
                "failcallbackUrl": failcallback_url,
                "nationalIdentityNumber": national_identity_number,
                "birthDate": birth_date,
                "gsmNumber": gsm_number,
                "totalTerm": total_term,
                "type": type,
                "timeToLive": time_to_live,
                "orderId": order_id,
                "promotionId": promotion_id,
                "companyCode": company_code,
                "cart": cart,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/lendings",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_monthly_payments_v1(
        self,
        *,
        reference_id: str,
        max_term: int,
        promotion_id: int | None = None,
        cart: Mapping[str, Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Monthly Payments.

        ``POST /v1/query/monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Estimated monthly return service based on the customer's cart.

        Args:
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            max_term: (``maxTerm``, gövde, zorunlu) The maxterm information sent in the request
                is optional and additional information.
            promotion_id: (``promotionId``, gövde) Predetermined ID for the promotion to be
                applied.
            cart: (gövde) Contains price and cart product information.

        Yanıt alanları: interestRate, amount, totalPaymentAmount, annualEffectiveInterestRate,
        type

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "maxTerm": max_term,
                "promotionId": promotion_id,
                "cart": cart,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/query/monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_monthly_payments_v1_2(
        self,
        *,
        x_company_id: str,
        x_sub_company_id: int,
        reference_id: str,
        max_term: int,
        cart: Mapping[str, Any],
        promotion_id: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Monthly Payments.

        ``POST /v1/query/monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API queries available monthly payment options based on company information,
        reference information, maximum term, promotion information and cart content. The
        response includes available payment terms, interest rates and payment amounts.

        Args:
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the monthly payment query.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the monthly payment query.
            reference_id: (``referenceId``, gövde, zorunlu) Unique reference identifier of the
                monthly payment query request.
            max_term: (``maxTerm``, gövde, zorunlu) Maximum term to be considered for monthly
                payment options.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the monthly
                payment query.
            cart: (gövde, zorunlu) Cart information containing price and item details.

        Yanıt alanları: monthlyPayments, term, interestRate, amount, totalPaymentAmount,
        annualEffectiveInterestRate, monthlyEffectiveInterestRate, type, responseCode,
        responseMessage, errors, message, code

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "referenceId": reference_id,
                "maxTerm": max_term,
                "promotionId": promotion_id,
                "cart": cart,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/query/monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_pre_approved_monthly_payments_v1(
        self,
        *,
        reference_id: str,
        national_identity_number: str,
        gsm_number: str,
        max_term: int,
        order_id: str,
        cart: Mapping[str, Any],
        birthdate: str | None = None,
        promotion_id: int | None = None,
        is_mixed_cart: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Pre Approved Monthly Payments.

        ``POST /v1/query/pre-approved-monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Returns the pre-approved monthly payment table according to the customer's cart and
        personal information.

        Args:
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) National
                identification number.
            birthdate: (gövde) Customer's date of birth
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's confirmed mobile phone
                number.
            max_term: (``maxTerm``, gövde, zorunlu) The maxterm information sent in the request
                is optional and additional information.
            order_id: (``orderId``, gövde, zorunlu) Order number
            promotion_id: (``promotionId``, gövde) Predetermined id for the promotion to be
                applied
            cart: (gövde, zorunlu) Contains price and cart product information
            is_mixed_cart: (``IsMixedCart``, gövde) Type of products in the basket as a whole

        Yanıt alanları: isSuccess, isActiveCustomer, isDigitalChannelCustomer, responseCode,
        responseMessage, preApprovedApplicationId, monthlyPayments, term, interestRate, amount,
        totalPaymentAmount, annualEffectiveInterestRate, type

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "nationalIdentityNumber": national_identity_number,
                "birthdate": birthdate,
                "gsmNumber": gsm_number,
                "maxTerm": max_term,
                "orderId": order_id,
                "promotionId": promotion_id,
                "cart": cart,
                "IsMixedCart": is_mixed_cart,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/query/pre-approved-monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def ecommerce_pre_approved_monthly_payments_v1_2(
        self,
        *,
        x_company_id: str,
        x_sub_company_id: int,
        agent_code: str,
        reference_id: str,
        national_identity_number: str,
        birth_date: str,
        gsm_number: str,
        max_term: int,
        order_id: str,
        company_code: str,
        cart: Mapping[str, Any],
        promotion_id: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Pre Approved Monthly Payments.

        ``POST /v1/query/pre-approved-monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API queries pre-approved monthly payment options for a customer based on company
        information, customer identity information, order details and cart content.

        Args:
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the request.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the request.
            agent_code: (``agentCode``, gövde, zorunlu) Agent code associated with the request.
            reference_id: (``referenceId``, gövde, zorunlu) Unique reference identifier of the
                request.
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) Customer's
                national identity number.
            birth_date: (``birthDate``, gövde, zorunlu) Customer's birth date.
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's mobile phone number.
            max_term: (``maxTerm``, gövde, zorunlu) Maximum term to be considered for monthly
                payment options.
            order_id: (``orderId``, gövde, zorunlu) Order identifier related to the payment
                query.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the payment
                query.
            company_code: (``companyCode``, gövde, zorunlu) Company code associated with the
                payment query.
            cart: (gövde, zorunlu) Cart information containing price and item details.

        Yanıt alanları: isSuccess, isActiveCustomer, isDigitalChannelCustomer, responseCode,
        responseMessage, preApprovedApplicationId, monthlyPayments, term, interestRate,
        totalPaymentAmount, amount, annualEffectiveInterestRate, monthlyEffectiveInterestRate,
        type, contributionAmount, contributionRate, commissionBsmvAmount, commissionKkdfAmount,
        shopIncome

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "agentCode": agent_code,
                "referenceId": reference_id,
                "nationalIdentityNumber": national_identity_number,
                "birthDate": birth_date,
                "gsmNumber": gsm_number,
                "maxTerm": max_term,
                "orderId": order_id,
                "promotionId": promotion_id,
                "companyCode": company_code,
                "cart": cart,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/query/pre-approved-monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncEcommerce(AsyncResource):
    """E-ticaret (asenkron) - ``kt.ecommerce``."""

    async def ecommerce_application_refund_v1(
        self,
        *,
        application_id: str,
        reference_id: str,
        refund_type: str,
        refund_amount: Number,
        order_date: int,
        order_id: str,
        promotion_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Application Refund.

        ``POST /v1/lendings/{applicationId}/refund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Allows partial or full refund of funding.

        Args:
            application_id: (``applicationId``, yol, zorunlu)
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            refund_type: (``refundType``, gövde, zorunlu) Full or partial refund. Enum: [ FULL,
                PARTIAL ].
            refund_amount: (``refundAmount``, gövde, zorunlu) Refund amount.
            order_date: (``orderDate``, gövde, zorunlu) Date of the returned order
            order_id: (``orderId``, gövde, zorunlu) Id of the returned order.
            promotion_id: (``promotionId``, gövde) Preset id for applied promotion

        Yanıt alanları: isSuccess, responseCode, responseMessage, bankReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "refundType": refund_type,
                "refundAmount": refund_amount,
                "orderDate": order_date,
                "orderId": order_id,
                "promotionId": promotion_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/lendings/{applicationId}/refund",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_application_refund_v1_2(
        self,
        *,
        application_id: str,
        x_company_id: str,
        x_sub_company_id: int,
        reference_id: str,
        refund_type: str,
        refund_amount: Number,
        order_date: int,
        order_id: str,
        application_id_: str | None = None,
        promotion_id: str | None = None,
        invoice_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Application Refund.

        ``POST /v1/lendings/{applicationId}/refund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API performs a refund transaction for a lending application. The refund is
        processed using the specified application id, company information, reference information
        and refund details.

        Args:
            application_id: (``applicationId``, yol, zorunlu) Unique lending application
                identifier for which the refund will be processed.
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the refund request.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the refund request.
            application_id_: (``applicationId``, gövde)
            reference_id: (``referenceId``, gövde, zorunlu) Reference identifier of the refund
                transaction.
            refund_type: (``refundType``, gövde, zorunlu) Type of the refund transaction.
            refund_amount: (``refundAmount``, gövde, zorunlu) Amount to be refunded.
            order_date: (``orderDate``, gövde, zorunlu) Order date related to the refund
                transaction.
            order_id: (``orderId``, gövde, zorunlu) Order identifier related to the refund
                transaction.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the refund
                transaction.
            invoice_number: (``invoiceNumber``, gövde) Invoice number related to the refund
                transaction.

        Yanıt alanları: isSuccess, responseCode, responseMessage, bankReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "applicationId": application_id_,
                "referenceId": reference_id,
                "refundType": refund_type,
                "refundAmount": refund_amount,
                "orderDate": order_date,
                "orderId": order_id,
                "promotionId": promotion_id,
                "invoiceNumber": invoice_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/lendings/{applicationId}/refund",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_get_lending_information_v1(
        self,
        *,
        application_id: str,
        applicaction_id: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Get Lending Information.

        ``GET /v1/lendings/{applicationId}``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Its purpose is to question the details of the loan applied for.

        Args:
            application_id: (``applicationId``, yol, zorunlu)
            applicaction_id: (``applicactionId``, sorgu, zorunlu) Application Number

        Yanıt alanları: applicationId, isApproved, applicationDate, responseCode,
        responseMessage, type, allocationInformation, isSuccess, allocationDate,
        totalRefundAmount, refundHistory, referenceId, bankReferenceId, refundDate, refundType,
        refundAmount, paymentPlan, lendingAmount, interestRate, term, totalPaymentAmount,
        annualEffectiveInterestRate, monthlyPayments, amount, dueDate, isPaid, paymentDate,
        details, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information
        """
        _query = merge(
            {
                "applicactionId": applicaction_id,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/lendings/{applicationId}",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            options=request_options,
        )

    async def ecommerce_get_lending_information_v1_2(
        self,
        *,
        application_id: str,
        client_id: str,
        x_sub_company_id: int,
        date: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Get Lending Information.

        ``GET /v1/lendings/{applicationId}``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API retrieves the details of a lending application by application id. The response
        includes application status, invoice information, allocation information, refund
        history, payment plan and digital onboarding information.

        Args:
            application_id: (``applicationId``, yol, zorunlu) Unique lending application
                identifier to be queried.
            client_id: (sorgu, zorunlu) Client identifier used to determine the company
                initiating the request.
            x_sub_company_id: (``x-sub-company-id``, sorgu, zorunlu) Sub-company identifier used
                to determine the related sub-company for the request.
            date: (sorgu, zorunlu) Date parameter used to query the lending application details.

        Yanıt alanları: applicationId, isApproved, isInvoiceApproved, applicationDate,
        responseCode, responseMessage, type, isActiveCustomer, isDigitalChannelCustomer,
        allocationInformation, isSuccess, allocationDate, refundInformation, totalRefundAmount,
        refundHistory, referenceId, bankReferenceId, refundDate, refundType, refundAmount,
        invoiceInformation, invoiceStatus, invoiceDescription, paymentPlan, lendingAmount,
        interestRate, totalPaymentAmount, annualEffectiveInterestRate,
        monthlyEffectiveInterestRate, term, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information
        """
        _query = merge(
            {
                "client_id": client_id,
                "x-sub-company-id": x_sub_company_id,
                "date": date,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/lendings/{applicationId}",
            scope="digital_payments",
            flow="client_credentials",
            path_params={"applicationId": application_id},
            query=_query,
            options=request_options,
        )

    async def ecommerce_lendings_v1(
        self,
        *,
        reference_id: str,
        pre_approved_application_id: str,
        national_identity_number: str,
        gsm_number: str,
        total_term: int,
        type: str,
        time_to_live: int,
        order_id: str,
        cart: Mapping[str, Any],
        callback_url: str | None = None,
        birthdate: str | None = None,
        promotion_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Lendings.

        ``POST /v1/lendings``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Allows you to apply for funding.

        Args:
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            pre_approved_application_id: (``preApprovedApplicationId``, gövde, zorunlu)
                Pre-approved funding application number.
            callback_url: (``callbackUrl``, gövde) URL to return after financing disbursement
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) National
                identification number.
            birthdate: (gövde)
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's confirmed mobile phone
                number.
            total_term: (``totalTerm``, gövde, zorunlu) Total term.
            type: (gövde, zorunlu) Selected financing type.
            time_to_live: (``timeToLive``, gövde, zorunlu) The lifetime of the basket. It should
                be used and returned within this period.
            order_id: (``orderId``, gövde, zorunlu) Order number.
            promotion_id: (``promotionId``, gövde) Predetermined id for the promotion to be
                applied
            cart: (gövde, zorunlu) Contains price and cart product information.

        Yanıt alanları: applicationId, isApproved, applicationDate, responseCode,
        responseMessage, bankRedirectionUrl, timeToLive, paymentPlan, lendingAmount,
        interestRate, term, totalPaymentAmount, annualEffectiveInterestRate, monthlyPayments,
        amount, dueDate, details, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "preApprovedApplicationId": pre_approved_application_id,
                "callbackUrl": callback_url,
                "nationalIdentityNumber": national_identity_number,
                "birthdate": birthdate,
                "gsmNumber": gsm_number,
                "totalTerm": total_term,
                "type": type,
                "timeToLive": time_to_live,
                "orderId": order_id,
                "promotionId": promotion_id,
                "cart": cart,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/lendings",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_lendings_v1_2(
        self,
        *,
        x_company_id: str,
        x_sub_company_id: int,
        reference_id: str,
        pre_approved_application_id: str,
        callback_url: str,
        failcallback_url: str,
        national_identity_number: str,
        birth_date: str,
        gsm_number: str,
        total_term: int,
        type: str,
        time_to_live: int,
        order_id: str,
        company_code: str,
        cart: Mapping[str, Any],
        promotion_id: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Lendings.

        ``POST /v1/lendings``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API creates a lending application using the customer's pre-approved application
        information, selected term, order details, callback URLs and cart content. The response
        includes the application result, bank redirection URL and payment plan details.

        Args:
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the lending application.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the lending application.
            reference_id: (``referenceId``, gövde, zorunlu) Unique reference identifier of the
                lending application request.
            pre_approved_application_id: (``preApprovedApplicationId``, gövde, zorunlu)
                Pre-approved application identifier obtained from the pre-approved monthly payments
                query.
            callback_url: (``callbackUrl``, gövde, zorunlu) URL to which the customer will be
                redirected after a successful lending application flow.
            failcallback_url: (``failcallbackUrl``, gövde, zorunlu) URL to which the customer
                will be redirected if the lending application flow fails.
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) Customer's
                national identity number.
            birth_date: (``birthDate``, gövde, zorunlu) Customer's birth date.
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's mobile phone number.
            total_term: (``totalTerm``, gövde, zorunlu) Total term selected for the lending
                application.
            type: (gövde, zorunlu) Type of the selected lending/payment option.
            time_to_live: (``timeToLive``, gövde, zorunlu) Validity duration of the lending
                application flow.
            order_id: (``orderId``, gövde, zorunlu) Order identifier related to the lending
                application.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the lending
                application.
            company_code: (``companyCode``, gövde, zorunlu) Company code associated with the
                lending application.
            cart: (gövde, zorunlu) Cart information containing price and item details.

        Yanıt alanları: applicationId, isApproved, applicationDate, responseCode,
        responseMessage, bankRedirectionUrl, timeToLive, paymentPlan, lendingAmount,
        interestRate, totalPaymentAmount, annualEffectiveInterestRate,
        monthlyEffectiveInterestRate, term, monthlyPayments, amount, type, dueDate, details,
        name

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "referenceId": reference_id,
                "preApprovedApplicationId": pre_approved_application_id,
                "callbackUrl": callback_url,
                "failcallbackUrl": failcallback_url,
                "nationalIdentityNumber": national_identity_number,
                "birthDate": birth_date,
                "gsmNumber": gsm_number,
                "totalTerm": total_term,
                "type": type,
                "timeToLive": time_to_live,
                "orderId": order_id,
                "promotionId": promotion_id,
                "companyCode": company_code,
                "cart": cart,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/lendings",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_monthly_payments_v1(
        self,
        *,
        reference_id: str,
        max_term: int,
        promotion_id: int | None = None,
        cart: Mapping[str, Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Monthly Payments.

        ``POST /v1/query/monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Estimated monthly return service based on the customer's cart.

        Args:
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            max_term: (``maxTerm``, gövde, zorunlu) The maxterm information sent in the request
                is optional and additional information.
            promotion_id: (``promotionId``, gövde) Predetermined ID for the promotion to be
                applied.
            cart: (gövde) Contains price and cart product information.

        Yanıt alanları: interestRate, amount, totalPaymentAmount, annualEffectiveInterestRate,
        type

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "maxTerm": max_term,
                "promotionId": promotion_id,
                "cart": cart,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/query/monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_monthly_payments_v1_2(
        self,
        *,
        x_company_id: str,
        x_sub_company_id: int,
        reference_id: str,
        max_term: int,
        cart: Mapping[str, Any],
        promotion_id: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Monthly Payments.

        ``POST /v1/query/monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API queries available monthly payment options based on company information,
        reference information, maximum term, promotion information and cart content. The
        response includes available payment terms, interest rates and payment amounts.

        Args:
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the monthly payment query.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the monthly payment query.
            reference_id: (``referenceId``, gövde, zorunlu) Unique reference identifier of the
                monthly payment query request.
            max_term: (``maxTerm``, gövde, zorunlu) Maximum term to be considered for monthly
                payment options.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the monthly
                payment query.
            cart: (gövde, zorunlu) Cart information containing price and item details.

        Yanıt alanları: monthlyPayments, term, interestRate, amount, totalPaymentAmount,
        annualEffectiveInterestRate, monthlyEffectiveInterestRate, type, responseCode,
        responseMessage, errors, message, code

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "referenceId": reference_id,
                "maxTerm": max_term,
                "promotionId": promotion_id,
                "cart": cart,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/query/monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_pre_approved_monthly_payments_v1(
        self,
        *,
        reference_id: str,
        national_identity_number: str,
        gsm_number: str,
        max_term: int,
        order_id: str,
        cart: Mapping[str, Any],
        birthdate: str | None = None,
        promotion_id: int | None = None,
        is_mixed_cart: bool | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Pre Approved Monthly Payments.

        ``POST /v1/query/pre-approved-monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Returns the pre-approved monthly payment table according to the customer's cart and
        personal information.

        Args:
            reference_id: (``referenceId``, gövde, zorunlu) Unique ID number of the request
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) National
                identification number.
            birthdate: (gövde) Customer's date of birth
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's confirmed mobile phone
                number.
            max_term: (``maxTerm``, gövde, zorunlu) The maxterm information sent in the request
                is optional and additional information.
            order_id: (``orderId``, gövde, zorunlu) Order number
            promotion_id: (``promotionId``, gövde) Predetermined id for the promotion to be
                applied
            cart: (gövde, zorunlu) Contains price and cart product information
            is_mixed_cart: (``IsMixedCart``, gövde) Type of products in the basket as a whole

        Yanıt alanları: isSuccess, isActiveCustomer, isDigitalChannelCustomer, responseCode,
        responseMessage, preApprovedApplicationId, monthlyPayments, term, interestRate, amount,
        totalPaymentAmount, annualEffectiveInterestRate, type

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceId": reference_id,
                "nationalIdentityNumber": national_identity_number,
                "birthdate": birthdate,
                "gsmNumber": gsm_number,
                "maxTerm": max_term,
                "orderId": order_id,
                "promotionId": promotion_id,
                "cart": cart,
                "IsMixedCart": is_mixed_cart,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/query/pre-approved-monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def ecommerce_pre_approved_monthly_payments_v1_2(
        self,
        *,
        x_company_id: str,
        x_sub_company_id: int,
        agent_code: str,
        reference_id: str,
        national_identity_number: str,
        birth_date: str,
        gsm_number: str,
        max_term: int,
        order_id: str,
        company_code: str,
        cart: Mapping[str, Any],
        promotion_id: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ecommerce Pre Approved Monthly Payments.

        ``POST /v1/query/pre-approved-monthly-payments``

        Kapsam: ``digital_payments`` · Akış: client credentials

        This API queries pre-approved monthly payment options for a customer based on company
        information, customer identity information, order details and cart content.

        Args:
            x_company_id: (``x-company-id``, gövde, zorunlu) Company identifier used to
                determine the company initiating the request.
            x_sub_company_id: (``x-sub-company-id``, gövde, zorunlu) Sub-company identifier used
                to determine the related sub-company for the request.
            agent_code: (``agentCode``, gövde, zorunlu) Agent code associated with the request.
            reference_id: (``referenceId``, gövde, zorunlu) Unique reference identifier of the
                request.
            national_identity_number: (``nationalIdentityNumber``, gövde, zorunlu) Customer's
                national identity number.
            birth_date: (``birthDate``, gövde, zorunlu) Customer's birth date.
            gsm_number: (``gsmNumber``, gövde, zorunlu) Customer's mobile phone number.
            max_term: (``maxTerm``, gövde, zorunlu) Maximum term to be considered for monthly
                payment options.
            order_id: (``orderId``, gövde, zorunlu) Order identifier related to the payment
                query.
            promotion_id: (``promotionId``, gövde) Promotion identifier related to the payment
                query.
            company_code: (``companyCode``, gövde, zorunlu) Company code associated with the
                payment query.
            cart: (gövde, zorunlu) Cart information containing price and item details.

        Yanıt alanları: isSuccess, isActiveCustomer, isDigitalChannelCustomer, responseCode,
        responseMessage, preApprovedApplicationId, monthlyPayments, term, interestRate,
        totalPaymentAmount, amount, annualEffectiveInterestRate, monthlyEffectiveInterestRate,
        type, contributionAmount, contributionRate, commissionBsmvAmount, commissionKkdfAmount,
        shopIncome

        Doküman: https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "x-company-id": x_company_id,
                "x-sub-company-id": x_sub_company_id,
                "agentCode": agent_code,
                "referenceId": reference_id,
                "nationalIdentityNumber": national_identity_number,
                "birthDate": birth_date,
                "gsmNumber": gsm_number,
                "maxTerm": max_term,
                "orderId": order_id,
                "promotionId": promotion_id,
                "companyCode": company_code,
                "cart": cart,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/query/pre-approved-monthly-payments",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
