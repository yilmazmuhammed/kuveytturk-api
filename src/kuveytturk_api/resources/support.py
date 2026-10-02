"""Destek yönetimi uç noktaları (``kt.support``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Resource, merge

__all__ = ["AsyncSupport", "Support"]


class Support(Resource):
    """Destek yönetimi - ``kt.support``."""

    def kt_incident_activity_type_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Activity Type List.

        ``GET /v1/incident/activityTypes``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Returns the list of activity types to be used while inserting an activity.

        Yanıt alanları: activityTypeId, activityTypeName

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-activity-type-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/incident/activityTypes",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def kt_incident_cancel(
        self,
        *,
        incident_id: int | None = None,
        user_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Cancel.

        ``POST /v1/incident/cancel``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Cancels the given incident if the status of the incident permits and the user has a
        right to perform the operation.

        Args:
            incident_id: (``incidentId``, gövde)
            user_name: (``userName``, gövde)

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-cancel
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/incident/cancel",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_creation(
        self,
        *,
        summary_description: str,
        incident_description: str,
        product_id: int,
        user_name: str,
        bt_incident_id: int | None = None,
        customer_id: int | None = None,
        document_list: Sequence[Any] | None = None,
        optional_field_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Creation.

        ``POST /v1/incident/operation/create``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Creates an incident record with the provided summary, description, product, user, BT
        incident, customer, document, and optional field information. The response returns the
        created incident identifier and operation result.

        Args:
            summary_description: (``summaryDescription``, gövde, zorunlu) Short summary of the
                incident.
            incident_description: (``incidentDescription``, gövde, zorunlu) Detailed description
                of the incident.
            product_id: (``productId``, gövde, zorunlu) Product identifier related to the
                incident.
            user_name: (``userName``, gövde, zorunlu) User name of the person creating or
                associated with the incident.
            bt_incident_id: (``btIncidentId``, gövde) BT incident identifier associated with the
                incident.
            customer_id: (``customerId``, gövde) Customer identifier related to the incident.
            document_list: (``documentList``, gövde) List of documents attached to the incident.
            optional_field_list: (``optionalFieldList``, gövde) List of additional key-value
                fields related to the incident.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "summaryDescription": summary_description,
                "incidentDescription": incident_description,
                "productId": product_id,
                "userName": user_name,
                "btIncidentId": bt_incident_id,
                "customerId": customer_id,
                "documentList": document_list,
                "optionalFieldList": optional_field_list,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/incident/operation/create",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_creation_by_company(
        self,
        *,
        summary_description: str,
        incident_description: str,
        product_id: int,
        user_name: str,
        customer_id: int,
        software_company_id: int,
        referance_id: int | None = None,
        document_list: Sequence[Any] | None = None,
        optional_field_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Creation By Company.

        ``POST /v1/company/incident/create``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Creates a company incident record with the provided incident details, customer
        information, related reference information, optional documents, and additional optional
        fields. The response returns the created incident identifier and operation result.

        Args:
            summary_description: (``summaryDescription``, gövde, zorunlu) Short summary of the
                incident.
            incident_description: (``incidentDescription``, gövde, zorunlu) Detailed description
                of the incident.
            product_id: (``productId``, gövde, zorunlu) Product identifier related to the
                incident.
            user_name: (``userName``, gövde, zorunlu) User name of the person creating or
                associated with the incident.
            customer_id: (``customerId``, gövde, zorunlu) Customer identifier related to the
                incident.
            referance_id: (``referanceId``, gövde) Reference identifier associated with the
                incident.
            software_company_id: (``softwareCompanyId``, gövde, zorunlu) Software company
                identifier associated with the incident.
            document_list: (``documentList``, gövde) List of documents attached to the incident.
            optional_field_list: (``optionalFieldList``, gövde) List of additional key-value
                fields related to the incident.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation-by-company
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "summaryDescription": summary_description,
                "incidentDescription": incident_description,
                "productId": product_id,
                "userName": user_name,
                "customerId": customer_id,
                "referanceId": referance_id,
                "softwareCompanyId": software_company_id,
                "documentList": document_list,
                "optionalFieldList": optional_field_list,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/company/incident/create",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_defined_document_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Defined Document List.

        ``GET /v1/incident/defiendDocuments``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Returns the list of defined documents to be used for attaching documents while creating
        an incident record.

        Yanıt alanları: docId, docName, isMandatory

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-defined-document-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/incident/defiendDocuments",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def kt_incident_info(
        self,
        *,
        incident_id: int,
        user_name: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Info.

        ``POST /v1/incident/information/info``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves detailed incident information by using the provided incident identifier and
        user name. The response includes incident ownership, assignment, product, status, date,
        workflow, and solution details.

        Args:
            incident_id: (``incidentId``, gövde, zorunlu) Unique identifier of the incident to
                be queried.
            user_name: (``userName``, gövde, zorunlu) User name of the requester or user
                associated with the incident query.

        Yanıt alanları: userName, assignedUserCode, demandUnitId, summaryDescription,
        incidentDescription, productId, statusId, incidentId, incidentNo, btIncidentId,
        flowStatusId, assignmentGroupId, openDate, closeDate, startDate, solutionTypeId,
        solutionMethod, solutionDescription, divitInstanceId, workFlowInstanceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-info
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/incident/information/info",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_insert_activity(
        self,
        *,
        incident_id: int,
        activity_type_id: int,
        description: str,
        send_mail: bool,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Insert Activity.

        ``POST /v1/incident/insertActivity``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Inserts an activity record for the given incident as the given activity type.

        Args:
            incident_id: (``incidentId``, gövde, zorunlu) ID of the incident to which activity
                record will be inserted.
            activity_type_id: (``activityTypeId``, gövde, zorunlu) Type ID of the activity.
                Detailed info can be found via KT Incident Activity Type List endpoint.
            description: (gövde, zorunlu) Explanation of the activity.
            send_mail: (``sendMail``, gövde, zorunlu) Whether an email about this activity will
                be sent to the user who creaeted the incident.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-activity
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "activityTypeId": activity_type_id,
                "description": description,
                "sendMail": send_mail,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/incident/insertActivity",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_insert_document(
        self,
        *,
        document_contract: Sequence[Any] | None = None,
        incident_id: int | None = None,
        user_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Insert Document.

        ``POST /v1/incident/insertDocument``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Inserts additional documents into the given incident.

        Args:
            document_contract: (``documentContract``, gövde)
            incident_id: (``incidentId``, gövde)
            user_name: (``userName``, gövde)

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-document
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "documentContract": document_contract,
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/incident/insertDocument",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_neova_info(
        self,
        *,
        incident_no: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Neova Info.

        ``POST /v1/incident/neova/info``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves detailed Neova incident information by using the provided incident number. The
        response includes incident status, assignment, description, solution, product, creator
        user, history, activity, document, and optional field details.

        Args:
            incident_no: (``incidentNo``, gövde, zorunlu) Incident number used to retrieve Neova
                incident details.

        Yanıt alanları: incidentId, incidentNo, statusId, assignmentGroupName, assignedUserCode,
        assignedUserName, summaryDescription, incidentDescription, solutionDescription,
        userName, optionalFieldList, key, product, productCode, productName, parentCategoryCode,
        demandUnitName, creatorUserInfo, userId, userCode, firstName, lastName, email,
        organizationName, incidentHistoryList, fieldName, previous, current, systemDate,
        activityList, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-info
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentNo": incident_no,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/incident/neova/info",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_neova_list(
        self,
        *,
        incident_no: str | None = None,
        parent_category_name: str | None = None,
        sub_category_name: str | None = None,
        parent_product_name: str | None = None,
        product_name: str | None = None,
        demand_unit_name: str | None = None,
        assignment_group_name: str | None = None,
        assignment_person: str | None = None,
        status_name: str | None = None,
        open_person_name: str | None = None,
        open_person_group_name: str | None = None,
        open_person_parent_group_name: str | None = None,
        open_date: DateLike | None = None,
        summary_description: str | None = None,
        incident_description: str | None = None,
        close_date: DateLike | None = None,
        solution_description: str | None = None,
        solution_type: str | None = None,
        status_id: str | None = None,
        user_name: str | None = None,
        activity_description: str | None = None,
        action_to_be_taken: int | None = None,
        reopen_count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Neova List.

        ``POST /v1/incident/neova/list``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves the Neova incident list according to the provided filter criteria. The request
        can include incident, category, product, demand unit, assignment, status, opening,
        solution, activity, action, and reopen count information. The response returns matching
        incident records with their category, product, assignment, status, date, description,
        solution, and reopen count details.

        Args:
            incident_no: (``IncidentNo``, gövde) Incident number used to filter the incident
                list.
            parent_category_name: (``ParentCategoryName``, gövde) Parent category name used to
                filter incidents.
            sub_category_name: (``SubCategoryName``, gövde) Subcategory name used to filter
                incidents.
            parent_product_name: (``ParentProductName``, gövde) Parent product name used to
                filter incidents.
            product_name: (``ProductName``, gövde) Product name used to filter incidents.
            demand_unit_name: (``DemandUnitName``, gövde) Demand unit name used to filter
                incidents.
            assignment_group_name: (``AssignmentGroupName``, gövde) Assignment group name used
                to filter incidents.
            assignment_person: (``AssignmentPerson``, gövde) Assigned person information used to
                filter incidents.
            status_name: (``StatusName``, gövde) Status name used to filter incidents.
            open_person_name: (``OpenPersonName``, gövde) Name of the user who opened the
                incident.
            open_person_group_name: (``OpenPersonGroupName``, gövde) Group name of the user who
                opened the incident.
            open_person_parent_group_name: (``OpenPersonParentGroupName``, gövde) Parent group
                name of the user who opened the incident.
            open_date: (``OpenDate``, gövde) Opening date used to filter incidents.
            summary_description: (``SummaryDescription``, gövde) Summary description used to
                filter incidents.
            incident_description: (``IncidentDescription``, gövde) Incident description used to
                filter incidents.
            close_date: (``CloseDate``, gövde) Closing date used to filter incidents.
            solution_description: (``SolutionDescription``, gövde) Solution description used to
                filter incidents.
            solution_type: (``SolutionType``, gövde) Solution type used to filter incidents.
            status_id: (``StatusId``, gövde) Status identifier used to filter incidents.
            user_name: (``UserName``, gövde) User name used in the incident list query.
            activity_description: (``ActivityDescription``, gövde) Activity description used to
                filter incidents.
            action_to_be_taken: (``ActionToBeTaken``, gövde) Action to be taken value used to
                filter incidents.
            reopen_count: (``ReopenCount``, gövde) Reopen count used to filter incidents.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: IncidentNo, ParentCategoryName, SubCategoryName, ParentProductName,
        ProductName, DemandUnitName, AssignmentGroupName, AssignmentPerson, StatusName,
        OpenPersonName, OpenPersonGroupName, OpenPersonParentGroupName, OpenDate,
        SummaryDescription, IncidentDescription, CloseDate, SolutionDescription, SolutionType,
        ReopenCount

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IncidentNo": incident_no,
                "ParentCategoryName": parent_category_name,
                "SubCategoryName": sub_category_name,
                "ParentProductName": parent_product_name,
                "ProductName": product_name,
                "DemandUnitName": demand_unit_name,
                "AssignmentGroupName": assignment_group_name,
                "AssignmentPerson": assignment_person,
                "StatusName": status_name,
                "OpenPersonName": open_person_name,
                "OpenPersonGroupName": open_person_group_name,
                "OpenPersonParentGroupName": open_person_parent_group_name,
                "OpenDate": open_date,
                "SummaryDescription": summary_description,
                "IncidentDescription": incident_description,
                "CloseDate": close_date,
                "SolutionDescription": solution_description,
                "SolutionType": solution_type,
                "StatusId": status_id,
                "UserName": user_name,
                "ActivityDescription": activity_description,
                "ActionToBeTaken": action_to_be_taken,
                "ReopenCount": reopen_count,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/incident/neova/list",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_neova_update(
        self,
        *,
        incident_no: str,
        parent_category_name: str | None = None,
        sub_category_name: str | None = None,
        parent_product_name: str | None = None,
        product_name: str | None = None,
        demand_unit_name: str | None = None,
        assignment_group_name: str | None = None,
        assignment_person: str | None = None,
        status_name: str | None = None,
        open_person_name: str | None = None,
        open_person_group_name: str | None = None,
        open_person_parent_group_name: str | None = None,
        open_date: DateLike | None = None,
        summary_description: str | None = None,
        incident_description: str | None = None,
        close_date: DateLike | None = None,
        solution_description: str | None = None,
        solution_type: str | None = None,
        status_id: str | None = None,
        user_name: str | None = None,
        activity_description: str | None = None,
        action_to_be_taken: int | None = None,
        reopen_count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Neova Update.

        ``POST /v1/incident/neova/update``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Updates Neova incident information according to the provided incident, category,
        product, demand unit, assignment, status, opening, solution, activity, action, and
        reopen count details. The response indicates whether the update operation was completed
        successfully.

        Args:
            incident_no: (``IncidentNo``, gövde, zorunlu) Incident number of the record to be
                updated.
            parent_category_name: (``ParentCategoryName``, gövde) Parent category name of the
                incident.
            sub_category_name: (``SubCategoryName``, gövde) Subcategory name of the incident.
            parent_product_name: (``ParentProductName``, gövde) Parent product name related to
                the incident.
            product_name: (``ProductName``, gövde) Product name related to the incident.
            demand_unit_name: (``DemandUnitName``, gövde) Demand unit name related to the
                incident.
            assignment_group_name: (``AssignmentGroupName``, gövde) Assignment group name
                responsible for the incident.
            assignment_person: (``AssignmentPerson``, gövde) Assigned person information of the
                incident.
            status_name: (``StatusName``, gövde) Status name of the incident.
            open_person_name: (``OpenPersonName``, gövde) Name of the user who opened the
                incident.
            open_person_group_name: (``OpenPersonGroupName``, gövde) Group name of the user who
                opened the incident.
            open_person_parent_group_name: (``OpenPersonParentGroupName``, gövde) Parent group
                name of the user who opened the incident.
            open_date: (``OpenDate``, gövde) Date and time when the incident was opened.
            summary_description: (``SummaryDescription``, gövde) Short summary description of
                the incident.
            incident_description: (``IncidentDescription``, gövde) Detailed description of the
                incident.
            close_date: (``CloseDate``, gövde) Date and time when the incident was closed.
            solution_description: (``SolutionDescription``, gövde) Description of the solution
                applied to the incident.
            solution_type: (``SolutionType``, gövde) Solution type applied to the incident.
            status_id: (``StatusId``, gövde) Status identifier of the incident.
            user_name: (``UserName``, gövde) User name used in the incident update operation.
            activity_description: (``ActivityDescription``, gövde) Activity description related
                to the incident update.
            action_to_be_taken: (``ActionToBeTaken``, gövde) Action to be taken value for the
                incident.
            reopen_count: (``ReopenCount``, gövde) Number of times the incident was reopened.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-update
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IncidentNo": incident_no,
                "ParentCategoryName": parent_category_name,
                "SubCategoryName": sub_category_name,
                "ParentProductName": parent_product_name,
                "ProductName": product_name,
                "DemandUnitName": demand_unit_name,
                "AssignmentGroupName": assignment_group_name,
                "AssignmentPerson": assignment_person,
                "StatusName": status_name,
                "OpenPersonName": open_person_name,
                "OpenPersonGroupName": open_person_group_name,
                "OpenPersonParentGroupName": open_person_parent_group_name,
                "OpenDate": open_date,
                "SummaryDescription": summary_description,
                "IncidentDescription": incident_description,
                "CloseDate": close_date,
                "SolutionDescription": solution_description,
                "SolutionType": solution_type,
                "StatusId": status_id,
                "UserName": user_name,
                "ActivityDescription": activity_description,
                "ActionToBeTaken": action_to_be_taken,
                "ReopenCount": reopen_count,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/incident/neova/update",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_optional_field_list(
        self,
        *,
        product_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Optional Field List.

        ``POST /v1/incident/optionalFieldList``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Returns the list of optional field related to the provided product.

        Args:
            product_id: (``productId``, gövde, zorunlu) Id of the product.

        Yanıt alanları: optionalFieldName, isMandatory

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-optional-field-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "productId": product_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/incident/optionalFieldList",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def kt_incident_product_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Product List.

        ``GET /v1/incident/information/products``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves the product list used for incident operations. The response includes product
        identifier, related demand unit workgroup, demand unit name, and product path
        information.

        Yanıt alanları: productId, demandUnitWorkgroupId, demandUnitName, productPath

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-product-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/incident/information/products",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def kt_incident_reopen(
        self,
        *,
        incident_id: int | None = None,
        user_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Reopen.

        ``POST /v1/incident/reopen``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Reopens the given incident if the status of the incident permits and the user has a
        right to perform the operation.

        Args:
            incident_id: (``incidentId``, gövde)
            user_name: (``userName``, gövde)

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-reopen
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/incident/reopen",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncSupport(AsyncResource):
    """Destek yönetimi (asenkron) - ``kt.support``."""

    async def kt_incident_activity_type_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Activity Type List.

        ``GET /v1/incident/activityTypes``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Returns the list of activity types to be used while inserting an activity.

        Yanıt alanları: activityTypeId, activityTypeName

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-activity-type-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/incident/activityTypes",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def kt_incident_cancel(
        self,
        *,
        incident_id: int | None = None,
        user_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Cancel.

        ``POST /v1/incident/cancel``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Cancels the given incident if the status of the incident permits and the user has a
        right to perform the operation.

        Args:
            incident_id: (``incidentId``, gövde)
            user_name: (``userName``, gövde)

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-cancel
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/incident/cancel",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_creation(
        self,
        *,
        summary_description: str,
        incident_description: str,
        product_id: int,
        user_name: str,
        bt_incident_id: int | None = None,
        customer_id: int | None = None,
        document_list: Sequence[Any] | None = None,
        optional_field_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Creation.

        ``POST /v1/incident/operation/create``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Creates an incident record with the provided summary, description, product, user, BT
        incident, customer, document, and optional field information. The response returns the
        created incident identifier and operation result.

        Args:
            summary_description: (``summaryDescription``, gövde, zorunlu) Short summary of the
                incident.
            incident_description: (``incidentDescription``, gövde, zorunlu) Detailed description
                of the incident.
            product_id: (``productId``, gövde, zorunlu) Product identifier related to the
                incident.
            user_name: (``userName``, gövde, zorunlu) User name of the person creating or
                associated with the incident.
            bt_incident_id: (``btIncidentId``, gövde) BT incident identifier associated with the
                incident.
            customer_id: (``customerId``, gövde) Customer identifier related to the incident.
            document_list: (``documentList``, gövde) List of documents attached to the incident.
            optional_field_list: (``optionalFieldList``, gövde) List of additional key-value
                fields related to the incident.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "summaryDescription": summary_description,
                "incidentDescription": incident_description,
                "productId": product_id,
                "userName": user_name,
                "btIncidentId": bt_incident_id,
                "customerId": customer_id,
                "documentList": document_list,
                "optionalFieldList": optional_field_list,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/incident/operation/create",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_creation_by_company(
        self,
        *,
        summary_description: str,
        incident_description: str,
        product_id: int,
        user_name: str,
        customer_id: int,
        software_company_id: int,
        referance_id: int | None = None,
        document_list: Sequence[Any] | None = None,
        optional_field_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Creation By Company.

        ``POST /v1/company/incident/create``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Creates a company incident record with the provided incident details, customer
        information, related reference information, optional documents, and additional optional
        fields. The response returns the created incident identifier and operation result.

        Args:
            summary_description: (``summaryDescription``, gövde, zorunlu) Short summary of the
                incident.
            incident_description: (``incidentDescription``, gövde, zorunlu) Detailed description
                of the incident.
            product_id: (``productId``, gövde, zorunlu) Product identifier related to the
                incident.
            user_name: (``userName``, gövde, zorunlu) User name of the person creating or
                associated with the incident.
            customer_id: (``customerId``, gövde, zorunlu) Customer identifier related to the
                incident.
            referance_id: (``referanceId``, gövde) Reference identifier associated with the
                incident.
            software_company_id: (``softwareCompanyId``, gövde, zorunlu) Software company
                identifier associated with the incident.
            document_list: (``documentList``, gövde) List of documents attached to the incident.
            optional_field_list: (``optionalFieldList``, gövde) List of additional key-value
                fields related to the incident.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation-by-company
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "summaryDescription": summary_description,
                "incidentDescription": incident_description,
                "productId": product_id,
                "userName": user_name,
                "customerId": customer_id,
                "referanceId": referance_id,
                "softwareCompanyId": software_company_id,
                "documentList": document_list,
                "optionalFieldList": optional_field_list,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/company/incident/create",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_defined_document_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Defined Document List.

        ``GET /v1/incident/defiendDocuments``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Returns the list of defined documents to be used for attaching documents while creating
        an incident record.

        Yanıt alanları: docId, docName, isMandatory

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-defined-document-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/incident/defiendDocuments",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def kt_incident_info(
        self,
        *,
        incident_id: int,
        user_name: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Info.

        ``POST /v1/incident/information/info``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves detailed incident information by using the provided incident identifier and
        user name. The response includes incident ownership, assignment, product, status, date,
        workflow, and solution details.

        Args:
            incident_id: (``incidentId``, gövde, zorunlu) Unique identifier of the incident to
                be queried.
            user_name: (``userName``, gövde, zorunlu) User name of the requester or user
                associated with the incident query.

        Yanıt alanları: userName, assignedUserCode, demandUnitId, summaryDescription,
        incidentDescription, productId, statusId, incidentId, incidentNo, btIncidentId,
        flowStatusId, assignmentGroupId, openDate, closeDate, startDate, solutionTypeId,
        solutionMethod, solutionDescription, divitInstanceId, workFlowInstanceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-info
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/incident/information/info",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_insert_activity(
        self,
        *,
        incident_id: int,
        activity_type_id: int,
        description: str,
        send_mail: bool,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Insert Activity.

        ``POST /v1/incident/insertActivity``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Inserts an activity record for the given incident as the given activity type.

        Args:
            incident_id: (``incidentId``, gövde, zorunlu) ID of the incident to which activity
                record will be inserted.
            activity_type_id: (``activityTypeId``, gövde, zorunlu) Type ID of the activity.
                Detailed info can be found via KT Incident Activity Type List endpoint.
            description: (gövde, zorunlu) Explanation of the activity.
            send_mail: (``sendMail``, gövde, zorunlu) Whether an email about this activity will
                be sent to the user who creaeted the incident.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-activity
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "activityTypeId": activity_type_id,
                "description": description,
                "sendMail": send_mail,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/incident/insertActivity",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_insert_document(
        self,
        *,
        document_contract: Sequence[Any] | None = None,
        incident_id: int | None = None,
        user_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Insert Document.

        ``POST /v1/incident/insertDocument``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Inserts additional documents into the given incident.

        Args:
            document_contract: (``documentContract``, gövde)
            incident_id: (``incidentId``, gövde)
            user_name: (``userName``, gövde)

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-document
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "documentContract": document_contract,
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/incident/insertDocument",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_neova_info(
        self,
        *,
        incident_no: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Neova Info.

        ``POST /v1/incident/neova/info``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves detailed Neova incident information by using the provided incident number. The
        response includes incident status, assignment, description, solution, product, creator
        user, history, activity, document, and optional field details.

        Args:
            incident_no: (``incidentNo``, gövde, zorunlu) Incident number used to retrieve Neova
                incident details.

        Yanıt alanları: incidentId, incidentNo, statusId, assignmentGroupName, assignedUserCode,
        assignedUserName, summaryDescription, incidentDescription, solutionDescription,
        userName, optionalFieldList, key, product, productCode, productName, parentCategoryCode,
        demandUnitName, creatorUserInfo, userId, userCode, firstName, lastName, email,
        organizationName, incidentHistoryList, fieldName, previous, current, systemDate,
        activityList, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-info
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentNo": incident_no,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/incident/neova/info",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_neova_list(
        self,
        *,
        incident_no: str | None = None,
        parent_category_name: str | None = None,
        sub_category_name: str | None = None,
        parent_product_name: str | None = None,
        product_name: str | None = None,
        demand_unit_name: str | None = None,
        assignment_group_name: str | None = None,
        assignment_person: str | None = None,
        status_name: str | None = None,
        open_person_name: str | None = None,
        open_person_group_name: str | None = None,
        open_person_parent_group_name: str | None = None,
        open_date: DateLike | None = None,
        summary_description: str | None = None,
        incident_description: str | None = None,
        close_date: DateLike | None = None,
        solution_description: str | None = None,
        solution_type: str | None = None,
        status_id: str | None = None,
        user_name: str | None = None,
        activity_description: str | None = None,
        action_to_be_taken: int | None = None,
        reopen_count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Neova List.

        ``POST /v1/incident/neova/list``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves the Neova incident list according to the provided filter criteria. The request
        can include incident, category, product, demand unit, assignment, status, opening,
        solution, activity, action, and reopen count information. The response returns matching
        incident records with their category, product, assignment, status, date, description,
        solution, and reopen count details.

        Args:
            incident_no: (``IncidentNo``, gövde) Incident number used to filter the incident
                list.
            parent_category_name: (``ParentCategoryName``, gövde) Parent category name used to
                filter incidents.
            sub_category_name: (``SubCategoryName``, gövde) Subcategory name used to filter
                incidents.
            parent_product_name: (``ParentProductName``, gövde) Parent product name used to
                filter incidents.
            product_name: (``ProductName``, gövde) Product name used to filter incidents.
            demand_unit_name: (``DemandUnitName``, gövde) Demand unit name used to filter
                incidents.
            assignment_group_name: (``AssignmentGroupName``, gövde) Assignment group name used
                to filter incidents.
            assignment_person: (``AssignmentPerson``, gövde) Assigned person information used to
                filter incidents.
            status_name: (``StatusName``, gövde) Status name used to filter incidents.
            open_person_name: (``OpenPersonName``, gövde) Name of the user who opened the
                incident.
            open_person_group_name: (``OpenPersonGroupName``, gövde) Group name of the user who
                opened the incident.
            open_person_parent_group_name: (``OpenPersonParentGroupName``, gövde) Parent group
                name of the user who opened the incident.
            open_date: (``OpenDate``, gövde) Opening date used to filter incidents.
            summary_description: (``SummaryDescription``, gövde) Summary description used to
                filter incidents.
            incident_description: (``IncidentDescription``, gövde) Incident description used to
                filter incidents.
            close_date: (``CloseDate``, gövde) Closing date used to filter incidents.
            solution_description: (``SolutionDescription``, gövde) Solution description used to
                filter incidents.
            solution_type: (``SolutionType``, gövde) Solution type used to filter incidents.
            status_id: (``StatusId``, gövde) Status identifier used to filter incidents.
            user_name: (``UserName``, gövde) User name used in the incident list query.
            activity_description: (``ActivityDescription``, gövde) Activity description used to
                filter incidents.
            action_to_be_taken: (``ActionToBeTaken``, gövde) Action to be taken value used to
                filter incidents.
            reopen_count: (``ReopenCount``, gövde) Reopen count used to filter incidents.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: IncidentNo, ParentCategoryName, SubCategoryName, ParentProductName,
        ProductName, DemandUnitName, AssignmentGroupName, AssignmentPerson, StatusName,
        OpenPersonName, OpenPersonGroupName, OpenPersonParentGroupName, OpenDate,
        SummaryDescription, IncidentDescription, CloseDate, SolutionDescription, SolutionType,
        ReopenCount

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IncidentNo": incident_no,
                "ParentCategoryName": parent_category_name,
                "SubCategoryName": sub_category_name,
                "ParentProductName": parent_product_name,
                "ProductName": product_name,
                "DemandUnitName": demand_unit_name,
                "AssignmentGroupName": assignment_group_name,
                "AssignmentPerson": assignment_person,
                "StatusName": status_name,
                "OpenPersonName": open_person_name,
                "OpenPersonGroupName": open_person_group_name,
                "OpenPersonParentGroupName": open_person_parent_group_name,
                "OpenDate": open_date,
                "SummaryDescription": summary_description,
                "IncidentDescription": incident_description,
                "CloseDate": close_date,
                "SolutionDescription": solution_description,
                "SolutionType": solution_type,
                "StatusId": status_id,
                "UserName": user_name,
                "ActivityDescription": activity_description,
                "ActionToBeTaken": action_to_be_taken,
                "ReopenCount": reopen_count,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/incident/neova/list",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_neova_update(
        self,
        *,
        incident_no: str,
        parent_category_name: str | None = None,
        sub_category_name: str | None = None,
        parent_product_name: str | None = None,
        product_name: str | None = None,
        demand_unit_name: str | None = None,
        assignment_group_name: str | None = None,
        assignment_person: str | None = None,
        status_name: str | None = None,
        open_person_name: str | None = None,
        open_person_group_name: str | None = None,
        open_person_parent_group_name: str | None = None,
        open_date: DateLike | None = None,
        summary_description: str | None = None,
        incident_description: str | None = None,
        close_date: DateLike | None = None,
        solution_description: str | None = None,
        solution_type: str | None = None,
        status_id: str | None = None,
        user_name: str | None = None,
        activity_description: str | None = None,
        action_to_be_taken: int | None = None,
        reopen_count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Neova Update.

        ``POST /v1/incident/neova/update``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Updates Neova incident information according to the provided incident, category,
        product, demand unit, assignment, status, opening, solution, activity, action, and
        reopen count details. The response indicates whether the update operation was completed
        successfully.

        Args:
            incident_no: (``IncidentNo``, gövde, zorunlu) Incident number of the record to be
                updated.
            parent_category_name: (``ParentCategoryName``, gövde) Parent category name of the
                incident.
            sub_category_name: (``SubCategoryName``, gövde) Subcategory name of the incident.
            parent_product_name: (``ParentProductName``, gövde) Parent product name related to
                the incident.
            product_name: (``ProductName``, gövde) Product name related to the incident.
            demand_unit_name: (``DemandUnitName``, gövde) Demand unit name related to the
                incident.
            assignment_group_name: (``AssignmentGroupName``, gövde) Assignment group name
                responsible for the incident.
            assignment_person: (``AssignmentPerson``, gövde) Assigned person information of the
                incident.
            status_name: (``StatusName``, gövde) Status name of the incident.
            open_person_name: (``OpenPersonName``, gövde) Name of the user who opened the
                incident.
            open_person_group_name: (``OpenPersonGroupName``, gövde) Group name of the user who
                opened the incident.
            open_person_parent_group_name: (``OpenPersonParentGroupName``, gövde) Parent group
                name of the user who opened the incident.
            open_date: (``OpenDate``, gövde) Date and time when the incident was opened.
            summary_description: (``SummaryDescription``, gövde) Short summary description of
                the incident.
            incident_description: (``IncidentDescription``, gövde) Detailed description of the
                incident.
            close_date: (``CloseDate``, gövde) Date and time when the incident was closed.
            solution_description: (``SolutionDescription``, gövde) Description of the solution
                applied to the incident.
            solution_type: (``SolutionType``, gövde) Solution type applied to the incident.
            status_id: (``StatusId``, gövde) Status identifier of the incident.
            user_name: (``UserName``, gövde) User name used in the incident update operation.
            activity_description: (``ActivityDescription``, gövde) Activity description related
                to the incident update.
            action_to_be_taken: (``ActionToBeTaken``, gövde) Action to be taken value for the
                incident.
            reopen_count: (``ReopenCount``, gövde) Number of times the incident was reopened.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-update
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IncidentNo": incident_no,
                "ParentCategoryName": parent_category_name,
                "SubCategoryName": sub_category_name,
                "ParentProductName": parent_product_name,
                "ProductName": product_name,
                "DemandUnitName": demand_unit_name,
                "AssignmentGroupName": assignment_group_name,
                "AssignmentPerson": assignment_person,
                "StatusName": status_name,
                "OpenPersonName": open_person_name,
                "OpenPersonGroupName": open_person_group_name,
                "OpenPersonParentGroupName": open_person_parent_group_name,
                "OpenDate": open_date,
                "SummaryDescription": summary_description,
                "IncidentDescription": incident_description,
                "CloseDate": close_date,
                "SolutionDescription": solution_description,
                "SolutionType": solution_type,
                "StatusId": status_id,
                "UserName": user_name,
                "ActivityDescription": activity_description,
                "ActionToBeTaken": action_to_be_taken,
                "ReopenCount": reopen_count,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/incident/neova/update",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_optional_field_list(
        self,
        *,
        product_id: int,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Optional Field List.

        ``POST /v1/incident/optionalFieldList``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Returns the list of optional field related to the provided product.

        Args:
            product_id: (``productId``, gövde, zorunlu) Id of the product.

        Yanıt alanları: optionalFieldName, isMandatory

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-optional-field-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "productId": product_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/incident/optionalFieldList",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def kt_incident_product_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Product List.

        ``GET /v1/incident/information/products``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Retrieves the product list used for incident operations. The response includes product
        identifier, related demand unit workgroup, demand unit name, and product path
        information.

        Yanıt alanları: productId, demandUnitWorkgroupId, demandUnitName, productPath

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-product-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/incident/information/products",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def kt_incident_reopen(
        self,
        *,
        incident_id: int | None = None,
        user_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Incident Reopen.

        ``POST /v1/incident/reopen``

        Kapsam: ``incident_operations`` · Akış: client credentials

        Reopens the given incident if the status of the incident permits and the user has a
        right to perform the operation.

        Args:
            incident_id: (``incidentId``, gövde)
            user_name: (``userName``, gövde)

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-reopen
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incidentId": incident_id,
                "userName": user_name,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/incident/reopen",
            scope="incident_operations",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
