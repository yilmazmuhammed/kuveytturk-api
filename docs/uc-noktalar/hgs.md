<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.hgs

HGS servisleri · 3 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`hgs_balance_information`](#hgs_balance_information) | `POST /v1/hgs/balance-info` | CC |
| [`hgs_product_information`](#hgs_product_information) | `POST /v1/hgs/product-info` | CC |
| [`hgs_usage_transactions`](#hgs_usage_transactions) | `POST /v1/hgs/usage-transactions` | CC |

## `hgs_balance_information` { #hgs_balance_information }

**HGS Balance Information** · `POST /v1/hgs/balance-info` · kapsam `public` · client credentials

This API takes plate and HGS barcode numbers as request parameters and returns the HGS balance information in detail. The response includes barcode number, balance, system date, and transaction status information.

```python
yanit = kt.hgs.hgs_balance_information(plate_no=..., barcodeno=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `plate_no` | `plateNo` | gövde | metin | evet | Represents the plate number of the vehicle. |
| `barcodeno` | `barcodeno` | gövde | metin | evet | Represents the HGS barcode number. |

Yanıt alanları (dokümana göre): `barcodeNo`, `Status`, `balance`, `systemDate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-balance-information)

## `hgs_product_information` { #hgs_product_information }

**HGS Product Information** · `POST /v1/hgs/product-info` · kapsam `public` · client credentials

This API takes plate number and HGS barcode number as request parameters and returns the product details of the related HGS barcode. The response includes barcode number, plate number, balance, product status, cancellation date, sales date, vehicle class, and payment type information.

```python
yanit = kt.hgs.hgs_product_information(plate_no=..., barcodeno=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `plate_no` | `plateNo` | gövde | metin | evet | Represents the plate number of the vehicle. |
| `barcodeno` | `barcodeno` | gövde | metin | evet | Represents the HGS barcode number. |

Yanıt alanları (dokümana göre): `barcodeNo`, `plateNo`, `balance`, `productStatusDescription`, `cancelDate`, `salesDate`, `vehicleClass`, `paymentType`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-product-information)

## `hgs_usage_transactions` { #hgs_usage_transactions }

**HGS Usage Transactions** · `POST /v1/hgs/usage-transactions` · kapsam `public` · client credentials

This API returns HGS usage transaction information for the customer. It takes plate number, HGS barcode number, start date, and end date as request parameters. The response includes order number, entry and exit date/time, entry and exit locations, description, and amount information.

```python
yanit = kt.hgs.hgs_usage_transactions(plate_no=..., barcode_no=..., start=..., end=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `plate_no` | `plateNo` | gövde | metin | evet | Represents the plate number of the vehicle. |
| `barcode_no` | `barcodeNo` | gövde | metin | evet | Represents the HGS barcode number. |
| `start` | `start` | gövde | metin | evet | Represents the start date for querying HGS usage transactions. |
| `end` | `end` | gövde | metin | evet | Represents the end date for querying HGS usage transactions. |

Yanıt alanları (dokümana göre): `OrderNo`, `entryDateTime`, `exitDateTime`, `entryLocation`, `exitLocation`, `description`, `amount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-usage-transactions)
