<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.treasury

Hazine servisleri (kıymetli maden, kur) · 5 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`fx_and_precious_metal_rates`](#fx_and_precious_metal_rates) | `GET /v1/fx/rates` | CC |
| [`fx_and_precious_metals_transaction_history`](#fx_and_precious_metals_transaction_history) | `POST /v1/fx/fxtransactions` | CC |
| [`precious_metal_buy`](#precious_metal_buy) | `POST /v1/preciousmetal/buy` | CC |
| [`precious_metal_rates`](#precious_metal_rates) | `GET /v1/preciousmetal/rates` | CC |
| [`precious_metal_sell`](#precious_metal_sell) | `POST /v1/preciousmetal/sell` | CC |

## `fx_and_precious_metal_rates` { #fx_and_precious_metal_rates }

**FX and Precious Metal Rates** · `GET /v1/fx/rates` · kapsam `public` · client credentials

This API retrieves the current foreign exchange rates, including currency information, buy/sell rates and parity rates. Foreign exchange rates represent the bank's rates at the time the request is sent.

```python
yanit = kt.treasury.fx_and_precious_metal_rates()
```

Yanıt alanları (dokümana göre): `name`, `fxCode`, `fxId`, `buyRate`, `sellRate`, `parityBuyRate`, `paritySellRate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metal-rates)

## `fx_and_precious_metals_transaction_history` { #fx_and_precious_metals_transaction_history }

**FX and Precious Metals Transaction History** · `POST /v1/fx/fxtransactions` · kapsam `public` · client credentials

It carries out precious metal sales transactions.

```python
yanit = kt.treasury.fx_and_precious_metals_transaction_history(sender_account_suffix=..., receiver_account_number=..., receiver_account_suffix=..., money_transfer_description=..., money_transfer_amount=..., transfer_type=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `cm_customer_id` | `cm:CustomerId` | gövde | tam sayı |  |  |
| `sender_account_suffix` | `senderAccountSuffix` | gövde | tam sayı | evet | Sender account suffix for the account from which the amount will be transferred. |
| `receiver_account_number` | `receiverAccountNumber` | gövde | tam sayı | evet | Receiver account number to which the amount will be transferred. |
| `receiver_account_suffix` | `receiverAccountSuffix` | gövde | tam sayı | evet | Receiver account suffix for the target account. |
| `money_transfer_description` | `moneyTransferDescription` | gövde | metin | evet | Description of the money transfer transaction. |
| `money_transfer_amount` | `moneyTransferAmount` | gövde | sayı | evet | Amount to be transferred. |
| `transfer_type` | `transferType` | gövde | tam sayı | evet | Transfer type value that identifies the transaction type. |

Gövde alanları istekte `request` → `moneyTransferContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `executionReferenceId`, `moneyTransferTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metals-transaction-history)

## `precious_metal_buy` { #precious_metal_buy }

**Precious Metal Buy** · `POST /v1/preciousmetal/buy` · kapsam `public` · client credentials

Performs precious metal purchasing transactions. The request includes the source account, target precious metal account, corporate web user name, buy rate and precious metal amount. The response returns the transaction amount, currency amount, exchange rate and tax information for the completed transaction.

```python
yanit = kt.treasury.precious_metal_buy(account_suffix_from=..., account_suffix_to=..., corporate_web_user_name=..., buy_rate=..., exchange_amount=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `cm_customer_id` | `cm:CustomerId` | gövde | tam sayı |  |  |
| `cm_language_id` | `cm:LanguageId` | gövde | tam sayı |  |  |
| `account_suffix_from` | `AccountSuffixFrom` | gövde | tam sayı | evet | Additional number of the account from which the precious metal purchase amount will be withdrawn. |
| `account_suffix_to` | `AccountSuffixTo` | gövde | tam sayı | evet | Additional number of the account to which the purchased precious metal will be deposited. |
| `corporate_web_user_name` | `CorporateWebUserName` | gövde | metin | evet | Corporate web user name of the account owner performing the precious metal purchase transaction. |
| `buy_rate` | `BuyRate` | gövde | sayı | evet | Exchange rate at which the precious metal will be purchased. This value is obtained from the exchange rate API. |
| `exchange_amount` | `ExchangeAmount` | gövde | sayı | evet | Amount of precious metal to be purchased. |

Yanıt alanları (dokümana göre): `ExecutionReferenceId`, `FromFec`, `ToFec`, `TransactionAmount`, `CurrencyAmount`, `FxRate`, `TaxFecCode`, `TaxAmount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-buy)

## `precious_metal_rates` { #precious_metal_rates }

**Precious Metal Rates** · `GET /v1/preciousmetal/rates` · kapsam `public` · client credentials

A service for querying many common precious metal rates. Precious metal rates represent the bank's rates at the time the request is sent.

```python
yanit = kt.treasury.precious_metal_rates()
```

Yanıt alanları (dokümana göre): `FxName`, `FxCode`, `BuyRate`, `SellRate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-rates)

## `precious_metal_sell` { #precious_metal_sell }

**Precious Metal Sell** · `POST /v1/preciousmetal/sell` · kapsam `public` · client credentials

Performs precious metal sales transactions. The request includes the source precious metal account, target account, corporate web user name, sell rate and precious metal amount. The response returns the transaction amount, currency amount and exchange rate for the completed transaction.

```python
yanit = kt.treasury.precious_metal_sell(account_suffix_from=..., account_suffix_to=..., corporate_web_user_name=..., sell_rate=..., exchange_amount=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `cm_customer_id` | `cm:CustomerId` | gövde | tam sayı |  |  |
| `cm_language_id` | `cm:LanguageId` | gövde | tam sayı |  |  |
| `account_suffix_from` | `AccountSuffixFrom` | gövde | tam sayı | evet | Additional number of the account from which the precious metal amount will be withdrawn. |
| `account_suffix_to` | `AccountSuffixTo` | gövde | tam sayı | evet | Additional number of the account to which the sale amount will be deposited. |
| `corporate_web_user_name` | `CorporateWebUserName` | gövde | metin | evet | Corporate web user name of the account owner performing the precious metal sale transaction. |
| `sell_rate` | `SellRate` | gövde | sayı | evet | Exchange rate at which the precious metal will be sold. This value is obtained from the exchange rate API. |
| `exchange_amount` | `ExchangeAmount` | gövde | sayı | evet | Amount of precious metal to be sold. |

Yanıt alanları (dokümana göre): `ExecutionReferenceId`, `FromFec`, `ToFec`, `TransactionAmount`, `CurrencyAmount`, `FxRate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-sell)
