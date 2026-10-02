"""Kredibilite uç noktaları (``kt.credibility``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["AsyncCredibility", "Credibility"]


class Credibility(Resource):
    """Kredibilite - ``kt.credibility``."""

    def customer_overall_limit_values(
        self,
        *,
        account_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Overall Limit Values.

        ``POST /v1/Loans/LastAllotmentTopLimit``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves the latest allotment top limit information for the specified account number.
        The response includes customer and group level cash, non-cash, total limit, and risk
        information.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) Account number used to retrieve
                the latest allotment top limit information.

        Yanıt alanları: CashLimit, NonCashLimit, TotalLimit, CashRisk, NonCashRisk, TotalRisk,
        GroupCashLimit, GroupNonCashLimit, GroupTotalLimit, GroupCashRisk, GroupNonCashRisk,
        GroupTotalRisk

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/customer-overall-limit-values
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumber": account_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/Loans/LastAllotmentTopLimit",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def final_credit_decision_recommendation(
        self,
        *,
        account_number_list: Sequence[Any],
        group_number: int,
        credere_art_report_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Final Credit Decision Recommendation.

        ``POST /v1/Loans/AllotmentFinalDecision``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves final credit decision recommendation and allotment decision summary
        information for the provided account number list, group number, and Credere ART report
        number. The response includes approved limits, product limits, guarantor information,
        collateral limits, constraints, summary details, other conditions, and approval date.

        Args:
            account_number_list: (``accountNumberList``, gövde, zorunlu) List of account numbers
                to be included in the allotment final decision inquiry.
            group_number: (``groupNumber``, gövde, zorunlu) Group number used to retrieve the
                allotment decision summary.
            credere_art_report_number: (``credereArtReportNumber``, gövde, zorunlu) Credere ART
                report number associated with the allotment decision.

        Yanıt alanları: TopLimitList, AllotmentTopLimit, customerName, approvedCashLimit,
        approvedNonCashLimit, totalLimit, ProductLimitList, allotmentProductLimit, productName,
        approvedLimit, collateralType, collateralRange, collateralMargin, GuarantorList,
        allotmentGuarantor, description, OtherConditions, textValue, CollateralLimitList,
        allotmentCollateralLimit, approvedTotalLimit, ConstraintList, allotmentConstraint, name,
        typeName, constraintDetail, amount, SummaryList, allotmentSummary, allotmentSummaryName,
        ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/final-credit-decision-recommendation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumberList": account_number_list,
                "groupNumber": group_number,
                "credereArtReportNumber": credere_art_report_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/Loans/AllotmentFinalDecision",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_invoice_detail_v2(
        self,
        *,
        delivery_id_list: Sequence[Any],
        invoice_number_serial: str,
        invoice_date: DateLike,
        attachment: str,
        document_extension: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Invoice Detail V2.

        ``POST /v2/purchase/invoice``

        Kapsam: ``payments`` · Akış: client credentials

        Submits invoice details to the BOA system for delivery records related to the purchase
        process. The request includes the delivery ID list, invoice serial number, invoice date,
        document content and document extension. The response returns whether the invoice
        submission was successful and includes error details if available.

        Args:
            delivery_id_list: (``DeliveryIdList``, gövde, zorunlu) List of delivery record IDs
                to be associated with the invoice.
            invoice_number_serial: (``InvoiceNumberSerial``, gövde, zorunlu) Invoice serial and
                number information.
            invoice_date: (``InvoiceDate``, gövde, zorunlu) Invoice date.
            attachment: (``Attachment``, gövde, zorunlu) Content of the invoice document. It is
                typically sent as base64 encoded document data.
            document_extension: (``DocumentExtension``, gövde, zorunlu) File extension of the
                submitted invoice document. For example: pdf, jpg, png.

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/send-invoice-detail-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DeliveryIdList": delivery_id_list,
                "InvoiceNumberSerial": invoice_number_serial,
                "InvoiceDate": invoice_date,
                "Attachment": attachment,
                "DocumentExtension": document_extension,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/purchase/invoice",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def tardes_agricultural_score_inquiry(
        self,
        *,
        identity_number: str,
        force_daily: bool,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Tardes Agricultural Score Inquiry.

        ``POST /v1/inquiry/gettardesscore``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves Tardes agricultural score details by using the provided identity number and
        daily query preference. The response includes Tardes score information and the related
        score reason details.

        Args:
            identity_number: (``identityNumber``, gövde, zorunlu) Identity number used to
                retrieve Tardes agricultural score details.
            force_daily: (``forceDaily``, gövde, zorunlu) Indicates whether the score inquiry
                should be performed as a daily query.

        Yanıt alanları: tardesScoreInfo, tardesScoreId, referenceNumber, identityNumber,
        identityType, agricultureScore, scoreDate, exceptionCode, exceptionName, processStage,
        lastTransactionDate, systemDate, updateSystemDate, resourceCode, tardesScoreReasons,
        tardesScoreReasonCodeId, reasonCode, reasonName

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/tardes-agricultural-score-inquiry
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "identityNumber": identity_number,
                "forceDaily": force_daily,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/inquiry/gettardesscore",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def taxpayer_gib_identity_information(
        self,
        *,
        identity_number: str,
        force_online: bool,
        resource_code: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Taxpayer - GIB Identity Information.

        ``POST /v1/inquiry/gib-tax-payer``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves taxpayer identity and registration information from GIB by using the provided
        identity number, online query preference, and resource code. The response includes
        taxpayer identity, tax office, company, establishment, birth, address, occupation,
        branch, and activity details.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number or tax number
                used to retrieve taxpayer information.
            force_online: (``ForceOnline``, gövde, zorunlu) Indicates whether the inquiry should
                be performed online instead of using existing cached data.
            resource_code: (``ResourceCode``, gövde, zorunlu) Resource code used for the
                taxpayer inquiry process.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: queryResult, errorCodeDescription, queryReferenceNumber, taxPayerId,
        identityNumber, taxNumber, taxOfficeCode, taxOfficeName, title, surname, name,
        fathersName, corporatePersonQualifiedCode, corporatePersonQualifiedCodeDescription,
        companyType, companyTypeDescription, firmStatus, firmStatusDescription,
        taxLiabilityBeginDate, taxLiabilityEndDate, establishmentDate, establishmentCityName,
        establishmentCityCode, establishmentCountyName, establishmentCountyCode, birthDate,
        birthCityName, birthCityCode, birthCountyName, birthCountyCode, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/taxpayer-gib-identity-information
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ForceOnline": force_online,
                "ResourceCode": resource_code,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/inquiry/gib-tax-payer",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncCredibility(AsyncResource):
    """Kredibilite (asenkron) - ``kt.credibility``."""

    async def customer_overall_limit_values(
        self,
        *,
        account_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Overall Limit Values.

        ``POST /v1/Loans/LastAllotmentTopLimit``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves the latest allotment top limit information for the specified account number.
        The response includes customer and group level cash, non-cash, total limit, and risk
        information.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) Account number used to retrieve
                the latest allotment top limit information.

        Yanıt alanları: CashLimit, NonCashLimit, TotalLimit, CashRisk, NonCashRisk, TotalRisk,
        GroupCashLimit, GroupNonCashLimit, GroupTotalLimit, GroupCashRisk, GroupNonCashRisk,
        GroupTotalRisk

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/customer-overall-limit-values
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumber": account_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/Loans/LastAllotmentTopLimit",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def final_credit_decision_recommendation(
        self,
        *,
        account_number_list: Sequence[Any],
        group_number: int,
        credere_art_report_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Final Credit Decision Recommendation.

        ``POST /v1/Loans/AllotmentFinalDecision``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves final credit decision recommendation and allotment decision summary
        information for the provided account number list, group number, and Credere ART report
        number. The response includes approved limits, product limits, guarantor information,
        collateral limits, constraints, summary details, other conditions, and approval date.

        Args:
            account_number_list: (``accountNumberList``, gövde, zorunlu) List of account numbers
                to be included in the allotment final decision inquiry.
            group_number: (``groupNumber``, gövde, zorunlu) Group number used to retrieve the
                allotment decision summary.
            credere_art_report_number: (``credereArtReportNumber``, gövde, zorunlu) Credere ART
                report number associated with the allotment decision.

        Yanıt alanları: TopLimitList, AllotmentTopLimit, customerName, approvedCashLimit,
        approvedNonCashLimit, totalLimit, ProductLimitList, allotmentProductLimit, productName,
        approvedLimit, collateralType, collateralRange, collateralMargin, GuarantorList,
        allotmentGuarantor, description, OtherConditions, textValue, CollateralLimitList,
        allotmentCollateralLimit, approvedTotalLimit, ConstraintList, allotmentConstraint, name,
        typeName, constraintDetail, amount, SummaryList, allotmentSummary, allotmentSummaryName,
        ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/final-credit-decision-recommendation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumberList": account_number_list,
                "groupNumber": group_number,
                "credereArtReportNumber": credere_art_report_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/Loans/AllotmentFinalDecision",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_invoice_detail_v2(
        self,
        *,
        delivery_id_list: Sequence[Any],
        invoice_number_serial: str,
        invoice_date: DateLike,
        attachment: str,
        document_extension: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Invoice Detail V2.

        ``POST /v2/purchase/invoice``

        Kapsam: ``payments`` · Akış: client credentials

        Submits invoice details to the BOA system for delivery records related to the purchase
        process. The request includes the delivery ID list, invoice serial number, invoice date,
        document content and document extension. The response returns whether the invoice
        submission was successful and includes error details if available.

        Args:
            delivery_id_list: (``DeliveryIdList``, gövde, zorunlu) List of delivery record IDs
                to be associated with the invoice.
            invoice_number_serial: (``InvoiceNumberSerial``, gövde, zorunlu) Invoice serial and
                number information.
            invoice_date: (``InvoiceDate``, gövde, zorunlu) Invoice date.
            attachment: (``Attachment``, gövde, zorunlu) Content of the invoice document. It is
                typically sent as base64 encoded document data.
            document_extension: (``DocumentExtension``, gövde, zorunlu) File extension of the
                submitted invoice document. For example: pdf, jpg, png.

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/send-invoice-detail-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DeliveryIdList": delivery_id_list,
                "InvoiceNumberSerial": invoice_number_serial,
                "InvoiceDate": invoice_date,
                "Attachment": attachment,
                "DocumentExtension": document_extension,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/purchase/invoice",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def tardes_agricultural_score_inquiry(
        self,
        *,
        identity_number: str,
        force_daily: bool,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Tardes Agricultural Score Inquiry.

        ``POST /v1/inquiry/gettardesscore``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves Tardes agricultural score details by using the provided identity number and
        daily query preference. The response includes Tardes score information and the related
        score reason details.

        Args:
            identity_number: (``identityNumber``, gövde, zorunlu) Identity number used to
                retrieve Tardes agricultural score details.
            force_daily: (``forceDaily``, gövde, zorunlu) Indicates whether the score inquiry
                should be performed as a daily query.

        Yanıt alanları: tardesScoreInfo, tardesScoreId, referenceNumber, identityNumber,
        identityType, agricultureScore, scoreDate, exceptionCode, exceptionName, processStage,
        lastTransactionDate, systemDate, updateSystemDate, resourceCode, tardesScoreReasons,
        tardesScoreReasonCodeId, reasonCode, reasonName

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/tardes-agricultural-score-inquiry
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "identityNumber": identity_number,
                "forceDaily": force_daily,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/inquiry/gettardesscore",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def taxpayer_gib_identity_information(
        self,
        *,
        identity_number: str,
        force_online: bool,
        resource_code: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Taxpayer - GIB Identity Information.

        ``POST /v1/inquiry/gib-tax-payer``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves taxpayer identity and registration information from GIB by using the provided
        identity number, online query preference, and resource code. The response includes
        taxpayer identity, tax office, company, establishment, birth, address, occupation,
        branch, and activity details.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number or tax number
                used to retrieve taxpayer information.
            force_online: (``ForceOnline``, gövde, zorunlu) Indicates whether the inquiry should
                be performed online instead of using existing cached data.
            resource_code: (``ResourceCode``, gövde, zorunlu) Resource code used for the
                taxpayer inquiry process.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: queryResult, errorCodeDescription, queryReferenceNumber, taxPayerId,
        identityNumber, taxNumber, taxOfficeCode, taxOfficeName, title, surname, name,
        fathersName, corporatePersonQualifiedCode, corporatePersonQualifiedCodeDescription,
        companyType, companyTypeDescription, firmStatus, firmStatusDescription,
        taxLiabilityBeginDate, taxLiabilityEndDate, establishmentDate, establishmentCityName,
        establishmentCityCode, establishmentCountyName, establishmentCountyCode, birthDate,
        birthCityName, birthCityCode, birthCountyName, birthCountyCode, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/credibility/taxpayer-gib-identity-information
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ForceOnline": force_online,
                "ResourceCode": resource_code,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/inquiry/gib-tax-payer",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
