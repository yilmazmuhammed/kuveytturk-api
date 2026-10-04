<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.other

Diğer · 9 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`calculate_welcome_participation_account_profit_share`](#calculate_welcome_participation_account_profit_share) | `POST /v1/welcomeprofitsharecalculation` | CC | test edildi | test edilmedi |
| [`credi_tech_intelligence_inquiry_by_credit_allocation_status`](#credi_tech_intelligence_inquiry_by_credit_allocation_status) | `POST /v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber` | CC | test edilmedi | test edilmedi |
| [`credit_tech_pos`](#credit_tech_pos) | `POST /v1/data/credittechpos` | CC | test edilmedi | test edilmedi |
| [`fraud_notifications_exists`](#fraud_notifications_exists) | `POST /v1/inquiry/is-fraud-notification-exists` | CC | test edildi | test edilmedi |
| [`get_fraud_notifications_last_day`](#get_fraud_notifications_last_day) | `POST /v1/inquiry/get-fraud-notifications-daily` | CC | test edildi | test edilmedi |
| [`get_process_design_xml_by_business_process_id`](#get_process_design_xml_by_business_process_id) | `POST /v1/bpm/post/grcprocessdesignxml` | CC | test edildi | test edilmedi |
| [`saglam_pay_get_customer_full_info`](#saglam_pay_get_customer_full_info) | `GET /v1/get-customer-info-by-customerId-full` | CC | test edilmedi | test edilmedi |
| [`visa_payment_status_notification`](#visa_payment_status_notification) | `POST /v1/StatusNotify` | CC | test edilmedi | test edilmedi |
| [`visa_statement_delivery`](#visa_statement_delivery) | `POST /v1/StatementDelivery` | CC | test edilmedi | test edilmedi |

## `calculate_welcome_participation_account_profit_share` { #calculate_welcome_participation_account_profit_share }

**Calculate Welcome Participation Account Profit Share** · `POST /v1/welcomeprofitsharecalculation` · kapsam `public` · client credentials

Calculates the welcome participation account profit share according to the provided product, maturity, currency, deposit amount, currency range, index currency, and FATSI code information. The response includes net and gross profit share rates for the selected term and yearly calculation.

```python
yanit = kt.other.calculate_welcome_participation_account_profit_share(product_code=..., maturity_term=..., fec=..., product_group=..., deposit_amount=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | sunucu hatası — İşleminiz gerçekleştirilemedi. Daha sonra tekrar deneyiniz. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `product_code` | `_productCode` | gövde | metin | evet | Product code used for the welcome profit share calculation. |
| `maturity_term` | `_maturityTerm` | gövde | tam sayı | evet | Maturity term or expiry day used in the calculation. |
| `fec` | `fec` | gövde | tam sayı | evet | Currency type identifier used for the deposit amount. |
| `product_group` | `productGroup` | gövde | tam sayı | evet | Product group identifier used for the calculation. |
| `deposit_amount` | `depositAmount` | gövde | sayı | evet | Deposit amount used in the profit share calculation. |
| `currency_begin` | `CurrencyBegin` | gövde | sayı |  | Beginning currency value used in the calculation. |
| `currency_end` | `CurrencyEnd` | gövde | sayı |  | Ending currency value used in the calculation. |
| `index_fec` | `IndexFec` | gövde | tam sayı |  | Index currency identifier used in the calculation. |
| `fatsi_code` | `FatsiCode` | gövde | tam sayı |  | FATSI code used in the profit share calculation. |

Yanıt alanları (dokümana göre): `NetProfitShare`, `GrossProfitShare`, `NetProfitShareYearly`, `GrossProfitShareYearly`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/calculate-welcome-participation-account-profit-share)

## `credi_tech_intelligence_inquiry_by_credit_allocation_status` { #credi_tech_intelligence_inquiry_by_credit_allocation_status }

**CrediTech Intelligence Inquiry By Credit Allocation Status** · `POST /v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber` · kapsam `loans` · client credentials

Checks the inquiry permission status for the specified Creditecht report number. The response returns the inquiry permission check result for the related report.

```python
yanit = kt.other.credi_tech_intelligence_inquiry_by_credit_allocation_status(creditecht_report_number=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — {'code': 403, 'message': 'Invalid Scope'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `creditecht_report_number` | `creditechtReportNumber` | gövde | tam sayı | evet | Creditecht report number used to check inquiry permission status. |

Yanıt alanları (dokümana göre): `isInquiryPermissionCheck`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/creditech-intelligence-inquiry-by-credit-allocation-status)

## `credit_tech_pos` { #credit_tech_pos }

**CreditTech Pos API** · `POST /v1/data/credittechpos` · kapsam `payments` · client credentials

Retrieves CreditTech POS data for the specified identity number and query period range. The response includes the response date and a list of POS transaction amount records grouped by tax number and period information.

```python
yanit = kt.other.credit_tech_pos(query_begin_period=..., query_end_period=..., identity_number=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `query_begin_period` | `QueryBeginPeriod` | gövde | tam sayı | evet | Start period of the query in YYYYMM format. |
| `query_end_period` | `QueryEndPeriod` | gövde | tam sayı | evet | End period of the query in YYYYMM format. |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number or tax number used to query CreditTech POS data. |

Gövde alanları istekte `input` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `ResponseDate`, `DataContractList`, `LocalAmount`, `QueryBeginPeriod`, `QueryEndPeriod`, `TaxNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/credittech-pos-api)

## `fraud_notifications_exists` { #fraud_notifications_exists }

**Fraud Notifications Exists** · `POST /v1/inquiry/is-fraud-notification-exists` · kapsam `public` · client credentials

Checks whether an active fraud notification record exists for the provided identity number. The response indicates whether a matching fraud notification record was found.

```python
yanit = kt.other.fraud_notifications_exists(identity_number=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: POST and path: /v1/inquiry/is-fraud-notification-exists'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number or tax number used to check whether a fraud notification record exists. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `isExists`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/fraud-notifications-exists)

## `get_fraud_notifications_last_day` { #get_fraud_notifications_last_day }

**Get Fraud Notifications Last Day** · `POST /v1/inquiry/get-fraud-notifications-daily` · kapsam `public` · client credentials

This API retrieves fraud notification records for the last 24 hours based on the given reference date. The response includes corporation and individual fraud notification records.

```python
yanit = kt.other.get_fraud_notifications_last_day(reference_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: POST and path: /v1/inquiry/get-fraud-notifications-daily'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_date` | `referenceDate` | gövde | tarih | evet | Reference date used to retrieve fraud notifications for the last 24 hours. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `corporationRecords`, `blackListCorporationID`, `title`, `taxNumber`, `tradeRegisterNumber`, `customerNumber`, `companyType`, `address`, `city`, `county`, `neighborhood`, `phone`, `inquirySource`, `firstAuthorizedPersonName`, `firstAuthorizedPersonLastName`, `description`, `blackListTypeID`, `userName`, `host_Name`, `dateAdded`, `updateUserName`, `updateHostName`, `dateUpdated`, `status`, `blackListDetailId`, `divitInstanceId`, `isActive`, `senderName`, `attemptDate`, `senderBankCode`, `fraudType`, `individualRecords`, `blackListPersonalID`, `firstName`, `lastName`, `mothersName`, `fathersName`, `identityNumber`, `birthDate`, `birthPlace`, `birthPlaceText`, `jobTitle`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/get-fraud-notifications-last-day)

## `get_process_design_xml_by_business_process_id` { #get_process_design_xml_by_business_process_id }

**Get Process Design Xml By Business Process Id** · `POST /v1/bpm/post/grcprocessdesignxml` · kapsam `public` · client credentials

This API is used to retrieve the process design XML definition for a specified business process. The request includes the business process ID, and the response returns the corresponding BPMN process design XML content.

```python
yanit = kt.other.get_process_design_xml_by_business_process_id(business_process_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — responseValue: 0 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `business_process_id` | `businessProcessId` | gövde | tam sayı | evet | Business process ID for which the process design XML definition will be retrieved. |

Yanıt alanları (dokümana göre): `responseValue`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/get-process-design-xml-by-business-process-id)

## `saglam_pay_get_customer_full_info` { #saglam_pay_get_customer_full_info }

**Saglam Pay Get Customer Full Info** · `GET /v1/get-customer-info-by-customerId-full` · kapsam `public` · client credentials

Retrieves full customer-related account and money transfer information by using the provided customer and account details. The response includes the execution reference identifier and money transfer transaction identifier generated for the operation.

```python
yanit = kt.other.saglam_pay_get_customer_full_info(sender_account_number=..., sender_account_suffix=..., receiver_account_number=..., receiver_account_suffix=..., money_transfer_amount=..., transfer_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_number` | `SenderAccountNumber` | sorgu | tam sayı | evet | Sender customer account number used for the operation. |
| `sender_account_suffix` | `SenderAccountSuffix` | sorgu | tam sayı | evet | Sender account suffix used to identify the source account. |
| `receiver_account_number` | `ReceiverAccountNumber` | sorgu | tam sayı | evet | Receiver account number used to identify the destination account. |
| `receiver_account_suffix` | `ReceiverAccountSuffix` | sorgu | tam sayı | evet | Receiver account suffix used to identify the destination account. |
| `money_transfer_description` | `MoneyTransferDescription` | sorgu | metin |  | Description text for the money transfer transaction. |
| `money_transfer_amount` | `MoneyTransferAmount` | sorgu | sayı | evet | Amount of the money transfer transaction. |
| `transfer_type` | `TransferType` | sorgu | tam sayı | evet | Transfer type information used for the money transfer operation. |

Yanıt alanları (dokümana göre): `ExecutionReferenceId`, `MoneyTransferTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/saglam-pay-get-customer-full-info)

## `visa_payment_status_notification` { #visa_payment_status_notification }

**Visa Payment Status Notification** · `POST /v1/StatusNotify` · kapsam `public` · client credentials

Sends a document for status notification by using the provided document template identifier and Base64 encoded document content. The response returns the generated document operation identifier and operation result.

```python
yanit = kt.other.visa_payment_status_notification(document_template_id=..., doc_base64_content=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `document_template_id` | `DocumentTemplateId` | gövde | tam sayı | evet | Document template identifier used for the status notification document. |
| `doc_base64_content` | `DocBase64Content` | gövde | metin | evet | Base64 encoded content of the document to be sent. |

Gövde alanları istekte `documentApiContract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/visa-payment-status-notification)

## `visa_statement_delivery` { #visa_statement_delivery }

**Visa Statement Delivery** · `POST /v1/StatementDelivery` · kapsam `public` · client credentials

Sends a document for statement delivery by using the provided document template identifier and Base64 encoded document content. The response returns the generated document operation identifier and operation result.

```python
yanit = kt.other.visa_statement_delivery(document_template_id=..., doc_base64_content=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `document_template_id` | `DocumentTemplateId` | gövde | tam sayı | evet | Document template identifier used for the statement delivery document. |
| `doc_base64_content` | `DocBase64Content` | gövde | metin | evet | Base64 encoded content of the document to be sent. |

Gövde alanları istekte `documentApiContract` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/visa-statement-delivery)
