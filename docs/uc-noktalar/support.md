<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.support

Destek yönetimi · 14 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`kt_incident_activity_type_list`](#kt_incident_activity_type_list) | `GET /v1/incident/activityTypes` | CC | test edilmedi | test edilmedi |
| [`kt_incident_cancel`](#kt_incident_cancel) | `POST /v1/incident/cancel` | CC | test edilmedi | test edilmedi |
| [`kt_incident_creation`](#kt_incident_creation) | `POST /v1/incident/operation/create` | CC | test edilmedi | test edilmedi |
| [`kt_incident_creation_by_company`](#kt_incident_creation_by_company) | `POST /v1/company/incident/create` | CC | test edilmedi | test edilmedi |
| [`kt_incident_defined_document_list`](#kt_incident_defined_document_list) | `GET /v1/incident/defiendDocuments` | CC | test edilmedi | test edilmedi |
| [`kt_incident_info`](#kt_incident_info) | `POST /v1/incident/information/info` | CC | test edilmedi | test edilmedi |
| [`kt_incident_insert_activity`](#kt_incident_insert_activity) | `POST /v1/incident/insertActivity` | CC | test edilmedi | test edilmedi |
| [`kt_incident_insert_document`](#kt_incident_insert_document) | `POST /v1/incident/insertDocument` | CC | test edilmedi | test edilmedi |
| [`kt_incident_neova_info`](#kt_incident_neova_info) | `POST /v1/incident/neova/info` | CC | test edilmedi | test edilmedi |
| [`kt_incident_neova_list`](#kt_incident_neova_list) | `POST /v1/incident/neova/list` | CC | test edilmedi | test edilmedi |
| [`kt_incident_neova_update`](#kt_incident_neova_update) | `POST /v1/incident/neova/update` | CC | test edilmedi | test edilmedi |
| [`kt_incident_optional_field_list`](#kt_incident_optional_field_list) | `POST /v1/incident/optionalFieldList` | CC | test edilmedi | test edilmedi |
| [`kt_incident_product_list`](#kt_incident_product_list) | `GET /v1/incident/information/products` | CC | test edilmedi | test edilmedi |
| [`kt_incident_reopen`](#kt_incident_reopen) | `POST /v1/incident/reopen` | CC | test edilmedi | test edilmedi |

## `kt_incident_activity_type_list` { #kt_incident_activity_type_list }

**KT Incident Activity Type List** · `GET /v1/incident/activityTypes` · kapsam `incident_operations` · client credentials

Returns the list of activity types to be used while inserting an activity.

```python
yanit = kt.support.kt_incident_activity_type_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `activityTypeId`, `activityTypeName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-activity-type-list)

## `kt_incident_cancel` { #kt_incident_cancel }

**KT Incident Cancel** · `POST /v1/incident/cancel` · kapsam `incident_operations` · client credentials

Cancels the given incident if the status of the incident permits and the user has a right to perform the operation.

```python
yanit = kt.support.kt_incident_cancel()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_id` | `incidentId` | gövde | tam sayı |  |  |
| `user_name` | `userName` | gövde | metin |  |  |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-cancel)

## `kt_incident_creation` { #kt_incident_creation }

**KT Incident Creation** · `POST /v1/incident/operation/create` · kapsam `incident_operations` · client credentials

Creates an incident record with the provided summary, description, product, user, BT incident, customer, document, and optional field information. The response returns the created incident identifier and operation result.

```python
yanit = kt.support.kt_incident_creation(summary_description=..., incident_description=..., product_id=..., user_name=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `summary_description` | `summaryDescription` | gövde | metin | evet | Short summary of the incident. |
| `incident_description` | `incidentDescription` | gövde | metin | evet | Detailed description of the incident. |
| `product_id` | `productId` | gövde | tam sayı | evet | Product identifier related to the incident. |
| `user_name` | `userName` | gövde | metin | evet | User name of the person creating or associated with the incident. |
| `bt_incident_id` | `btIncidentId` | gövde | tam sayı |  | BT incident identifier associated with the incident. |
| `customer_id` | `customerId` | gövde | tam sayı |  | Customer identifier related to the incident. |
| `document_list` | `documentList` | gövde | liste |  | List of documents attached to the incident. |
| `optional_field_list` | `optionalFieldList` | gövde | liste |  | List of additional key-value fields related to the incident. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation)

## `kt_incident_creation_by_company` { #kt_incident_creation_by_company }

**KT Incident Creation By Company** · `POST /v1/company/incident/create` · kapsam `incident_operations` · client credentials

Creates a company incident record with the provided incident details, customer information, related reference information, optional documents, and additional optional fields. The response returns the created incident identifier and operation result.

```python
yanit = kt.support.kt_incident_creation_by_company(summary_description=..., incident_description=..., product_id=..., user_name=..., customer_id=..., software_company_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `summary_description` | `summaryDescription` | gövde | metin | evet | Short summary of the incident. |
| `incident_description` | `incidentDescription` | gövde | metin | evet | Detailed description of the incident. |
| `product_id` | `productId` | gövde | tam sayı | evet | Product identifier related to the incident. |
| `user_name` | `userName` | gövde | metin | evet | User name of the person creating or associated with the incident. |
| `customer_id` | `customerId` | gövde | tam sayı | evet | Customer identifier related to the incident. |
| `referance_id` | `referanceId` | gövde | tam sayı |  | Reference identifier associated with the incident. |
| `software_company_id` | `softwareCompanyId` | gövde | tam sayı | evet | Software company identifier associated with the incident. |
| `document_list` | `documentList` | gövde | liste |  | List of documents attached to the incident. |
| `optional_field_list` | `optionalFieldList` | gövde | liste |  | List of additional key-value fields related to the incident. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation-by-company)

## `kt_incident_defined_document_list` { #kt_incident_defined_document_list }

**KT Incident Defined Document List** · `GET /v1/incident/defiendDocuments` · kapsam `incident_operations` · client credentials

Returns the list of defined documents to be used for attaching documents while creating an incident record.

```python
yanit = kt.support.kt_incident_defined_document_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `docId`, `docName`, `isMandatory`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-defined-document-list)

## `kt_incident_info` { #kt_incident_info }

**KT Incident Info** · `POST /v1/incident/information/info` · kapsam `incident_operations` · client credentials

Retrieves detailed incident information by using the provided incident identifier and user name. The response includes incident ownership, assignment, product, status, date, workflow, and solution details.

```python
yanit = kt.support.kt_incident_info(incident_id=..., user_name=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_id` | `incidentId` | gövde | tam sayı | evet | Unique identifier of the incident to be queried. |
| `user_name` | `userName` | gövde | metin | evet | User name of the requester or user associated with the incident query. |

Yanıt alanları (dokümana göre): `userName`, `assignedUserCode`, `demandUnitId`, `summaryDescription`, `incidentDescription`, `productId`, `statusId`, `incidentId`, `incidentNo`, `btIncidentId`, `flowStatusId`, `assignmentGroupId`, `openDate`, `closeDate`, `startDate`, `solutionTypeId`, `solutionMethod`, `solutionDescription`, `divitInstanceId`, `workFlowInstanceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-info)

## `kt_incident_insert_activity` { #kt_incident_insert_activity }

**KT Incident Insert Activity** · `POST /v1/incident/insertActivity` · kapsam `incident_operations` · client credentials

Inserts an activity record for the given incident as the given activity type.

```python
yanit = kt.support.kt_incident_insert_activity(incident_id=..., activity_type_id=..., description=..., send_mail=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_id` | `incidentId` | gövde | tam sayı | evet | ID of the incident to which activity record will be inserted. |
| `activity_type_id` | `activityTypeId` | gövde | tam sayı | evet | Type ID of the activity. Detailed info can be found via KT Incident Activity Type List endpoint. |
| `description` | `description` | gövde | metin | evet | Explanation of the activity. |
| `send_mail` | `sendMail` | gövde | bool | evet | Whether an email about this activity will be sent to the user who creaeted the incident. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-activity)

## `kt_incident_insert_document` { #kt_incident_insert_document }

**KT Incident Insert Document** · `POST /v1/incident/insertDocument` · kapsam `incident_operations` · client credentials

Inserts additional documents into the given incident.

```python
yanit = kt.support.kt_incident_insert_document()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `document_contract` | `documentContract` | gövde | liste |  |  |
| `incident_id` | `incidentId` | gövde | tam sayı |  |  |
| `user_name` | `userName` | gövde | metin |  |  |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-document)

## `kt_incident_neova_info` { #kt_incident_neova_info }

**KT Incident Neova Info** · `POST /v1/incident/neova/info` · kapsam `incident_operations` · client credentials

Retrieves detailed Neova incident information by using the provided incident number. The response includes incident status, assignment, description, solution, product, creator user, history, activity, document, and optional field details.

```python
yanit = kt.support.kt_incident_neova_info(incident_no=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_no` | `incidentNo` | gövde | metin | evet | Incident number used to retrieve Neova incident details. |

Yanıt alanları (dokümana göre): `incidentId`, `incidentNo`, `statusId`, `assignmentGroupName`, `assignedUserCode`, `assignedUserName`, `summaryDescription`, `incidentDescription`, `solutionDescription`, `userName`, `optionalFieldList`, `key`, `product`, `productCode`, `productName`, `parentCategoryCode`, `demandUnitName`, `creatorUserInfo`, `userId`, `userCode`, `firstName`, `lastName`, `email`, `organizationName`, `incidentHistoryList`, `fieldName`, `previous`, `current`, `systemDate`, `activityList`, `activityDescription`, `description`, `documentList`, `docId`, `documentName`, `fileExtension`, `fileContent`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-info)

## `kt_incident_neova_list` { #kt_incident_neova_list }

**KT Incident Neova List** · `POST /v1/incident/neova/list` · kapsam `incident_operations` · client credentials

Retrieves the Neova incident list according to the provided filter criteria. The request can include incident, category, product, demand unit, assignment, status, opening, solution, activity, action, and reopen count information. The response returns matching incident records with their category, product, assignment, status, date, description, solution, and reopen count details.

```python
yanit = kt.support.kt_incident_neova_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_no` | `IncidentNo` | gövde | metin |  | Incident number used to filter the incident list. |
| `parent_category_name` | `ParentCategoryName` | gövde | metin |  | Parent category name used to filter incidents. |
| `sub_category_name` | `SubCategoryName` | gövde | metin |  | Subcategory name used to filter incidents. |
| `parent_product_name` | `ParentProductName` | gövde | metin |  | Parent product name used to filter incidents. |
| `product_name` | `ProductName` | gövde | metin |  | Product name used to filter incidents. |
| `demand_unit_name` | `DemandUnitName` | gövde | metin |  | Demand unit name used to filter incidents. |
| `assignment_group_name` | `AssignmentGroupName` | gövde | metin |  | Assignment group name used to filter incidents. |
| `assignment_person` | `AssignmentPerson` | gövde | metin |  | Assigned person information used to filter incidents. |
| `status_name` | `StatusName` | gövde | metin |  | Status name used to filter incidents. |
| `open_person_name` | `OpenPersonName` | gövde | metin |  | Name of the user who opened the incident. |
| `open_person_group_name` | `OpenPersonGroupName` | gövde | metin |  | Group name of the user who opened the incident. |
| `open_person_parent_group_name` | `OpenPersonParentGroupName` | gövde | metin |  | Parent group name of the user who opened the incident. |
| `open_date` | `OpenDate` | gövde | tarih |  | Opening date used to filter incidents. |
| `summary_description` | `SummaryDescription` | gövde | metin |  | Summary description used to filter incidents. |
| `incident_description` | `IncidentDescription` | gövde | metin |  | Incident description used to filter incidents. |
| `close_date` | `CloseDate` | gövde | tarih |  | Closing date used to filter incidents. |
| `solution_description` | `SolutionDescription` | gövde | metin |  | Solution description used to filter incidents. |
| `solution_type` | `SolutionType` | gövde | metin |  | Solution type used to filter incidents. |
| `status_id` | `StatusId` | gövde | metin |  | Status identifier used to filter incidents. |
| `user_name` | `UserName` | gövde | metin |  | User name used in the incident list query. |
| `activity_description` | `ActivityDescription` | gövde | metin |  | Activity description used to filter incidents. |
| `action_to_be_taken` | `ActionToBeTaken` | gövde | tam sayı |  | Action to be taken value used to filter incidents. |
| `reopen_count` | `ReopenCount` | gövde | tam sayı |  | Reopen count used to filter incidents. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `IncidentNo`, `ParentCategoryName`, `SubCategoryName`, `ParentProductName`, `ProductName`, `DemandUnitName`, `AssignmentGroupName`, `AssignmentPerson`, `StatusName`, `OpenPersonName`, `OpenPersonGroupName`, `OpenPersonParentGroupName`, `OpenDate`, `SummaryDescription`, `IncidentDescription`, `CloseDate`, `SolutionDescription`, `SolutionType`, `ReopenCount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-list)

## `kt_incident_neova_update` { #kt_incident_neova_update }

**KT Incident Neova Update** · `POST /v1/incident/neova/update` · kapsam `incident_operations` · client credentials

Updates Neova incident information according to the provided incident, category, product, demand unit, assignment, status, opening, solution, activity, action, and reopen count details. The response indicates whether the update operation was completed successfully.

```python
yanit = kt.support.kt_incident_neova_update(incident_no=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_no` | `IncidentNo` | gövde | metin | evet | Incident number of the record to be updated. |
| `parent_category_name` | `ParentCategoryName` | gövde | metin |  | Parent category name of the incident. |
| `sub_category_name` | `SubCategoryName` | gövde | metin |  | Subcategory name of the incident. |
| `parent_product_name` | `ParentProductName` | gövde | metin |  | Parent product name related to the incident. |
| `product_name` | `ProductName` | gövde | metin |  | Product name related to the incident. |
| `demand_unit_name` | `DemandUnitName` | gövde | metin |  | Demand unit name related to the incident. |
| `assignment_group_name` | `AssignmentGroupName` | gövde | metin |  | Assignment group name responsible for the incident. |
| `assignment_person` | `AssignmentPerson` | gövde | metin |  | Assigned person information of the incident. |
| `status_name` | `StatusName` | gövde | metin |  | Status name of the incident. |
| `open_person_name` | `OpenPersonName` | gövde | metin |  | Name of the user who opened the incident. |
| `open_person_group_name` | `OpenPersonGroupName` | gövde | metin |  | Group name of the user who opened the incident. |
| `open_person_parent_group_name` | `OpenPersonParentGroupName` | gövde | metin |  | Parent group name of the user who opened the incident. |
| `open_date` | `OpenDate` | gövde | tarih |  | Date and time when the incident was opened. |
| `summary_description` | `SummaryDescription` | gövde | metin |  | Short summary description of the incident. |
| `incident_description` | `IncidentDescription` | gövde | metin |  | Detailed description of the incident. |
| `close_date` | `CloseDate` | gövde | tarih |  | Date and time when the incident was closed. |
| `solution_description` | `SolutionDescription` | gövde | metin |  | Description of the solution applied to the incident. |
| `solution_type` | `SolutionType` | gövde | metin |  | Solution type applied to the incident. |
| `status_id` | `StatusId` | gövde | metin |  | Status identifier of the incident. |
| `user_name` | `UserName` | gövde | metin |  | User name used in the incident update operation. |
| `activity_description` | `ActivityDescription` | gövde | metin |  | Activity description related to the incident update. |
| `action_to_be_taken` | `ActionToBeTaken` | gövde | tam sayı |  | Action to be taken value for the incident. |
| `reopen_count` | `ReopenCount` | gövde | tam sayı |  | Number of times the incident was reopened. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-update)

## `kt_incident_optional_field_list` { #kt_incident_optional_field_list }

**KT Incident Optional Field List** · `POST /v1/incident/optionalFieldList` · kapsam `incident_operations` · client credentials

Returns the list of optional field related to the provided product.

```python
yanit = kt.support.kt_incident_optional_field_list(product_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `product_id` | `productId` | gövde | tam sayı | evet | Id of the product. |

Yanıt alanları (dokümana göre): `optionalFieldName`, `isMandatory`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-optional-field-list)

## `kt_incident_product_list` { #kt_incident_product_list }

**KT Incident Product List** · `GET /v1/incident/information/products` · kapsam `incident_operations` · client credentials

Retrieves the product list used for incident operations. The response includes product identifier, related demand unit workgroup, demand unit name, and product path information.

```python
yanit = kt.support.kt_incident_product_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: incident_operations | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `productId`, `demandUnitWorkgroupId`, `demandUnitName`, `productPath`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-product-list)

## `kt_incident_reopen` { #kt_incident_reopen }

**KT Incident Reopen** · `POST /v1/incident/reopen` · kapsam `incident_operations` · client credentials

Reopens the given incident if the status of the incident permits and the user has a right to perform the operation.

```python
yanit = kt.support.kt_incident_reopen()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incident_id` | `incidentId` | gövde | tam sayı |  |  |
| `user_name` | `userName` | gövde | metin |  |  |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-reopen)
