"""Bağışlar uç noktaları (``kt.donations``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["AsyncDonations", "Donations"]


class Donations(Resource):
    """Bağışlar - ``kt.donations``."""

    def campaign_list_for_organization(
        self,
        *,
        organization_id: int,
        password: str,
        start_date: DateLike,
        end_date: DateLike,
        campaign_account_suffix: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Campaign List for Organization.

        ``POST /v1/donations/campaignList``

        Kapsam: ``donations`` · Akış: authorization code (müşteri girişi gerekir)

        Returns the list of all transactions between the start and end date made to the
        organization.

        Args:
            organization_id: (``organizationId``, gövde, zorunlu) Organization Code
            password: (gövde, zorunlu) Organization Password
            start_date: (``startDate``, gövde, zorunlu) Report Start Date
            end_date: (``endDate``, gövde, zorunlu) Report End Date
            campaign_account_suffix: (``campaignAccountSuffix``, gövde, zorunlu) Customer
                Account Suffix

        Yanıt alanları: AccountNumber, AccountSuffix, Balance, FECName, IBAN, BranchId,
        BranchName, TransactionCount, TransactionList, Amount, TranDate, ValueDate, BusinessKey,
        CurrentBalance, Description, SenderIdentityNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/campaign-list-for-organization
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "organizationId": organization_id,
                "password": password,
                "startDate": start_date,
                "endDate": end_date,
                "campaignAccountSuffix": campaign_account_suffix,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/donations/campaignList",
            scope="donations",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def donation_list_for_organization(
        self,
        *,
        customer_id: int,
        campaign_id: int | None = None,
        last_payment_id: int | None = None,
        is_canceled_included: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Donation List for Organization.

        ``POST /v1/donations/donationList``

        Kapsam: ``donations`` · Akış: client credentials

        Retrieves the donation payment list for an organization. The request can be filtered by
        campaign account number, campaign ID, last payment ID, cancellation inclusion flag and
        date range. The response includes donation summary information and detailed payment
        records.

        Args:
            customer_id: (``CustomerId``, gövde, zorunlu) Campaign account number of the
                organization for which donation payments will be listed.
            campaign_id: (``campaignId``, gövde) Campaign identifier used to filter donation
                payments.
            last_payment_id: (``lastPaymentId``, gövde) Last payment identifier used for
                pagination or retrieving records after a specific payment.
            is_canceled_included: (``isCanceledIncluded``, gövde) Indicates whether canceled
                donation payments should be included in the response.
            start_date: (``startDate``, gövde) Start date of the donation payment search range.
            end_date: (``endDate``, gövde) End date of the donation payment search range.

        Yanıt alanları: DonationDetail, LastPaymentId, DonationCount, PaymentList, PaymentId,
        TranDate, BankCode, BankName, CampaignId, CampaignCode, CampaignName, UnitAmount,
        Quantity, TotalAmount, FecCode, CampaignAccountNumber, CampaignAccountSuffix,
        StatusName, TranTaxNumber, TranTitle, TranGsmNumber, TranPhoneNumber, TranEMail,
        TranCountry, TranCountryName, TranCity, TranCityName, TranCounty, TranAddress,
        Description, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "CustomerId": customer_id,
                "campaignId": campaign_id,
                "lastPaymentId": last_payment_id,
                "isCanceledIncluded": is_canceled_included,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/donations/donationList",
            scope="donations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def donation_list_for_organization_tdv(
        self,
        *,
        organization_id: int,
        password: str,
        campaign_id: int,
        last_payment_id: int,
        is_canceled_included: int,
        start_date: str,
        end_date: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Donation List for Organization TDV.

        ``POST /v1/donations/donationListTdv``

        Kapsam: ``donations`` · Akış: client credentials

        Retrieves the donation payment list for TDV within the specified date range. The request
        can be filtered by organization ID, campaign ID, last payment ID, cancellation inclusion
        flag and date range. The response includes donation summary information and detailed
        payment records.

        Args:
            organization_id: (``organizationId``, gövde, zorunlu) Organization identifier used
                to retrieve donation payments.
            password: (gövde, zorunlu) Organization password used for request authorization.
            campaign_id: (``campaignId``, gövde, zorunlu) Campaign identifier used to filter
                donation payments.
            last_payment_id: (``lastPaymentId``, gövde, zorunlu) Last payment identifier used
                for pagination or retrieving records after a specific payment.
            is_canceled_included: (``isCanceledIncluded``, gövde, zorunlu) Indicates whether
                canceled donation payments should be included in the response. Use 0 for false and 1
                for true.
            start_date: (``startDate``, gövde, zorunlu) Start date of the donation payment
                search range. For example: 2015-06-01.
            end_date: (``endDate``, gövde, zorunlu) End date of the donation payment search
                range. For example: 2015-06-30.

        Yanıt alanları: DonationDetail, LastPaymentId, DonationCount, PaymentList, PaymentId,
        TranDate, PaymentAccountNo, BusinessKey, BankCode, BankName, BranchCode, BranchName,
        ChannelName, CampaignId, CampaignName, CampaignCode, UnitAmount, Quantity, TotalAmount,
        FecCode, CampaignAccountNumber, CampaignAccountSuffix, StatusName, TranTaxNumber,
        TranTitle, TranGsmNumber, TranPhoneNumber, TranBirthDate, TranGenderName, TranEducation,
        ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization-tdv
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "organizationId": organization_id,
                "password": password,
                "campaignId": campaign_id,
                "lastPaymentId": last_payment_id,
                "isCanceledIncluded": is_canceled_included,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/donations/donationListTdv",
            scope="donations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def external_payments_list(
        self,
        *,
        organization_id: int,
        password: str,
        start_date: str,
        end_date: str,
        account_suffix: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """External Payments List.

        ``POST /v1/donations/externalPayments``

        Kapsam: ``donations`` · Akış: authorization code (müşteri girişi gerekir)

        Returns all the external payments, such as EFT, money transfers, and cash processing,
        made to the selected campaign within the specified date range for the authenticated
        organization.

        Args:
            organization_id: (``organizationId``, gövde, zorunlu) Organization Code
            password: (gövde, zorunlu) Organization Password
            start_date: (``startDate``, gövde, zorunlu) Report Start Date e.g., "2015-06-01"
            end_date: (``endDate``, gövde, zorunlu) Report End Date e.g., "2015-06-01"
            account_suffix: (``accountSuffix``, gövde, zorunlu) Account Suffix Number

        Yanıt alanları: Amount, ProcessDate, BusinessKey, SenderIdentityNumber,
        ReceiverIdentityNumber, SenderName, ReceiverName, Description, BranchId, ProcessType,
        BranchName, FecName, SenderIbanNumber, SenderBankCode, SenderBranchId

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/external-payments-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "organizationId": organization_id,
                "password": password,
                "startDate": start_date,
                "endDate": end_date,
                "accountSuffix": account_suffix,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/donations/externalPayments",
            scope="donations",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncDonations(AsyncResource):
    """Bağışlar (asenkron) - ``kt.donations``."""

    async def campaign_list_for_organization(
        self,
        *,
        organization_id: int,
        password: str,
        start_date: DateLike,
        end_date: DateLike,
        campaign_account_suffix: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Campaign List for Organization.

        ``POST /v1/donations/campaignList``

        Kapsam: ``donations`` · Akış: authorization code (müşteri girişi gerekir)

        Returns the list of all transactions between the start and end date made to the
        organization.

        Args:
            organization_id: (``organizationId``, gövde, zorunlu) Organization Code
            password: (gövde, zorunlu) Organization Password
            start_date: (``startDate``, gövde, zorunlu) Report Start Date
            end_date: (``endDate``, gövde, zorunlu) Report End Date
            campaign_account_suffix: (``campaignAccountSuffix``, gövde, zorunlu) Customer
                Account Suffix

        Yanıt alanları: AccountNumber, AccountSuffix, Balance, FECName, IBAN, BranchId,
        BranchName, TransactionCount, TransactionList, Amount, TranDate, ValueDate, BusinessKey,
        CurrentBalance, Description, SenderIdentityNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/campaign-list-for-organization
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "organizationId": organization_id,
                "password": password,
                "startDate": start_date,
                "endDate": end_date,
                "campaignAccountSuffix": campaign_account_suffix,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/donations/campaignList",
            scope="donations",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def donation_list_for_organization(
        self,
        *,
        customer_id: int,
        campaign_id: int | None = None,
        last_payment_id: int | None = None,
        is_canceled_included: int | None = None,
        start_date: str | None = None,
        end_date: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Donation List for Organization.

        ``POST /v1/donations/donationList``

        Kapsam: ``donations`` · Akış: client credentials

        Retrieves the donation payment list for an organization. The request can be filtered by
        campaign account number, campaign ID, last payment ID, cancellation inclusion flag and
        date range. The response includes donation summary information and detailed payment
        records.

        Args:
            customer_id: (``CustomerId``, gövde, zorunlu) Campaign account number of the
                organization for which donation payments will be listed.
            campaign_id: (``campaignId``, gövde) Campaign identifier used to filter donation
                payments.
            last_payment_id: (``lastPaymentId``, gövde) Last payment identifier used for
                pagination or retrieving records after a specific payment.
            is_canceled_included: (``isCanceledIncluded``, gövde) Indicates whether canceled
                donation payments should be included in the response.
            start_date: (``startDate``, gövde) Start date of the donation payment search range.
            end_date: (``endDate``, gövde) End date of the donation payment search range.

        Yanıt alanları: DonationDetail, LastPaymentId, DonationCount, PaymentList, PaymentId,
        TranDate, BankCode, BankName, CampaignId, CampaignCode, CampaignName, UnitAmount,
        Quantity, TotalAmount, FecCode, CampaignAccountNumber, CampaignAccountSuffix,
        StatusName, TranTaxNumber, TranTitle, TranGsmNumber, TranPhoneNumber, TranEMail,
        TranCountry, TranCountryName, TranCity, TranCityName, TranCounty, TranAddress,
        Description, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "CustomerId": customer_id,
                "campaignId": campaign_id,
                "lastPaymentId": last_payment_id,
                "isCanceledIncluded": is_canceled_included,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/donations/donationList",
            scope="donations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def donation_list_for_organization_tdv(
        self,
        *,
        organization_id: int,
        password: str,
        campaign_id: int,
        last_payment_id: int,
        is_canceled_included: int,
        start_date: str,
        end_date: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Donation List for Organization TDV.

        ``POST /v1/donations/donationListTdv``

        Kapsam: ``donations`` · Akış: client credentials

        Retrieves the donation payment list for TDV within the specified date range. The request
        can be filtered by organization ID, campaign ID, last payment ID, cancellation inclusion
        flag and date range. The response includes donation summary information and detailed
        payment records.

        Args:
            organization_id: (``organizationId``, gövde, zorunlu) Organization identifier used
                to retrieve donation payments.
            password: (gövde, zorunlu) Organization password used for request authorization.
            campaign_id: (``campaignId``, gövde, zorunlu) Campaign identifier used to filter
                donation payments.
            last_payment_id: (``lastPaymentId``, gövde, zorunlu) Last payment identifier used
                for pagination or retrieving records after a specific payment.
            is_canceled_included: (``isCanceledIncluded``, gövde, zorunlu) Indicates whether
                canceled donation payments should be included in the response. Use 0 for false and 1
                for true.
            start_date: (``startDate``, gövde, zorunlu) Start date of the donation payment
                search range. For example: 2015-06-01.
            end_date: (``endDate``, gövde, zorunlu) End date of the donation payment search
                range. For example: 2015-06-30.

        Yanıt alanları: DonationDetail, LastPaymentId, DonationCount, PaymentList, PaymentId,
        TranDate, PaymentAccountNo, BusinessKey, BankCode, BankName, BranchCode, BranchName,
        ChannelName, CampaignId, CampaignName, CampaignCode, UnitAmount, Quantity, TotalAmount,
        FecCode, CampaignAccountNumber, CampaignAccountSuffix, StatusName, TranTaxNumber,
        TranTitle, TranGsmNumber, TranPhoneNumber, TranBirthDate, TranGenderName, TranEducation,
        ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization-tdv
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "organizationId": organization_id,
                "password": password,
                "campaignId": campaign_id,
                "lastPaymentId": last_payment_id,
                "isCanceledIncluded": is_canceled_included,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/donations/donationListTdv",
            scope="donations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def external_payments_list(
        self,
        *,
        organization_id: int,
        password: str,
        start_date: str,
        end_date: str,
        account_suffix: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """External Payments List.

        ``POST /v1/donations/externalPayments``

        Kapsam: ``donations`` · Akış: authorization code (müşteri girişi gerekir)

        Returns all the external payments, such as EFT, money transfers, and cash processing,
        made to the selected campaign within the specified date range for the authenticated
        organization.

        Args:
            organization_id: (``organizationId``, gövde, zorunlu) Organization Code
            password: (gövde, zorunlu) Organization Password
            start_date: (``startDate``, gövde, zorunlu) Report Start Date e.g., "2015-06-01"
            end_date: (``endDate``, gövde, zorunlu) Report End Date e.g., "2015-06-01"
            account_suffix: (``accountSuffix``, gövde, zorunlu) Account Suffix Number

        Yanıt alanları: Amount, ProcessDate, BusinessKey, SenderIdentityNumber,
        ReceiverIdentityNumber, SenderName, ReceiverName, Description, BranchId, ProcessType,
        BranchName, FecName, SenderIbanNumber, SenderBankCode, SenderBranchId

        Doküman: https://developer.kuveytturk.com.tr/documentation/donations/external-payments-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "organizationId": organization_id,
                "password": password,
                "startDate": start_date,
                "endDate": end_date,
                "accountSuffix": account_suffix,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/donations/externalPayments",
            scope="donations",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )
