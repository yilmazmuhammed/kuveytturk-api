<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.transfers

Para transferleri · 10 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`cash_withdrawal_from_atm_via_qr_code`](#cash_withdrawal_from_atm_via_qr_code) | `POST /v1/transfers/fromATMByQRCode` | AC | test edilmedi | test edilmedi |
| [`customer_iban_info_for_money_transfer`](#customer_iban_info_for_money_transfer) | `GET /v1/moneytransfer/{iban}/customeribaninfo` | CC | test edildi | test edilmedi |
| [`internal_money_transfer`](#internal_money_transfer) | `POST /v1/moneytransfer/interbankmoneytransfer` | CC | test edilmedi | test edilmedi |
| [`investment_account_activities_report`](#investment_account_activities_report) | `POST /v1/investment/report-for-account-activities` | CC | test edildi | test edilmedi |
| [`money_transfer_payment_type`](#money_transfer_payment_type) | `POST /v1/moneytransfer/paymenttype` | CC | kısmen test edildi | test edilmedi |
| [`money_transfer_state`](#money_transfer_state) | `GET /v1/moneytransfer-state` | CC | test edildi | test edilmedi |
| [`money_transfer_to_gsm`](#money_transfer_to_gsm) | `POST /v1/transfers/toGSM` | AC | test edilmedi | test edilmedi |
| [`outgoing_money_transfer`](#outgoing_money_transfer) | `POST /v1/moneytransfer/outgoingmoneytransfer` | CC | kısmen test edildi | test edilmedi |
| [`outgoing_money_transfer_v2`](#outgoing_money_transfer_v2) | `POST /v2/moneytransfer/outgoingmoneytransfer` | AC | test edilmedi | test edilmedi |
| [`transaction_validation_list`](#transaction_validation_list) | `GET /v1/transactionvalidation/transactionlist` | CC | kısmen test edildi | test edilmedi |

## `cash_withdrawal_from_atm_via_qr_code` { #cash_withdrawal_from_atm_via_qr_code }

**Cash Withdrawal from ATM via QR Code** · `POST /v1/transfers/fromATMByQRCode` · kapsam `transfers` · authorization code (müşteri girişi gerekir)

This API enables cash withdrawal from an ATM via QR code. The customer scans the QR code displayed on the ATM using a mobile application and sends the QR code information to Kuveyt Türk through this service. To proceed with the transfer, Kuveyt Türk sends a one-time password via SMS to the customer and returns a transaction id to the developer. The customer enters the SMS code in the third-party application, and the third-party application sends the transaction id and SMS code to Kuveyt Türk through the Execute Money Transfer API. If the transaction id and SMS code match, Kuveyt Türk authenticates the transaction.

```python
yanit = kt.transfers.cash_withdrawal_from_atm_via_qr_code(sender_account_suffix=..., amount=..., qr_code=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `SenderAccountSuffix` | gövde | tam sayı | evet | Account suffix of the sender account to be used for the cash withdrawal transaction. |
| `amount` | `Amount` | gövde | sayı | evet | Amount to be withdrawn from the ATM. |
| `qr_code` | `QRCode` | gövde | metin | evet | QR code data read from the ATM and sent to the service for validation. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/cash-withdrawal-from-atm-via-qr-code)

## `customer_iban_info_for_money_transfer` { #customer_iban_info_for_money_transfer }

**Customer Iban Info for Money Transfer** · `GET /v1/moneytransfer/{iban}/customeribaninfo` · kapsam `transfers` · client credentials

This API is used to retrieve customer account information associated with a given IBAN. The service returns masked customer name, bank name, bank ID and FEC information for the queried IBAN.

```python
yanit = kt.transfers.customer_iban_info_for_money_transfer(iban=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — nesne (iban) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `iban` | `iban` | yol | metin | evet | IBAN number for which customer account information will be retrieved. This value is sent as a route parameter. |

Yanıt alanları (dokümana göre): `customerName`, `bankName`, `bankId`, `fec`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/money-transfers/customer-iban-info-for-money-transfer)

## `internal_money_transfer` { #internal_money_transfer }

**Money Transfer (Veeraman)** · `POST /v1/moneytransfer/interbankmoneytransfer` · kapsam `transfers` · client credentials

This API is used to initiate an internal account-to-account money transfer transaction. The sender account number is retrieved from the customer information in the authorization context, and the request includes sender suffix, receiver account information, transfer amount, description and transfer type.

```python
yanit = kt.transfers.internal_money_transfer(sender_account_suffix=..., receiver_account_number=..., receiver_account_suffix=..., money_transfer_amount=..., transfer_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `senderAccountSuffix` | gövde | tam sayı | evet | Sender account suffix number from which the money transfer amount will be withdrawn. |
| `receiver_account_number` | `receiverAccountNumber` | gövde | tam sayı | evet | Receiver customer account number to which the money transfer will be sent. |
| `receiver_account_suffix` | `receiverAccountSuffix` | gövde | tam sayı | evet | Receiver account suffix number to which the money transfer will be sent. |
| `money_transfer_description` | `moneyTransferDescription` | gövde | metin |  | Description or comment added to the money transfer transaction. |
| `money_transfer_amount` | `moneyTransferAmount` | gövde | sayı | evet | Amount that will be transferred. |
| `transfer_type` | `transferType` | gövde | tam sayı | evet | Money transfer type used to identify the transfer scenario. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `moneyTransferTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-veeraman)

## `investment_account_activities_report` { #investment_account_activities_report }

**Money Transfer Report For Kuveyt Türk Investment Securities Inc.** · `POST /v1/investment/report-for-account-activities` · kapsam `transfers` · client credentials

Retrieves the account activities report for Kuveyt Türk Investment Securities Inc. according to the provided language and transaction date. The response includes money transfer and account activity details such as transaction identifier, transfer type, amount, intermediary account number, currency, comment, and system date.

```python
yanit = kt.transfers.investment_account_activities_report(language_id=..., transaction_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: POST and path: /v1/investment/report-for-account-activities'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `language_id` | `languageId` | gövde | tam sayı | evet | Language identifier used for report content and descriptions. |
| `transaction_date` | `transactionDate` | gövde | tarih | evet | Transaction date used to retrieve account activities. |

Gövde alanları istekte `contract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `accountActivities`, `bankMoneyTransferId`, `transactionId`, `transferType`, `transferAmount`, `intermediaryAccountNumber`, `currency`, `comment`, `systemDate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/money-transfer-report-for-kuveyt-turk-investment-securities-inc)

## `money_transfer_payment_type` { #money_transfer_payment_type }

**Money Transfer Payment Type** · `POST /v1/moneytransfer/paymenttype` · kapsam `transfers` · client credentials

Bir transfer için geçerli ödeme türünü sorgular. Dikkat: resmî dokümandaki açıklama ve parametreler başka bir uç noktadan kopyalanmış; buradaki parametreler sandbox'ın doğrulama hatalarına göre belirlendi.

```python
yanit = kt.transfers.money_transfer_payment_type(sender_account_suffix=..., receiver_iban=..., amount=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | kısmen test edildi | sunucu hatası (500) — Kullanıcı senderAccountSuffix, receiverIban, amount ile üç kez denedi: başlıksız, LanguageId+DeviceId ile ve transferType=2 eklenerek. Üçü de 500 Object referen… | 2026-10-07 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `senderAccountSuffix` | gövde | tam sayı | evet | Gönderen hesabın ek numarası. |
| `receiver_iban` | `receiverIban` | gövde | metin | evet | Alıcının IBAN'ı. |
| `amount` | `amount` | gövde | sayı | evet | Transfer tutarı. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-payment-type)

## `money_transfer_state` { #money_transfer_state }

**Money Transfer State** · `GET /v1/moneytransfer-state` · kapsam `transfers` · client credentials

This API is used to check the current state of a money transfer transaction. The transaction can be queried by outGoingId for outgoing transfer types or by virmanKey for VIRMAN transactions. The transferType parameter determines which transaction type will be checked.

```python
yanit = kt.transfers.money_transfer_state(transfer_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: GET and path: /v1/moneytransfer-state'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `out_going_id` | `outGoingId` | sorgu | metin |  | Outgoing money transfer ID used to query the transfer state. Required for transfer types other than VIRMAN. |
| `virman_key` | `virmanKey` | sorgu | metin |  | Encrypted business key used to query VIRMAN transaction state. Required when transferType is VIRMAN. |
| `transfer_type` | `transferType` | sorgu | metin | evet | Money transfer type to be queried. Possible values include VIRMAN, HAVALE, FAST, POS and PÖS - EFT. |

Yanıt alanları (dokümana göre): `transferType`, `state`, `stateDescription`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-state)

## `money_transfer_to_gsm` { #money_transfer_to_gsm }

**Money Transfer to GSM** · `POST /v1/transfers/toGSM` · kapsam `transfers` · authorization code (müşteri girişi gerekir)

Sends money from an authorized user’s current or deposit account (sent via token) to any phone number. In order to proceed the transfer, Kuveyt Turk sends a one-time-password via SMS to the customer and gives a transaction ID to the developer, the customer enters the code to the third-party app, and the third-party app sends the ID and the SMS code to Kuveyt Turk via “Execute Money Transfer” API. If the ID and the SMS codes match, then Kuveyt Turk authenticates the transaction. The parameters sent include, amount, comment, sender’s branch ID, receiver’s phone number, and sender’s account suffix.

```python
yanit = kt.transfers.money_transfer_to_gsm(sender_account_suffix=..., receiver_name=..., receiver_phone_number=..., amount=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `SenderAccountSuffix` | gövde | tam sayı | evet | Indicates the sender's account suffix number. |
| `receiver_name` | `ReceiverName` | gövde | metin | evet | Indicates the receiver's name. |
| `receiver_phone_number` | `ReceiverPhoneNumber` | gövde | metin | evet | Indicates the receiver's phone number. |
| `amount` | `Amount` | gövde | sayı | evet | Amount that will be sent. |
| `comment` | `Comment` | gövde | metin |  | Comment that customer adds to the transaction. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/money-transfer-to-gsm)

## `outgoing_money_transfer` { #outgoing_money_transfer }

**Para Transferi (Havale & EFT & FAST & Virman)** · `POST /v1/moneytransfer/outgoingmoneytransfer` · kapsam `transfers` · client credentials

Müşteri hesabından bir IBAN'a para transferi (havale / EFT / FAST) başlatır. Dikkat: resmî dokümandaki parametre listesi eksik; buradaki zorunlu alanlar sandbox'ın doğrulama hatalarına göre belirlendi.

```python
yanit = kt.transfers.outgoing_money_transfer(sender_account_suffix=..., receiver_iban=..., money_transfer_amount=..., corporate_web_user_name=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | kısmen test edildi | sunucu hatası (500) — Kullanıcı 1 TL kendi hesapları arasında denedi (senderAccountSuffix, receiverIban, moneyTransferAmount, corporateWebUserName, moneyTransferDescription). Yanıt: … | 2026-10-07 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `senderAccountSuffix` | gövde | tam sayı | evet | Tutarın çekileceği gönderen hesabın ek numarası. |
| `receiver_iban` | `receiverIban` | gövde | metin | evet | Alıcının IBAN'ı. (Dokümanda yer almıyor; sandbox zorunlu tutuyor.) |
| `money_transfer_amount` | `moneyTransferAmount` | gövde | sayı | evet | Transfer edilecek tutar. |
| `corporate_web_user_name` | `corporateWebUserName` | gövde | metin | evet | İşlemi yapan kurumsal internet şubesi kullanıcı adı. (Dokümanda yer almıyor; sandbox zorunlu tutuyor.) |
| `money_transfer_description` | `moneyTransferDescription` | gövde | metin |  | Transfer açıklaması. |
| `transfer_type` | `transferType` | gövde | tam sayı |  | Transfer senaryosunu belirleyen tür kodu (dokümanda değerleri açıklanmıyor). |
| `receiver_account_number` | `receiverAccountNumber` | gövde | tam sayı |  | Alıcı müşteri/hesap numarası (dokümandaki alan). |
| `receiver_account_suffix` | `receiverAccountSuffix` | gövde | tam sayı |  | Alıcı hesabın ek numarası (dokümandaki alan). |

Yanıt alanları (dokümana göre): `executionReferenceId`, `moneyTransferTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/para-transferleri/para-transferi-havale-eft-fast-virman)

## `outgoing_money_transfer_v2` { #outgoing_money_transfer_v2 }

**Outgoing Money Transfer V2** · `POST /v2/moneytransfer/outgoingmoneytransfer` · kapsam `transfers` · authorization code (müşteri girişi gerekir)

Müşteri girişiyle (authorization code) para transferi. Dikkat: resmî dokümandaki açıklama ve parametreler hesap hareketleri uç noktasından kopyalanmış görünüyor; gerçek gövde alanları doğrulanamadı. Alanları extra_body ile ya da kt.request() ile gönderin.

```python
yanit = kt.transfers.outgoing_money_transfer_v2(suffix=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | gövde | tam sayı | evet | Account suffix for which transaction records will be retrieved. |
| `item_count` | `itemCount` | gövde | tam sayı |  | Maximum number of account activity records to be returned. |
| `begin_date` | `beginDate` | gövde | tarih |  | Start date from which account activity records will be retrieved. |
| `end_date` | `endDate` | gövde | tarih |  | End date until which account activity records will be retrieved. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountActivities`, `suffix`, `date`, `description`, `amount`, `balance`, `transactionReference`, `fxCode`, `transactionCode`, `transactionCodeDescription`, `senderIdentityNumber`, `transactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/money-transfers/outgoing-money-transfer-v2)

## `transaction_validation_list` { #transaction_validation_list }

**Transaction Validation List** · `GET /v1/transactionvalidation/transactionlist` · kapsam `public` · client credentials

This API is used to retrieve the transaction list used in transaction validation processes. The service returns transaction validation records filtered by transaction GUID and date range. It also returns the total transaction amount and total transaction count for the retrieved transaction list.

```python
yanit = kt.transfers.transaction_validation_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | kısmen test edildi | erişilebilir, parametre/iş kuralı hatası — TransactionGuid: ile gerçekleşen bir işlem bulunmamaktadır. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_guid` | `transactionGuid` | sorgu | metin |  | Unique transaction GUID used to filter transaction validation records. |
| `begin_date` | `beginDate` | sorgu | tarih |  | Start date from which transaction validation records will be retrieved. |
| `end_date` | `endDate` | sorgu | tarih |  | End date until which transaction validation records will be retrieved. |

Yanıt alanları (dokümana göre): `transactionContract`, `totalAmount`, `totalTransactionCount`, `transactionList`, `transactionGuid`, `executionReferenceId`, `amount`, `tranDate`, `transactionDescription`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/money-transfers/transaction-validation-list)
