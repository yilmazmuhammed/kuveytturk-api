<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.accounts

Hesap yönetimi (kurumun kendi hesapları) · 8 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`account_activity_list`](#account_activity_list) | `POST /v1/accountActivities` | CC | test edilmedi | test edilmedi |
| [`account_list_v3`](#account_list_v3) | `GET /v3/accounts` | CC | test edildi | test edilmedi |
| [`account_list_with_suffix_v3`](#account_list_with_suffix_v3) | `GET /v3/accounts/{suffix}` | CC | test edildi | test edilmedi |
| [`account_transactions_v3`](#account_transactions_v3) | `GET /v3/accounts/{suffix}/transactions` | CC | test edildi | test edilmedi |
| [`account_transactions_v4_detail`](#account_transactions_v4_detail) | `GET /v4/accounts/{suffix}/transactions` | CC | test edildi | test edilmedi |
| [`account_verification_v2`](#account_verification_v2) | `POST /v2/accounts/verification` | CC | test edilmedi | test edilmedi |
| [`pdf_receipt_v3`](#pdf_receipt_v3) | `POST /v3/accounts/transactions/pdfReceipts` | CC | kısmen test edildi | test edilmedi |
| [`receipt_v3`](#receipt_v3) | `POST /v3/accounts/transactions/receipts` | CC | test edildi | test edilmedi |

## `account_activity_list` { #account_activity_list }

**Account Activity List** · `POST /v1/accountActivities` · kapsam `account_activities` · client credentials

Retrieves the account activities within the specified date range for the client making the request.

```python
yanit = kt.accounts.account_activity_list(begin_date=..., end_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — kapsam: account_activities | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `begin_date` | `BeginDate` | gövde | tarih | evet | Specifies after which date the account activities will be retrieved. |
| `end_date` | `EndDate` | gövde | tarih | evet | Specifies before which date the account activities will be retrieved. |

Gövde alanları istekte `request` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/account-activity-list)

## `account_list_v3` { #account_list_v3 }

**Account List V3** · `GET /v3/accounts` · kapsam `accounts` · client credentials

This API is used to retrieve the account list of the customer associated with the authorization context. The response includes account details such as account suffix, balance, available balance, currency information, IBAN, account type, branch information, customer name, maturity dates and account status. The account list can be filtered by account suffix and optional account status or balance filters.

```python
yanit = kt.accounts.account_list_v3()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — accountList: 50 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | sorgu | tam sayı |  | Account suffix used to retrieve a specific account. |
| `only_has_available_balance` | `onlyHasAvailableBalance` | sorgu | bool |  | Indicates whether only accounts with available balance should be returned. |
| `only_open` | `onlyOpen` | sorgu | bool |  | Indicates whether only open accounts should be returned. |
| `only_with_no_balance` | `onlyWithNoBalance` | sorgu | bool |  | Indicates whether only accounts with no balance should be returned. |
| `only_current` | `onlyCurrent` | sorgu | bool |  | Indicates whether only current accounts should be returned. |
| `shared_with_multi_signature` | `sharedWithMultiSignature` | sorgu | bool |  | Indicates whether shared accounts requiring multiple signatures should be included. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountList`, `name`, `suffix`, `balance`, `avaibleBalance`, `fxId`, `iban`, `type`, `openDate`, `branchName`, `branchId`, `withHoldingAmount`, `customerName`, `maturityBeginDate`, `maturityEndDate`, `isActive`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-v3)

## `account_list_with_suffix_v3` { #account_list_with_suffix_v3 }

**Account List With Suffix v3** · `GET /v3/accounts/{suffix}` · kapsam `accounts` · client credentials

This API is used to retrieve account information for the specified account suffix of the customer associated with the authorization context. The response includes account details such as account suffix, balance, available balance, currency information, IBAN, account type, branch information, customer name, maturity dates and account status. Additional filters can be used to narrow the account list by balance, account status, current account type and shared account signature type.

```python
yanit = kt.accounts.account_list_with_suffix_v3(suffix=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — accountList: 1 kayıt (suffix) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | yol | tam sayı | evet | Account suffix used to retrieve a specific account. This value is sent as a route parameter. |
| `only_has_available_balance` | `onlyHasAvailableBalance` | sorgu | bool |  | Indicates whether only accounts with available balance should be returned. |
| `only_open` | `onlyOpen` | sorgu | bool |  | Indicates whether only open accounts should be returned. |
| `only_with_no_balance` | `onlyWithNoBalance` | sorgu | bool |  | Indicates whether only accounts with no balance should be returned. |
| `only_current` | `onlyCurrent` | sorgu | bool |  | Indicates whether only current accounts should be returned. |
| `shared_with_multi_signature` | `sharedWithMultiSignature` | sorgu | bool |  | Indicates whether shared accounts requiring multiple signatures should be included. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountList`, `name`, `suffix`, `balance`, `avaibleBalance`, `fxId`, `iban`, `type`, `openDate`, `branchName`, `branchId`, `withHoldingAmount`, `customerName`, `maturityBeginDate`, `maturityEndDate`, `isActive`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-with-suffix-v3)

## `account_transactions_v3` { #account_transactions_v3 }

**Account Transactions V3** · `GET /v3/accounts/{suffix}/transactions` · kapsam `accounts` · client credentials

This API is used to retrieve account transaction history for the specified account suffix of the customer associated with the authorization context. The transaction list can be filtered by item count, begin date and end date. The response includes transaction details such as transaction date, description, amount, balance, transaction reference, currency code, resource code, IBAN and request number.

```python
yanit = kt.accounts.account_transactions_v3(suffix=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — accountActivities: 0 kayıt (suffix) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | yol | tam sayı | evet | Account suffix for which transaction records will be retrieved. This value is sent as a route parameter. |
| `item_count` | `itemCount` | sorgu | tam sayı |  | Maximum number of account activity records to be returned. |
| `begin_date` | `beginDate` | sorgu | tarih |  | Start date from which account activity records will be retrieved. |
| `end_date` | `endDate` | sorgu | tarih |  | End date until which account activity records will be retrieved. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountActivities`, `suffix`, `date`, `description`, `amount`, `balance`, `transactionReference`, `businessKey`, `seqNum`, `fxCode`, `transactionCode`, `resourceCode`, `iban`, `senderIdentityNumber`, `senderTCKNorVKN`, `receiverTCKNorVKN`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v3)

## `account_transactions_v4_detail` { #account_transactions_v4_detail }

**Account Transactions V4 - Detail** · `GET /v4/accounts/{suffix}/transactions` · kapsam `accounts` · client credentials

This API is used to retrieve account transaction history for the specified account suffix of the customer associated with the authorization context. The transaction list can be filtered by item count, begin date and end date. The response includes transaction details such as transaction date, description, amount, balance, transaction reference, currency code, resource code and IBAN.

```python
yanit = kt.accounts.account_transactions_v4_detail(suffix=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — results: 0 kayıt (suffix) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | yol | tam sayı | evet | Account suffix for which transaction records will be retrieved. This value is sent as a route parameter. |
| `item_count` | `itemCount` | sorgu | tam sayı |  | Maximum number of account activity records to be returned. |
| `begin_date` | `beginDate` | sorgu | tarih |  | Start date from which account activity records will be retrieved. |
| `end_date` | `endDate` | sorgu | tarih |  | End date until which account activity records will be retrieved. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountActivities`, `suffix`, `date`, `description`, `amount`, `balance`, `transactionReference`, `fxCode`, `resourceCode`, `iban`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v4-detail)

## `account_verification_v2` { #account_verification_v2 }

**Prevalidation Data Provider** · `POST /v2/accounts/verification` · kapsam `accounts` · client credentials

This API verifies beneficiary account information before processing a payment or transfer. The verification is performed using creditor account, creditor name, creditor address, creditor organisation identification and creditor agent information.

```python
yanit = kt.accounts.account_verification_v2(correlation_identifier=..., context=..., uetr=..., creditor_account=..., creditor_name=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `correlation_identifier` | `correlation_identifier` | gövde | metin | evet | Unique correlation identifier used to track the verification request. |
| `context` | `context` | gövde | metin | evet | Context information related to the verification request. |
| `uetr` | `uetr` | gövde | metin | evet | Unique end_to_end Transaction Reference associated with the transaction. |
| `creditor_account` | `creditor_account` | gövde | metin | evet | Creditor account number or account identifier to be verified. |
| `creditor_name` | `creditor_name` | gövde | metin | evet | Name of the creditor to be verified. |
| `creditor_address` | `creditor_address` | gövde | nesne |  | Address information of the creditor. |
| `creditor_organisation_identification` | `creditor_organisation_identification` | gövde | nesne |  | Organisation identification information of the creditor. |
| `creditor_agent` | `creditor_agent` | gövde | nesne |  | Financial institution or agent information of the creditor. |
| `creditor_agent_branch_identification` | `creditor_agent_branch_identification` | gövde | metin |  | Branch identification of the creditor agent. |
| `x_bic` | `x-bic` | gövde | metin |  | BIC value provided in the request context. |
| `subject_dn` | `SubjectDN` | gövde | metin |  | Subject distinguished name information used for certificate or institution identification. |
| `institution` | `Institution` | gövde | metin |  | Institution information associated with the verification request. |

Yanıt alanları (dokümana göre): `correlation_identifier`, `response`, `account_validation_status`, `creditor_account_match`, `creditor_name_match`, `creditor_address_match`, `creditor_organisation_identification_match`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/prevalidation-data-provider)

## `pdf_receipt_v3` { #pdf_receipt_v3 }

**PDF Receipt V3** · `POST /v3/accounts/transactions/pdfReceipts` · kapsam `accounts` · client credentials

This API is used to retrieve PDF receipt data for a transaction. The customer account number is retrieved from the authorization context, and the transaction is identified by the executionReferenceId value sent in the request body. The response returns the receipt PDF content in Base64 format.

```python
yanit = kt.accounts.pdf_receipt_v3(execution_reference_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | kısmen test edildi | erişilebilir, parametre/iş kuralı hatası — MessageResourceError:Message_APIBanking.WarningAboutGuid | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `execution_reference_id` | `executionReferenceId` | gövde | metin | evet | Reference ID of the transaction for which the PDF receipt data will be retrieved. |

Yanıt alanları (dokümana göre): `contract`, `pdfData`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-own/pdf-receipt-v3)

## `receipt_v3` { #receipt_v3 }

**Dekont V3** · `POST /v3/accounts/transactions/receipts` · kapsam `accounts` · client credentials

Bu API, transactionReference değeri ile tanımlanan bir transaction için receipt bilgilerini almak amacıyla kullanılır. Servis; title, description, amount, currency bilgisi ve slip list, left header, right header, body ve footer bölümlerini içeren receipt detaylarını döndürür.

```python
yanit = kt.accounts.receipt_v3(transaction_reference=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — nesne (transaction_reference) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_reference` | `transactionReference` | gövde | metin | evet | Receipt bilgisi alınacak şifrelenmiş transaction reference değeridir. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `title`, `description`, `amount`, `fecName`, `slipList`, `key`, `leftHeader`, `rightHeader`, `body`, `footer`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-hesaplariniz/dekont-v3)
