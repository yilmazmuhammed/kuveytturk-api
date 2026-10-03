# Loglama

Gönderilen her isteği ve dönen yanıtı görmek için:

```python
import kuveytturk_api

kuveytturk_api.enable_logging("debug")   # ya da "info": istek başına tek satır
```

Kod değiştirmeden:

```bash
KUVEYTTURK_LOG=debug python betiginiz.py
```

```text
kuveytturk_api DEBUG → POST https://prep-identity.kuveytturk.com.tr/connect/token
    Authorization: Basic <gizlendi>
    form: grant_type=client_credentials, scope=transfers
kuveytturk_api DEBUG ← POST /connect/token -> 200 (0.11 sn)
    yanıt: access_token=<gizlendi, 1900 karakter>, expires_in=3600, token_type=Bearer, scope=transfers
kuveytturk_api DEBUG → GET https://prep-gateway.kuveytturk.com.tr/v1/moneytransfer/TR.../customeribaninfo
    Accept: application/json
    Authorization: Bearer <gizlendi, 1900 karakter>
    Signature: <gizlendi, 344 karakter>
kuveytturk_api DEBUG ← GET /v1/moneytransfer/TR.../customeribaninfo -> 400 (0.70 sn)
    gövde: {"results":[{"errorMessage":"Iban sorgusuna izin verilmemektedir.", ...}]}
```

| Düzey | Ne yazılır |
| - | - |
| `info` | İstek başına tek satır: metot, yol, durum kodu, süre. Sorgu ve gövde yazılmaz. |
| `debug` | İsteğin tamamı (adres, başlıklar, gövde) ve yanıtın gövdesi; token istekleri dahil |
| `warning` | Yalnızca ağ hataları |

Access token, imza, client secret, authorization code ve refresh token her düzeyde maskelenir.

!!! warning
    `debug` düzeyinde gövdeler olduğu gibi yazılır ve müşteri verisi (IBAN, bakiye, ad) içerir.
    Bu düzeyi yalnızca geliştirme sırasında kullanın.

Kendi `logging` yapılandırmanız varsa `enable_logging` yerine logger'ın düzeyini ayarlamanız
yeterlidir:

```python
import logging
logging.getLogger("kuveytturk_api").setLevel(logging.INFO)
```
