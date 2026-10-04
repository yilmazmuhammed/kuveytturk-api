<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.sms_otp

SMS / OTP · 5 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`pr_customer_validation`](#pr_customer_validation) | `POST /v1/paymentrequest/customerValidation` | CC | test edilmedi | test edilmedi |
| [`pr_get_account_details_by_iban`](#pr_get_account_details_by_iban) | `POST /v1/paymentrequest/getAccountByIban` | CC | test edilmedi | test edilmedi |
| [`pr_get_fast_result`](#pr_get_fast_result) | `GET /v1/paymentrequest/getFastResult` | CC | test edildi | test edilmedi |
| [`pr_payment_request_control`](#pr_payment_request_control) | `POST /v1/paymentrequest/paymentControl` | CC | test edilmedi | test edilmedi |
| [`pr_payment_transaction`](#pr_payment_transaction) | `POST /v1/paymentrequest/transfer` | CC | test edilmedi | test edilmedi |

## `pr_customer_validation` { #pr_customer_validation }

**PR - Customer Validation** · `POST /v1/paymentrequest/customerValidation` · kapsam `public` · client credentials

Validates customer information for payment request operations by using the provided IBAN and title. The response includes customer, IBAN, title match, payment request permission, customer status, language, FAST limit, customer type, and result details.

```python
yanit = kt.sms_otp.pr_customer_validation(iban=..., title=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `iban` | `iban` | gövde | metin | evet | IBAN used to validate the customer for payment request operations. |
| `title` | `title` | gövde | metin | evet | Customer title used to validate title matching for the provided IBAN. |

Yanıt alanları (dokümana göre): `customerId`, `isIbanFound`, `isIbanActive`, `isTitleMatch`, `isPaymentRequestAllowed`, `isCustomerActive`, `languageId`, `fastLimit`, `customerType`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-customer-validation)

## `pr_get_account_details_by_iban` { #pr_get_account_details_by_iban }

**PR - Get Account Details By IBAN** · `POST /v1/paymentrequest/getAccountByIban` · kapsam `accounts` · client credentials

Retrieves account balance information for payment request operations by using the provided IBAN and account number. The response includes balance and blocked balance details for the related account.

```python
yanit = kt.sms_otp.pr_get_account_details_by_iban(i_ban=..., account_number=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `i_ban` | `iBAN` | gövde | metin | evet | IBAN used to retrieve account balance details. |
| `account_number` | `accountNumber` | gövde | tam sayı | evet | Account number used together with the IBAN to retrieve account balance details. |

Yanıt alanları (dokümana göre): `balance`, `blockedBalance`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-account-details-by-iban)

## `pr_get_fast_result` { #pr_get_fast_result }

**PR - Get FAST Result** · `GET /v1/paymentrequest/getFastResult` · kapsam `public` · client credentials

Retrieves the FAST transaction result for payment request operations by using the provided OI reference number. The response includes the transfer completion date and result code of the related FAST transaction.

```python
yanit = kt.sms_otp.pr_get_fast_result(oi_reference=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: GET and path: /v1/paymentrequest/getFastResult'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `oi_reference` | `oiReference` | sorgu | metin | evet | OI reference number used to retrieve the FAST transaction result. |

Yanıt alanları (dokümana göre): `transferCompleteDate`, `resultCode`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-fast-result)

## `pr_payment_request_control` { #pr_payment_request_control }

**PR - Payment Request Control** · `POST /v1/paymentrequest/paymentControl` · kapsam `public` · client credentials

Checks and validates a payment request by using the provided payment reference, flow type, creditor identity, creditor title, creditor IBAN, amount, and payment intent information. The response returns the payment request control result, return code, and validation result details.

```python
yanit = kt.sms_otp.pr_payment_request_control(request_payment_reference=..., request_payment_flow_type=..., creditor_identity_value=..., creditor_title=..., creditor_iban=..., amount=..., payment_intent=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `request_payment_reference` | `requestPaymentReference` | gövde | metin | evet | Payment request reference number used to identify the payment request. |
| `request_payment_flow_type` | `requestPaymentFlowType` | gövde | metin | evet | Flow type of the payment request. |
| `creditor_identity_value` | `creditorIdentityValue` | gövde | metin | evet | Identity value of the creditor. |
| `creditor_title` | `creditorTitle` | gövde | metin | evet | Title or name of the creditor. |
| `creditor_iban` | `creditorIBAN` | gövde | metin | evet | IBAN of the creditor account. |
| `amount` | `amount` | gövde | metin | evet | Payment request amount. |
| `payment_intent` | `paymentIntent` | gövde | metin | evet | Payment intent or purpose information of the payment request. |

Yanıt alanları (dokümana göre): `isSuccess`, `returnCode`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-request-control)

## `pr_payment_transaction` { #pr_payment_transaction }

**PR - Payment Transaction** · `POST /v1/paymentrequest/transfer` · kapsam `transfers` · client credentials

Retrieves the account list for payment request transfer operations according to the provided customer, language, account suffix, balance, account status, current account, and multi-signature sharing filters. The response includes account details such as account name, suffix, balance, available balance, currency, IBAN, product type, opening date, branch information, customer name, maturity dates, and active status.

```python
yanit = kt.sms_otp.pr_payment_transaction(account_number=..., language_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_number` | `accountNumber` | gövde | tam sayı | evet | Customer account number used to retrieve the account list. |
| `language_id` | `languageId` | gövde | tam sayı | evet | Language identifier used for account information and descriptions. |
| `account_suffix` | `accountSuffix` | gövde | tam sayı |  | Account suffix used to filter the account list. |
| `only_has_avaible_balance` | `onlyHasAvaibleBalance` | gövde | bool |  | Indicates whether only accounts with available balance should be returned. |
| `only_open` | `onlyOpen` | gövde | bool |  | Indicates whether only open accounts should be returned. |
| `only_with_no_balance` | `onlyWithNoBalance` | gövde | bool |  | Indicates whether only accounts with no balance should be returned. |
| `only_current` | `onlyCurrent` | gövde | bool |  | Indicates whether only current accounts should be returned. |
| `shared_with_multi_signature` | `sharedWithMultiSignature` | gövde | bool |  | Indicates whether accounts shared with multi-signature authorization should be included. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `accountList`, `name`, `suffix`, `fxId`, `iban`, `type`, `openDate`, `branchName`, `branchId`, `withHoldingAmount`, `customerName`, `maturityBeginDate`, `maturityEndDate`, `isActive`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-transaction)
