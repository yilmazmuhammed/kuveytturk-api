"""Diğer uç noktaları (``kt.other``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Number, Resource, merge

__all__ = ["AsyncOther", "Other"]


class Other(Resource):
    """Diğer - ``kt.other``."""

    def calculate_welcome_participation_account_profit_share(
        self,
        *,
        product_code: str,
        maturity_term: int,
        fec: int,
        product_group: int,
        deposit_amount: Number,
        currency_begin: Number | None = None,
        currency_end: Number | None = None,
        index_fec: int | None = None,
        fatsi_code: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Calculate Welcome Participation Account Profit Share.

        ``POST /v1/welcomeprofitsharecalculation``

        Kapsam: ``public`` · Akış: client credentials

        Calculates the welcome participation account profit share according to the provided
        product, maturity, currency, deposit amount, currency range, index currency, and FATSI
        code information. The response includes net and gross profit share rates for the
        selected term and yearly calculation.

        Args:
            product_code: (``_productCode``, gövde, zorunlu) Product code used for the welcome
                profit share calculation.
            maturity_term: (``_maturityTerm``, gövde, zorunlu) Maturity term or expiry day used
                in the calculation.
            fec: (gövde, zorunlu) Currency type identifier used for the deposit amount.
            product_group: (``productGroup``, gövde, zorunlu) Product group identifier used for
                the calculation.
            deposit_amount: (``depositAmount``, gövde, zorunlu) Deposit amount used in the
                profit share calculation.
            currency_begin: (``CurrencyBegin``, gövde) Beginning currency value used in the
                calculation.
            currency_end: (``CurrencyEnd``, gövde) Ending currency value used in the
                calculation.
            index_fec: (``IndexFec``, gövde) Index currency identifier used in the calculation.
            fatsi_code: (``FatsiCode``, gövde) FATSI code used in the profit share calculation.

        Yanıt alanları: NetProfitShare, GrossProfitShare, NetProfitShareYearly,
        GrossProfitShareYearly

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/calculate-welcome-participation-account-profit-share
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "_productCode": product_code,
                "_maturityTerm": maturity_term,
                "fec": fec,
                "productGroup": product_group,
                "depositAmount": deposit_amount,
                "CurrencyBegin": currency_begin,
                "CurrencyEnd": currency_end,
                "IndexFec": index_fec,
                "FatsiCode": fatsi_code,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/welcomeprofitsharecalculation",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def credi_tech_intelligence_inquiry_by_credit_allocation_status(
        self,
        *,
        creditecht_report_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """CrediTech Intelligence Inquiry By Credit Allocation Status.

        ``POST /v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber``

        Kapsam: ``loans`` · Akış: client credentials

        Checks the inquiry permission status for the specified Creditecht report number. The
        response returns the inquiry permission check result for the related report.

        Args:
            creditecht_report_number: (``creditechtReportNumber``, gövde, zorunlu) Creditecht
                report number used to check inquiry permission status.

        Yanıt alanları: isInquiryPermissionCheck

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/creditech-intelligence-inquiry-by-credit-allocation-status
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "creditechtReportNumber": creditecht_report_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def credit_tech_pos(
        self,
        *,
        query_begin_period: int,
        query_end_period: int,
        identity_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """CreditTech Pos API.

        ``POST /v1/data/credittechpos``

        Kapsam: ``payments`` · Akış: client credentials

        Retrieves CreditTech POS data for the specified identity number and query period range.
        The response includes the response date and a list of POS transaction amount records
        grouped by tax number and period information.

        Args:
            query_begin_period: (``QueryBeginPeriod``, gövde, zorunlu) Start period of the query
                in YYYYMM format.
            query_end_period: (``QueryEndPeriod``, gövde, zorunlu) End period of the query in
                YYYYMM format.
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number or tax number
                used to query CreditTech POS data.

        Gövde alanları istekte ``input`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ResponseDate, DataContractList, LocalAmount, QueryBeginPeriod,
        QueryEndPeriod, TaxNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/credittech-pos-api
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "QueryBeginPeriod": query_begin_period,
                "QueryEndPeriod": query_end_period,
                "IdentityNumber": identity_number,
            },
            extra_body,
        )
        _body = {"input": _body}
        return self._client.request(
            "POST",
            "/v1/data/credittechpos",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def fraud_notifications_exists(
        self,
        *,
        identity_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Fraud Notifications Exists.

        ``POST /v1/inquiry/is-fraud-notification-exists``

        Kapsam: ``public`` · Akış: client credentials

        Checks whether an active fraud notification record exists for the provided identity
        number. The response indicates whether a matching fraud notification record was found.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number or tax number
                used to check whether a fraud notification record exists.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: isExists

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/fraud-notifications-exists
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/inquiry/is-fraud-notification-exists",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def get_fraud_notifications_last_day(
        self,
        *,
        reference_date: DateLike,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Fraud Notifications Last Day.

        ``POST /v1/inquiry/get-fraud-notifications-daily``

        Kapsam: ``public`` · Akış: client credentials

        This API retrieves fraud notification records for the last 24 hours based on the given
        reference date. The response includes corporation and individual fraud notification
        records.

        Args:
            reference_date: (``referenceDate``, gövde, zorunlu) Reference date used to retrieve
                fraud notifications for the last 24 hours.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: corporationRecords, blackListCorporationID, title, taxNumber,
        tradeRegisterNumber, customerNumber, companyType, address, city, county, neighborhood,
        phone, inquirySource, firstAuthorizedPersonName, firstAuthorizedPersonLastName,
        description, blackListTypeID, userName, host_Name, dateAdded, updateUserName,
        updateHostName, dateUpdated, status, blackListDetailId, divitInstanceId, isActive,
        senderName, attemptDate, senderBankCode, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/get-fraud-notifications-last-day
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceDate": reference_date,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/inquiry/get-fraud-notifications-daily",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def get_process_design_xml_by_business_process_id(
        self,
        *,
        business_process_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Process Design Xml By Business Process Id.

        ``POST /v1/bpm/post/grcprocessdesignxml``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve the process design XML definition for a specified business
        process. The request includes the business process ID, and the response returns the
        corresponding BPMN process design XML content.

        Args:
            business_process_id: (``businessProcessId``, gövde, zorunlu) Business process ID for
                which the process design XML definition will be retrieved.

        Yanıt alanları: responseValue

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/get-process-design-xml-by-business-process-id
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "businessProcessId": business_process_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/bpm/post/grcprocessdesignxml",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def saglam_pay_get_customer_full_info(
        self,
        *,
        sender_account_number: int,
        sender_account_suffix: int,
        receiver_account_number: int,
        receiver_account_suffix: int,
        money_transfer_amount: Number,
        transfer_type: int,
        money_transfer_description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Saglam Pay Get Customer Full Info.

        ``GET /v1/get-customer-info-by-customerId-full``

        Kapsam: ``public`` · Akış: client credentials

        Retrieves full customer-related account and money transfer information by using the
        provided customer and account details. The response includes the execution reference
        identifier and money transfer transaction identifier generated for the operation.

        Args:
            sender_account_number: (``SenderAccountNumber``, sorgu, zorunlu) Sender customer
                account number used for the operation.
            sender_account_suffix: (``SenderAccountSuffix``, sorgu, zorunlu) Sender account
                suffix used to identify the source account.
            receiver_account_number: (``ReceiverAccountNumber``, sorgu, zorunlu) Receiver
                account number used to identify the destination account.
            receiver_account_suffix: (``ReceiverAccountSuffix``, sorgu, zorunlu) Receiver
                account suffix used to identify the destination account.
            money_transfer_description: (``MoneyTransferDescription``, sorgu) Description text
                for the money transfer transaction.
            money_transfer_amount: (``MoneyTransferAmount``, sorgu, zorunlu) Amount of the money
                transfer transaction.
            transfer_type: (``TransferType``, sorgu, zorunlu) Transfer type information used for
                the money transfer operation.

        Yanıt alanları: ExecutionReferenceId, MoneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/saglam-pay-get-customer-full-info
        """
        _query = merge(
            {
                "SenderAccountNumber": sender_account_number,
                "SenderAccountSuffix": sender_account_suffix,
                "ReceiverAccountNumber": receiver_account_number,
                "ReceiverAccountSuffix": receiver_account_suffix,
                "MoneyTransferDescription": money_transfer_description,
                "MoneyTransferAmount": money_transfer_amount,
                "TransferType": transfer_type,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/get-customer-info-by-customerId-full",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def visa_payment_status_notification(
        self,
        *,
        document_template_id: int,
        doc_base64_content: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Visa Payment Status Notification.

        ``POST /v1/StatusNotify``

        Kapsam: ``public`` · Akış: client credentials

        Sends a document for status notification by using the provided document template
        identifier and Base64 encoded document content. The response returns the generated
        document operation identifier and operation result.

        Args:
            document_template_id: (``DocumentTemplateId``, gövde, zorunlu) Document template
                identifier used for the status notification document.
            doc_base64_content: (``DocBase64Content``, gövde, zorunlu) Base64 encoded content of
                the document to be sent.

        Gövde alanları istekte ``documentApiContract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/visa-payment-status-notification
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DocumentTemplateId": document_template_id,
                "DocBase64Content": doc_base64_content,
            },
            extra_body,
        )
        _body = {"documentApiContract": _body}
        return self._client.request(
            "POST",
            "/v1/StatusNotify",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def visa_statement_delivery(
        self,
        *,
        document_template_id: int,
        doc_base64_content: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Visa Statement Delivery.

        ``POST /v1/StatementDelivery``

        Kapsam: ``public`` · Akış: client credentials

        Sends a document for statement delivery by using the provided document template
        identifier and Base64 encoded document content. The response returns the generated
        document operation identifier and operation result.

        Args:
            document_template_id: (``DocumentTemplateId``, gövde, zorunlu) Document template
                identifier used for the statement delivery document.
            doc_base64_content: (``DocBase64Content``, gövde, zorunlu) Base64 encoded content of
                the document to be sent.

        Gövde alanları istekte ``documentApiContract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/visa-statement-delivery
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DocumentTemplateId": document_template_id,
                "DocBase64Content": doc_base64_content,
            },
            extra_body,
        )
        _body = {"documentApiContract": _body}
        return self._client.request(
            "POST",
            "/v1/StatementDelivery",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncOther(AsyncResource):
    """Diğer (asenkron) - ``kt.other``."""

    async def calculate_welcome_participation_account_profit_share(
        self,
        *,
        product_code: str,
        maturity_term: int,
        fec: int,
        product_group: int,
        deposit_amount: Number,
        currency_begin: Number | None = None,
        currency_end: Number | None = None,
        index_fec: int | None = None,
        fatsi_code: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Calculate Welcome Participation Account Profit Share.

        ``POST /v1/welcomeprofitsharecalculation``

        Kapsam: ``public`` · Akış: client credentials

        Calculates the welcome participation account profit share according to the provided
        product, maturity, currency, deposit amount, currency range, index currency, and FATSI
        code information. The response includes net and gross profit share rates for the
        selected term and yearly calculation.

        Args:
            product_code: (``_productCode``, gövde, zorunlu) Product code used for the welcome
                profit share calculation.
            maturity_term: (``_maturityTerm``, gövde, zorunlu) Maturity term or expiry day used
                in the calculation.
            fec: (gövde, zorunlu) Currency type identifier used for the deposit amount.
            product_group: (``productGroup``, gövde, zorunlu) Product group identifier used for
                the calculation.
            deposit_amount: (``depositAmount``, gövde, zorunlu) Deposit amount used in the
                profit share calculation.
            currency_begin: (``CurrencyBegin``, gövde) Beginning currency value used in the
                calculation.
            currency_end: (``CurrencyEnd``, gövde) Ending currency value used in the
                calculation.
            index_fec: (``IndexFec``, gövde) Index currency identifier used in the calculation.
            fatsi_code: (``FatsiCode``, gövde) FATSI code used in the profit share calculation.

        Yanıt alanları: NetProfitShare, GrossProfitShare, NetProfitShareYearly,
        GrossProfitShareYearly

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/calculate-welcome-participation-account-profit-share
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "_productCode": product_code,
                "_maturityTerm": maturity_term,
                "fec": fec,
                "productGroup": product_group,
                "depositAmount": deposit_amount,
                "CurrencyBegin": currency_begin,
                "CurrencyEnd": currency_end,
                "IndexFec": index_fec,
                "FatsiCode": fatsi_code,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/welcomeprofitsharecalculation",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def credi_tech_intelligence_inquiry_by_credit_allocation_status(
        self,
        *,
        creditecht_report_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """CrediTech Intelligence Inquiry By Credit Allocation Status.

        ``POST /v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber``

        Kapsam: ``loans`` · Akış: client credentials

        Checks the inquiry permission status for the specified Creditecht report number. The
        response returns the inquiry permission check result for the related report.

        Args:
            creditecht_report_number: (``creditechtReportNumber``, gövde, zorunlu) Creditecht
                report number used to check inquiry permission status.

        Yanıt alanları: isInquiryPermissionCheck

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/creditech-intelligence-inquiry-by-credit-allocation-status
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "creditechtReportNumber": creditecht_report_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def credit_tech_pos(
        self,
        *,
        query_begin_period: int,
        query_end_period: int,
        identity_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """CreditTech Pos API.

        ``POST /v1/data/credittechpos``

        Kapsam: ``payments`` · Akış: client credentials

        Retrieves CreditTech POS data for the specified identity number and query period range.
        The response includes the response date and a list of POS transaction amount records
        grouped by tax number and period information.

        Args:
            query_begin_period: (``QueryBeginPeriod``, gövde, zorunlu) Start period of the query
                in YYYYMM format.
            query_end_period: (``QueryEndPeriod``, gövde, zorunlu) End period of the query in
                YYYYMM format.
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number or tax number
                used to query CreditTech POS data.

        Gövde alanları istekte ``input`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ResponseDate, DataContractList, LocalAmount, QueryBeginPeriod,
        QueryEndPeriod, TaxNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/credittech-pos-api
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "QueryBeginPeriod": query_begin_period,
                "QueryEndPeriod": query_end_period,
                "IdentityNumber": identity_number,
            },
            extra_body,
        )
        _body = {"input": _body}
        return await self._client.request(
            "POST",
            "/v1/data/credittechpos",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def fraud_notifications_exists(
        self,
        *,
        identity_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Fraud Notifications Exists.

        ``POST /v1/inquiry/is-fraud-notification-exists``

        Kapsam: ``public`` · Akış: client credentials

        Checks whether an active fraud notification record exists for the provided identity
        number. The response indicates whether a matching fraud notification record was found.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number or tax number
                used to check whether a fraud notification record exists.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: isExists

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/fraud-notifications-exists
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/inquiry/is-fraud-notification-exists",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def get_fraud_notifications_last_day(
        self,
        *,
        reference_date: DateLike,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Fraud Notifications Last Day.

        ``POST /v1/inquiry/get-fraud-notifications-daily``

        Kapsam: ``public`` · Akış: client credentials

        This API retrieves fraud notification records for the last 24 hours based on the given
        reference date. The response includes corporation and individual fraud notification
        records.

        Args:
            reference_date: (``referenceDate``, gövde, zorunlu) Reference date used to retrieve
                fraud notifications for the last 24 hours.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: corporationRecords, blackListCorporationID, title, taxNumber,
        tradeRegisterNumber, customerNumber, companyType, address, city, county, neighborhood,
        phone, inquirySource, firstAuthorizedPersonName, firstAuthorizedPersonLastName,
        description, blackListTypeID, userName, host_Name, dateAdded, updateUserName,
        updateHostName, dateUpdated, status, blackListDetailId, divitInstanceId, isActive,
        senderName, attemptDate, senderBankCode, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/get-fraud-notifications-last-day
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceDate": reference_date,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/inquiry/get-fraud-notifications-daily",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def get_process_design_xml_by_business_process_id(
        self,
        *,
        business_process_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Process Design Xml By Business Process Id.

        ``POST /v1/bpm/post/grcprocessdesignxml``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to retrieve the process design XML definition for a specified business
        process. The request includes the business process ID, and the response returns the
        corresponding BPMN process design XML content.

        Args:
            business_process_id: (``businessProcessId``, gövde, zorunlu) Business process ID for
                which the process design XML definition will be retrieved.

        Yanıt alanları: responseValue

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/get-process-design-xml-by-business-process-id
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "businessProcessId": business_process_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/bpm/post/grcprocessdesignxml",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def saglam_pay_get_customer_full_info(
        self,
        *,
        sender_account_number: int,
        sender_account_suffix: int,
        receiver_account_number: int,
        receiver_account_suffix: int,
        money_transfer_amount: Number,
        transfer_type: int,
        money_transfer_description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Saglam Pay Get Customer Full Info.

        ``GET /v1/get-customer-info-by-customerId-full``

        Kapsam: ``public`` · Akış: client credentials

        Retrieves full customer-related account and money transfer information by using the
        provided customer and account details. The response includes the execution reference
        identifier and money transfer transaction identifier generated for the operation.

        Args:
            sender_account_number: (``SenderAccountNumber``, sorgu, zorunlu) Sender customer
                account number used for the operation.
            sender_account_suffix: (``SenderAccountSuffix``, sorgu, zorunlu) Sender account
                suffix used to identify the source account.
            receiver_account_number: (``ReceiverAccountNumber``, sorgu, zorunlu) Receiver
                account number used to identify the destination account.
            receiver_account_suffix: (``ReceiverAccountSuffix``, sorgu, zorunlu) Receiver
                account suffix used to identify the destination account.
            money_transfer_description: (``MoneyTransferDescription``, sorgu) Description text
                for the money transfer transaction.
            money_transfer_amount: (``MoneyTransferAmount``, sorgu, zorunlu) Amount of the money
                transfer transaction.
            transfer_type: (``TransferType``, sorgu, zorunlu) Transfer type information used for
                the money transfer operation.

        Yanıt alanları: ExecutionReferenceId, MoneyTransferTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/saglam-pay-get-customer-full-info
        """
        _query = merge(
            {
                "SenderAccountNumber": sender_account_number,
                "SenderAccountSuffix": sender_account_suffix,
                "ReceiverAccountNumber": receiver_account_number,
                "ReceiverAccountSuffix": receiver_account_suffix,
                "MoneyTransferDescription": money_transfer_description,
                "MoneyTransferAmount": money_transfer_amount,
                "TransferType": transfer_type,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/get-customer-info-by-customerId-full",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def visa_payment_status_notification(
        self,
        *,
        document_template_id: int,
        doc_base64_content: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Visa Payment Status Notification.

        ``POST /v1/StatusNotify``

        Kapsam: ``public`` · Akış: client credentials

        Sends a document for status notification by using the provided document template
        identifier and Base64 encoded document content. The response returns the generated
        document operation identifier and operation result.

        Args:
            document_template_id: (``DocumentTemplateId``, gövde, zorunlu) Document template
                identifier used for the status notification document.
            doc_base64_content: (``DocBase64Content``, gövde, zorunlu) Base64 encoded content of
                the document to be sent.

        Gövde alanları istekte ``documentApiContract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/visa-payment-status-notification
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DocumentTemplateId": document_template_id,
                "DocBase64Content": doc_base64_content,
            },
            extra_body,
        )
        _body = {"documentApiContract": _body}
        return await self._client.request(
            "POST",
            "/v1/StatusNotify",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def visa_statement_delivery(
        self,
        *,
        document_template_id: int,
        doc_base64_content: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Visa Statement Delivery.

        ``POST /v1/StatementDelivery``

        Kapsam: ``public`` · Akış: client credentials

        Sends a document for statement delivery by using the provided document template
        identifier and Base64 encoded document content. The response returns the generated
        document operation identifier and operation result.

        Args:
            document_template_id: (``DocumentTemplateId``, gövde, zorunlu) Document template
                identifier used for the statement delivery document.
            doc_base64_content: (``DocBase64Content``, gövde, zorunlu) Base64 encoded content of
                the document to be sent.

        Gövde alanları istekte ``documentApiContract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/visa-statement-delivery
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DocumentTemplateId": document_template_id,
                "DocBase64Content": doc_base64_content,
            },
            extra_body,
        )
        _body = {"documentApiContract": _body}
        return await self._client.request(
            "POST",
            "/v1/StatementDelivery",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
