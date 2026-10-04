<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.information

Bilgi servisleri (şube, ATM, parametre sorguları...) · 12 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`bank_branch_list`](#bank_branch_list) | `GET /v1/data/banks/{bankId}/branches` | CC | test edilmedi | test edilmedi |
| [`bank_list`](#bank_list) | `GET /v1/data/banks` | CC | test edildi | test edilmedi |
| [`calculate_profit_share_rate`](#calculate_profit_share_rate) | `POST /v1/calculateprofitsharerate` | CC | test edildi | test edilmedi |
| [`central_notification`](#central_notification) | `POST /v1/notification/sendInfEng` | CC | test edilmedi | test edilmedi |
| [`collect_installment`](#collect_installment) | `POST /v1/collections/collectInstallment` | CC | test edilmedi | test edilmedi |
| [`collection_list`](#collection_list) | `POST /v1/collections` | CC | test edildi | test edilmedi |
| [`get_class_info`](#get_class_info) | `POST /v1/erp/lms/getClassInfo` | CC | test edildi | test edilmedi |
| [`iban_validation_utility`](#iban_validation_utility) | `POST /v1/validation/ibanvalidator` | CC | test edildi | test edilmedi |
| [`kuveyt_turk_atm_list`](#kuveyt_turk_atm_list) | `GET /v1/data/atms` | CC | test edildi | test edilmedi |
| [`kuveyt_turk_branch_list`](#kuveyt_turk_branch_list) | `GET /v1/data/branches` | CC | test edildi | test edilmedi |
| [`kuveyt_turk_xtm_list`](#kuveyt_turk_xtm_list) | `GET /v1/data/xtms` | CC | test edildi | test edilmedi |
| [`loan_finance_calculation_parameter`](#loan_finance_calculation_parameter) | `GET /v1/data/loans` | CC | test edilmedi | test edilmedi |

## `bank_branch_list` { #bank_branch_list }

**Bank Branch List** · `GET /v1/data/banks/{bankId}/branches` · kapsam `public` · client credentials

Returns the list of branches of given bank id and city id within Turkish Banking System.

```python
yanit = kt.information.bank_branch_list(bank_id=..., city_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | parametre değeri bilinmiyor — yol parametresi: bankId | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `bank_id` | `bankId` | yol | tam sayı | evet | Bank code for listing branches |
| `city_id` | `cityId` | sorgu | tam sayı | evet | Specify the city of branches |

Yanıt alanları (dokümana göre): `branchId`, `name`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/bank-branch-list)

## `bank_list` { #bank_list }

**Bank List** · `GET /v1/data/banks` · kapsam `public` · client credentials

Returns the list of banks within Turkish Banking System.

```python
yanit = kt.information.bank_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — 52 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `bankId`, `name`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/bank-list)

## `calculate_profit_share_rate` { #calculate_profit_share_rate }

**Calculate Profit Share Rate** · `POST /v1/calculateprofitsharerate` · kapsam `public` · client credentials

This API calculates the profit share rate according to Kuveyt Turk rates and gives information about the profit to be obtained.

```python
yanit = kt.information.calculate_profit_share_rate(expire_day=..., fx_type=..., product=..., amount=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | sunucu hatası — İşleminiz gerçekleştirilemedi. Daha sonra tekrar deneyiniz. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `expire_day` | `expireDay` | gövde | tam sayı | evet | Specifies the number of days to be due. Takes the max value of 999 |
| `fx_type` | `fxType` | gövde | tam sayı | evet | Specifies the type of currency to be calculated. (Takes the value "0" for TL.), (Takes the value "1" for USD.), (Takes the value "19" for EUR), (Takes the value "24" for XAU(gr). ) |
| `product` | `product` | gövde | tam sayı | evet | Specifies the product group to be calculated. (It takes the value "2" for the participation account.), (It takes the value "3" for the participation account with interim profit share payment.) |
| `amount` | `amount` | gövde | sayı | evet | Specifies the amount to be deposited into the participation account. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/calculate-profit-share-rate)

## `central_notification` { #central_notification }

**Central Notification** · `POST /v1/notification/sendInfEng` · kapsam `public` · client credentials

Sends a notification by using the provided template code, parameter list, request JSON, and request type. The response returns the notification operation identifier and operation result.

```python
yanit = kt.information.central_notification(template_code=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `template_code` | `templateCode` | gövde | metin | evet | Template code used to generate and send the notification. |
| `parameters` | `parameters` | gövde | liste |  | List of key-value parameters to be used in the notification template. |
| `request_json` | `requestJson` | gövde | metin |  | JSON request content related to the notification operation. |
| `request_type` | `requestType` | gövde | metin |  | Request type information used to classify or process the notification request. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification)

## `collect_installment` { #collect_installment }

**Collect Installment** · `POST /v1/collections/collectInstallment` · kapsam `loans` · client credentials

Collects the installment from the customer's account provided in the parameters.

```python
yanit = kt.information.collect_installment(process_id=..., account_number=..., account_suffix=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `process_id` | `processId` | gövde | tam sayı | evet | Installment Id. |
| `collection_account_number` | `collectionAccountNumber` | gövde | tam sayı |  |  |
| `collection_account_suffix` | `collectionAccountSuffix` | gövde | tam sayı |  |  |
| `account_number` | `accountNumber` | gövde | tam sayı | evet | The account number of the customer. |
| `account_suffix` | `accountSuffix` | gövde | tam sayı | evet | The account suffix number of the customer. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/collect-installment)

## `collection_list` { #collection_list }

**Collection List** · `POST /v1/collections` · kapsam `loans` · client credentials

Returns the list of collection records associated with the account number provided in the parameters.

```python
yanit = kt.information.collection_list(account_number=..., account_suffix=..., process_id=..., is_ptt_collection=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: POST and path: /v1/collections'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_number` | `accountNumber` | gövde | tam sayı | evet | The account number of the customer. |
| `account_suffix` | `accountSuffix` | gövde | tam sayı | evet | The account suffix number of the customer. |
| `process_id` | `processId` | gövde | tam sayı | evet | Installment Id. |
| `is_ptt_collection` | `isPTTCollection` | gövde | bool | evet | Whether the collection is the PTT Collection. |

Yanıt alanları (dokümana göre): `processId`, `installmentType`, `installmentTypeName`, `projectAccountNumber`, `projectAccountSuffix`, `projectBranchId`, `maturityDate`, `installmentAmount`, `debtFEC`, `isLeasing`, `customerMainState`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/collection-list)

## `get_class_info` { #get_class_info }

**Get Class Info** · `POST /v1/erp/lms/getClassInfo` · kapsam `public` · client credentials

To ensure that the active training information of the class is displayed on the screens placed at the doors of the classrooms.

```python
yanit = kt.information.get_class_info()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — nesne (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `classroom_id` | `classroomId` | gövde | tam sayı |  |  |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/get-class-info)

## `iban_validation_utility` { #iban_validation_utility }

**IBAN Validation Utility** · `POST /v1/validation/ibanvalidator` · kapsam `public` · client credentials

This API endpoint is a utility endpoint that performs validity control for a given IBAN (i.e. Internation Bank Identifier Number). The validity control is performed format-wise only. This implies that the existence/reality of the IBAN or its association with any Bank is not taken into concern during the validity control.

```python
yanit = kt.information.iban_validation_utility(iban=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: POST and path: /v1/validation/ibanvalidator'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `iban` | `iban` | gövde | metin | evet | This input parameter represents the IBAN (i.e. International Bank Identifier Number) that is associated with a bank account. Its usage is mandatory in the request call and It can be associated with any world-wide bank (i.e. it does not necessarly have to be associated with Kuveyt Turk). |

Yanıt alanları (dokümana göre): `IsValid`, `ValidationMessage`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/iban-validation-utility)

## `kuveyt_turk_atm_list` { #kuveyt_turk_atm_list }

**Kuveyt Turk ATM List** · `GET /v1/data/atms` · kapsam `public` · client credentials

Returns the list of off-site Kuveyt Turk ATMs.

```python
yanit = kt.information.kuveyt_turk_atm_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — 3 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `name`, `cityName`, `longitude`, `latitude`, `address`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-atm-list)

## `kuveyt_turk_branch_list` { #kuveyt_turk_branch_list }

**Kuveyt Turk Branch List** · `GET /v1/data/branches` · kapsam `public` · client credentials

Returns the list of Kuveyt Turk branches.

```python
yanit = kt.information.kuveyt_turk_branch_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — 4 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `name`, `cityName`, `longitude`, `latitude`, `address`, `phone`, `fax`, `email`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-branch-list)

## `kuveyt_turk_xtm_list` { #kuveyt_turk_xtm_list }

**Kuveyt Turk XTM List** · `GET /v1/data/xtms` · kapsam `public` · client credentials

Returns the list of Kuveyt Turk XTMs.

```python
yanit = kt.information.kuveyt_turk_xtm_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — 2 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `name`, `cityName`, `longitude`, `latitude`, `address`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-xtm-list)

## `loan_finance_calculation_parameter` { #loan_finance_calculation_parameter }

**Loan/Finance Calculation Parameter** · `GET /v1/data/loans` · kapsam `public` · client credentials

Returns the list of loan product types. This API is used to determine loan calculation parameters.

```python
yanit = kt.information.loan_finance_calculation_parameter()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | uygulamanın kapsam yetkisi yok — {'code': 403, 'message': 'Invalid Scope'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `productTypeCode`, `productName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/notification-services/loan-finance-calculation-parameter)
