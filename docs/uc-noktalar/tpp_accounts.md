<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.tpp_accounts

Hesap yönetimi (TPP - müşteri adına) · 5 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`account_list_v2`](#account_list_v2) | `GET /v2/accounts` | AC | test edildi | test edilmedi |
| [`account_list_with_suffix_v2`](#account_list_with_suffix_v2) | `GET /v2/accounts/{suffix}` | AC | test edilmedi | test edilmedi |
| [`account_transactions_v2`](#account_transactions_v2) | `GET /v2/accounts/{suffix}/transactions` | AC | test edildi | test edilmedi |
| [`receipt_v1`](#receipt_v1) | `GET /v1/accounts/{suffix}/transactions/{businessKey}` | AC | test edildi | test edilmedi |
| [`receipt_v2`](#receipt_v2) | `POST /v2/accounts/transactions/receipts` | AC | test edildi | test edilmedi |

## `account_list_v2` { #account_list_v2 }

**Account List V2** · `GET /v2/accounts` · kapsam `accounts` · authorization code (müşteri girişi gerekir)

This API is used to retrieve the account list of the customer associated with the authorization context. The response includes account details such as account number, account suffix, balance, available balance, currency information, IBAN, account type, branch information, customer name, maturity dates and account status. The account list can be filtered by account suffix and optional account status or balance filters.

```python
yanit = kt.tpp_accounts.account_list_v2()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — müşteri girişiyle elle test edildi (Sandık banka hesabı entegrasyonu oturumu); alanlar dokümanla aynı | 2026-10-03 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | sorgu | tam sayı |  | Account suffix used to retrieve a specific account. |
| `only_has_available_balance` | `onlyHasAvailableBalance` | sorgu | bool |  | Indicates whether only accounts with available balance should be returned. |
| `only_open` | `onlyOpen` | sorgu | bool |  | Indicates whether only open accounts should be returned. |
| `only_with_no_balance` | `onlyWithNoBalance` | sorgu | bool |  | Indicates whether only accounts with no balance should be returned. |
| `only_current` | `onlyCurrent` | sorgu | bool |  | Indicates whether only current accounts should be returned. |
| `shared_with_multi_signature` | `sharedWithMultiSignature` | sorgu | bool |  | Indicates whether shared accounts requiring multiple signatures should be included. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountList`, `accountNumber`, `name`, `suffix`, `balance`, `availableBalance`, `fxId`, `fxCode`, `iban`, `type`, `openDate`, `branchName`, `branchId`, `withHoldingAmount`, `customerName`, `maturityBeginDate`, `maturityEndDate`, `isActive`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-list-v2)

## `account_list_with_suffix_v2` { #account_list_with_suffix_v2 }

**Account List V2 (withouth suffix)** · `GET /v2/accounts/{suffix}` · kapsam `accounts` · authorization code (müşteri girişi gerekir)

Retrieves the account information for the authenticated customer by account suffix. The response includes account details such as balance, available balance, currency, IBAN, account type, branch information, maturity dates and account status.

```python
yanit = kt.tpp_accounts.account_list_with_suffix_v2(suffix=..., customer_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | yol | tam sayı | evet | Account suffix used to retrieve a specific account. |
| `customer_id` | `CustomerId` | sorgu | tam sayı | evet | Customer number used to retrieve the account list. |
| `language_id` | `LanguageId` | sorgu | tam sayı |  | Language identifier used for localized account information. |
| `only_has_available_balance` | `onlyHasAvailableBalance` | sorgu | bool |  | Indicates whether only accounts with available balance should be returned. |
| `only_open` | `onlyOpen` | sorgu | bool |  | Indicates whether only open accounts should be returned. |
| `only_with_no_balance` | `onlyWithNoBalance` | sorgu | bool |  | Indicates whether only accounts with no balance should be returned. |
| `only_current` | `onlyCurrent` | sorgu | bool |  | Indicates whether only current accounts should be returned. |
| `shared_with_multi_signature` | `sharedWithMultiSignature` | sorgu | bool |  | Indicates whether accounts shared with multi-signature authorization should be included. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountList`, `accountNumber`, `name`, `suffix`, `availableBalance`, `fxId`, `fxCode`, `iban`, `type`, `openDate`, `branchName`, `branchId`, `withHoldingAmount`, `customerName`, `maturityBeginDate`, `maturityEndDate`, `isActive`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/account-list-v2-withouth-suffix)

## `account_transactions_v2` { #account_transactions_v2 }

**Account Transactions V2** · `GET /v2/accounts/{suffix}/transactions` · kapsam `accounts` · authorization code (müşteri girişi gerekir)

This API is used to retrieve account transaction history for the specified account suffix of the customer associated with the authorization context. The transaction list can be filtered by item count, begin date and end date. The response includes transaction details such as transaction date, description, amount, balance, transaction reference, transaction ID, currency code, transaction code, sequence number, sender/receiver identity information and resource code.

```python
yanit = kt.tpp_accounts.account_transactions_v2(suffix=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — müşteri girişiyle elle test edildi (Sandık banka hesabı entegrasyonu oturumu); 22 kayıt, tarih filtresi tutarsız | 2026-10-03 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | yol | tam sayı | evet | Account suffix for which transaction records will be retrieved. This value is sent as a route parameter. |
| `item_count` | `itemCount` | sorgu | tam sayı |  | Maximum number of account activity records to be returned. |
| `begin_date` | `beginDate` | sorgu | tarih |  | Start date from which account activity records will be retrieved. |
| `end_date` | `endDate` | sorgu | tarih |  | End date until which account activity records will be retrieved. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountActivities`, `suffix`, `date`, `description`, `amount`, `balance`, `transactionReference`, `transactionId`, `fxCode`, `transactionCode`, `seqNum`, `receiverTCKNorVKN`, `senderTCKNorVKN`, `resourceCode`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-transactions-v2)

## `receipt_v1` { #receipt_v1 }

**Receipt** · `GET /v1/accounts/{suffix}/transactions/{businessKey}` · kapsam `accounts` · authorization code (müşteri girişi gerekir)

Returns the receipt values of the transaction that is given by the businesskey. The API response is divided into four parts in order to help visualize the receipt: "leftHeader, rightHeader, body, footer". The entire data in these properties is also available in the slipList property.

```python
yanit = kt.tpp_accounts.receipt_v1(suffix=..., business_key=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — müşteri girişiyle elle test edildi (Sandık banka hesabı entegrasyonu oturumu); üç farklı hareketle 404 Path not found | 2026-10-03 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `suffix` | `suffix` | yol | metin | evet |  |
| `business_key` | `businessKey` | yol | metin | evet |  |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/receipt)

## `receipt_v2` { #receipt_v2 }

**Receipt V2** · `POST /v2/accounts/transactions/receipts` · kapsam `accounts` · authorization code (müşteri girişi gerekir)

This API is used to retrieve receipt information for a transaction identified by the transactionReference value. The service returns receipt details such as title, description, amount, currency information and receipt sections including slip list, left header, right header, body and footer.

```python
yanit = kt.tpp_accounts.receipt_v2(transaction_reference=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor, içerik boş — müşteri girişiyle elle test edildi (Sandık banka hesabı entegrasyonu oturumu); denenen iki harekette slipList yok | 2026-10-03 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_reference` | `transactionReference` | gövde | metin | evet | Encrypted transaction reference value for which receipt information will be retrieved. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `title`, `description`, `amount`, `fecName`, `slipList`, `key`, `leftHeader`, `rightHeader`, `body`, `footer`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/receipt-v2)
