<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.cash_management

Nakit yönetimi · 17 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`cheque_information_micro`](#cheque_information_micro) | `POST /v1/cheque-information-micro` | CC |
| [`digital_banking_payment`](#digital_banking_payment) | `POST /v1/vpos/digitalPayment` | CC |
| [`digital_banking_refund`](#digital_banking_refund) | `POST /v1/vpos/digitalPaymentRefund` | CC |
| [`digital_banking_transaction_status`](#digital_banking_transaction_status) | `POST /v1/vpos/digitalPaymentStatus` | CC |
| [`school_installment_payment_system_active_registration_inquiry`](#school_installment_payment_system_active_registration_inquiry) | `POST /v1/school-installment/registration-inquiry` | CC |
| [`school_installment_system_registration_and_installment_cancellation`](#school_installment_system_registration_and_installment_cancellation) | `POST /v1/school-installment/cancelation` | CC |
| [`school_installment_system_school_guaranteed_registration_payment`](#school_installment_system_school_guaranteed_registration_payment) | `POST /v1/school-installment/transaction-information` | CC |
| [`supplier_financing_buyer_order_confirmation`](#supplier_financing_buyer_order_confirmation) | `POST /v1/supplierfinance/approvefrompurchaserer` | CC |
| [`supplier_financing_buyer_order_listing`](#supplier_financing_buyer_order_listing) | `POST /v1/supplierfinance/getorderbypurchaser` | CC |
| [`supplier_financing_invoice_cancellation`](#supplier_financing_invoice_cancellation) | `POST /v1/supplychainfinance/cancelinvoice` | CC |
| [`supplier_financing_order_last_approval_by_supplier`](#supplier_financing_order_last_approval_by_supplier) | `POST /v1/supplierfinance/lastapprovefromsupplier` | CC |
| [`supplier_financing_repayment_plan_calculation`](#supplier_financing_repayment_plan_calculation) | `POST /v1/supplierfinance/getpaybackplan` | CC |
| [`supplier_financing_vendor_company_invoice_approval`](#supplier_financing_vendor_company_invoice_approval) | `POST /v1/supplychainfinance/supplierapproveinvoice` | CC |
| [`supplier_financing_vendor_invoice_listing`](#supplier_financing_vendor_invoice_listing) | `POST /v1/supplychainfinance/supplierinvoicelist` | CC |
| [`supplier_financing_vendor_order_cancellation`](#supplier_financing_vendor_order_cancellation) | `POST /v1/supplierfinance/cancelFromSupplier` | CC |
| [`supplier_financing_vendor_order_confirmation`](#supplier_financing_vendor_order_confirmation) | `POST /v1/supplierfinance/lastapprovefromsupplierer` | CC |
| [`supplier_financing_vendor_order_initiation`](#supplier_financing_vendor_order_initiation) | `POST /supplierfinance/saveordersupplier` | CC |

## `cheque_information_micro` { #cheque_information_micro }

**cheque-information-micro** · `POST /v1/cheque-information-micro` · kapsam `public` · client credentials

It is an API that provides the necessary data for customers to view information about checks they are owed or owed.

```python
yanit = kt.cash_management.cheque_information_micro()
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `state` | `state` | gövde | metin |  |  |
| `status` | `status` | gövde | metin |  |  |
| `currency` | `currency` | gövde | metin |  |  |
| `start_date` | `startDate` | gövde | metin |  |  |
| `finish_date` | `finishDate` | gövde | metin |  |  |
| `language_id` | `languageId` | gövde | tam sayı |  |  |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/cheque-information-micro)

## `digital_banking_payment` { #digital_banking_payment }

**Digital Banking Payment** · `POST /v1/vpos/digitalPayment` · kapsam `digital_payments` · client credentials

Collects the payment information from the customer's profile provided in the parameters.

```python
yanit = kt.cash_management.digital_banking_payment(transaction_id=..., merchant_id=..., soft_descriptor=..., product_type=..., cost_amount=..., comission_amount=..., amount=..., transaction_currency=..., token_interval=..., payment_method=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_id` | `TransactionId` | gövde | metin | evet | Processing of a singular number. |
| `merchant_id` | `MerchantId` | gövde | metin | evet | Company code defined by the Bank |
| `soft_descriptor` | `SoftDescriptor` | gövde | metin | evet | Merchant processing token. |
| `product_type` | `ProductType` | gövde | metin | evet | Calculated costs and commission types of payment |
| `cost_amount` | `CostAmount` | gövde | sayı | evet | Transaction fees received from customers |
| `comission_amount` | `ComissionAmount` | gövde | sayı | evet | A commission fee will be taken from the workplace. |
| `amount` | `Amount` | gövde | sayı | evet | Transaction amount |
| `transaction_currency` | `TransactionCurrency` | gövde | tam sayı | evet | Transaction currency |
| `token_interval` | `TokenInterval` | gövde | tam sayı | evet | Token claimed in minutes validity period |
| `success_redirect_url` | `SuccessRedirectUrl` | gövde | metin |  | Customer redirects address for success by banking |
| `fail_redirect_url` | `FailRedirectUrl` | gövde | metin |  | Customer redirect address for fail by banking |
| `payment_method` | `PaymentMethod` | gövde | metin | evet | Payment method is information |
| `os` | `OS` | gövde | metin |  | Operating system info of the mobile application. |
| `product_type_condition` | `ProductTypeCondition` | gövde | metin |  | Calculated cost and commission information for different product type |
| `pan` | `Pan` | gövde | metin |  | The process, which indicates that the customer information |

Gövde alanları istekte `DigitalPaymentTransactionContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `AccessToken`, `TokenExpireDate`, `ReturnCode`, `ReturnMessage`, `ApplicationName`, `ApplicationParameter`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/digital-banking-payment)

## `digital_banking_refund` { #digital_banking_refund }

**Digital Banking Refund** · `POST /v1/vpos/digitalPaymentRefund` · kapsam `digital_payments` · client credentials

Does a refund or a partial refund on the transactions made during the previous day.

```python
yanit = kt.cash_management.digital_banking_refund(transaction_id=..., org_transaction_id=..., amount=..., currency=..., comission_amount=..., description=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_id` | `TransactionId` | gövde | metin | evet | The singular transaction number of the return transaction |
| `org_transaction_id` | `OrgTransactionId` | gövde | metin | evet | The unique transaction number of the original transaction returned by ComPay to the bank |
| `amount` | `Amount` | gövde | sayı | evet | The amount of information to be returned |
| `currency` | `Currency` | gövde | metin | evet | Transaction currency |
| `comission_amount` | `ComissionAmount` | gövde | sayı | evet | Amount of commission to be taken from the workplace for the return transaction. |
| `description` | `Description` | gövde | metin | evet | Transaction description |

Gövde alanları istekte `DigitalPaymentRefundTransactionContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `ReturnCode`, `ReturnMessage`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/digital-banking-refund)

## `digital_banking_transaction_status` { #digital_banking_transaction_status }

**Digital Banking Transaction Status** · `POST /v1/vpos/digitalPaymentStatus` · kapsam `digital_payments` · client credentials

Returns the status of the transaction provided in the parameters.

```python
yanit = kt.cash_management.digital_banking_transaction_status(transaction_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_id` | `TransactionId` | gövde | metin | evet | The singular transaction number of the transaction |

Gövde alanları istekte `DigitalPaymentStatContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `ReturnCode`, `ReturnMessage`, `DiscountedAmount`, `ProductType`, `CostAmount`, `ComissionAmount`, `Amount`, `TransactionType`, `TransactionId`, `OrgTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/digital-banking-transaction-status)

## `school_installment_payment_system_active_registration_inquiry` { #school_installment_payment_system_active_registration_inquiry }

**School Installment Payment System Active Registration Inquiry API** · `POST /v1/school-installment/registration-inquiry` · kapsam `loans` · client credentials

Institutions could check through this API using the Turkish National Identity Number (TCKN) to determine if a student currently has an OTS registration. OTS registration is considered "Yes" or "No" as follows: - Canceled registration = "No" - All installments collected without credit = "No" - All installments collected, including some with credit = "Yes" - If there are installments pending payment = "Yes" * As long as any payment (credit or cash) is pending, OTS is considered to exist.

```python
yanit = kt.cash_management.school_installment_payment_system_active_registration_inquiry(identity_number=..., client_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Öğrenci TCKN bilgisi |
| `client_id` | `ClientId` | gövde | metin | evet | Kurum token bilgisi |

Gövde alanları istekte `payment` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-payment-system-active-registration-inquiry-api)

## `school_installment_system_registration_and_installment_cancellation` { #school_installment_system_registration_and_installment_cancellation }

**School Installment System Registration and Installment Cancellation API** · `POST /v1/school-installment/cancelation` · kapsam `loans` · client credentials

Schools/Institutions can perform cancellations based on installments or Turkish National Identity Number (TCKN) via this API. - When only the TCKN is entered, all records and installments associated with that TCKN are not cancelled. - When both the TCKN and Invoice Number are sent, only the relevant installment is cancelled.

```python
yanit = kt.cash_management.school_installment_system_registration_and_installment_cancellation(client_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin |  | Öğrenci TCKN bilgisi |
| `client_id` | `ClientId` | gövde | metin | evet | Kurum token bilgisi |
| `invoice_number` | `InvoiceNumber` | gövde | metin |  | Fatura/Taksit Numarası |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-registration-and-installment-cancellation-api)

## `school_installment_system_school_guaranteed_registration_payment` { #school_installment_system_school_guaranteed_registration_payment }

**School Installment System School Guaranteed Registration Payment** · `POST /v1/school-installment/transaction-information` · kapsam `loans` · client credentials

School-Guaranteed schools can use this API to track parent payments based on payment documentation or date range. --PaymentType description: --0 --&gt; account or card, --1 --&gt; not converted to credit but unpaid, --2 --&gt; converted to credit, parent paid, --3 --&gt; converted to credit, school paid

```python
yanit = kt.cash_management.school_installment_system_school_guaranteed_registration_payment(client_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin |  | Öğrenci TCKN bilgisi |
| `client_id` | `ClientId` | gövde | metin | evet | Kurum token bilgisi |

Gövde alanları istekte `payment` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-school-guaranteed-registration-payment)

## `supplier_financing_buyer_order_confirmation` { #supplier_financing_buyer_order_confirmation }

**Supplier Financing Buyer Order Confirmation** · `POST /v1/supplierfinance/approvefrompurchaserer` · kapsam `loans` · client credentials

It is the API where invoices are uploaded to the system by the receiving company.

```python
yanit = kt.cash_management.supplier_financing_buyer_order_confirmation(purchaser_tax_number=..., supplier_order_gu_id_id=..., supplier_order_id=..., list_approve_from_purchaser_contract=..., tax_exclusive_amount=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `purchaser_tax_number` | `PurchaserTaxNumber` | gövde | metin | evet | Identify Purchaser Tax Number. |
| `supplier_order_gu_id_id` | `SupplierOrderGuIdId` | gövde | metin | evet | Order Number (GUID). |
| `contract` | `contract` | gövde | liste |  |  |
| `supplier_order_id` | `SupplierOrderId` | gövde | metin | evet | Order Number. |
| `list_approve_from_purchaser_contract` | `ListApproveFromPurchaserContract` | gövde | liste | evet | Contains invoice info. |
| `used_invoice_amount` | `UsedInvoiceAmount` | gövde | sayı |  | How much of the bill will be used. |
| `tax_exclusive_amount` | `TaxExclusiveAmount` | gövde | sayı | evet | Tax exclusive amount. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderGuidId`, `Status`, `StatusName`, `ResultMessage`, `executionReferenceId`, `SupplierOrderInvoiceList`, `InvoiceNumber`, `InvoiceStatus`, `InvoiceStatusName`, `InvoiceAmount`, `PaymentAmount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-confirmation)

## `supplier_financing_buyer_order_listing` { #supplier_financing_buyer_order_listing }

**Supplier Financing Buyer Order Listing** · `POST /v1/supplierfinance/getorderbypurchaser` · kapsam `loans` · client credentials

Retrieves supplier financing buyer order records according to the provided purchaser, supplier, order, date range, and transaction date filter criteria. The response includes supplier order, invoice, payment, status, amount, currency, profit rate, commission rate, and description details.

```python
yanit = kt.cash_management.supplier_financing_buyer_order_listing(client_id=..., purchaser_tax_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `client_id` | `ClientId` | gövde | metin | evet | Client identifier used for the supplier financing order listing request. |
| `purchaser_tax_number` | `PurchaserTaxNumber` | gövde | metin | evet | Tax number of the purchaser used to filter supplier financing orders. |
| `first_transaction_date` | `FirstTransactionDate` | gövde | tarih |  | Start date of the transaction date range. |
| `end_transaction_date` | `EndTransactionDate` | gövde | tarih |  | End date of the transaction date range. |
| `supplier_order_id` | `supplierOrderId` | gövde | tam sayı |  | Supplier order identifier used to filter a specific order. |
| `is_transaction_date_invoice_date` | `isTransactionDateInvoiceDate` | gövde | tam sayı |  | Indicates whether the transaction date filter should be evaluated as invoice date. |
| `supplier_tax_number` | `supplierTaxNumber` | gövde | metin |  | Tax number of the supplier used to filter supplier financing orders. |
| `order_number` | `orderNumber` | gövde | metin |  | Order number used to filter supplier financing orders. |

Gövde alanları istekte `listOrderContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderId`, `SupplierOrderGuidId`, `OrderNumber`, `InvoiceNumber`, `Status`, `StatusName`, `InvoiceStatus`, `InvoiceStatusName`, `OrderDate`, `OrderAmount`, `InvoiceAmount`, `PaymentAmount`, `LoanProfitRate`, `LoanCommissionRate`, `FecCode`, `Description`, `SupplierTaxNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-listing)

## `supplier_financing_invoice_cancellation` { #supplier_financing_invoice_cancellation }

**Supplier Financing Invoice Cancellation** · `POST /v1/supplychainfinance/cancelinvoice` · kapsam `loans` · client credentials

This API cancels a supply chain finance invoice. The cancellation operation is processed using the client identifier, purchaser invoice upload GUID, API client invoice upload GUID and purchaser tax number. The response includes the invoice cancellation status and result message.

```python
yanit = kt.cash_management.supplier_financing_invoice_cancellation(client_id=..., purchaser_invoice_upload_guid=..., api_client_invoice_upload_guid=..., purchaser_tax_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `client_id` | `client_id` | gövde | metin | evet | Client identifier used for the invoice cancellation request. |
| `purchaser_invoice_upload_guid` | `PurchaserInvoiceUploadGUID` | gövde | metin | evet | GUID identifier of the purchaser invoice upload record to be cancelled. |
| `api_client_invoice_upload_guid` | `APIClientInvoiceUploadGUID` | gövde | metin | evet | GUID identifier of the invoice upload record on the API client side. |
| `purchaser_tax_number` | `PurchaserTaxNumber` | gövde | metin | evet | Tax number of the purchaser related to the invoice cancellation request. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `PurchaserInvoiceUploadGUID`, `APIClientInvoiceUploadGUID`, `Status`, `StatusName`, `ResultMessage`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-invoice-cancellation)

## `supplier_financing_order_last_approval_by_supplier` { #supplier_financing_order_last_approval_by_supplier }

**Supplier Financing Order Last Approval by Supplier** · `POST /v1/supplierfinance/lastapprovefromsupplier` · kapsam `loans` · client credentials

This API performs the final approval of a supplier financing order by the supplier. The approval operation is processed using the client identifier, supplier tax number, supplier order identifier and supplier order GUID.

```python
yanit = kt.cash_management.supplier_financing_order_last_approval_by_supplier(client_id=..., supplier_tax_number=..., supplier_order_id=..., supplier_order_guid_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `client_id` | `client_id` | gövde | metin | evet | Client identifier used for the supplier financing final approval request. |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Tax number of the supplier approving the supplier financing order. |
| `supplier_order_id` | `SupplierOrderId` | gövde | tam sayı | evet | Unique identifier of the supplier financing order to be approved. |
| `supplier_order_guid_id` | `SupplierOrderGuidId` | gövde | metin | evet | GUID identifier of the supplier financing order to be approved. |

Gövde alanları istekte `Contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderGuidId`, `Status`, `StatusName`, `ResultMessage`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-order-last-approval-by-supplier)

## `supplier_financing_repayment_plan_calculation` { #supplier_financing_repayment_plan_calculation }

**Supplier Financing Repayment Plan Calculation** · `POST /v1/supplierfinance/getpaybackplan` · kapsam `loans` · client credentials

It is the API where the order is canceled by the vendor.

```python
yanit = kt.cash_management.supplier_financing_repayment_plan_calculation(supplier_tax_number=..., supplier_order_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Identify the supplier tax number. |
| `supplier_order_id` | `SupplierOrderId` | gövde | metin | evet | Order number. |
| `maturity_day_count` | `MaturityDayCount` | gövde | tam sayı |  | Maturity day count. |
| `early_payment_day_count` | `EarlyPaymentDayCount` | gövde | tam sayı |  | Early payment day count. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderGuidId`, `OrderNumber`, `Status`, `StatusName`, `ResultMessage`, `executionReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-repayment-plan-calculation)

## `supplier_financing_vendor_company_invoice_approval` { #supplier_financing_vendor_company_invoice_approval }

**Supplier Financing Vendor Company Invoice Approval** · `POST /v1/supplychainfinance/supplierapproveinvoice` · kapsam `loans` · client credentials

This API approves a supply chain finance invoice by the supplier. The approval operation is processed using the client identifier, purchaser invoice upload GUID, API client invoice upload GUID and supplier tax number. The response includes invoice approval status, result message and invoice list details.

```python
yanit = kt.cash_management.supplier_financing_vendor_company_invoice_approval(client_id=..., purchaser_invoice_upload_guid=..., api_client_invoice_upload_guid=..., supplier_tax_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `client_id` | `client_id` | gövde | metin | evet | Client identifier used for the supplier invoice approval request. |
| `purchaser_invoice_upload_guid` | `PurchaserInvoiceUploadGUID` | gövde | metin | evet | GUID identifier of the purchaser invoice upload record to be approved by the supplier. |
| `api_client_invoice_upload_guid` | `APIClientInvoiceUploadGUID` | gövde | metin | evet | GUID identifier of the invoice upload record on the API client side. |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Tax number of the supplier approving the invoice. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `PurchaserInvoiceUploadGUID`, `APIClientInvoiceUploadGUID`, `Status`, `StatusName`, `ResultMessage`, `InvoiceList`, `InvoiceNumber`, `InvoiceStatus`, `InvoiceStatusName`, `InvoiceAmount`, `PaymentAmount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-company-invoice-approval)

## `supplier_financing_vendor_invoice_listing` { #supplier_financing_vendor_invoice_listing }

**Supplier Financing Vendor Invoice Listing** · `POST /v1/supplychainfinance/supplierinvoicelist` · kapsam `loans` · client credentials

This API retrieves supply chain finance invoice records for a supplier based on the provided purchaser invoice upload GUID, purchaser tax number, supplier tax number and transaction date criteria. The response includes invoice identifiers, invoice status, invoice amount, payment amount, loan profit rate, currency code and tax number details.

```python
yanit = kt.cash_management.supplier_financing_vendor_invoice_listing(client_id=..., supplier_tax_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `client_id` | `client_id` | gövde | metin | evet | Client identifier used for the supplier invoice list request. |
| `purchaser_invoice_upload_guid` | `PurchaserInvoiceUploadGUID` | gövde | metin |  | GUID identifier of the purchaser invoice upload record used to filter invoices. |
| `purchaser_tax_number` | `PurchaserTaxNumber` | gövde | metin |  | Tax number of the purchaser used to filter supplier invoices. |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Tax number of the supplier used to filter supplier invoices. |
| `first_transaction_date` | `FirstTransactionDate` | gövde | tarih |  | Start date of the transaction date range. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `PurchaserInvoiceUploadGUID`, `APIClientInvoiceUploadGUID`, `InvoiceList`, `InvoiceNumber`, `InvoiceStatus`, `InvoiceStatusName`, `InvoiceAmount`, `PaymentAmount`, `LoanProfitRate`, `InvoiceFecCode`, `SupplierTaxNumber`, `PurchaserTaxNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-invoice-listing)

## `supplier_financing_vendor_order_cancellation` { #supplier_financing_vendor_order_cancellation }

**Supplier Financing Vendor Order Cancellation** · `POST /v1/supplierfinance/cancelFromSupplier` · kapsam `loans` · client credentials

It is the API where the order is canceled by the vendor.

```python
yanit = kt.cash_management.supplier_financing_vendor_order_cancellation(supplier_tax_number=..., supplier_order_id=..., order_number=..., supplier_order_guid_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Identify Supplier Tax Number. |
| `supplier_order_id` | `SupplierOrderId` | gövde | metin | evet | Order Number. |
| `order_number` | `OrderNumber` | gövde | metin | evet | Order number. |
| `supplier_order_guid_id` | `SupplierOrderGuidId` | gövde | metin | evet | Order Number (GUID). |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderGuidId`, `OrderNumber`, `Status`, `StatusName`, `ResultMessage`, `executionReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-cancellation)

## `supplier_financing_vendor_order_confirmation` { #supplier_financing_vendor_order_confirmation }

**Supplier Financing Vendor Order Confirmation** · `POST /v1/supplierfinance/lastapprovefromsupplierer` · kapsam `loans` · client credentials

It is the API through which the order is approved by the vendor.

```python
yanit = kt.cash_management.supplier_financing_vendor_order_confirmation(supplier_tax_number=..., supplier_order_gu_id_id=..., supplier_order_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Identify Supplier Tax Number. |
| `supplier_order_gu_id_id` | `SupplierOrderGuIdId` | gövde | metin | evet | Order Number (GUID). |
| `supplier_order_id` | `SupplierOrderId` | gövde | metin | evet | Order Number. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderGuidId`, `Status`, `StatusName`, `ResultMessage`, `executionReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-confirmation)

## `supplier_financing_vendor_order_initiation` { #supplier_financing_vendor_order_initiation }

**Supplier Financing Vendor Order Initiation** · `POST /supplierfinance/saveordersupplier` · kapsam `loans` · client credentials

It is the API used to initiate orders.

```python
yanit = kt.cash_management.supplier_financing_vendor_order_initiation(supplier_tax_number=..., purchaser_tax_number=..., order_number=..., amount=..., fec=..., maturity_day_count=..., early_payment_day_count=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `supplier_tax_number` | `SupplierTaxNumber` | gövde | metin | evet | Identify Supplier Tax Number. |
| `purchaser_tax_number` | `PurchaserTaxNumber` | gövde | metin | evet | Identify Purchaser Tax Number. |
| `order_number` | `OrderNumber` | gövde | metin | evet | Supplier specific order number. |
| `amount` | `Amount` | gövde | sayı | evet | Order Amount. |
| `fec` | `Fec` | gövde | tam sayı | evet | Order Fec (Always 0). |
| `maturity_day_count` | `MaturityDayCount` | gövde | tam sayı | evet | Maturity day count. |
| `early_payment_day_count` | `EarlyPaymentDayCount` | gövde | tam sayı | evet | How soon will the payment be made . |
| `description` | `Description` | gövde | metin |  | description |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `SupplierOrderGuidId`, `Status`, `StatusName`, `ResultMessage`, `executionReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-initiation)
