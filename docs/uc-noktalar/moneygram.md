<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.moneygram

MoneyGram · 6 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`money_gram_country_list`](#money_gram_country_list) | `GET /v1/moneygram/countrylist` | CC | test edildi | test edilmedi |
| [`money_gram_currency_list`](#money_gram_currency_list) | `GET /v1/moneygram/currencylist` | CC | test edildi | test edilmedi |
| [`money_gram_get_fee`](#money_gram_get_fee) | `POST /v1/moneygram/getfee` | AC | test edilmedi | test edilmedi |
| [`money_gram_query_fee`](#money_gram_query_fee) | `GET /v1/moneygram/queryfee` | CC | test edildi | test edilmedi |
| [`money_gram_query_reference`](#money_gram_query_reference) | `POST /v1/moneygram/queryreference` | AC | test edilmedi | test edilmedi |
| [`money_gram_send`](#money_gram_send) | `POST /v1/moneygram/send` | AC | test edilmedi | test edilmedi |

## `money_gram_country_list` { #money_gram_country_list }

**MoneyGram Country List** · `GET /v1/moneygram/countrylist` · kapsam `public` · client credentials

&lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and response models may change over time. &lt;/div&gt; Returns the list of countries within MoneyGram Payment System.

```python
yanit = kt.moneygram.money_gram_country_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: GET and path: /v1/moneygram/countrylist'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `countryCode`, `countryName`, `countryNameTR`, `baseReceiveCurrency`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-country-list)

## `money_gram_currency_list` { #money_gram_currency_list }

**MoneyGram Currency List** · `GET /v1/moneygram/currencylist` · kapsam `public` · client credentials

&lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and response models may change over time. &lt;/div&gt; Returns the list of currencies of interested countries within Moneygram Payment System.

```python
yanit = kt.moneygram.money_gram_currency_list()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: GET and path: /v1/moneygram/currencylist'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

Yanıt alanları (dokümana göre): `currencyCode`, `currencyName`, `currencyNameTR`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-currency-list)

## `money_gram_get_fee` { #money_gram_get_fee }

**MoneyGram Get Fee** · `POST /v1/moneygram/getfee` · kapsam `transfers` · authorization code (müşteri girişi gerekir)

Get fee results. Countries can pay only with allowed currencies. In order to proceed the transfer, sender must select payment type accordibg these results. The parameters sent include receiveCountry, amount, and choiceType.

```python
yanit = kt.moneygram.money_gram_get_fee(receive_country=..., send_currency=..., amount=..., choice_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `receive_country` | `receiveCountry` | gövde | metin | evet | Indicates receive country code info. |
| `send_currency` | `sendCurrency` | gövde | metin | evet | Indicates send currency code info. |
| `amount` | `amount` | gövde | sayı | evet | Amount that will be sent. |
| `choice_type` | `choiceType` | gövde | tam sayı | evet | Fee type according to send amount. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-get-fee)

## `money_gram_query_fee` { #money_gram_query_fee }

**MoneyGram Query Fee** · `GET /v1/moneygram/queryfee` · kapsam `transfers` · client credentials

Get fee results. Countries can pay only with allowed currencies. In order to proceed the transfer, sender must select payment type accordibg these results. The parameters sent include receiveCountry, amount, and choiceType.

```python
yanit = kt.moneygram.money_gram_query_fee(receive_country=..., amount=..., choice_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | bu ortamda yok (404) — {'code': 404, 'message': 'Path not found. Method: GET and path: /v1/moneygram/queryfee'} | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `receive_country` | `receiveCountry` | sorgu | metin | evet | Indicates receive country code info. |
| `amount` | `amount` | sorgu | sayı | evet | Amount that will be sent. |
| `choice_type` | `choiceType` | sorgu | tam sayı | evet | Fee type according to send amount. |

Yanıt alanları (dokümana göre): `sendAmount`, `feeAmount`, `sendCurrency`, `totalAmount`, `validReceiveAmount`, `validReceiveCurrency`, `validExchangeRate`, `receiveCountryName`, `deliveryOption`, `deliveryOptionNameTR`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-fee)

## `money_gram_query_reference` { #money_gram_query_reference }

**MoneyGram Query Reference** · `POST /v1/moneygram/queryreference` · kapsam `transfers` · authorization code (müşteri girişi gerekir)

According the reference number, returns detail informations about the money transfer.

```python
yanit = kt.moneygram.money_gram_query_reference(reference_number=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | müşteri girişi gerekiyor | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_number` | `referenceNumber` | gövde | metin | evet | Transaction reference number. |

Yanıt alanları (dokümana göre): `ReferenceNumber`, `TransactionStatusTR`, `SenderFirstName`, `SenderLastName`, `ReceiverFirstName`, `ReceiverLastName`, `DateTimeSent`, `ReceiveAmount`, `ReceiveCurrency`, `SenderCountry`, `DeliveryOption`, `SenderHomePhone`, `SenderAddress`, `OriginalSendFee`, `OriginalExchangeRate`, `SenderCity`, `ReceiverCountry`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-reference)

## `money_gram_send` { #money_gram_send }

**MoneyGram Send** · `POST /v1/moneygram/send` · kapsam `transfers` · authorization code (müşteri girişi gerekir)

According the customer information, sender person can send money to countries which moneygram payment system allows.In order to proceed the transfer, Kuveyt Turk sends a one-time-password via SMS to the customer and gives a transaction id to the developer, the customer enters the code to the third party app, and the third party app sends the id and the SMS code to Kuveyt Turk via “Moneygram Send” API.If the id and the sms codes match, then Kuveyt Turk authenticates the transaction.

```python
yanit = kt.moneygram.money_gram_send()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `transaction_contract` | `TransactionContract` | gövde | nesne |  |  |
| `sender_customer` | `SenderCustomer` | gövde | nesne |  |  |
| `receiver_customer` | `ReceiverCustomer` | gövde | nesne |  |  |

Gövde alanları istekte `MoneyGramTranContract` → `SendMoneygramContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `ReferenceNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-send)
