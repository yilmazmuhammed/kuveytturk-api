<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.cards

Kredi kartı işlemleri · 4 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`credit_card_list_v3`](#credit_card_list_v3) | `GET /v3/creditcard/cardlist` | CC | test edildi | test edilmedi |
| [`credit_card_money_transfer`](#credit_card_money_transfer) | `POST /v1/moneytransfer/creditcardmoneytransfer` | CC | test edilmedi | test edilmedi |
| [`credit_card_transactions_list_v3`](#credit_card_transactions_list_v3) | `GET /v3/creditcard/{cardnumber}/transactions` | CC | test edilmedi | test edilmedi |
| [`virtual_card_limit_update`](#virtual_card_limit_update) | `POST /v1/cards/virtualcardlimitupdate` | AC | test edilmedi | test edilmedi |

## `credit_card_list_v3` { #credit_card_list_v3 }

**Credit Card List V3** · `GET /v3/creditcard/cardlist` · kapsam `cards` · client credentials

This API is used to retrieve the credit card list for the customer. The response returns card information such as masked card number, shadow card number, expiration date, card holder name, card type and supplementary card type.

```python
yanit = kt.cards.credit_card_list_v3()
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — creditCardListResponseModel: 2 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | sorgu | metin |  | Customer number for which the credit card list will be retrieved. |

Yanıt alanları (dokümana göre): `cardList`, `maskedCardNumber`, `shadowCardNumber`, `expireDate`, `ownerName`, `cardType`, `supplementaryCardType`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-list-v3)

## `credit_card_money_transfer` { #credit_card_money_transfer }

**Credit Card Money Transfer** · `POST /v1/moneytransfer/creditcardmoneytransfer` · kapsam `transfers` · client credentials

This API is used to initiate a money transfer transaction from a customer account to a credit card. The customer account number is retrieved from the authorization context. The request includes sender account suffix, receiver account information, transfer amount, transfer description and transfer type. The response returns the transaction execution reference and the created money transfer transaction ID.

```python
yanit = kt.cards.credit_card_money_transfer(sender_account_suffix=..., receiver_account_number=..., receiver_account_suffix=..., money_transfer_amount=..., transfer_type=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `sender_account_suffix` | `senderAccountSuffix` | gövde | tam sayı | evet | Sender account suffix number from which the money transfer amount will be withdrawn. |
| `receiver_account_number` | `receiverAccountNumber` | gövde | tam sayı | evet | Receiver account number associated with the credit card money transfer. |
| `receiver_account_suffix` | `receiverAccountSuffix` | gövde | tam sayı | evet | Receiver account suffix associated with the credit card money transfer. |
| `money_transfer_description` | `moneyTransferDescription` | gövde | metin |  | Description or comment added to the money transfer transaction. |
| `money_transfer_amount` | `moneyTransferAmount` | gövde | sayı | evet | Amount that will be transferred. |
| `transfer_type` | `transferType` | gövde | tam sayı | evet | Money transfer type used to identify the transfer scenario. |

Yanıt alanları (dokümana göre): `executionReferenceId`, `moneyTransferTransactionId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-money-transfer)

## `credit_card_transactions_list_v3` { #credit_card_transactions_list_v3 }

**Credit Card Transactions List V3** · `GET /v3/creditcard/{cardnumber}/transactions` · kapsam `cards` · client credentials

This API is used to retrieve credit card transaction information for the specified card number. The response includes pending provision transactions and current credit card transactions.

```python
yanit = kt.cards.credit_card_transactions_list_v3(cardnumber=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | parametre değeri bilinmiyor — yol parametresi: cardnumber | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `cardnumber` | `cardnumber` | yol | metin | evet | Credit card number for which transaction information will be retrieved. This value is sent as a route parameter. |

Yanıt alanları (dokümana göre): `cardPendingProvisionInfoResponseModel`, `creditCardStatementTransactionType`, `amount`, `message`, `transactionDate`, `transactionHour`, `fecCode`, `domesticAmount`, `originalAmount`, `mccGroupCode`, `currentTransactionInfoResponseModel`, `transactionId`, `category`, `currencyDef`, `earnedGoldPoint`, `installmentNumber`, `isTransactionRefund`, `isTrnIncludeInstallment`, `mechantName`, `shadowCardNumber`, `transactionAmount`, `transactionTime`, `bkmUniqueMerchantId`, `totalInstallmentAmount`, `provisionNumber`, `errors`, `executionReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-transactions-list-v3)

## `virtual_card_limit_update` { #virtual_card_limit_update }

**Virtual Card Limit Update** · `POST /v1/cards/virtualcardlimitupdate` · kapsam `cards` · authorization code (müşteri girişi gerekir)

This API updates the limit of a virtual credit card for the authenticated customer. &gt; This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.cards.virtual_card_limit_update(credit_card_number=..., limit=..., customer_id=..., language_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `credit_card_number` | `CreditCardNumber` | gövde | metin | evet | Virtual credit card number whose limit will be updated. |
| `limit` | `Limit` | gövde | sayı | evet | New limit amount to be assigned to the virtual credit card. |
| `customer_id` | `CustomerId` | gövde | tam sayı | evet | Unique customer identifier. |
| `language_id` | `LanguageId` | gövde | tam sayı | evet | Language identifier used for localized messages and responses. |

Gövde alanları istekte `request` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/virtual-card-limit-update)
