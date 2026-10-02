"""Finansman çözümleri uç noktaları (``kt.financing``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Resource, merge

__all__ = ["AsyncFinancing", "Financing"]


class Financing(Resource):
    """Finansman çözümleri - ``kt.financing``."""

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


class AsyncFinancing(AsyncResource):
    """Finansman çözümleri (asenkron) - ``kt.financing``."""

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
