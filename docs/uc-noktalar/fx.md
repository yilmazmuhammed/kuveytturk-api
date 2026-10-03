<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.fx

Döviz işlemleri · 5 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`fx_currency_buy`](#fx_currency_buy) | `POST /v1/fx/buy` | CC |
| [`fx_currency_list`](#fx_currency_list) | `GET /v1/data/fecs` | CC |
| [`fx_currency_rates`](#fx_currency_rates) | `GET /v2/fx/rates` | CC |
| [`fx_currency_sell`](#fx_currency_sell) | `POST /v1/fx/sell` | CC |
| [`fx_transaction_history`](#fx_transaction_history) | `POST /v1/fx/fxtransactions` | CC |

## `fx_currency_buy` { #fx_currency_buy }

**FX Currency Buy** · `POST /v1/fx/buy` · kapsam `public` · client credentials

This API is used to perform a foreign exchange buy transaction. The customer account number and language information are retrieved from the authorization context. The request includes source account suffix, target account suffix, corporate web user name, buy rate, foreign currency amount and TL amount. The response returns transaction amount, currency amount, applied FX rate, tax information and execution reference information.

```python
yanit = kt.fx.fx_currency_buy(account_suffix_from=..., account_suffix_to=..., buy_rate=..., exchange_amount=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_suffix_from` | `AccountSuffixFrom` | gövde | tam sayı | evet | Source account suffix from which the TL amount will be withdrawn. |
| `account_suffix_to` | `AccountSuffixTo` | gövde | tam sayı | evet | Target account suffix where the purchased foreign currency will be deposited. |
| `corporate_web_user_name` | `CorporateWebUserName` | gövde | metin |  | Corporate web user name used to perform the transaction. |
| `buy_rate` | `BuyRate` | gövde | sayı | evet | Foreign exchange buy rate used for the transaction. |
| `exchange_amount` | `ExchangeAmount` | gövde | sayı | evet | Amount of foreign currency to be purchased. |
| `tl_amount` | `TLAmount` | gövde | sayı |  | TL amount of the transaction. |

Yanıt alanları (dokümana göre): `ExecutionReferenceId`, `FromFec`, `ToFec`, `TransactionAmount`, `CurrencyAmount`, `FxRate`, `TaxFecCode`, `TaxAmount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-buy)

## `fx_currency_list` { #fx_currency_list }

**FX Currency List** · `GET /v1/data/fecs` · kapsam `public` · client credentials

This API is used to retrieve currency information. The response returns currency details such as ISO code, international code, FEC name, FEC code, FEC group and FEC ID.

```python
yanit = kt.fx.fx_currency_list()
```

Yanıt alanları (dokümana göre): `isoCode`, `internationalCode`, `name`, `code`, `group`, `id`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-list)

## `fx_currency_rates` { #fx_currency_rates }

**FX Currency Rates** · `GET /v2/fx/rates` · kapsam `public` · client credentials

This API is used to retrieve foreign exchange rates for the customer account associated with the client configuration. The response returns currency name, currency code, buy rate, sell rate and spread status information.

```python
yanit = kt.fx.fx_currency_rates()
```

Yanıt alanları (dokümana göre): `name`, `fxCode`, `buyRate`, `sellRate`, `isSpreadApplied`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-rates)

## `fx_currency_sell` { #fx_currency_sell }

**FX Currency Sell** · `POST /v1/fx/sell` · kapsam `public` · client credentials

This API is used to perform a foreign exchange sell transaction. The customer account number and language information are retrieved from the authorization context. The request includes source account suffix, target account suffix, corporate web user name, sell rate, foreign currency amount and TL amount. The response returns transaction amount, currency amount, applied FX rate and execution reference information.

```python
yanit = kt.fx.fx_currency_sell(account_suffix_from=..., account_suffix_to=..., sell_rate=..., exchange_amount=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_suffix_from` | `AccountSuffixFrom` | gövde | tam sayı | evet | Source foreign currency account suffix from which the exchange amount will be withdrawn. |
| `account_suffix_to` | `AccountSuffixTo` | gövde | tam sayı | evet | Target account suffix where the TL amount will be deposited. |
| `corporate_web_user_name` | `CorporateWebUserName` | gövde | metin |  | Corporate web user name used to perform the transaction. |
| `sell_rate` | `SellRate` | gövde | sayı | evet | Foreign exchange sell rate used for the transaction. |
| `exchange_amount` | `ExchangeAmount` | gövde | sayı | evet | Amount of foreign currency to be sold. |
| `tl_amount` | `TLAmount` | gövde | sayı |  | TL amount of the transaction. |

Yanıt alanları (dokümana göre): `ExecutionReferenceId`, `FromFec`, `ToFec`, `TransactionAmount`, `CurrencyAmount`, `FxRate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-sell)

## `fx_transaction_history` { #fx_transaction_history }

**FX Transaction History** · `POST /v1/fx/fxtransactions` · kapsam `public` · client credentials

This API is used to initiate an internal money transfer transaction based on the customer account number from the authorization context. The request contains money transfer contract information including sender account suffix, receiver account information, transfer amount, transfer description and transfer type. The response returns the transaction execution reference and the created money transfer transaction ID.

```python
yanit = kt.fx.fx_transaction_history(sender_account_suffix=..., receiver_account_number=..., receiver_account_suffix=..., money_transfer_amount=..., transfer_type=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `senderAccountSuffix` | gövde | tam sayı | evet | Sender account suffix number from which the money transfer amount will be withdrawn. |
| `receiver_account_number` | `receiverAccountNumber` | gövde | tam sayı | evet | Receiver customer account number to which the money transfer will be sent. |
| `receiver_account_suffix` | `receiverAccountSuffix` | gövde | tam sayı | evet | Receiver account suffix number to which the money transfer will be sent. |
| `money_transfer_description` | `moneyTransferDescription` | gövde | metin |  | Description or comment added to the money transfer transaction. |
| `money_transfer_amount` | `moneyTransferAmount` | gövde | sayı | evet | Amount that will be transferred. |
| `transfer_type` | `transferType` | gövde | tam sayı | evet | Money transfer type used to identify the transfer scenario. |

Gövde alanları istekte `request` → `moneyTransferContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `executionReferenceId`, `moneyTransferTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-transaction-history)
