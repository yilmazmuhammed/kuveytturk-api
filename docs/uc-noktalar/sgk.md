<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.sgk

SGK · 1 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`consume_insurance_queue`](#consume_insurance_queue) | `POST /v1/insurance/consumeQueue` | CC | test edilmedi | test edilmedi |

## `consume_insurance_queue` { #consume_insurance_queue }

**Consume Insurance Queue** · `POST /v1/insurance/consumeQueue` · kapsam `public` · client credentials

Consumes an insurance queue message by using the provided unique identifier, business key, and Base64 encoded data. The response indicates whether the queue consumption operation was completed successfully.

```python
yanit = kt.sgk.consume_insurance_queue(unique_id=..., business_key=..., base64_data=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `unique_id` | `UniqueId` | gövde | metin | evet | Unique identifier of the queue message. |
| `business_key` | `BusinessKey` | gövde | sayı | evet | Business key associated with the queue message. |
| `base64_data` | `Base64Data` | gövde | metin | evet | Base64 encoded content of the queue message. |

Gövde alanları istekte `QueueMessage` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/sgk/consume-insurance-queue)
