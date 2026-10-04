<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.payment_solutions

Ödeme çözümleri · 15 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`digital_payment_get_token`](#digital_payment_get_token) | `POST /v1/vpos/digitalPaymentGetToken` | CC | test edilmedi | test edilmedi |
| [`digital_payment_query`](#digital_payment_query) | `POST /v1/vpos/digitalPaymentQuery` | CC | test edildi | test edilmedi |
| [`digital_payment_refund`](#digital_payment_refund) | `POST /v1/vpos/digitalPaymentDoRefund` | CC | test edilmedi | test edilmedi |
| [`digital_payment_send_document`](#digital_payment_send_document) | `POST /v1/vpos/sendDocument` | CC | test edilmedi | test edilmedi |
| [`pos_merchant_number_list`](#pos_merchant_number_list) | `GET /v1/pos/merchant-number` | CC | test edildi | test edilmedi |
| [`pos_transaction_details_for_tpp_v2`](#pos_transaction_details_for_tpp_v2) | `POST /v2/pos/detail-transactions` | AC | test edilmedi | test edilmedi |
| [`pos_transaction_details_v3`](#pos_transaction_details_v3) | `POST /v3/pos/detail-transactions` | CC | kısmen test edildi | test edilmedi |
| [`pos_transactions_summary_for_tpp_v2`](#pos_transactions_summary_for_tpp_v2) | `POST /v2/pos/transactions` | AC | test edilmedi | test edilmedi |
| [`pos_transactions_summary_v3`](#pos_transactions_summary_v3) | `POST /v3/pos/transactions` | CC | kısmen test edildi | test edilmedi |
| [`send_order_distribution_detail_v2`](#send_order_distribution_detail_v2) | `POST /v3/purchase/orderdistribution` | CC | test edilmedi | test edilmedi |
| [`virtual_pos`](#virtual_pos) | `POST /v1/vpos` | CC | test edilmedi | test edilmedi |
| [`virtual_pos_end_day_all_list`](#virtual_pos_end_day_all_list) | `POST /v1/vpos/endDayAllList` | AC | test edilmedi | test edilmedi |
| [`virtual_pos_end_of_day`](#virtual_pos_end_of_day) | `POST /v1/vpos/endOfDay` | AC | test edilmedi | test edilmedi |
| [`virtual_pos_general_transaction`](#virtual_pos_general_transaction) | `POST /v1/vpos/transaction` | AC | test edilmedi | test edilmedi |
| [`virtual_pos_order_filter`](#virtual_pos_order_filter) | `POST /v1/vpos/orderFilter` | AC | test edilmedi | test edilmedi |

## `digital_payment_get_token` { #digital_payment_get_token }

**Digital Payment Get Token** · `POST /v1/vpos/digitalPaymentGetToken` · kapsam `digital_payments` · client credentials

It is used to finance e commerce. It can work with various payment methods. (Funding,Money Transfer,etc)

```python
yanit = kt.payment_solutions.digital_payment_get_token(transaction_id=..., order_number=..., merchant_id=..., is_sub_merchant=..., soft_descriptor=..., payment_type=..., amount=..., channel=..., order_item_count=..., currency=..., basket_product_list=..., request_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_id` | `transactionId` | gövde | metin | evet | End-to-end unique ID for the transaction |
| `order_number` | `orderNumber` | gövde | metin | evet | Order number in the merchant |
| `merchant_id` | `merchantId` | gövde | tam sayı | evet | Merchant code defined by Kuveyt Türk |
| `is_sub_merchant` | `isSubMerchant` | gövde | tam sayı | evet | 1: Yes, 0: No |
| `description` | `description` | gövde | metin |  | Optional description |
| `soft_descriptor` | `softDescriptor` | gövde | metin | evet | Accounting description for slip |
| `payment_type` | `paymentType` | gövde | tam sayı | evet | 1: Money transfer, 2: Financing |
| `commission_amount` | `commissionAmount` | gövde | sayı |  | Fee taken from the merchant |
| `amount` | `amount` | gövde | sayı | evet | Transaction amount |
| `transaction_currency` | `transactionCurrency` | gövde | metin |  |  |
| `token_interval` | `tokenInterval` | gövde | tam sayı |  | Validity period in msec. If it is less than ours, this will be considered |
| `success_redirect_url` | `successRedirectUrl` | gövde | metin |  | Customer redirect address for success |
| `fail_redirect_url` | `failRedirectUrl` | gövde | metin |  | Customer redirect address for failure |
| `channel` | `channel` | gövde | metin | evet | WM, MM, WW |
| `order_item_count` | `orderItemCount` | gövde | tam sayı | evet | Distinct count of items in the basket |
| `currency` | `currency` | gövde | tam sayı | evet | Transaction currency |
| `basket_product_list` | `basketProductList` | gövde | liste | evet | Basket Product List |
| `request_date` | `requestDate` | gövde | tarih | evet | Date info in order to use for reconciliation, cancel and query |

Gövde alanları istekte `ApiTransactionContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `accessToken`, `tokenExpireDate`, `returnCode`, `returnMessage`, `applicationName`, `applicationParameter`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-get-token)

## `digital_payment_query` { #digital_payment_query }

**Digital Payment Query** · `POST /v1/vpos/digitalPaymentQuery` · kapsam `digital_payments` · client credentials

Used to query the transaction result

```python
yanit = kt.payment_solutions.digital_payment_query(merchant_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — nesne (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_id` | `transactionId` | gövde | metin |  | End-to-end unique ID for the transaction. |
| `merchant_id` | `merchantId` | gövde | tam sayı | evet | Merchant code defined by Kuveyt Turk. |
| `start_date` | `startDate` | gövde | tarih |  | When there is no transaction ID, start date of the transaction list. |
| `end_date` | `endDate` | gövde | tarih |  | When there is no Transaction ID, end date of the transaction list. |

Gövde alanları istekte `QueryContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `returnCode`, `returnMessage`, `transactionId`, `statusCode`, `statusMessage`, `paymentType`, `commissionAmount`, `amount`, `currency`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-query)

## `digital_payment_refund` { #digital_payment_refund }

**Digital Payment Refund** · `POST /v1/vpos/digitalPaymentDoRefund` · kapsam `digital_payments` · client credentials

Used for digital payment's refund transactions.

```python
yanit = kt.payment_solutions.digital_payment_refund(transaction_id=..., org_transaction_id=..., merchant_id=..., amount=..., currency=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_id` | `transactionId` | gövde | metin | evet | Unique ID for refund transaction |
| `org_transaction_id` | `orgTransactionId` | gövde | metin | evet | Transaction ID from sale/funding will be refund |
| `merchant_id` | `merchantId` | gövde | tam sayı | evet | Merchant's ID given by the bank |
| `amount` | `amount` | gövde | sayı | evet | Refund amount |
| `currency` | `currency` | gövde | tam sayı | evet | Currency code for refund transaction |
| `commission_amount` | `commissionAmount` | gövde | sayı |  | Commission amount for refund transaction |
| `description` | `description` | gövde | metin |  | Description for refund transaction |

Gövde alanları istekte `RefundContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `ReturnCode`, `ReturnMessage`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-refund)

## `digital_payment_send_document` { #digital_payment_send_document }

**Digital Payment Send Document** · `POST /v1/vpos/sendDocument` · kapsam `digital_payments` · client credentials

Used to send document after funding/sale transactions.

```python
yanit = kt.payment_solutions.digital_payment_send_document()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `document_list` | `documentList` | gövde | liste |  |  |

Gövde alanları istekte `SendDocumentContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `transactionId`, `returnCode`, `returnMessage`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-send-document)

## `pos_merchant_number_list` { #pos_merchant_number_list }

**Pos Merchant Number List** · `GET /v1/pos/merchant-number` · kapsam `public` · client credentials

Retrieves POS merchant detail transactions according to the provided customer, corporate user, merchant, count, and date range filters. The response includes POS transaction details such as authorization, batch, merchant, card, branch, currency, installment, commission, amount, terminal, transaction, and request information.

```python
yanit = kt.payment_solutions.pos_merchant_number_list(customer_id=..., start_date=..., end_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: GET and path: /v1/pos/merchant-number'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_id` | `customerId` | sorgu | tam sayı | evet | Customer identifier used to retrieve POS merchant detail transactions. |
| `corporate_user_name` | `corporateUserName` | sorgu | metin |  | Corporate user name used to filter POS merchant detail transactions. |
| `merchant_block_number` | `merchantBlockNumber` | sorgu | tam sayı |  | Merchant block number used to filter POS transactions. |
| `merchant_number` | `merchantNumber` | sorgu | metin |  | Merchant number used to filter POS transactions. |
| `count` | `count` | sorgu | tam sayı |  | Maximum number of POS transaction records to return. |
| `start_date` | `startDate` | sorgu | tarih | evet | Start date of the POS transaction query period. |
| `end_date` | `endDate` | sorgu | tarih | evet | End date of the POS transaction query period. |

Yanıt alanları (dokümana göre): `posDetailTransactions`, `authorizationNumber`, `batchNumber`, `blockDay`, `blockPeriod`, `blockedAccountSuffix`, `branchCode`, `branchName`, `cardBrand`, `cardSourceGroupCode`, `cardType`, `chainMerchantNumber`, `citizenshipNumber`, `currencyCode`, `currencyCodeDescription`, `currentAccountSuffix`, `customerNumber`, `deferringCount`, `deferringDate`, `installmentAmount`, `installmentCount`, `installmentDate`, `installmentNumber`, `isContactlessFlag`, `maskedCardNumber`, `mcc`, `merchantBlockNumber`, `merchantName`, `merchantNumber`, `merchantValueDate`, `netAmountTrn`, `offlineFlag`, `originalAmount`, `poolEodDate`, `requestDate`, `requestTime`, `stan`, `taxNumber`, `terminalNumber`, `totalCommBsmvAmountTrn`, `totalCommissionAmountTrn`, `totalCommissionRate`, `tradeName`, `trnCodeDescription`, `trnDescription`, `trnEffect`, `trnOrderId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-merchant-number-list)

## `pos_transaction_details_for_tpp_v2` { #pos_transaction_details_for_tpp_v2 }

**POS Transaction Details For TPP(Third Party Provider) V2** · `POST /v2/pos/detail-transactions` · kapsam `cards` · authorization code (müşteri girişi gerekir)

With this API, you can behave as a TPP (Third Party Provider) / Fintech and access Kuveyt Turk customers POS transaction details after you get the consent of the customer. If you want to access POS Transaction details only for your own account, you should use the POS Transaction Details V3. &gt; This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.pos_transaction_details_for_tpp_v2(merchant_block_number=..., count=..., start_date=..., end_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `merchant_block_number` | `merchantBlockNumber` | gövde | metin | evet | Represents the blocked number which belongs to customer for POS transactions. This information must be obtained using the POS Transactions Summary V2 service. |
| `merchant_number` | `merchantNumber` | gövde | metin |  | Represents the merchant number which belongs to customer for POS transactions. If the merchant number is not given, a search will be made for all merchant numbers belongs to the customer. |
| `count` | `count` | gövde | metin | evet | Represents the number of detail records to query. Max count value must be a thousand (1000). |
| `start_date` | `startDate` | gövde | tarih | evet | Represents a filter parameter indicating the lower date bound before which the transactions happened. |
| `end_date` | `endDate` | gövde | tarih | evet | Represents a filter parameter indicating the upper date bound before which the transactions happened (Enddate is included in the search). |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-for-tpp-third-party-provider-v2)

## `pos_transaction_details_v3` { #pos_transaction_details_v3 }

**POS Transaction Details V3** · `POST /v3/pos/detail-transactions` · kapsam `cards` · client credentials

With this API, you can only access the POS transaction details of your own accounts. If you want to behave as a TPP (Third Party Provider) / Fintech you should use the POS Transaction Details V2. &gt; This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.pos_transaction_details_v3(merchant_block_number=..., count=..., start_date=..., end_date=..., corporate_user_name=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | kısmen test edildi | erişilebilir, parametre/iş kuralı hatası — merchantBlockNumber parametresi zorunlu alandır. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `merchant_block_number` | `merchantBlockNumber` | gövde | metin | evet | Represents the blocked number which belongs to customer for POS transactions. This information must be obtained using the POS Transactions Summary V2 service. |
| `merchant_number` | `merchantNumber` | gövde | metin |  | Represents the merchant number which belongs to customer for POS transactions. If the merchant number is not given, a search will be made for all merchant numbers belongs to the customer. |
| `count` | `count` | gövde | metin | evet | Represents the number of detail records to query. Max count value must be a thousand (1000). |
| `start_date` | `startDate` | gövde | tarih | evet | Represents a filter parameter indicating the lower date bound before which the transactions happened. |
| `end_date` | `endDate` | gövde | tarih | evet | Represents a filter parameter indicating the upper date bound before which the transactions happened (Enddate is included in the search). |
| `corporate_user_name` | `corporateUserName` | gövde | metin | evet | Represents the User Name information belonging to an authorized user of the customer for POS transaction details. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-v3)

## `pos_transactions_summary_for_tpp_v2` { #pos_transactions_summary_for_tpp_v2 }

**Üçüncü Taraf Sağlayıcı (TPP) için POS İşlemleri Özeti V2** · `POST /v2/pos/transactions` · kapsam `cards` · authorization code (müşteri girişi gerekir)

Bu API, belirtilen müşteri ve üye işyeri numarası için verilen tarih aralığı ve ekstre tipine göre POS işlem bilgilerini getirir. &gt; Bu API beta aşamasındadır. İstek ve yanıt modelleri zamanla değişebilir.

```python
yanit = kt.payment_solutions.pos_transactions_summary_for_tpp_v2(customer_id=..., member_number=..., start_date=..., end_date=..., extract_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_id` | `customerId` | gövde | tam sayı | evet | POS işlem bilgileri getirilecek müşterinin tekil müşteri numarasıdır. |
| `member_number` | `memberNumber` | gövde | metin | evet | POS işlem bilgileri sorgulanacak üye işyeri numarasıdır. |
| `start_date` | `startDate` | gövde | tarih | evet | İşlem sorgu döneminin başlangıç tarihidir. |
| `end_date` | `endDate` | gövde | tarih | evet | İşlem sorgu döneminin bitiş tarihidir. |
| `extract_type` | `extractType` | gövde | metin | evet | POS işlem sorgusunu filtrelemek için kullanılan ekstre tipidir. |

Yanıt alanları (dokümana göre): `posTransactions`, `blockedDate`, `amount`, `commissionRate`, `commissionAmount`, `bsmv`, `blockedNumber`, `unBlockedDate`, `netAmount`, `internationalFecCode`, `fecCode`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/odeme-cozumleri/ucuncu-taraf-saglayici-tpp-icin-pos-islemleri-ozeti-v2)

## `pos_transactions_summary_v3` { #pos_transactions_summary_v3 }

**POS Transactions Summary V3** · `POST /v3/pos/transactions` · kapsam `cards` · client credentials

With this API, you can only access the POS transactions of your own accounts. If you want to behave as a TPP (Third Party Provider) / Fintech you should use the POS Transaction V2. &gt; This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.pos_transactions_summary_v3(corporate_user_name=..., start_date=..., end_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | kısmen test edildi | erişilebilir, parametre/iş kuralı hatası — Yetkili kullanıcı adı gönderilmelidir. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `corporate_user_name` | `corporateUserName` | gövde | metin | evet | Represents the User Name information belonging to an authorized user of the customer for POS transactions. |
| `member_number` | `memberNumber` | gövde | metin |  | Represents the merchant number that belongs to the customer for POS transactions. If the merchant number is not given, a search will be made for all merchant numbers belonging to the customer. |
| `start_date` | `startDate` | gövde | tarih | evet | Represents a filter parameter indicating the lower date bound before which the transactions happened. |
| `end_date` | `endDate` | gövde | tarih | evet | Represents a filter parameter indicating the upper date bound before which the transactions happened (End date is included in the search). |
| `extract_type` | `extractType` | gövde | metin |  | Represents the POS transaction status. H: All Transactions, B: Blocked Transactions, C: UnBlocked Transactions. If the extractType is not given, a search will be made according to "H" value. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transactions-summary-v3)

## `send_order_distribution_detail_v2` { #send_order_distribution_detail_v2 }

**Send Order Distribution Detail V2** · `POST /v3/purchase/orderdistribution` · kapsam `payments` · client credentials

Submits order distribution and delivery details to the BOA system for the purchase process. The request includes distribution records with delivery, cargo, waybill and rejection information, along with optional document attachment details. The response returns whether the order distribution submission was successful and includes error details if available.

```python
yanit = kt.payment_solutions.send_order_distribution_detail_v2(distribution_list=..., e_tender_delivery_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `distribution_list` | `DistributionList` | gövde | liste | evet | List of order distribution records to be submitted. |
| `e_tender_delivery_id` | `ETenderDeliveryId` | gövde | tam sayı | evet | Identifier of the e-tender delivery record associated with the distribution item or the overall request. |
| `attachment` | `Attachment` | gövde | metin |  | Content of the related document. It is typically sent as base64 encoded document data. |
| `document_extension` | `DocumentExtension` | gövde | metin |  | File extension of the submitted document. For example: pdf, jpg, png. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/send-order-distribution-detail-v2)

## `virtual_pos` { #virtual_pos }

**Virtual POS** · `POST /v1/vpos` · kapsam `cards` · client credentials

This endpoint is used to initiate a Virtual POS 3D Model payment transaction. The request includes card details, merchant information, transaction amount, redirection URLs, and transaction security information. The response returns the content required for the 3D authentication or payment flow.

```python
yanit = kt.payment_solutions.virtual_pos(ok_url=..., fail_url=..., hash_data=..., merchant_id=..., user_name=..., transaction_type=..., currency_code=..., transaction_security=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `api_version` | `APIVersion` | gövde | metin |  | API version information to be used for the transaction. |
| `ok_url` | `OkUrl` | gövde | metin | evet | URL where the cardholder will be redirected if the transaction is successful. |
| `fail_url` | `FailUrl` | gövde | metin | evet | URL where the cardholder will be redirected if the transaction fails. |
| `hash_data` | `HashData` | gövde | metin | evet | Hash value generated for transaction verification. |
| `merchant_id` | `MerchantId` | gövde | tam sayı | evet | Merchant identifier. |
| `customer_id` | `$CustomerId` | gövde | tam sayı |  |  |
| `user_name` | `UserName` | gövde | metin | evet | Virtual POS user name. |
| `card_number` | `$CardNumber` | gövde | metin |  |  |
| `card_expire_date_year` | `$CardExpireDateYear` | gövde | tam sayı |  |  |
| `card_expire_date_month` | `$CardExpireDateMonth` | gövde | tam sayı |  |  |
| `card_cvv2` | `$CardCVV2` | gövde | tam sayı |  |  |
| `card_holder_name` | `$CardHolderName` | gövde | metin |  |  |
| `card_holder_ip_address` | `CardHolderIPAddress` | gövde | metin |  | IP address of the cardholder. |
| `card_type` | `CardType` | gövde | metin |  | Card type information. |
| `transaction_type` | `TransactionType` | gövde | metin | evet | Type of transaction to be performed. |
| `installment_count` | `InstallmentCount` | gövde | tam sayı |  | Number of installments. For single payment transactions, 0 or 1 can be sent. |
| `amount` | `$Amount` | gövde | sayı |  |  |
| `display_amount` | `$DisplayAmount` | gövde | sayı |  |  |
| `description` | `Description` | gövde | metin |  | Description of the transaction. |
| `currency_code` | `CurrencyCode` | gövde | tam sayı | evet | Currency code of the transaction. |
| `merchant_order_id` | `$MerchantOrderId` | gövde | tam sayı |  |  |
| `transaction_security` | `TransactionSecurity` | gövde | tam sayı | evet | Indicates the transaction security level. |
| `kuveyt_turk_v_pos_additional_data` | `KuveytTurkVPosAdditionalData` | gövde | nesne |  | Object that contains additional data related to the transaction. |
| `exp_sign` | `ExpSign` | gövde | metin |  | Additional signature information related to the transaction. |
| `customer_ip_address` | `CustomerIPAddress` | gövde | metin |  | Customer IP address. |
| `three_d_secure_level` | `ThreeDSecureLevel` | gövde | tam sayı |  | Indicates the 3D Secure level. |
| `batch_id` | `BatchID` | gövde | tam sayı |  | Batch identifier associated with the transaction. |
| `identity_tax_number` | `$IdentityTaxNumber` | gövde | metin |  |  |
| `qery_id` | `QeryId` | gövde | tam sayı |  | Query identifier. |
| `debt_id` | `DebtId` | gövde | tam sayı |  | Debt identifier. |
| `debtor_name` | `DebtorName` | gövde | metin |  | Name, surname, or title of the debtor. |
| `period` | `Period` | gövde | metin |  | Debt or payment period information. |
| `surcharge_amount` | `$SurchargeAmount` | gövde | sayı |  |  |
| `sgk_debt_amount` | `$SGKDebtAmount` | gövde | sayı |  |  |
| `hash_password` | `HashPassword` | gövde | metin |  | Password used for hash generation. |
| `installment_maturity_commision_flag` | `InstallmentMaturityCommisionFlag` | gövde | tam sayı |  | Indicates whether installment maturity commission will be applied. |
| `explain` | `Explain` | gövde | metin |  | Additional explanation field for the transaction. |
| `explain2` | `Explain2` | gövde | metin |  | Second additional explanation field for the transaction. |
| `explain3` | `Explain3` | gövde | metin |  | Third additional explanation field for the transaction. |

Gövde alanları istekte `KuveytTurkVPosMessage` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `ClientResponse`, `ContentType`, `BusinessKey`, `OrderId`, `ReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos)

## `virtual_pos_end_day_all_list` { #virtual_pos_end_day_all_list }

**Virtual POS EndDayAll List** · `POST /v1/vpos/endDayAllList` · kapsam `cards` · authorization code (müşteri girişi gerekir)

This endpoint is used to retrieve the end-of-day transaction list for a Virtual POS merchant within the specified date range. The request includes the date filter and Virtual POS login information required to validate the merchant. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.virtual_pos_end_day_all_list(order_filter_contract=..., v_pos_login_contract=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `order_filter_contract` | `OrderFilterContract` | gövde | nesne | evet | Object that contains the end-of-day list filter criteria. |
| `v_pos_login_contract` | `VPosLoginContract` | gövde | nesne | evet | Object that contains Virtual POS merchant login information. |

Yanıt alanları (dokümana göre): `OrderId`, `MerchantOrderId`, `MerchantId`, `CardHolderName`, `CardType`, `CardNumber`, `OrderDate`, `OrderStatus`, `LastOrderStatus`, `OrderType`, `TransactionStatus`, `FirstAmount`, `CancelAmount`, `DrawbackAmount`, `PartialDrawbackAmount`, `ClosedAmount`, `FEC`, `VPSEntryMode`, `InstallmentCount`, `DeferringCount`, `TransactionSecurity`, `ResponseCode`, `ResponseExplain`, `EndOfDayStatus`, `TransactionSide`, `CardHolderIPAddress`, `MerchantIPAddress`, `MerchantUserName`, `ProvNumber`, `BatchId`, `MerchantBatchId`, `CardExpireDate`, `CVV2`, `CVV2Encrypted`, `PosTerminalId`, `Explain`, `Explain2`, `Explain3`, `RRN`, `Stan`, `UserName`, `Host_Name`, `SystemDate`, `UpdateUserName`, `UpdateHostName`, `UpdateSystemDate`, `HostIP`, `LastOrderStatusDescription`, `OrderTypeDescription`, `TransactionStatusDescription`, `EndOfDayStatusDescription`, `FecDescription`, `TransactionSecurityDescription`, `HashPassword`, `OrderIdList`, `CustomerId`, `TransactionType`, `TransactionTypeDescription`, `UpperLimit`, `LowerLimit`, `StartDate`, `EndDate`, `SaleOrderCount`, `DrawbackOrderCount`, `SumOfOrderCount`, `SaleOrderAmount`, `DrawbackOrderAmount`, `SumOfOrderAmount`, `EndOfDayId`, `TransactionStatusDesc`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-enddayall-list)

## `virtual_pos_end_of_day` { #virtual_pos_end_of_day }

**Virtual POS EndOfDay** · `POST /v1/vpos/endOfDay` · kapsam `cards` · authorization code (müşteri girişi gerekir)

This endpoint is used to perform the end-of-day closing operation for Virtual POS transactions within the specified date range. The request includes the date filter, merchant information, and Virtual POS login information required to validate the merchant and process eligible transactions. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.virtual_pos_end_of_day(order_filter_contract=..., v_pos_login_contract=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `order_filter_contract` | `OrderFilterContract` | gövde | nesne | evet | Object that contains the end-of-day closing filter criteria. |
| `v_pos_login_contract` | `VPosLoginContract` | gövde | nesne | evet | Object that contains Virtual POS merchant login information. |

Yanıt alanları (dokümana göre): `VPosMessage`, `VPosMessageV2`, `VposMessageCommon`, `LoginResponse`, `IsEnrolled`, `IsVirtual`, `PareqHtmlFormString`, `ProvisionNumber`, `RRN`, `Stan`, `ResponseCode`, `IsSuccess`, `ResponseMessage`, `OrderId`, `TransactionTime`, `MerchantOrderId`, `HashData`, `MD`, `AuthenticationPacket`, `ACSURL`, `Password`, `CurrencyCode`, `TransactionType`, `SafeKey`, `ReferenceId`, `MerchantId`, `BusinessKey`, `PaymentOrderList`, `WebFlowResponse`, `StartAuthenticationResult`, `MDStatus`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-endofday)

## `virtual_pos_general_transaction` { #virtual_pos_general_transaction }

**Virtual POS General Transaction** · `POST /v1/vpos/transaction` · kapsam `cards` · authorization code (müşteri girişi gerekir)

This endpoint is used to perform Virtual POS transaction operations such as refund, partial refund, and sale reversal for an existing order. The request includes the order information, transaction type, optional refund amount, and Virtual POS login information required to validate the merchant. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.virtual_pos_general_transaction(order_filter_contract=..., v_pos_login_contract=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `order_filter_contract` | `OrderFilterContract` | gövde | nesne | evet | Object that contains the transaction operation details. |
| `v_pos_login_contract` | `VPosLoginContract` | gövde | nesne | evet | Object that contains Virtual POS merchant login information. |

Yanıt alanları (dokümana göre): `VPosMessage`, `VPosMessageV2`, `VposMessageCommon`, `LoginResponse`, `IsEnrolled`, `IsVirtual`, `PareqHtmlFormString`, `ProvisionNumber`, `RRN`, `Stan`, `ResponseCode`, `IsSuccess`, `ResponseMessage`, `OrderId`, `TransactionTime`, `MerchantOrderId`, `HashData`, `MD`, `AuthenticationPacket`, `ACSURL`, `Password`, `CurrencyCode`, `TransactionType`, `SafeKey`, `ReferenceId`, `MerchantId`, `BusinessKey`, `PaymentOrderList`, `WebFlowResponse`, `StartAuthenticationResult`, `MDStatus`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-general-transaction)

## `virtual_pos_order_filter` { #virtual_pos_order_filter }

**Virtual POS Order Filter** · `POST /v1/vpos/orderFilter` · kapsam `cards` · authorization code (müşteri girişi gerekir)

This endpoint is used to retrieve Virtual POS order records based on the specified filter criteria. The request includes date range, cardholder name, amount limits, merchant information, and Virtual POS login information required to validate the merchant. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.payment_solutions.virtual_pos_order_filter(order_filter_contract=..., v_pos_login_contract=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `order_filter_contract` | `OrderFilterContract` | gövde | nesne | evet | Object that contains the order filter criteria. |
| `v_pos_login_contract` | `VPosLoginContract` | gövde | nesne | evet | Object that contains Virtual POS merchant login information. |

Yanıt alanları (dokümana göre): `OrderId`, `MerchantOrderId`, `MerchantId`, `CardHolderName`, `CardType`, `CardNumber`, `OrderDate`, `OrderStatus`, `LastOrderStatus`, `OrderType`, `TransactionStatus`, `FirstAmount`, `CancelAmount`, `DrawbackAmount`, `PartialDrawbackAmount`, `ClosedAmount`, `FEC`, `VPSEntryMode`, `InstallmentCount`, `DeferringCount`, `TransactionSecurity`, `ResponseCode`, `ResponseExplain`, `EndOfDayStatus`, `TransactionSide`, `CardHolderIPAddress`, `MerchantIPAddress`, `MerchantUserName`, `ProvNumber`, `BatchId`, `MerchantBatchId`, `CardExpireDate`, `CVV2`, `CVV2Encrypted`, `PosTerminalId`, `Explain`, `Explain2`, `Explain3`, `RRN`, `Stan`, `UserName`, `HostName`, `SystemDate`, `UpdateUserName`, `UpdateHostName`, `UpdateSystemDate`, `HostIP`, `LastOrderStatusDescription`, `OrderTypeDescription`, `TransactionStatusDescription`, `EndOfDayStatusDescription`, `FecDescription`, `TransactionSecurityDescription`, `HashPassword`, `OrderIdList`, `CustomerId`, `TransactionType`, `TransactionTypeDescription`, `UpperLimit`, `LowerLimit`, `StartDate`, `EndDate`, `SaleOrderCount`, `DrawbackOrderCount`, `SumOfOrderCount`, `SaleOrderAmount`, `DrawbackOrderAmount`, `SumOfOrderAmount`, `EndOfDayId`, `TransactionStatusDesc`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-order-filter)
