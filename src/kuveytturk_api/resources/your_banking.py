"""Senin Bankan uç noktaları (``kt.your_banking``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["AsyncYourBanking", "YourBanking"]


class YourBanking(Resource):
    """Senin Bankan - ``kt.your_banking``."""

    def your_banking_account_application(
        self,
        *,
        identity_number: str,
        application_code: str,
        birth_day: DateLike,
        name_and_surname: str,
        gsm_country_code: int,
        gsm_area_code: int,
        gsm_number: str,
        sms_validation_code: str,
        identity_card_serial: str | None = None,
        identity_card_number: str | None = None,
        identity_card_serial_number: str | None = None,
        occupation_city_id: int | None = None,
        occupation_county_id: int | None = None,
        maidenhood_surname: str | None = None,
        education_level_id: int | None = None,
        profession_id: int | None = None,
        email_address: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application.

        ``POST /v1/yourbank/accountApplications``

        Kapsam: ``accounts`` · Akış: client credentials

        This endpoint is used to create or validate a YourBank account application by checking
        the applicant’s identity information. The request includes identity details, application
        information, mobile phone information, SMS validation code, education, profession, and
        contact information. >This API is in beta stage. Request and response models may change
        over time.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number of the
                applicant.
            application_code: (``ApplicationCode``, gövde, zorunlu) Code of the application
                type.
            birth_day: (``BirthDay``, gövde, zorunlu) Birth date of the applicant.
            name_and_surname: (``NameAndSurname``, gövde, zorunlu) Full name of the applicant.
            identity_card_serial: (``IdentityCardSerial``, gövde) Identity card serial
                information of the applicant.
            identity_card_number: (``IdentityCardNumber``, gövde) Identity card number of the
                applicant.
            identity_card_serial_number: (``IdentityCardSerialNumber``, gövde) Identity card
                serial number of the applicant.
            occupation_city_id: (``OccupationCityId``, gövde) City identifier of the applicant’s
                occupation location.
            occupation_county_id: (``OccupationCountyId``, gövde) County identifier of the
                applicant’s occupation location.
            gsm_country_code: (``GsmCountryCode``, gövde, zorunlu) GSM country code of the
                applicant’s mobile phone number.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant’s
                mobile phone number.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.
            sms_validation_code: (``SMSValidationCode``, gövde, zorunlu) SMS validation code
                sent to the applicant.
            maidenhood_surname: (``MaidenhoodSurname``, gövde) Maidenhood surname of the
                applicant.
            education_level_id: (``EducationLevelId``, gövde) Education level identifier of the
                applicant.
            profession_id: (``ProfessionId``, gövde) Profession identifier of the applicant.
            email_address: (``EmailAddress``, gövde) Email address of the applicant.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ApplicationCode": application_code,
                "BirthDay": birth_day,
                "NameAndSurname": name_and_surname,
                "IdentityCardSerial": identity_card_serial,
                "IdentityCardNumber": identity_card_number,
                "IdentityCardSerialNumber": identity_card_serial_number,
                "OccupationCityId": occupation_city_id,
                "OccupationCountyId": occupation_county_id,
                "GsmCountryCode": gsm_country_code,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
                "SMSValidationCode": sms_validation_code,
                "MaidenhoodSurname": maidenhood_surname,
                "EducationLevelId": education_level_id,
                "ProfessionId": profession_id,
                "EmailAddress": email_address,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/yourbank/accountApplications",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def your_banking_account_application_documents(
        self,
        *,
        identity_number: str,
        application_code: str,
        gsm_country_code: int,
        gsm_area_code: int,
        gsm_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application Documents.

        ``POST /v1/yourbank/accountApplicationDocuments``

        Kapsam: ``accounts`` · Akış: client credentials

        Retrieves Your Banking account application documents according to the provided identity
        number, application code, and GSM information. The response includes document name,
        document code, document identifier, application code, document content, and document
        extension details.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number used to
                retrieve account application documents.
            application_code: (``ApplicationCode``, gövde, zorunlu) Application code used to
                retrieve documents related to the account application.
            gsm_country_code: (``GsmCountryCode``, gövde, zorunlu) GSM country code of the
                applicant.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Yanıt alanları: DocumentName, DocumentCode, DocumentId, ApplicationCode,
        DocumentContent, DocumentExtension

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-documents
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ApplicationCode": application_code,
                "GsmCountryCode": gsm_country_code,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/yourbank/accountApplicationDocuments",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def your_banking_account_application_sms_validation(
        self,
        *,
        application_id: int,
        identity_number: str,
        gsm_country_code: int,
        gsm_area_code: int,
        gsm_number: str,
        sms_validation_code: str,
        block: str | None = None,
        district_name: str | None = None,
        flat_number: str | None = None,
        street_name: str | None = None,
        site_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application SMS Validation.

        ``POST /v1/yourbank/accountSmsOtp``

        Kapsam: ``accounts`` · Akış: client credentials

        This endpoint is used to validate the SMS OTP code and create or update person
        information for a YourBank account application. The request includes the application
        identifier, applicant identity number, mobile phone information, SMS validation code,
        and address details. >This API is in beta stage. Request and response models may change
        over time.

        Args:
            application_id: (``ApplicationId``, gövde, zorunlu) Unique identifier of the account
                application.
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number of the
                applicant.
            gsm_country_code: (``GsmCountryCode``, gövde, zorunlu) GSM country code of the
                applicant’s mobile phone number.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant’s
                mobile phone number.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.
            sms_validation_code: (``SMSValidationCode``, gövde, zorunlu) SMS OTP validation code
                sent to the applicant.
            block: (``Block``, gövde) Block information of the applicant’s address.
            district_name: (``DistrictName``, gövde) District name of the applicant’s address.
            flat_number: (``FlatNumber``, gövde) Flat number of the applicant’s address.
            street_name: (``StreetName``, gövde) Street name of the applicant’s address.
            site_name: (``SiteName``, gövde) Site name of the applicant’s address.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-sms-validation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "ApplicationId": application_id,
                "IdentityNumber": identity_number,
                "GsmCountryCode": gsm_country_code,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
                "SMSValidationCode": sms_validation_code,
                "Block": block,
                "DistrictName": district_name,
                "FlatNumber": flat_number,
                "StreetName": street_name,
                "SiteName": site_name,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/yourbank/accountSmsOtp",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def your_banking_account_application_status_query(
        self,
        *,
        identity_number: str,
        gsm_area_code: int,
        gsm_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application Status Query.

        ``POST /v1/yourbank/accountApplicationStatus``

        Kapsam: ``accounts`` · Akış: client credentials

        This endpoint is used to retrieve account application status information for YourBank
        applications. The request includes the applicant identity number and mobile phone
        information. The response returns the matching application status records, including
        customer, application number, status, application code, and application type
        information. >This API is in beta stage. Request and response models may change over
        time.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number of the
                applicant whose account application status will be queried.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant’s
                mobile phone number.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.

        Yanıt alanları: PersonId, CustomerName, ApplicationNumber, ApplicationStatus,
        StatusName, ApplicationCode, ApplicationTypeName

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-status-query
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/yourbank/accountApplicationStatus",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncYourBanking(AsyncResource):
    """Senin Bankan (asenkron) - ``kt.your_banking``."""

    async def your_banking_account_application(
        self,
        *,
        identity_number: str,
        application_code: str,
        birth_day: DateLike,
        name_and_surname: str,
        gsm_country_code: int,
        gsm_area_code: int,
        gsm_number: str,
        sms_validation_code: str,
        identity_card_serial: str | None = None,
        identity_card_number: str | None = None,
        identity_card_serial_number: str | None = None,
        occupation_city_id: int | None = None,
        occupation_county_id: int | None = None,
        maidenhood_surname: str | None = None,
        education_level_id: int | None = None,
        profession_id: int | None = None,
        email_address: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application.

        ``POST /v1/yourbank/accountApplications``

        Kapsam: ``accounts`` · Akış: client credentials

        This endpoint is used to create or validate a YourBank account application by checking
        the applicant’s identity information. The request includes identity details, application
        information, mobile phone information, SMS validation code, education, profession, and
        contact information. >This API is in beta stage. Request and response models may change
        over time.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number of the
                applicant.
            application_code: (``ApplicationCode``, gövde, zorunlu) Code of the application
                type.
            birth_day: (``BirthDay``, gövde, zorunlu) Birth date of the applicant.
            name_and_surname: (``NameAndSurname``, gövde, zorunlu) Full name of the applicant.
            identity_card_serial: (``IdentityCardSerial``, gövde) Identity card serial
                information of the applicant.
            identity_card_number: (``IdentityCardNumber``, gövde) Identity card number of the
                applicant.
            identity_card_serial_number: (``IdentityCardSerialNumber``, gövde) Identity card
                serial number of the applicant.
            occupation_city_id: (``OccupationCityId``, gövde) City identifier of the applicant’s
                occupation location.
            occupation_county_id: (``OccupationCountyId``, gövde) County identifier of the
                applicant’s occupation location.
            gsm_country_code: (``GsmCountryCode``, gövde, zorunlu) GSM country code of the
                applicant’s mobile phone number.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant’s
                mobile phone number.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.
            sms_validation_code: (``SMSValidationCode``, gövde, zorunlu) SMS validation code
                sent to the applicant.
            maidenhood_surname: (``MaidenhoodSurname``, gövde) Maidenhood surname of the
                applicant.
            education_level_id: (``EducationLevelId``, gövde) Education level identifier of the
                applicant.
            profession_id: (``ProfessionId``, gövde) Profession identifier of the applicant.
            email_address: (``EmailAddress``, gövde) Email address of the applicant.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ApplicationCode": application_code,
                "BirthDay": birth_day,
                "NameAndSurname": name_and_surname,
                "IdentityCardSerial": identity_card_serial,
                "IdentityCardNumber": identity_card_number,
                "IdentityCardSerialNumber": identity_card_serial_number,
                "OccupationCityId": occupation_city_id,
                "OccupationCountyId": occupation_county_id,
                "GsmCountryCode": gsm_country_code,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
                "SMSValidationCode": sms_validation_code,
                "MaidenhoodSurname": maidenhood_surname,
                "EducationLevelId": education_level_id,
                "ProfessionId": profession_id,
                "EmailAddress": email_address,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/yourbank/accountApplications",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def your_banking_account_application_documents(
        self,
        *,
        identity_number: str,
        application_code: str,
        gsm_country_code: int,
        gsm_area_code: int,
        gsm_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application Documents.

        ``POST /v1/yourbank/accountApplicationDocuments``

        Kapsam: ``accounts`` · Akış: client credentials

        Retrieves Your Banking account application documents according to the provided identity
        number, application code, and GSM information. The response includes document name,
        document code, document identifier, application code, document content, and document
        extension details.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number used to
                retrieve account application documents.
            application_code: (``ApplicationCode``, gövde, zorunlu) Application code used to
                retrieve documents related to the account application.
            gsm_country_code: (``GsmCountryCode``, gövde, zorunlu) GSM country code of the
                applicant.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Yanıt alanları: DocumentName, DocumentCode, DocumentId, ApplicationCode,
        DocumentContent, DocumentExtension

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-documents
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ApplicationCode": application_code,
                "GsmCountryCode": gsm_country_code,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/yourbank/accountApplicationDocuments",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def your_banking_account_application_sms_validation(
        self,
        *,
        application_id: int,
        identity_number: str,
        gsm_country_code: int,
        gsm_area_code: int,
        gsm_number: str,
        sms_validation_code: str,
        block: str | None = None,
        district_name: str | None = None,
        flat_number: str | None = None,
        street_name: str | None = None,
        site_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application SMS Validation.

        ``POST /v1/yourbank/accountSmsOtp``

        Kapsam: ``accounts`` · Akış: client credentials

        This endpoint is used to validate the SMS OTP code and create or update person
        information for a YourBank account application. The request includes the application
        identifier, applicant identity number, mobile phone information, SMS validation code,
        and address details. >This API is in beta stage. Request and response models may change
        over time.

        Args:
            application_id: (``ApplicationId``, gövde, zorunlu) Unique identifier of the account
                application.
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number of the
                applicant.
            gsm_country_code: (``GsmCountryCode``, gövde, zorunlu) GSM country code of the
                applicant’s mobile phone number.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant’s
                mobile phone number.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.
            sms_validation_code: (``SMSValidationCode``, gövde, zorunlu) SMS OTP validation code
                sent to the applicant.
            block: (``Block``, gövde) Block information of the applicant’s address.
            district_name: (``DistrictName``, gövde) District name of the applicant’s address.
            flat_number: (``FlatNumber``, gövde) Flat number of the applicant’s address.
            street_name: (``StreetName``, gövde) Street name of the applicant’s address.
            site_name: (``SiteName``, gövde) Site name of the applicant’s address.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-sms-validation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "ApplicationId": application_id,
                "IdentityNumber": identity_number,
                "GsmCountryCode": gsm_country_code,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
                "SMSValidationCode": sms_validation_code,
                "Block": block,
                "DistrictName": district_name,
                "FlatNumber": flat_number,
                "StreetName": street_name,
                "SiteName": site_name,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/yourbank/accountSmsOtp",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def your_banking_account_application_status_query(
        self,
        *,
        identity_number: str,
        gsm_area_code: int,
        gsm_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Your Banking Account Application Status Query.

        ``POST /v1/yourbank/accountApplicationStatus``

        Kapsam: ``accounts`` · Akış: client credentials

        This endpoint is used to retrieve account application status information for YourBank
        applications. The request includes the applicant identity number and mobile phone
        information. The response returns the matching application status records, including
        customer, application number, status, application code, and application type
        information. >This API is in beta stage. Request and response models may change over
        time.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Identity number of the
                applicant whose account application status will be queried.
            gsm_area_code: (``GsmAreaCode``, gövde, zorunlu) GSM area code of the applicant’s
                mobile phone number.
            gsm_number: (``GsmNumber``, gövde, zorunlu) GSM number of the applicant.

        Yanıt alanları: PersonId, CustomerName, ApplicationNumber, ApplicationStatus,
        StatusName, ApplicationCode, ApplicationTypeName

        Doküman: https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-status-query
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "GsmAreaCode": gsm_area_code,
                "GsmNumber": gsm_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/yourbank/accountApplicationStatus",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
