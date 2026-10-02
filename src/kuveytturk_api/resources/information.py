"""Bilgi servisleri (şube, ATM, parametre sorguları...) uç noktaları (``kt.information``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Number, Resource, merge

__all__ = ["AsyncInformation", "Information"]


class Information(Resource):
    """Bilgi servisleri (şube, ATM, parametre sorguları...) - ``kt.information``."""

    def bank_branch_list(
        self,
        *,
        bank_id: int,
        city_id: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Bank Branch List.

        ``GET /v1/data/banks/{bankId}/branches``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of branches of given bank id and city id within Turkish Banking System.

        Args:
            bank_id: (``bankId``, yol, zorunlu) Bank code for listing branches
            city_id: (``cityId``, sorgu, zorunlu) Specify the city of branches

        Yanıt alanları: branchId, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/bank-branch-list
        """
        _query = merge(
            {
                "cityId": city_id,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/data/banks/{bankId}/branches",
            scope="public",
            flow="client_credentials",
            path_params={"bankId": bank_id},
            query=_query,
            options=request_options,
        )

    def bank_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Bank List.

        ``GET /v1/data/banks``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of banks within Turkish Banking System.

        Yanıt alanları: bankId, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/bank-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/data/banks",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def calculate_profit_share_rate(
        self,
        *,
        expire_day: int,
        fx_type: int,
        product: int,
        amount: Number,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Calculate Profit Share Rate.

        ``POST /v1/calculateprofitsharerate``

        Kapsam: ``public`` · Akış: client credentials

        This API calculates the profit share rate according to Kuveyt Turk rates and gives
        information about the profit to be obtained.

        Args:
            expire_day: (``expireDay``, gövde, zorunlu) Specifies the number of days to be due.
                Takes the max value of 999
            fx_type: (``fxType``, gövde, zorunlu) Specifies the type of currency to be
                calculated. (Takes the value "0" for TL.), (Takes the value "1" for USD.), (Takes
                the value "19" for EUR), (Takes the value "24" for XAU(gr). )
            product: (gövde, zorunlu) Specifies the product group to be calculated. (It takes
                the value "2" for the participation account.), (It takes the value "3" for the
                participation account with interim profit share payment.)
            amount: (gövde, zorunlu) Specifies the amount to be deposited into the participation
                account.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/calculate-profit-share-rate
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "expireDay": expire_day,
                "fxType": fx_type,
                "product": product,
                "amount": amount,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/calculateprofitsharerate",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def central_notification(
        self,
        *,
        template_code: str,
        parameters: Sequence[Any] | None = None,
        request_json: str | None = None,
        request_type: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Central Notification.

        ``POST /v1/notification/sendInfEng``

        Kapsam: ``public`` · Akış: client credentials

        Sends a notification by using the provided template code, parameter list, request JSON,
        and request type. The response returns the notification operation identifier and
        operation result.

        Args:
            template_code: (``templateCode``, gövde, zorunlu) Template code used to generate and
                send the notification.
            parameters: (gövde) List of key-value parameters to be used in the notification
                template.
            request_json: (``requestJson``, gövde) JSON request content related to the
                notification operation.
            request_type: (``requestType``, gövde) Request type information used to classify or
                process the notification request.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "templateCode": template_code,
                "parameters": parameters,
                "requestJson": request_json,
                "requestType": request_type,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/notification/sendInfEng",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def collect_installment(
        self,
        *,
        process_id: int,
        account_number: int,
        account_suffix: int,
        collection_account_number: int | None = None,
        collection_account_suffix: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Collect Installment.

        ``POST /v1/collections/collectInstallment``

        Kapsam: ``loans`` · Akış: client credentials

        Collects the installment from the customer's account provided in the parameters.

        Args:
            process_id: (``processId``, gövde, zorunlu) Installment Id.
            collection_account_number: (``collectionAccountNumber``, gövde)
            collection_account_suffix: (``collectionAccountSuffix``, gövde)
            account_number: (``accountNumber``, gövde, zorunlu) The account number of the
                customer.
            account_suffix: (``accountSuffix``, gövde, zorunlu) The account suffix number of the
                customer.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/collect-installment
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "processId": process_id,
                "collectionAccountNumber": collection_account_number,
                "collectionAccountSuffix": collection_account_suffix,
                "accountNumber": account_number,
                "accountSuffix": account_suffix,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/collections/collectInstallment",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def collection_list(
        self,
        *,
        account_number: int,
        account_suffix: int,
        process_id: int,
        is_ptt_collection: bool,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Collection List.

        ``POST /v1/collections``

        Kapsam: ``loans`` · Akış: client credentials

        Returns the list of collection records associated with the account number provided in
        the parameters.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) The account number of the
                customer.
            account_suffix: (``accountSuffix``, gövde, zorunlu) The account suffix number of the
                customer.
            process_id: (``processId``, gövde, zorunlu) Installment Id.
            is_ptt_collection: (``isPTTCollection``, gövde, zorunlu) Whether the collection is
                the PTT Collection.

        Yanıt alanları: processId, installmentType, installmentTypeName, projectAccountNumber,
        projectAccountSuffix, projectBranchId, maturityDate, installmentAmount, debtFEC,
        isLeasing, customerMainState

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/collection-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumber": account_number,
                "accountSuffix": account_suffix,
                "processId": process_id,
                "isPTTCollection": is_ptt_collection,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/collections",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def get_class_info(
        self,
        *,
        classroom_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Class Info.

        ``POST /v1/erp/lms/getClassInfo``

        Kapsam: ``public`` · Akış: client credentials

        To ensure that the active training information of the class is displayed on the screens
        placed at the doors of the classrooms.

        Args:
            classroom_id: (``classroomId``, gövde)

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/get-class-info
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "classroomId": classroom_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/erp/lms/getClassInfo",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def iban_validation_utility(
        self,
        *,
        iban: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """IBAN Validation Utility.

        ``POST /v1/validation/ibanvalidator``

        Kapsam: ``public`` · Akış: client credentials

        This API endpoint is a utility endpoint that performs validity control for a given IBAN
        (i.e. Internation Bank Identifier Number). The validity control is performed format-wise
        only. This implies that the existence/reality of the IBAN or its association with any
        Bank is not taken into concern during the validity control.

        Args:
            iban: (gövde, zorunlu) This input parameter represents the IBAN (i.e. International
                Bank Identifier Number) that is associated with a bank account. Its usage is
                mandatory in the request call and It can be associated with any world-wide bank
                (i.e. it does not necessarly have to be associated with Kuveyt Turk).

        Yanıt alanları: IsValid, ValidationMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/iban-validation-utility
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "iban": iban,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/validation/ibanvalidator",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kuveyt_turk_atm_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk ATM List.

        ``GET /v1/data/atms``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of off-site Kuveyt Turk ATMs.

        Yanıt alanları: name, cityName, longitude, latitude, address

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-atm-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/data/atms",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def kuveyt_turk_branch_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk Branch List.

        ``GET /v1/data/branches``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of Kuveyt Turk branches.

        Yanıt alanları: name, cityName, longitude, latitude, address, phone, fax, email

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-branch-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/data/branches",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def kuveyt_turk_xtm_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk XTM List.

        ``GET /v1/data/xtms``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of Kuveyt Turk XTMs.

        Yanıt alanları: name, cityName, longitude, latitude, address

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-xtm-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/data/xtms",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def loan_finance_calculation_parameter(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Calculation Parameter.

        ``GET /v1/data/loans``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of loan product types. This API is used to determine loan calculation
        parameters.

        Yanıt alanları: productTypeCode, productName

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/loan-finance-calculation-parameter
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/data/loans",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )


class AsyncInformation(AsyncResource):
    """Bilgi servisleri (şube, ATM, parametre sorguları...) (asenkron) - ``kt.information``."""

    async def bank_branch_list(
        self,
        *,
        bank_id: int,
        city_id: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Bank Branch List.

        ``GET /v1/data/banks/{bankId}/branches``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of branches of given bank id and city id within Turkish Banking System.

        Args:
            bank_id: (``bankId``, yol, zorunlu) Bank code for listing branches
            city_id: (``cityId``, sorgu, zorunlu) Specify the city of branches

        Yanıt alanları: branchId, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/bank-branch-list
        """
        _query = merge(
            {
                "cityId": city_id,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/data/banks/{bankId}/branches",
            scope="public",
            flow="client_credentials",
            path_params={"bankId": bank_id},
            query=_query,
            options=request_options,
        )

    async def bank_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Bank List.

        ``GET /v1/data/banks``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of banks within Turkish Banking System.

        Yanıt alanları: bankId, name

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/bank-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/data/banks",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def calculate_profit_share_rate(
        self,
        *,
        expire_day: int,
        fx_type: int,
        product: int,
        amount: Number,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Calculate Profit Share Rate.

        ``POST /v1/calculateprofitsharerate``

        Kapsam: ``public`` · Akış: client credentials

        This API calculates the profit share rate according to Kuveyt Turk rates and gives
        information about the profit to be obtained.

        Args:
            expire_day: (``expireDay``, gövde, zorunlu) Specifies the number of days to be due.
                Takes the max value of 999
            fx_type: (``fxType``, gövde, zorunlu) Specifies the type of currency to be
                calculated. (Takes the value "0" for TL.), (Takes the value "1" for USD.), (Takes
                the value "19" for EUR), (Takes the value "24" for XAU(gr). )
            product: (gövde, zorunlu) Specifies the product group to be calculated. (It takes
                the value "2" for the participation account.), (It takes the value "3" for the
                participation account with interim profit share payment.)
            amount: (gövde, zorunlu) Specifies the amount to be deposited into the participation
                account.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/calculate-profit-share-rate
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "expireDay": expire_day,
                "fxType": fx_type,
                "product": product,
                "amount": amount,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/calculateprofitsharerate",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def central_notification(
        self,
        *,
        template_code: str,
        parameters: Sequence[Any] | None = None,
        request_json: str | None = None,
        request_type: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Central Notification.

        ``POST /v1/notification/sendInfEng``

        Kapsam: ``public`` · Akış: client credentials

        Sends a notification by using the provided template code, parameter list, request JSON,
        and request type. The response returns the notification operation identifier and
        operation result.

        Args:
            template_code: (``templateCode``, gövde, zorunlu) Template code used to generate and
                send the notification.
            parameters: (gövde) List of key-value parameters to be used in the notification
                template.
            request_json: (``requestJson``, gövde) JSON request content related to the
                notification operation.
            request_type: (``requestType``, gövde) Request type information used to classify or
                process the notification request.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "templateCode": template_code,
                "parameters": parameters,
                "requestJson": request_json,
                "requestType": request_type,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/notification/sendInfEng",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def collect_installment(
        self,
        *,
        process_id: int,
        account_number: int,
        account_suffix: int,
        collection_account_number: int | None = None,
        collection_account_suffix: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Collect Installment.

        ``POST /v1/collections/collectInstallment``

        Kapsam: ``loans`` · Akış: client credentials

        Collects the installment from the customer's account provided in the parameters.

        Args:
            process_id: (``processId``, gövde, zorunlu) Installment Id.
            collection_account_number: (``collectionAccountNumber``, gövde)
            collection_account_suffix: (``collectionAccountSuffix``, gövde)
            account_number: (``accountNumber``, gövde, zorunlu) The account number of the
                customer.
            account_suffix: (``accountSuffix``, gövde, zorunlu) The account suffix number of the
                customer.

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/collect-installment
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "processId": process_id,
                "collectionAccountNumber": collection_account_number,
                "collectionAccountSuffix": collection_account_suffix,
                "accountNumber": account_number,
                "accountSuffix": account_suffix,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/collections/collectInstallment",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def collection_list(
        self,
        *,
        account_number: int,
        account_suffix: int,
        process_id: int,
        is_ptt_collection: bool,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Collection List.

        ``POST /v1/collections``

        Kapsam: ``loans`` · Akış: client credentials

        Returns the list of collection records associated with the account number provided in
        the parameters.

        Args:
            account_number: (``accountNumber``, gövde, zorunlu) The account number of the
                customer.
            account_suffix: (``accountSuffix``, gövde, zorunlu) The account suffix number of the
                customer.
            process_id: (``processId``, gövde, zorunlu) Installment Id.
            is_ptt_collection: (``isPTTCollection``, gövde, zorunlu) Whether the collection is
                the PTT Collection.

        Yanıt alanları: processId, installmentType, installmentTypeName, projectAccountNumber,
        projectAccountSuffix, projectBranchId, maturityDate, installmentAmount, debtFEC,
        isLeasing, customerMainState

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/collection-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountNumber": account_number,
                "accountSuffix": account_suffix,
                "processId": process_id,
                "isPTTCollection": is_ptt_collection,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/collections",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def get_class_info(
        self,
        *,
        classroom_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Get Class Info.

        ``POST /v1/erp/lms/getClassInfo``

        Kapsam: ``public`` · Akış: client credentials

        To ensure that the active training information of the class is displayed on the screens
        placed at the doors of the classrooms.

        Args:
            classroom_id: (``classroomId``, gövde)

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/get-class-info
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "classroomId": classroom_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/erp/lms/getClassInfo",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def iban_validation_utility(
        self,
        *,
        iban: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """IBAN Validation Utility.

        ``POST /v1/validation/ibanvalidator``

        Kapsam: ``public`` · Akış: client credentials

        This API endpoint is a utility endpoint that performs validity control for a given IBAN
        (i.e. Internation Bank Identifier Number). The validity control is performed format-wise
        only. This implies that the existence/reality of the IBAN or its association with any
        Bank is not taken into concern during the validity control.

        Args:
            iban: (gövde, zorunlu) This input parameter represents the IBAN (i.e. International
                Bank Identifier Number) that is associated with a bank account. Its usage is
                mandatory in the request call and It can be associated with any world-wide bank
                (i.e. it does not necessarly have to be associated with Kuveyt Turk).

        Yanıt alanları: IsValid, ValidationMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/iban-validation-utility
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "iban": iban,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/validation/ibanvalidator",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kuveyt_turk_atm_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk ATM List.

        ``GET /v1/data/atms``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of off-site Kuveyt Turk ATMs.

        Yanıt alanları: name, cityName, longitude, latitude, address

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-atm-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/data/atms",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def kuveyt_turk_branch_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk Branch List.

        ``GET /v1/data/branches``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of Kuveyt Turk branches.

        Yanıt alanları: name, cityName, longitude, latitude, address, phone, fax, email

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-branch-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/data/branches",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def kuveyt_turk_xtm_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk XTM List.

        ``GET /v1/data/xtms``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of Kuveyt Turk XTMs.

        Yanıt alanları: name, cityName, longitude, latitude, address

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-xtm-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/data/xtms",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def loan_finance_calculation_parameter(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Loan/Finance Calculation Parameter.

        ``GET /v1/data/loans``

        Kapsam: ``public`` · Akış: client credentials

        Returns the list of loan product types. This API is used to determine loan calculation
        parameters.

        Yanıt alanları: productTypeCode, productName

        Doküman: https://developer.kuveytturk.com.tr/documentation/notification-services/loan-finance-calculation-parameter
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/data/loans",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )
