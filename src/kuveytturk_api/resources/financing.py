"""Finansman çözümleri uç noktaları (``kt.financing``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncFinancing", "Financing"]


class Financing(Resource):
    """Finansman çözümleri - ``kt.financing``."""

    def corporate_app_agreement_v2(
        self,
        *,
        customer_number: int,
        language_id: int,
        product_code: str,
        application_date_time: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Corporate App Agreement V2.

        ``GET /v2/corporateAppAgreementData``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to retrieve credit card agreement documents before submitting a
        corporate credit card application. The service fetches the related corporate agreement
        data using the customer number, product code, language information, and application
        date, and returns the agreement contents in Base64 format.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                corporate credit card agreements will be retrieved.
            language_id: (``languageId``, sorgu, zorunlu) Language information used to return
                agreement documents.
            application_date_time: (``applicationDateTime``, sorgu) Application date
                information. Format: yyyy-MM-dd.
            product_code: (``productCode``, sorgu, zorunlu) Credit card product code for which
                agreement documents will be retrieved.

        Yanıt alanları: agreementListContract, agreementData, agreementDataName,
        interestFreeContractID, apiExecutionContract, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-app-agreement-v2
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "languageId": language_id,
                "applicationDateTime": application_date_time,
                "productCode": product_code,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/corporateAppAgreementData",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def corporate_credit_card_application(
        self,
        *,
        customer_number: int,
        digital_slip_choice: str,
        statement_day: str,
        product_code: str,
        statement_delivery_type: str,
        card_sending_address_id: int,
        product_number: str,
        installment_count: int,
        suffix_customer_id: int,
        required_rate: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Corporate Credit Card Application.

        ``POST /v2/corporateCreditCardApplication``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to submit and save a corporate credit card application in BOA. The
        service receives information such as the selected card product, statement day, card
        delivery address, installment information, digital slip preference, and related customer
        details to initiate the corporate credit card application process.

        Args:
            customer_number: (``customerNumber``, gövde, zorunlu) Main customer number for which
                the corporate credit card application will be submitted.
            digital_slip_choice: (``digitalSlipChoice``, gövde, zorunlu) Digital slip
                preference.
            statement_day: (``statementDay``, gövde, zorunlu) Selected statement day.
            product_code: (``productCode``, gövde, zorunlu) Credit card product code selected
                for the application.
            statement_delivery_type: (``statementDeliveryType``, gövde, zorunlu) Statement
                delivery type.
            card_sending_address_id: (``cardSendingAddressId``, gövde, zorunlu) BOA address ID
                where the card will be delivered.
            product_number: (``productNumber``, gövde, zorunlu) Credit card product number
                selected for the application.
            installment_count: (``installmentCount``, gövde, zorunlu) Installment count for the
                corporate card application.
            suffix_customer_id: (``suffixCustomerId``, gövde, zorunlu) Related
                individual/additional customer number associated with the corporate customer.
            required_rate: (``requiredRate``, gövde, zorunlu) Requested rate information for the
                corporate application.

        Yanıt alanları: insertedMainAppRecordId, insertedSuppAppRecordId, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-credit-card-application
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "customerNumber": customer_number,
                "digitalSlipChoice": digital_slip_choice,
                "statementDay": statement_day,
                "productCode": product_code,
                "statementDeliveryType": statement_delivery_type,
                "cardSendingAddressId": card_sending_address_id,
                "productNumber": product_number,
                "installmentCount": installment_count,
                "suffixCustomerId": suffix_customer_id,
                "requiredRate": required_rate,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/corporateCreditCardApplication",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def credit_limit_request(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Credit Limit Request.

        ``GET /v1/loans/allotmentLimit``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        You can request the customer''s (sent via token) credit limits in the bank. You can
        learn about top limits, product limits, and product collateral limits.

        Yanıt alanları: accountNumber, status, AllotmentStatusName, maturityDate, tranDate

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/credit-limit-request
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/loans/allotmentLimit",
            scope="loans",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    def customer_current_credit_allocation_flow_information(
        self,
        *,
        account_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Current Credit Allocation Flow Information.

        ``POST /v1/Loans/GetLatestRouteHistoryByAccountNumber``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves the latest route history records for the specified account number. The
        response includes allotment, authority, status, workflow, action, and user information
        related to the latest credit allocation route history.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) Account number used to retrieve
                the latest route history records.

        Yanıt alanları: accountNumber, authorityType, status, allotmentId, allotmentMainId,
        credereArtReportNumber, wFInstanceId, name, actionName, userCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-current-credit-allocation-flow-information
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
            "/v1/Loans/GetLatestRouteHistoryByAccountNumber",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def customer_suited_card_list(
        self,
        *,
        customer_number: int,
        language_id: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Suited Card List.

        ``GET /v2/customerSuitedCardList``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to list eligible individual and/or corporate credit card products that
        the customer can apply for. The service returns suitable card products, statement
        options, card delivery types, and the customer’s address and email information that can
        be used during the application process.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                eligible credit card products will be queried.
            language_id: (``languageId``, sorgu, zorunlu) Language information used to return
                product and parameter descriptions.

        Yanıt alanları: addressList, addressText, addressId, addressTypeName, apartmentNumber,
        emailAddressList, emailAddress, emailId, eligibleCCApplicationContract,
        isIndividualCard, immediateProductCode, productName, productCode, productNumber,
        minimumInstallment, maximumInstallment, statementContractList, statementDay,
        statementDayDescription, digitalSlipChoiceList, paramCode, paramDescription, paramValue,
        statementDeliveryTypeList, statementType, statementDescription, ecomChoiceList,
        cardSendingTypeList, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-suited-card-list
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "languageId": language_id,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/customerSuitedCardList",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def get_digital_channel_card_application_list_v2(
        self,
        *,
        customer_number: int,
        language_id: int,
        search_begin_date: str | None = None,
        search_end_date: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Digital Channel Card Application List V2.

        ``GET /v2/cardApplicationList``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to list the customer’s individual or corporate credit card application
        history. The service retrieves credit card applications submitted through digital
        channels based on the customer number, language information, and date range, and returns
        the application tracking details.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                credit card application history will be queried.
            language_id: (``languageId``, sorgu, zorunlu) Language information used to return
                application details.
            search_begin_date: (``searchBeginDate``, sorgu) Application search start date.
                Format: yyyy-MM-dd.
            search_end_date: (``searchEndDate``, sorgu) Application search end date. Format:
                yyyy-MM-dd.

        Yanıt alanları: embossBranch, embossCompanytransferDate, courierGivenDate, printDate,
        virtualCardDemandedFlag, hasSupplementaryCard, deliveryInquiryFlag, shadowCardNumber,
        isDebit, productCode, isIndividual, applicationDate, productName, statusCode,
        statusDescription, sendingAddress, preferredLimit, confirmedLimit,
        supplementaryCardFlag, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/get-digital-channel-card-application-list-v2
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "languageId": language_id,
                "searchBeginDate": search_begin_date,
                "searchEndDate": search_end_date,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/cardApplicationList",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def individual_app_agreement_v2(
        self,
        *,
        customer_number: int,
        product_code: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Individual App Agreement V2.

        ``GET /v2/individualAppAgreement``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to retrieve credit card agreement documents before submitting an
        individual credit card application. The service fetches the related agreement data using
        the customer number and product code, and returns the agreement contents in Base64
        format.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                individual credit card agreements will be retrieved.
            product_code: (``productCode``, sorgu, zorunlu) Credit card product code for which
                agreement documents will be retrieved.

        Yanıt alanları: agreementListContract, agreementData, agreementDataName,
        interestFreeContractID, apiExecutionContract, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-app-agreement-v2
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "productCode": product_code,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v2/individualAppAgreement",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def individual_credit_card_application_v2(
        self,
        *,
        customer_number: int,
        card_sending_address_id: int,
        product_code: str,
        product_number: str,
        statement_day: str,
        monthly_net_income: int,
        statement_delivery_type: str,
        digital_slip_choice: str,
        email_id: int,
        email: str,
        job_starting_year: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Individual Credit Card Application V2.

        ``POST /v2/individualCreditCardApplication``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to submit and save an individual credit card application in BOA. The
        service receives information such as customer number, selected card product, statement
        day, card delivery address, email information, digital slip preference, monthly income,
        and job start year to initiate the individual credit card application process.

        Args:
            customer_number: (``customerNumber``, gövde, zorunlu) Customer number for which the
                individual credit card application will be submitted.
            card_sending_address_id: (``cardSendingAddressId``, gövde, zorunlu) BOA address ID
                where the card will be delivered.
            product_code: (``productCode``, gövde, zorunlu) Credit card product code selected
                for the application.
            product_number: (``productNumber``, gövde, zorunlu) Credit card product number
                selected for the application.
            statement_day: (``statementDay``, gövde, zorunlu) Selected statement day.
            monthly_net_income: (``monthlyNetIncome``, gövde, zorunlu) Customer’s monthly net
                income information.
            statement_delivery_type: (``statementDeliveryType``, gövde, zorunlu) Statement
                delivery type.
            digital_slip_choice: (``digitalSlipChoice``, gövde, zorunlu) Digital slip
                preference.
            email_id: (``emailId``, gövde, zorunlu) BOA email record ID to be used in the
                application.
            email: (gövde, zorunlu) Email address to be used in the application.
            job_starting_year: (``jobStartingYear``, gövde, zorunlu) Customer’s job starting
                year information.

        Yanıt alanları: insertedRecordId, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-credit-card-application-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "customerNumber": customer_number,
                "cardSendingAddressId": card_sending_address_id,
                "productCode": product_code,
                "productNumber": product_number,
                "statementDay": statement_day,
                "monthlyNetIncome": monthly_net_income,
                "statementDeliveryType": statement_delivery_type,
                "digitalSlipChoice": digital_slip_choice,
                "emailId": email_id,
                "email": email,
                "jobStartingYear": job_starting_year,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/individualCreditCardApplication",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def loan_finance_calculation(
        self,
        *,
        product_code: str,
        installment_count: int,
        funding_amount: Number,
        is_total_amount_by_installment_amount: bool,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Calculation.

        ``GET /v1/calculations/loan``

        Kapsam: ``public`` · Akış: client credentials

        Calculates the loan repayment plan according to the provided product type, installment
        count, funding amount, and calculation preference. The response includes monthly profit
        rate, total installment amount, total profit amount, tax amounts, and installment
        details.

        Args:
            product_code: (``ProductCode``, sorgu, zorunlu) Product type code used for the loan
                calculation.
            installment_count: (``InstallmentCount``, sorgu, zorunlu) Number of installments to
                be used in the repayment plan.
            funding_amount: (``FundingAmount``, sorgu, zorunlu) Loan funding amount to be
                calculated.
            is_total_amount_by_installment_amount: (``IsTotalAmountByInstallmentAmount``, sorgu,
                zorunlu) Indicates whether the calculation will be performed based on installment
                amount.

        Yanıt alanları: monthlyProfitRate, fundingAmount, installmentCount,
        totalInstallmentAmount, totalProfitAmount, totalRUSFAmount, totalBITTAmount,
        installments, order, amount, principalAmount, profitAmount, bittAmount, rusfAmount,
        remainingPrincipalAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-calculation
        """
        _query = merge(
            {
                "ProductCode": product_code,
                "InstallmentCount": installment_count,
                "FundingAmount": funding_amount,
                "IsTotalAmountByInstallmentAmount": is_total_amount_by_installment_amount,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/calculations/loan",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def loan_finance_info(
        self,
        *,
        project_number: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Info.

        ``GET /v1/loans/{projectNumber}/info``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        Returns a loan belong to given account and project number.

        Args:
            project_number: (``projectNumber``, yol, zorunlu) Represents the procy identifier
                number.

        Yanıt alanları: productName, projectNumber, type, fxCode, projectStartDate,
        projectFinishDate, totalLoanAmount, loanAmount, remainDebt, paymentStatus

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-info
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/loans/{projectNumber}/info",
            scope="loans",
            flow="authorization_code",
            path_params={"projectNumber": project_number},
            query=_query,
            options=request_options,
        )

    def loan_finance_installments(
        self,
        *,
        project_number: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Installments.

        ``GET /v1/loans/{projectNumber}/installments``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        Returns list of installments belonging to the given project (each loan is considered as
        a project) number.

        Args:
            project_number: (``projectNumber``, yol, zorunlu) Indicates the project number
                (Project number is the ID-code given to each loan).

        Yanıt alanları: installmentNumber, fxCode, paymentStatus, maturityDate,
        installmentAmount, paymentAmount, collectedBITTAmount, collectedPrincipalAmount,
        collectedProfitAmount, collectedRUSFAmount, collectedVATAmount, installmentRemaining

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-installments
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/loans/{projectNumber}/installments",
            scope="loans",
            flow="authorization_code",
            path_params={"projectNumber": project_number},
            query=_query,
            options=request_options,
        )

    def loan_finance_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance List.

        ``GET /v1/loans``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        Returns a list of loans belonging to the given account number.

        Yanıt alanları: productName, projectNumber, type, fxCode, projectStartDate,
        projectFinishDate, totalLoanAmount, loanAmount, remainDebt, paymentStatus

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/loans",
            scope="loans",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    def loans_price_list(
        self,
        *,
        product_type: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loans Price List.

        ``GET /v1/loans/pricelist``

        Kapsam: ``loans`` · Akış: client credentials

        Provides information about the prices of loan product information.

        Args:
            product_type: (``productType``, sorgu, zorunlu) Refers to the loan product type. The
                expected values are from 1 to 3.

        Yanıt alanları: productName, nonPaymentPeriod, bITTRate, commissionRate,
        expertiseAmount, vehiclePledgeAmount, hypothecAmount, customerTypeDescription,
        pricingInfoList, MinMaturity, Maturity, ListPriceRate, VarianceNo, UpdateDate, bankName,
        productTypeName

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loans-price-list
        """
        _query = merge(
            {
                "productType": product_type,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/loans/pricelist",
            scope="loans",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def send_leasing_confirmation_form(
        self,
        *,
        reference_number: int,
        transaction_amount: Number,
        customs_tax_amount: Number,
        confirmation_form: str,
        customs_firm_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Leasing Confirmation Form.

        ``POST /v1/leasing/confirmation-form``

        Kapsam: ``loans`` · Akış: client credentials

        Receives the leasing confirmation form together with the related reference, transaction
        amount, customs tax amount, and customs firm information. The response returns the
        operation result for the confirmation form submission.

        Args:
            reference_number: (``referenceNumber``, gövde, zorunlu) Reference number associated
                with the leasing transaction.
            transaction_amount: (``transactionAmount``, gövde, zorunlu) Transaction amount of
                the leasing operation.
            customs_tax_amount: (``customsTaxAmount``, gövde, zorunlu) Customs tax amount
                related to the leasing transaction.
            confirmation_form: (``confirmationForm``, gövde, zorunlu) Confirmation form content
                or reference information submitted for the leasing transaction.
            customs_firm_id: (``customsFirmId``, gövde, zorunlu) Identifier of the customs firm
                related to the leasing transaction.

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-confirmation-form
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumber": reference_number,
                "transactionAmount": transaction_amount,
                "customsTaxAmount": customs_tax_amount,
                "confirmationForm": confirmation_form,
                "customsFirmId": customs_firm_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/leasing/confirmation-form",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_leasing_current_account_file(
        self,
        *,
        reference_number: int,
        current_excel: str,
        import_file_closing: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Leasing Current Account File.

        ``POST /v1/leasing/current-documents``

        Kapsam: ``loans`` · Akış: client credentials

        Receives the leasing current account document and import file closing document for the
        specified reference number. The response returns the operation result for the document
        submission.

        Args:
            reference_number: (``referenceNumber``, gövde, zorunlu) Reference number associated
                with the leasing transaction.
            current_excel: (``currentExcel``, gövde, zorunlu) Current account Excel document
                content or reference information submitted for the leasing transaction.
            import_file_closing: (``importFileClosing``, gövde, zorunlu) Import file closing
                document content or reference information submitted for the leasing transaction.

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-current-account-file
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumber": reference_number,
                "currentExcel": current_excel,
                "importFileClosing": import_file_closing,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/leasing/current-documents",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_leasing_release_documents(
        self,
        *,
        reference_number: int,
        invoice: str | None = None,
        customs_declaration: str | None = None,
        exit_excel: str | None = None,
        tax_payment_receipt: str | None = None,
        invoice_list: Sequence[Any] | None = None,
        customs_declaration_list: Sequence[Any] | None = None,
        exit_information_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Leasing Release Documents.

        ``POST /v1/leasing/exit-documents``

        Kapsam: ``loans`` · Akış: client credentials

        Receives leasing release documents for the specified reference number. The request may
        include invoice, customs declaration, exit Excel, tax payment receipt, invoice list,
        customs declaration list, and exit information details. The response returns the
        operation result for the document submission.

        Args:
            reference_number: (``ReferenceNumber``, gövde, zorunlu) Reference number associated
                with the leasing transaction.
            invoice: (``Invoice``, gövde) Invoice document content or reference information
                submitted for the leasing transaction.
            customs_declaration: (``CustomsDeclaration``, gövde) Customs declaration document
                content or reference information submitted for the leasing transaction.
            exit_excel: (``ExitExcel``, gövde) Exit Excel document content or reference
                information submitted for the leasing transaction.
            tax_payment_receipt: (``TaxPaymentReceipt``, gövde) Tax payment receipt document
                content or reference information submitted for the leasing transaction.
            invoice_list: (``InvoiceList``, gövde) List of invoice records related to the
                leasing release documents.
            customs_declaration_list: (``CustomsDeclarationList``, gövde) List of customs
                declaration records related to the leasing release documents.
            exit_information_list: (``ExitInformationList``, gövde) List of exit information
                records related to the leasing release documents.

        Gövde alanları istekte ``document`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-release-documents
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "ReferenceNumber": reference_number,
                "Invoice": invoice,
                "CustomsDeclaration": customs_declaration,
                "ExitExcel": exit_excel,
                "TaxPaymentReceipt": tax_payment_receipt,
                "InvoiceList": invoice_list,
                "CustomsDeclarationList": customs_declaration_list,
                "ExitInformationList": exit_information_list,
            },
            extra_body,
        )
        _body = {"document": _body}
        return self._client.request(
            "POST",
            "/v1/leasing/exit-documents",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncFinancing(AsyncResource):
    """Finansman çözümleri (asenkron) - ``kt.financing``."""

    async def corporate_app_agreement_v2(
        self,
        *,
        customer_number: int,
        language_id: int,
        product_code: str,
        application_date_time: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Corporate App Agreement V2.

        ``GET /v2/corporateAppAgreementData``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to retrieve credit card agreement documents before submitting a
        corporate credit card application. The service fetches the related corporate agreement
        data using the customer number, product code, language information, and application
        date, and returns the agreement contents in Base64 format.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                corporate credit card agreements will be retrieved.
            language_id: (``languageId``, sorgu, zorunlu) Language information used to return
                agreement documents.
            application_date_time: (``applicationDateTime``, sorgu) Application date
                information. Format: yyyy-MM-dd.
            product_code: (``productCode``, sorgu, zorunlu) Credit card product code for which
                agreement documents will be retrieved.

        Yanıt alanları: agreementListContract, agreementData, agreementDataName,
        interestFreeContractID, apiExecutionContract, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-app-agreement-v2
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "languageId": language_id,
                "applicationDateTime": application_date_time,
                "productCode": product_code,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/corporateAppAgreementData",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def corporate_credit_card_application(
        self,
        *,
        customer_number: int,
        digital_slip_choice: str,
        statement_day: str,
        product_code: str,
        statement_delivery_type: str,
        card_sending_address_id: int,
        product_number: str,
        installment_count: int,
        suffix_customer_id: int,
        required_rate: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Corporate Credit Card Application.

        ``POST /v2/corporateCreditCardApplication``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to submit and save a corporate credit card application in BOA. The
        service receives information such as the selected card product, statement day, card
        delivery address, installment information, digital slip preference, and related customer
        details to initiate the corporate credit card application process.

        Args:
            customer_number: (``customerNumber``, gövde, zorunlu) Main customer number for which
                the corporate credit card application will be submitted.
            digital_slip_choice: (``digitalSlipChoice``, gövde, zorunlu) Digital slip
                preference.
            statement_day: (``statementDay``, gövde, zorunlu) Selected statement day.
            product_code: (``productCode``, gövde, zorunlu) Credit card product code selected
                for the application.
            statement_delivery_type: (``statementDeliveryType``, gövde, zorunlu) Statement
                delivery type.
            card_sending_address_id: (``cardSendingAddressId``, gövde, zorunlu) BOA address ID
                where the card will be delivered.
            product_number: (``productNumber``, gövde, zorunlu) Credit card product number
                selected for the application.
            installment_count: (``installmentCount``, gövde, zorunlu) Installment count for the
                corporate card application.
            suffix_customer_id: (``suffixCustomerId``, gövde, zorunlu) Related
                individual/additional customer number associated with the corporate customer.
            required_rate: (``requiredRate``, gövde, zorunlu) Requested rate information for the
                corporate application.

        Yanıt alanları: insertedMainAppRecordId, insertedSuppAppRecordId, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-credit-card-application
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "customerNumber": customer_number,
                "digitalSlipChoice": digital_slip_choice,
                "statementDay": statement_day,
                "productCode": product_code,
                "statementDeliveryType": statement_delivery_type,
                "cardSendingAddressId": card_sending_address_id,
                "productNumber": product_number,
                "installmentCount": installment_count,
                "suffixCustomerId": suffix_customer_id,
                "requiredRate": required_rate,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/corporateCreditCardApplication",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def credit_limit_request(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Credit Limit Request.

        ``GET /v1/loans/allotmentLimit``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        You can request the customer''s (sent via token) credit limits in the bank. You can
        learn about top limits, product limits, and product collateral limits.

        Yanıt alanları: accountNumber, status, AllotmentStatusName, maturityDate, tranDate

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/credit-limit-request
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/loans/allotmentLimit",
            scope="loans",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    async def customer_current_credit_allocation_flow_information(
        self,
        *,
        account_number: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Current Credit Allocation Flow Information.

        ``POST /v1/Loans/GetLatestRouteHistoryByAccountNumber``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves the latest route history records for the specified account number. The
        response includes allotment, authority, status, workflow, action, and user information
        related to the latest credit allocation route history.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) Account number used to retrieve
                the latest route history records.

        Yanıt alanları: accountNumber, authorityType, status, allotmentId, allotmentMainId,
        credereArtReportNumber, wFInstanceId, name, actionName, userCode

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-current-credit-allocation-flow-information
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
            "/v1/Loans/GetLatestRouteHistoryByAccountNumber",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def customer_suited_card_list(
        self,
        *,
        customer_number: int,
        language_id: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Suited Card List.

        ``GET /v2/customerSuitedCardList``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to list eligible individual and/or corporate credit card products that
        the customer can apply for. The service returns suitable card products, statement
        options, card delivery types, and the customer’s address and email information that can
        be used during the application process.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                eligible credit card products will be queried.
            language_id: (``languageId``, sorgu, zorunlu) Language information used to return
                product and parameter descriptions.

        Yanıt alanları: addressList, addressText, addressId, addressTypeName, apartmentNumber,
        emailAddressList, emailAddress, emailId, eligibleCCApplicationContract,
        isIndividualCard, immediateProductCode, productName, productCode, productNumber,
        minimumInstallment, maximumInstallment, statementContractList, statementDay,
        statementDayDescription, digitalSlipChoiceList, paramCode, paramDescription, paramValue,
        statementDeliveryTypeList, statementType, statementDescription, ecomChoiceList,
        cardSendingTypeList, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-suited-card-list
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "languageId": language_id,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/customerSuitedCardList",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def get_digital_channel_card_application_list_v2(
        self,
        *,
        customer_number: int,
        language_id: int,
        search_begin_date: str | None = None,
        search_end_date: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Digital Channel Card Application List V2.

        ``GET /v2/cardApplicationList``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to list the customer’s individual or corporate credit card application
        history. The service retrieves credit card applications submitted through digital
        channels based on the customer number, language information, and date range, and returns
        the application tracking details.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                credit card application history will be queried.
            language_id: (``languageId``, sorgu, zorunlu) Language information used to return
                application details.
            search_begin_date: (``searchBeginDate``, sorgu) Application search start date.
                Format: yyyy-MM-dd.
            search_end_date: (``searchEndDate``, sorgu) Application search end date. Format:
                yyyy-MM-dd.

        Yanıt alanları: embossBranch, embossCompanytransferDate, courierGivenDate, printDate,
        virtualCardDemandedFlag, hasSupplementaryCard, deliveryInquiryFlag, shadowCardNumber,
        isDebit, productCode, isIndividual, applicationDate, productName, statusCode,
        statusDescription, sendingAddress, preferredLimit, confirmedLimit,
        supplementaryCardFlag, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/get-digital-channel-card-application-list-v2
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "languageId": language_id,
                "searchBeginDate": search_begin_date,
                "searchEndDate": search_end_date,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/cardApplicationList",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def individual_app_agreement_v2(
        self,
        *,
        customer_number: int,
        product_code: str,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Individual App Agreement V2.

        ``GET /v2/individualAppAgreement``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to retrieve credit card agreement documents before submitting an
        individual credit card application. The service fetches the related agreement data using
        the customer number and product code, and returns the agreement contents in Base64
        format.

        Args:
            customer_number: (``customerNumber``, sorgu, zorunlu) Customer number for which
                individual credit card agreements will be retrieved.
            product_code: (``productCode``, sorgu, zorunlu) Credit card product code for which
                agreement documents will be retrieved.

        Yanıt alanları: agreementListContract, agreementData, agreementDataName,
        interestFreeContractID, apiExecutionContract, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-app-agreement-v2
        """
        _query = merge(
            {
                "customerNumber": customer_number,
                "productCode": product_code,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v2/individualAppAgreement",
            scope="cards",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def individual_credit_card_application_v2(
        self,
        *,
        customer_number: int,
        card_sending_address_id: int,
        product_code: str,
        product_number: str,
        statement_day: str,
        monthly_net_income: int,
        statement_delivery_type: str,
        digital_slip_choice: str,
        email_id: int,
        email: str,
        job_starting_year: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Individual Credit Card Application V2.

        ``POST /v2/individualCreditCardApplication``

        Kapsam: ``cards`` · Akış: client credentials · Durum: COMING_SOON

        This API is used to submit and save an individual credit card application in BOA. The
        service receives information such as customer number, selected card product, statement
        day, card delivery address, email information, digital slip preference, monthly income,
        and job start year to initiate the individual credit card application process.

        Args:
            customer_number: (``customerNumber``, gövde, zorunlu) Customer number for which the
                individual credit card application will be submitted.
            card_sending_address_id: (``cardSendingAddressId``, gövde, zorunlu) BOA address ID
                where the card will be delivered.
            product_code: (``productCode``, gövde, zorunlu) Credit card product code selected
                for the application.
            product_number: (``productNumber``, gövde, zorunlu) Credit card product number
                selected for the application.
            statement_day: (``statementDay``, gövde, zorunlu) Selected statement day.
            monthly_net_income: (``monthlyNetIncome``, gövde, zorunlu) Customer’s monthly net
                income information.
            statement_delivery_type: (``statementDeliveryType``, gövde, zorunlu) Statement
                delivery type.
            digital_slip_choice: (``digitalSlipChoice``, gövde, zorunlu) Digital slip
                preference.
            email_id: (``emailId``, gövde, zorunlu) BOA email record ID to be used in the
                application.
            email: (gövde, zorunlu) Email address to be used in the application.
            job_starting_year: (``jobStartingYear``, gövde, zorunlu) Customer’s job starting
                year information.

        Yanıt alanları: insertedRecordId, errors

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-credit-card-application-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "customerNumber": customer_number,
                "cardSendingAddressId": card_sending_address_id,
                "productCode": product_code,
                "productNumber": product_number,
                "statementDay": statement_day,
                "monthlyNetIncome": monthly_net_income,
                "statementDeliveryType": statement_delivery_type,
                "digitalSlipChoice": digital_slip_choice,
                "emailId": email_id,
                "email": email,
                "jobStartingYear": job_starting_year,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/individualCreditCardApplication",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def loan_finance_calculation(
        self,
        *,
        product_code: str,
        installment_count: int,
        funding_amount: Number,
        is_total_amount_by_installment_amount: bool,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Calculation.

        ``GET /v1/calculations/loan``

        Kapsam: ``public`` · Akış: client credentials

        Calculates the loan repayment plan according to the provided product type, installment
        count, funding amount, and calculation preference. The response includes monthly profit
        rate, total installment amount, total profit amount, tax amounts, and installment
        details.

        Args:
            product_code: (``ProductCode``, sorgu, zorunlu) Product type code used for the loan
                calculation.
            installment_count: (``InstallmentCount``, sorgu, zorunlu) Number of installments to
                be used in the repayment plan.
            funding_amount: (``FundingAmount``, sorgu, zorunlu) Loan funding amount to be
                calculated.
            is_total_amount_by_installment_amount: (``IsTotalAmountByInstallmentAmount``, sorgu,
                zorunlu) Indicates whether the calculation will be performed based on installment
                amount.

        Yanıt alanları: monthlyProfitRate, fundingAmount, installmentCount,
        totalInstallmentAmount, totalProfitAmount, totalRUSFAmount, totalBITTAmount,
        installments, order, amount, principalAmount, profitAmount, bittAmount, rusfAmount,
        remainingPrincipalAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-calculation
        """
        _query = merge(
            {
                "ProductCode": product_code,
                "InstallmentCount": installment_count,
                "FundingAmount": funding_amount,
                "IsTotalAmountByInstallmentAmount": is_total_amount_by_installment_amount,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/calculations/loan",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def loan_finance_info(
        self,
        *,
        project_number: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Info.

        ``GET /v1/loans/{projectNumber}/info``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        Returns a loan belong to given account and project number.

        Args:
            project_number: (``projectNumber``, yol, zorunlu) Represents the procy identifier
                number.

        Yanıt alanları: productName, projectNumber, type, fxCode, projectStartDate,
        projectFinishDate, totalLoanAmount, loanAmount, remainDebt, paymentStatus

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-info
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/loans/{projectNumber}/info",
            scope="loans",
            flow="authorization_code",
            path_params={"projectNumber": project_number},
            query=_query,
            options=request_options,
        )

    async def loan_finance_installments(
        self,
        *,
        project_number: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Installments.

        ``GET /v1/loans/{projectNumber}/installments``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        Returns list of installments belonging to the given project (each loan is considered as
        a project) number.

        Args:
            project_number: (``projectNumber``, yol, zorunlu) Indicates the project number
                (Project number is the ID-code given to each loan).

        Yanıt alanları: installmentNumber, fxCode, paymentStatus, maturityDate,
        installmentAmount, paymentAmount, collectedBITTAmount, collectedPrincipalAmount,
        collectedProfitAmount, collectedRUSFAmount, collectedVATAmount, installmentRemaining

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-installments
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/loans/{projectNumber}/installments",
            scope="loans",
            flow="authorization_code",
            path_params={"projectNumber": project_number},
            query=_query,
            options=request_options,
        )

    async def loan_finance_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance List.

        ``GET /v1/loans``

        Kapsam: ``loans`` · Akış: authorization code (müşteri girişi gerekir)

        Returns a list of loans belonging to the given account number.

        Yanıt alanları: productName, projectNumber, type, fxCode, projectStartDate,
        projectFinishDate, totalLoanAmount, loanAmount, remainDebt, paymentStatus

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/loans",
            scope="loans",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    async def loans_price_list(
        self,
        *,
        product_type: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loans Price List.

        ``GET /v1/loans/pricelist``

        Kapsam: ``loans`` · Akış: client credentials

        Provides information about the prices of loan product information.

        Args:
            product_type: (``productType``, sorgu, zorunlu) Refers to the loan product type. The
                expected values are from 1 to 3.

        Yanıt alanları: productName, nonPaymentPeriod, bITTRate, commissionRate,
        expertiseAmount, vehiclePledgeAmount, hypothecAmount, customerTypeDescription,
        pricingInfoList, MinMaturity, Maturity, ListPriceRate, VarianceNo, UpdateDate, bankName,
        productTypeName

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/loans-price-list
        """
        _query = merge(
            {
                "productType": product_type,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/loans/pricelist",
            scope="loans",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def send_leasing_confirmation_form(
        self,
        *,
        reference_number: int,
        transaction_amount: Number,
        customs_tax_amount: Number,
        confirmation_form: str,
        customs_firm_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Leasing Confirmation Form.

        ``POST /v1/leasing/confirmation-form``

        Kapsam: ``loans`` · Akış: client credentials

        Receives the leasing confirmation form together with the related reference, transaction
        amount, customs tax amount, and customs firm information. The response returns the
        operation result for the confirmation form submission.

        Args:
            reference_number: (``referenceNumber``, gövde, zorunlu) Reference number associated
                with the leasing transaction.
            transaction_amount: (``transactionAmount``, gövde, zorunlu) Transaction amount of
                the leasing operation.
            customs_tax_amount: (``customsTaxAmount``, gövde, zorunlu) Customs tax amount
                related to the leasing transaction.
            confirmation_form: (``confirmationForm``, gövde, zorunlu) Confirmation form content
                or reference information submitted for the leasing transaction.
            customs_firm_id: (``customsFirmId``, gövde, zorunlu) Identifier of the customs firm
                related to the leasing transaction.

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-confirmation-form
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumber": reference_number,
                "transactionAmount": transaction_amount,
                "customsTaxAmount": customs_tax_amount,
                "confirmationForm": confirmation_form,
                "customsFirmId": customs_firm_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/leasing/confirmation-form",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_leasing_current_account_file(
        self,
        *,
        reference_number: int,
        current_excel: str,
        import_file_closing: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Leasing Current Account File.

        ``POST /v1/leasing/current-documents``

        Kapsam: ``loans`` · Akış: client credentials

        Receives the leasing current account document and import file closing document for the
        specified reference number. The response returns the operation result for the document
        submission.

        Args:
            reference_number: (``referenceNumber``, gövde, zorunlu) Reference number associated
                with the leasing transaction.
            current_excel: (``currentExcel``, gövde, zorunlu) Current account Excel document
                content or reference information submitted for the leasing transaction.
            import_file_closing: (``importFileClosing``, gövde, zorunlu) Import file closing
                document content or reference information submitted for the leasing transaction.

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-current-account-file
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumber": reference_number,
                "currentExcel": current_excel,
                "importFileClosing": import_file_closing,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/leasing/current-documents",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_leasing_release_documents(
        self,
        *,
        reference_number: int,
        invoice: str | None = None,
        customs_declaration: str | None = None,
        exit_excel: str | None = None,
        tax_payment_receipt: str | None = None,
        invoice_list: Sequence[Any] | None = None,
        customs_declaration_list: Sequence[Any] | None = None,
        exit_information_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Leasing Release Documents.

        ``POST /v1/leasing/exit-documents``

        Kapsam: ``loans`` · Akış: client credentials

        Receives leasing release documents for the specified reference number. The request may
        include invoice, customs declaration, exit Excel, tax payment receipt, invoice list,
        customs declaration list, and exit information details. The response returns the
        operation result for the document submission.

        Args:
            reference_number: (``ReferenceNumber``, gövde, zorunlu) Reference number associated
                with the leasing transaction.
            invoice: (``Invoice``, gövde) Invoice document content or reference information
                submitted for the leasing transaction.
            customs_declaration: (``CustomsDeclaration``, gövde) Customs declaration document
                content or reference information submitted for the leasing transaction.
            exit_excel: (``ExitExcel``, gövde) Exit Excel document content or reference
                information submitted for the leasing transaction.
            tax_payment_receipt: (``TaxPaymentReceipt``, gövde) Tax payment receipt document
                content or reference information submitted for the leasing transaction.
            invoice_list: (``InvoiceList``, gövde) List of invoice records related to the
                leasing release documents.
            customs_declaration_list: (``CustomsDeclarationList``, gövde) List of customs
                declaration records related to the leasing release documents.
            exit_information_list: (``ExitInformationList``, gövde) List of exit information
                records related to the leasing release documents.

        Gövde alanları istekte ``document`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-release-documents
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "ReferenceNumber": reference_number,
                "Invoice": invoice,
                "CustomsDeclaration": customs_declaration,
                "ExitExcel": exit_excel,
                "TaxPaymentReceipt": tax_payment_receipt,
                "InvoiceList": invoice_list,
                "CustomsDeclarationList": customs_declaration_list,
                "ExitInformationList": exit_information_list,
            },
            extra_body,
        )
        _body = {"document": _body}
        return await self._client.request(
            "POST",
            "/v1/leasing/exit-documents",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
