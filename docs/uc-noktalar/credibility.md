<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.credibility

Kredibilite · 5 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`customer_overall_limit_values`](#customer_overall_limit_values) | `POST /v1/Loans/LastAllotmentTopLimit` | CC |
| [`final_credit_decision_recommendation`](#final_credit_decision_recommendation) | `POST /v1/Loans/AllotmentFinalDecision` | CC |
| [`send_invoice_detail_v2`](#send_invoice_detail_v2) | `POST /v2/purchase/invoice` | CC |
| [`tardes_agricultural_score_inquiry`](#tardes_agricultural_score_inquiry) | `POST /v1/inquiry/gettardesscore` | CC |
| [`taxpayer_gib_identity_information`](#taxpayer_gib_identity_information) | `POST /v1/inquiry/gib-tax-payer` | CC |

## `customer_overall_limit_values` { #customer_overall_limit_values }

**Customer Overall Limit Values** · `POST /v1/Loans/LastAllotmentTopLimit` · kapsam `loans` · client credentials

Retrieves the latest allotment top limit information for the specified account number. The response includes customer and group level cash, non-cash, total limit, and risk information.

```python
yanit = kt.credibility.customer_overall_limit_values(account_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_number` | `accountNumber` | gövde | tam sayı | evet | Account number used to retrieve the latest allotment top limit information. |

Yanıt alanları (dokümana göre): `CashLimit`, `NonCashLimit`, `TotalLimit`, `CashRisk`, `NonCashRisk`, `TotalRisk`, `GroupCashLimit`, `GroupNonCashLimit`, `GroupTotalLimit`, `GroupCashRisk`, `GroupNonCashRisk`, `GroupTotalRisk`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credibility/customer-overall-limit-values)

## `final_credit_decision_recommendation` { #final_credit_decision_recommendation }

**Final Credit Decision Recommendation** · `POST /v1/Loans/AllotmentFinalDecision` · kapsam `loans` · client credentials

Retrieves final credit decision recommendation and allotment decision summary information for the provided account number list, group number, and Credere ART report number. The response includes approved limits, product limits, guarantor information, collateral limits, constraints, summary details, other conditions, and approval date.

```python
yanit = kt.credibility.final_credit_decision_recommendation(account_number_list=..., group_number=..., credere_art_report_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_number_list` | `accountNumberList` | gövde | liste | evet | List of account numbers to be included in the allotment final decision inquiry. |
| `group_number` | `groupNumber` | gövde | tam sayı | evet | Group number used to retrieve the allotment decision summary. |
| `credere_art_report_number` | `credereArtReportNumber` | gövde | tam sayı | evet | Credere ART report number associated with the allotment decision. |

Yanıt alanları (dokümana göre): `TopLimitList`, `AllotmentTopLimit`, `customerName`, `approvedCashLimit`, `approvedNonCashLimit`, `totalLimit`, `ProductLimitList`, `allotmentProductLimit`, `productName`, `approvedLimit`, `collateralType`, `collateralRange`, `collateralMargin`, `GuarantorList`, `allotmentGuarantor`, `description`, `OtherConditions`, `textValue`, `CollateralLimitList`, `allotmentCollateralLimit`, `approvedTotalLimit`, `ConstraintList`, `allotmentConstraint`, `name`, `typeName`, `constraintDetail`, `amount`, `SummaryList`, `allotmentSummary`, `allotmentSummaryName`, `previousLimitAmount`, `demandLimitAmount`, `approvedLimitAmount`, `approvedContendLimitAmount`, `systemDemandLimitAmount`, `firmDemandLimit`, `previousMaturity`, `demandMaturity`, `approvedMaturity`, `approvedContentMaturity`, `firmDemandMaturity`, `systemDemandMaturity`, `previousCollateralDescription`, `demandCollateralDescription`, `approvedCollateralDescription`, `approvedContentCollateralDescription`, `firmDemandCollateralDescription`, `systemDemandCollateralDescription`, `ApprovalDate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credibility/final-credit-decision-recommendation)

## `send_invoice_detail_v2` { #send_invoice_detail_v2 }

**Send Invoice Detail V2** · `POST /v2/purchase/invoice` · kapsam `payments` · client credentials

Submits invoice details to the BOA system for delivery records related to the purchase process. The request includes the delivery ID list, invoice serial number, invoice date, document content and document extension. The response returns whether the invoice submission was successful and includes error details if available.

```python
yanit = kt.credibility.send_invoice_detail_v2(delivery_id_list=..., invoice_number_serial=..., invoice_date=..., attachment=..., document_extension=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `delivery_id_list` | `DeliveryIdList` | gövde | liste | evet | List of delivery record IDs to be associated with the invoice. |
| `invoice_number_serial` | `InvoiceNumberSerial` | gövde | metin | evet | Invoice serial and number information. |
| `invoice_date` | `InvoiceDate` | gövde | tarih | evet | Invoice date. |
| `attachment` | `Attachment` | gövde | metin | evet | Content of the invoice document. It is typically sent as base64 encoded document data. |
| `document_extension` | `DocumentExtension` | gövde | metin | evet | File extension of the submitted invoice document. For example: pdf, jpg, png. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credibility/send-invoice-detail-v2)

## `tardes_agricultural_score_inquiry` { #tardes_agricultural_score_inquiry }

**Tardes Agricultural Score Inquiry** · `POST /v1/inquiry/gettardesscore` · kapsam `loans` · client credentials

Retrieves Tardes agricultural score details by using the provided identity number and daily query preference. The response includes Tardes score information and the related score reason details.

```python
yanit = kt.credibility.tardes_agricultural_score_inquiry(identity_number=..., force_daily=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `identityNumber` | gövde | metin | evet | Identity number used to retrieve Tardes agricultural score details. |
| `force_daily` | `forceDaily` | gövde | bool | evet | Indicates whether the score inquiry should be performed as a daily query. |

Yanıt alanları (dokümana göre): `tardesScoreInfo`, `tardesScoreId`, `referenceNumber`, `identityNumber`, `identityType`, `agricultureScore`, `scoreDate`, `exceptionCode`, `exceptionName`, `processStage`, `lastTransactionDate`, `systemDate`, `updateSystemDate`, `resourceCode`, `tardesScoreReasons`, `tardesScoreReasonCodeId`, `reasonCode`, `reasonName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credibility/tardes-agricultural-score-inquiry)

## `taxpayer_gib_identity_information` { #taxpayer_gib_identity_information }

**Taxpayer - GIB Identity Information** · `POST /v1/inquiry/gib-tax-payer` · kapsam `loans` · client credentials

Retrieves taxpayer identity and registration information from GIB by using the provided identity number, online query preference, and resource code. The response includes taxpayer identity, tax office, company, establishment, birth, address, occupation, branch, and activity details.

```python
yanit = kt.credibility.taxpayer_gib_identity_information(identity_number=..., force_online=..., resource_code=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number or tax number used to retrieve taxpayer information. |
| `force_online` | `ForceOnline` | gövde | bool | evet | Indicates whether the inquiry should be performed online instead of using existing cached data. |
| `resource_code` | `ResourceCode` | gövde | metin | evet | Resource code used for the taxpayer inquiry process. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `queryResult`, `errorCodeDescription`, `queryReferenceNumber`, `taxPayerId`, `identityNumber`, `taxNumber`, `taxOfficeCode`, `taxOfficeName`, `title`, `surname`, `name`, `fathersName`, `corporatePersonQualifiedCode`, `corporatePersonQualifiedCodeDescription`, `companyType`, `companyTypeDescription`, `firmStatus`, `firmStatusDescription`, `taxLiabilityBeginDate`, `taxLiabilityEndDate`, `establishmentDate`, `establishmentCityName`, `establishmentCityCode`, `establishmentCountyName`, `establishmentCountyCode`, `birthDate`, `birthCityName`, `birthCityCode`, `birthCountyName`, `birthCountyCode`, `isPotential`, `requestXML`, `responseXML`, `requestDate`, `responseDate`, `taxPayerHomeAddressContract`, `taxPayerWorkAddressContract`, `addressType`, `uAVTNumber`, `town`, `cityName`, `cityCode`, `countyName`, `countyCode`, `village`, `district`, `street`, `outerDoorNumber`, `innerDoorNumber`, `systemDate`, `addressText`, `occupationListInfoContract`, `activityCode`, `activityDescription`, `branchInformationList`, `workStartDate`, `workLeftDate`, `workplaceQualification`, `workplaceType`, `workLeftType`, `transportTaxOfficeCode`, `potential`, `branchName`, `branchNumber`, `taxOffice`, `activityInformationList`, `activityName`, `activityStartDate`, `activityEndDate`, `activityState`, `activityOrder`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credibility/taxpayer-gib-identity-information)
