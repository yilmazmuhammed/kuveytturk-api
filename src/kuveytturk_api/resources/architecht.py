"""Architecht uç noktaları (``kt.architecht``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["Architecht", "AsyncArchitecht"]


class Architecht(Resource):
    """Architecht - ``kt.architecht``."""

    def architecht_career_change(
        self,
        *,
        person_id: int,
        organization_id: int,
        job_id: int,
        position_id: int,
        assignment_grade: int,
        identity_number: str,
        effective_start_date: DateLike,
        effective_end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Architecht Career Change.

        ``POST /v1/architechtintegration/career/insertAssignment``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to create an assignment record for career integration. The request
        includes person, organization, job, position, assignment grade, identity number and
        effective date information. The response returns the execution reference and assignment
        creation result.

        Args:
            person_id: (``personId``, gövde, zorunlu) Person ID for whom the assignment will be
                created.
            organization_id: (``organizationId``, gövde, zorunlu) Organization ID associated
                with the assignment.
            job_id: (``jobId``, gövde, zorunlu) Job ID associated with the assignment.
            position_id: (``positionId``, gövde, zorunlu) Position ID associated with the
                assignment.
            assignment_grade: (``assignmentGrade``, gövde, zorunlu) Assignment grade
                information.
            identity_number: (``identityNumber``, gövde, zorunlu) Identity number of the person.
            effective_start_date: (``effectiveStartDate``, gövde, zorunlu) Effective start date
                of the assignment. Format: dd.MM.yyyy.
            effective_end_date: (``effectiveEndDate``, gövde) Effective end date of the
                assignment. Format: dd.MM.yyyy.

        Gövde alanları istekte ``assignmentContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: executionReferenceId, insertResult, processStatus, assignmentId

        Doküman: https://developer.kuveytturk.com.tr/documentation/architecht/architecht-career-change
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "personId": person_id,
                "organizationId": organization_id,
                "jobId": job_id,
                "positionId": position_id,
                "assignmentGrade": assignment_grade,
                "identityNumber": identity_number,
                "effectiveStartDate": effective_start_date,
                "effectiveEndDate": effective_end_date,
            },
            extra_body,
        )
        _body = {"assignmentContract": _body}
        return self._client.request(
            "POST",
            "/v1/architechtintegration/career/insertAssignment",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def customer_consent_cancellation(
        self,
        *,
        customer_id: str,
        token_data: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Consent Cancellation.

        ``POST /v1/airapi/revoke-consent``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to revoke customer consent records. The request includes the customer
        ID and token data list for the consents to be cancelled. The response returns the
        operation status with HTTP code and message information.

        Args:
            customer_id: (``customerId``, gövde, zorunlu) Customer ID for which consent records
                will be revoked.
            token_data: (``tokenData``, gövde, zorunlu) List of token data values identifying
                the consent records to be revoked.

        Yanıt alanları: httpcode, message

        Doküman: https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-cancellation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "customerId": customer_id,
                "tokenData": token_data,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/airapi/revoke-consent",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def customer_consent_list(
        self,
        *,
        customerid: int,
        tokentype: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Consent List.

        ``GET /v1/airapi/consent-list``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve the customer consent list. The service returns consent
        records filtered by customer ID and token type. The response includes token information,
        consent status, creation date, TPP name and TPP ID.

        Args:
            customerid: (sorgu, zorunlu) Customer ID for which the consent list will be
                retrieved.
            tokentype: (sorgu, zorunlu) Token type used to filter consent records.

        Yanıt alanları: token, status, created, tpp, tppId

        Doküman: https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-list
        """
        _query = merge(
            {
                "customerid": customerid,
                "tokentype": tokentype,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/airapi/consent-list",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )


class AsyncArchitecht(AsyncResource):
    """Architecht (asenkron) - ``kt.architecht``."""

    async def architecht_career_change(
        self,
        *,
        person_id: int,
        organization_id: int,
        job_id: int,
        position_id: int,
        assignment_grade: int,
        identity_number: str,
        effective_start_date: DateLike,
        effective_end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Architecht Career Change.

        ``POST /v1/architechtintegration/career/insertAssignment``

        Kapsam: ``public`` · Akış: client credentials

        This API is used to create an assignment record for career integration. The request
        includes person, organization, job, position, assignment grade, identity number and
        effective date information. The response returns the execution reference and assignment
        creation result.

        Args:
            person_id: (``personId``, gövde, zorunlu) Person ID for whom the assignment will be
                created.
            organization_id: (``organizationId``, gövde, zorunlu) Organization ID associated
                with the assignment.
            job_id: (``jobId``, gövde, zorunlu) Job ID associated with the assignment.
            position_id: (``positionId``, gövde, zorunlu) Position ID associated with the
                assignment.
            assignment_grade: (``assignmentGrade``, gövde, zorunlu) Assignment grade
                information.
            identity_number: (``identityNumber``, gövde, zorunlu) Identity number of the person.
            effective_start_date: (``effectiveStartDate``, gövde, zorunlu) Effective start date
                of the assignment. Format: dd.MM.yyyy.
            effective_end_date: (``effectiveEndDate``, gövde) Effective end date of the
                assignment. Format: dd.MM.yyyy.

        Gövde alanları istekte ``assignmentContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: executionReferenceId, insertResult, processStatus, assignmentId

        Doküman: https://developer.kuveytturk.com.tr/documentation/architecht/architecht-career-change
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "personId": person_id,
                "organizationId": organization_id,
                "jobId": job_id,
                "positionId": position_id,
                "assignmentGrade": assignment_grade,
                "identityNumber": identity_number,
                "effectiveStartDate": effective_start_date,
                "effectiveEndDate": effective_end_date,
            },
            extra_body,
        )
        _body = {"assignmentContract": _body}
        return await self._client.request(
            "POST",
            "/v1/architechtintegration/career/insertAssignment",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def customer_consent_cancellation(
        self,
        *,
        customer_id: str,
        token_data: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Consent Cancellation.

        ``POST /v1/airapi/revoke-consent``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to revoke customer consent records. The request includes the customer
        ID and token data list for the consents to be cancelled. The response returns the
        operation status with HTTP code and message information.

        Args:
            customer_id: (``customerId``, gövde, zorunlu) Customer ID for which consent records
                will be revoked.
            token_data: (``tokenData``, gövde, zorunlu) List of token data values identifying
                the consent records to be revoked.

        Yanıt alanları: httpcode, message

        Doküman: https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-cancellation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "customerId": customer_id,
                "tokenData": token_data,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/airapi/revoke-consent",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def customer_consent_list(
        self,
        *,
        customerid: int,
        tokentype: int,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Customer Consent List.

        ``GET /v1/airapi/consent-list``

        Kapsam: ``accounts`` · Akış: client credentials

        This API is used to retrieve the customer consent list. The service returns consent
        records filtered by customer ID and token type. The response includes token information,
        consent status, creation date, TPP name and TPP ID.

        Args:
            customerid: (sorgu, zorunlu) Customer ID for which the consent list will be
                retrieved.
            tokentype: (sorgu, zorunlu) Token type used to filter consent records.

        Yanıt alanları: token, status, created, tpp, tppId

        Doküman: https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-list
        """
        _query = merge(
            {
                "customerid": customerid,
                "tokentype": tokentype,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/airapi/consent-list",
            scope="accounts",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )
