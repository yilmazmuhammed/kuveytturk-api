<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.payments

Ödemeler · 15 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`account_validation_by_account_number_for_group_money_transfer`](#account_validation_by_account_number_for_group_money_transfer) | `POST /v1/groupmoneytransfer/accountvalidation` | CC | test edilmedi | test edilmedi |
| [`account_validation_by_iban_for_group_money_transfer`](#account_validation_by_iban_for_group_money_transfer) | `POST /v1/groupmoneytransfer/account` | CC | test edilmedi | test edilmedi |
| [`account_validation_by_iban_for_group_money_transfer_v2`](#account_validation_by_iban_for_group_money_transfer_v2) | `POST /v2/groupmoneytransfer/account` | CC | test edilmedi | test edilmedi |
| [`cancel_money_transfers_from_kt_bank_to_kuveyt_turk`](#cancel_money_transfers_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/cancellist` | CC | test edilmedi | test edilmedi |
| [`check_money_transfers_status_from_kt_bank_to_kuveyt_turk`](#check_money_transfers_status_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist` | AC | test edilmedi | test edilmedi |
| [`do_stamp_duty_tax_payment_offline`](#do_stamp_duty_tax_payment_offline) | `POST /v1/tax/do-stamp-duty-tax-payment-offline` | CC | test edilmedi | test edilmedi |
| [`insert_money_transfers_from_kt_bank_to_kuveyt_turk`](#insert_money_transfers_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/insertlist` | CC | test edilmedi | test edilmedi |
| [`invoice_company_list`](#invoice_company_list) | `GET /v1/invoices/companies` | AC | test edilmedi | test edilmedi |
| [`kt_bank_error_message_list`](#kt_bank_error_message_list) | `GET /v1/groupmoneytransfer/errormessagelist` | CC | test edilmedi | test edilmedi |
| [`kuveyt_turk_branch_list_for_group_money_transfer`](#kuveyt_turk_branch_list_for_group_money_transfer) | `GET /v1/groupmoneytransfer/branchlist` | CC | test edilmedi | test edilmedi |
| [`return_money_transfers_from_kt_bank_to_kuveyt_turk`](#return_money_transfers_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/returnlist` | CC | test edilmedi | test edilmedi |
| [`send_multiple_invoice_v2`](#send_multiple_invoice_v2) | `POST /v2/purchase/multipleinvoice` | CC | test edilmedi | test edilmedi |
| [`send_offer_vendor_detail`](#send_offer_vendor_detail) | `POST /v1/purchase/offervendor` | CC | test edilmedi | test edilmedi |
| [`send_order_distribution_detail`](#send_order_distribution_detail) | `POST /v1/purchase/orderdistribution` | CC | test edilmedi | test edilmedi |
| [`send_order_distribution_detail_v2`](#send_order_distribution_detail_v2) | `POST /v3/purchase/orderdistribution` | CC | test edilmedi | test edilmedi |

## `account_validation_by_account_number_for_group_money_transfer` { #account_validation_by_account_number_for_group_money_transfer }

**Account Validation By Account Number For Group Money Transfer** · `POST /v1/groupmoneytransfer/accountvalidation` · kapsam `intrabank_money_transfers` · client credentials

Validates a list of recipient accounts by account number and account suffix for group money transfer operations. The response returns validation results for each submitted account, including the reference number, message code, message detail, and customer name information.

```python
yanit = kt.payments.account_validation_by_account_number_for_group_money_transfer(account_list_to_validate=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: intrabank_money_transfers | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_list_to_validate` | `accountListToValidate` | gövde | liste | evet | List of account records to be validated by account number and account suffix. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`, `CustomerName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-account-number-for-group-money-transfer)

## `account_validation_by_iban_for_group_money_transfer` { #account_validation_by_iban_for_group_money_transfer }

**Account Validation By Iban For Group Money Transfer** · `POST /v1/groupmoneytransfer/account` · kapsam `intrabank_money_transfers` · client credentials

Validates a list of recipient accounts by IBAN for group money transfer operations. The response returns validation results for each submitted account, including the reference number, message code, message detail, and customer name information.

```python
yanit = kt.payments.account_validation_by_iban_for_group_money_transfer(account_list_to_validate=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: intrabank_money_transfers | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_list_to_validate` | `accountListToValidate` | gövde | liste | evet | List of account records to be validated by IBAN. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`, `CustomerName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer)

## `account_validation_by_iban_for_group_money_transfer_v2` { #account_validation_by_iban_for_group_money_transfer_v2 }

**Account Validation By Iban For Group Money Transfer V2** · `POST /v2/groupmoneytransfer/account` · kapsam `intrabank_money_transfers` · client credentials

This endpoint is used to validate a list of receiver accounts by IBAN for group money transfer operations. The request includes the reference number, receiver name, IBAN, and currency code for each account to be validated. The response returns validation results for each submitted account, including message details and customer name information when available.

```python
yanit = kt.payments.account_validation_by_iban_for_group_money_transfer_v2(account_list_to_validate=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: intrabank_money_transfers | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_list_to_validate` | `accountListToValidate` | gövde | liste | evet | List of accounts to be validated by IBAN. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`, `CustomerName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer-v2)

## `cancel_money_transfers_from_kt_bank_to_kuveyt_turk` { #cancel_money_transfers_from_kt_bank_to_kuveyt_turk }

**Cancel Money Transfers From KTBank To Kuveyt Turk** · `POST /v1/groupmoneytransfer/incomingtransfer/cancellist` · kapsam `intrabank_money_transfers` · client credentials

Cancels a list of incoming transfer records for group money transfer operations. The response returns cancellation results for each submitted transfer, including the reference number, message code, and message detail information.

```python
yanit = kt.payments.cancel_money_transfers_from_kt_bank_to_kuveyt_turk(incoming_transfer_list_to_cancel=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incoming_transfer_list_to_cancel` | `incomingTransferListToCancel` | gövde | liste | evet | List of incoming transfer records to be cancelled. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/cancel-money-transfers-from-ktbank-to-kuveyt-turk)

## `check_money_transfers_status_from_kt_bank_to_kuveyt_turk` { #check_money_transfers_status_from_kt_bank_to_kuveyt_turk }

**Check Money Transfers Status From KTBank to KuveytTurk** · `POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist` · kapsam `intrabank_money_transfers` · authorization code (müşteri girişi gerekir)

Checks the status of incoming transfer records for group money transfer operations by using the provided reference number list. The response returns status information for each submitted reference number, including message code, message detail, and transaction status.

```python
yanit = kt.payments.check_money_transfers_status_from_kt_bank_to_kuveyt_turk(reference_number_list=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_number_list` | `referenceNumberList` | gövde | liste | evet | List of reference numbers to be checked for incoming transfer status. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`, `TransactionStatus`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/check-money-transfers-status-from-ktbank-to-kuveytturk)

## `do_stamp_duty_tax_payment_offline` { #do_stamp_duty_tax_payment_offline }

**Do Stamp Duty Tax Payment Offline** · `POST /v1/tax/do-stamp-duty-tax-payment-offline` · kapsam `payments` · client credentials

Performs an offline stamp duty tax payment according to the provided taxpayer, payment, account, tax office, debit, accrual, vehicle, ATM amount, and reference information. The response includes payment, tax, amount, branch, channel, business key, taxpayer, transaction date, payer, corporation, and transaction reference details.

```python
yanit = kt.payments.do_stamp_duty_tax_payment_offline(contract=..., resource_code=..., main_debit_contract=..., tax_code=..., installment_number=..., tax_amount=..., total_amount=..., due_date=..., amount=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `contract` | `contract` | gövde | nesne | evet | Contains the offline stamp duty tax payment request details. |
| `resource_code` | `resourceCode` | gövde | metin | evet | Resource code used for the tax payment operation. |
| `do_notification` | `doNotification` | gövde | bool |  | Indicates whether notification should be sent after the payment. |
| `main_debit_contract` | `MainDebitContract` | gövde | nesne | evet | Contains main debit details of the tax payment. |
| `tax_code` | `TaxCode` | gövde | metin | evet | Tax code of the main debit record. |
| `installment_number` | `InstallmentNumber` | gövde | tam sayı | evet | Installment number of the tax payment. |
| `tax_amount` | `TaxAmount` | gövde | sayı | evet | Main tax amount. |
| `sub_tax_amount` | `SubTaxAmount` | gövde | sayı |  | Sub tax amount. |
| `total_amount` | `TotalAmount` | gövde | sayı | evet | Total payment amount. |
| `due_date` | `DueDate` | gövde | tarih | evet | Due date of the tax payment. |
| `debit_contract_list` | `DebitContractList` | gövde | liste |  | List of debit details related to the main debit record. |
| `opsatir_o_id` | `OpsatirOId` | gövde | metin |  | OPSATIR object identifier of the debit detail. |
| `opsh_o_id` | `OpshOId` | gövde | metin |  | OPSH object identifier of the debit detail. |
| `table_type` | `TableType` | gövde | tam sayı |  | Table type of the debit detail. |
| `serial_and_order_number` | `SerialAndOrderNumber` | gövde | metin |  | Serial and order number of the debit detail. |
| `sub_tax_code` | `SubTaxCode` | gövde | metin |  | Sub tax code of the debit detail. |
| `amount` | `Amount` | gövde | sayı | evet | Amount of the debit detail. |
| `description` | `Description` | gövde | metin |  | Description of the debit detail. |
| `discount_amount` | `DiscountAmount` | gövde | sayı |  | Discount amount of the debit detail. |
| `total_discount_amount` | `TotalDiscountAmount` | gövde | sayı |  | Total discount amount of the main debit record. |
| `service_call_id` | `ServiceCallId` | gövde | tam sayı |  | Service call identifier related to the tax inquiry or payment. |
| `early_payment_state` | `EarlyPaymentState` | gövde | bool |  | Indicates whether early payment status applies. |
| `late_state` | `LateState` | gövde | bool |  | Indicates whether late payment status applies. |
| `valid_installment` | `ValidInstallment` | gövde | bool |  | Indicates whether the installment is valid for payment. |
| `begin_installment_date` | `BeginInstallmentDate` | gövde | tarih |  | Begin date of the installment period. |
| `end_installment_date` | `EndInstallmentDate` | gövde | tarih |  | End date of the installment period. |
| `accrual_number` | `AccrualNumber` | gövde | metin |  | Accrual number of the tax payment. |
| `name` | `Name` | gövde | metin |  | Name related to the tax record. |
| `tax_price_id` | `TaxPriceId` | gövde | tam sayı |  | Tax price identifier. |

Yanıt alanları (dokümana göre): `installmentNumber`, `paymentId`, `taxCode`, `taxOfficeCode`, `period`, `year`, `serialNumber`, `orderNumber`, `paymentType`, `amount`, `branchId`, `channelId`, `businessKey`, `taxNumber`, `isOnlinePayment`, `transactionDate`, `firstName`, `lastName`, `corporationName`, `transactionReference`, `errors`, `message`, `code`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/do-stamp-duty-tax-payment-offline)

## `insert_money_transfers_from_kt_bank_to_kuveyt_turk` { #insert_money_transfers_from_kt_bank_to_kuveyt_turk }

**Insert Money Transfers From KT Bank To Kuveyt Turk** · `POST /v1/groupmoneytransfer/incomingtransfer/insertlist` · kapsam `intrabank_money_transfers` · client credentials

Creates a list of incoming transfer records for group money transfer operations. The request includes sender, receiver, account, branch, transaction, amount, currency, reference, and description information. The response returns the processing result for each submitted transfer, including the reference number, message code, and message detail.

```python
yanit = kt.payments.insert_money_transfers_from_kt_bank_to_kuveyt_turk(incoming_transfer_list=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incoming_transfer_list` | `incomingTransferList` | gövde | liste | evet | List of incoming transfer records to be created. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/insert-money-transfers-from-kt-bank-to-kuveyt-turk)

## `invoice_company_list` { #invoice_company_list }

**Invoice Company List** · `GET /v1/invoices/companies` · kapsam `payments` · authorization code (müşteri girişi gerekir)

&lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and response models may change over time. &lt;/div&gt; Retrieves all companies where bill payment can be made.

```python
yanit = kt.payments.invoice_company_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `companyList`, `description`, `name`, `companyId`, `fullName`, `companyDebtDetails`, `debtTypeId`, `installmentNumberName`, `installmentNumberDescription`, `installmentNumberLength`, `corporationType`, `corporationTypeInt`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/invoice-company-list)

## `kt_bank_error_message_list` { #kt_bank_error_message_list }

**KT Bank Error Message List** · `GET /v1/groupmoneytransfer/errormessagelist` · kapsam `intrabank_money_transfers` · client credentials

Retrieves the error message list used in group money transfer operations. The list can be filtered by message code. The response includes message type, message code, and message description information.

```python
yanit = kt.payments.kt_bank_error_message_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: intrabank_money_transfers | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `message_code` | `messageCode` | sorgu | metin |  | Message code used to filter the error message list. |

Yanıt alanları (dokümana göre): `MessageType`, `MessageCode`, `MessageDescription`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/kt-bank-error-message-list)

## `kuveyt_turk_branch_list_for_group_money_transfer` { #kuveyt_turk_branch_list_for_group_money_transfer }

**Kuveyt Turk Branch List For Group Money Transfer** · `GET /v1/groupmoneytransfer/branchlist` · kapsam `intrabank_money_transfers` · client credentials

Retrieves the branch list for group money transfer operations according to the provided branch, city, and county filter criteria. The response includes branch identity, location, contact, transaction date, and active status information.

```python
yanit = kt.payments.kuveyt_turk_branch_list_for_group_money_transfer()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: intrabank_money_transfers | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `branch_id` | `branchId` | sorgu | tam sayı |  | Branch identifier used to filter the branch list. |
| `branch_name` | `branchName` | sorgu | metin |  | Branch name used to filter the branch list. |
| `city_id` | `cityId` | sorgu | tam sayı |  | City identifier used to filter branches by city. |
| `city_name` | `cityName` | sorgu | metin |  | City name used to filter branches by city. |
| `county_id` | `countyId` | sorgu | tam sayı |  | County identifier used to filter branches by county. |
| `county_name` | `countyName` | sorgu | metin |  | County name used to filter branches by county. |

Yanıt alanları (dokümana göre): `BranchId`, `BranchName`, `CityId`, `CityName`, `CountyId`, `CountyName`, `BranchAddress`, `PhoneNumber`, `Email`, `FirstTransactionDate`, `IsActive`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/kuveyt-turk-branch-list-for-group-money-transfer)

## `return_money_transfers_from_kt_bank_to_kuveyt_turk` { #return_money_transfers_from_kt_bank_to_kuveyt_turk }

**Return Money Transfers From KTBank To Kuveyt Turk** · `POST /v1/groupmoneytransfer/incomingtransfer/returnlist` · kapsam `intrabank_money_transfers` · client credentials

Returns a list of incoming transfer records for group money transfer operations. The request includes the reference number and return description for each incoming transfer. The response returns the processing result for each submitted transfer, including the reference number, message code, and message detail.

```python
yanit = kt.payments.return_money_transfers_from_kt_bank_to_kuveyt_turk(incoming_transfer_list_to_return=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `incoming_transfer_list_to_return` | `incomingTransferListToReturn` | gövde | liste | evet | List of incoming transfer records to be returned. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `MessageCode`, `MessageDetail`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/return-money-transfers-from-ktbank-to-kuveyt-turk)

## `send_multiple_invoice_v2` { #send_multiple_invoice_v2 }

**Send Multiple Invoice V2** · `POST /v2/purchase/multipleinvoice` · kapsam `payments` · client credentials

Submits invoice details to the BOA system for multiple delivery records related to the purchase process. The request includes the delivery ID list, invoice serial number, invoice date, document content and document extension. The response returns whether the multiple invoice submission was successful and includes error details if available.

```python
yanit = kt.payments.send_multiple_invoice_v2(delivery_id_list=..., invoice_number_serial=..., invoice_date=..., attachment=..., document_extension=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `delivery_id_list` | `DeliveryIdList` | gövde | liste | evet | List of delivery record IDs to be associated with the invoice. |
| `invoice_number_serial` | `InvoiceNumberSerial` | gövde | metin | evet | Invoice serial and number information. |
| `invoice_date` | `InvoiceDate` | gövde | tarih | evet | Invoice date. |
| `attachment` | `Attachment` | gövde | metin | evet | Content of the invoice document. It is typically sent as base64 encoded document data. |
| `document_extension` | `DocumentExtension` | gövde | metin | evet | File extension of the submitted invoice document. For example: pdf, jpg, png. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/send-multiple-invoice-v2)

## `send_offer_vendor_detail` { #send_offer_vendor_detail }

**Send Offer Vendor Detail** · `POST /v1/purchase/offervendor` · kapsam `payments` · client credentials

This API endpoint is called to send the vendor information, price fields used in the purchase offer system.

```python
yanit = kt.payments.send_offer_vendor_detail(contract_list=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `contract_list` | `contractList` | gövde | nesne | evet | Offer detail object |
| `attachment` | `Attachment` | gövde | metin |  | Attachment base64 string. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/send-offer-vendor-detail)

## `send_order_distribution_detail` { #send_order_distribution_detail }

**Send Order Distribution Detail** · `POST /v1/purchase/orderdistribution` · kapsam `payments` · client credentials

This API endpoint is called to send the distribution details used in the purchase order system.

```python
yanit = kt.payments.send_order_distribution_detail()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `distribution_list` | `distributionList` | gövde | nesne |  | Order a distribution object. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail)

## `send_order_distribution_detail_v2` { #send_order_distribution_detail_v2 }

**Send Order Distribution Detail V2** · `POST /v3/purchase/orderdistribution` · kapsam `payments` · client credentials

This API endpoint is called to send the distribution details used in the purchase order system.

```python
yanit = kt.payments.send_order_distribution_detail_v2()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail-v2)
