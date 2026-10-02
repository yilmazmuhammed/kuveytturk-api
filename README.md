# kuveytturk-api

[Kuveyt Türk API Market](https://developer.kuveytturk.com.tr) için Python istemcisi.

- OAuth2 token'larını (client credentials ve authorization code) kendisi alır, saklar ve yeniler
- Her isteği RSA-SHA256 ile imzalar (`Signature` başlığı)
- Dokümandaki uç noktalar için tip ipuçlu, belgeli hazır metotlar ([liste](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/ENDPOINTS.md))
- Senkron (`KuveytTurk`) ve asenkron (`AsyncKuveytTurk`) istemci
- Anlamlı hata sınıfları; para hareketi yapan istekleri asla kendiliğinden tekrarlamaz

> Bu kütüphane **gayriresmîdir**; Kuveyt Türk tarafından geliştirilmemekte ve desteklenmemektedir.

## Kurulum

```bash
pip install kuveytturk-api
```

Python 3.9 ve üzeri gerekir.

## Hazırlık

1. [Geliştirici portalına](https://developer.kuveytturk.com.tr) kaydolup bir uygulama oluşturun.
   Uygulama sayfasından **Client ID** ve **Client Secret** değerlerini alın.
2. İstekleri imzalamak için bir RSA anahtar çifti gerekir. Portal uygulama oluştururken
   üretebilir; kendiniz üretmek isterseniz:

   ```python
   from kuveytturk_api import generate_key_pair

   private_pem, public_pem = generate_key_pair("private_key.pem", "public_key.pem")
   print(public_pem)  # bunu portaldaki uygulamanızın public key alanına yapıştırın
   ```

   Private key'i gizli tutun; kaynak koduna ya da sürüm kontrolüne koymayın.

## Hızlı başlangıç

```python
from kuveytturk_api import KuveytTurk

kt = KuveytTurk(
    client_id="...",
    client_secret="...",
    private_key="private_key.pem",   # dosya yolu ya da PEM içeriği
    environment="sandbox",           # canlı ortam için "production"
)

kurlar = kt.fx.fx_currency_rates()
print(kurlar.value)
```

Token almanıza ya da imza üretmenize gerek yoktur; istemci uç noktanın gerektirdiği kapsam
(scope) için token'ı alır, saklar ve süresi dolunca yeniler.

Ayarları ortam değişkenlerinden de okuyabilirsiniz (`.env.example` dosyasına bakın):

```python
kt = KuveytTurk.from_env()        # KUVEYTTURK_CLIENT_ID, KUVEYTTURK_CLIENT_SECRET, ...
kt = KuveytTurk.from_env(".env")  # bir .env dosyasından
```

## Yetkilendirme akışları

Her uç noktanın dokümanında bir **akış** yazar; kütüphane bunu bilir ve doğru token'ı kullanır.

### Client credentials

Müşteri girişi gerektirmeyen uç noktalar içindir; yukarıdaki örnekte olduğu gibi hiçbir ek adım
gerekmez.

### Authorization code (müşteri girişi)

Müşteri adına çalışan uç noktalar (ör. `kt.tpp_accounts`) için müşterinin bankanın giriş
sayfasında oturum açıp uygulamanıza izin vermesi gerekir.

**Betikler / geliştirme** — `redirect_uri` `http://localhost:PORT/...` ise tek satır yeter:
tarayıcı açılır, giriş tamamlanınca token alınır.

```python
from kuveytturk_api import FileTokenStore, KuveytTurk

kt = KuveytTurk.from_env(
    ".env",
    token_store=FileTokenStore(".kuveytturk/tokens.json"),  # yeniden çalıştırınca tekrar giriş istemez
)
if kt.auth.get_user_token() is None:
    kt.auth.login(["accounts", "offline_access"])   # offline_access -> refresh token

hesaplar = kt.tpp_accounts.account_list_v2()
for hesap in hesaplar["accountList"]:
    print(hesap["suffix"], hesap["iban"], hesap["balance"])
```

**Web uygulamaları** — yönlendirmeyi ve callback'i kendi rotalarınızda yaparsınız:

```python
# 1) Kullanıcıyı bankaya yönlendirin
state = kt.auth.new_state()                       # oturumda saklayın (CSRF koruması)
url = kt.auth.authorization_url(["accounts", "offline_access"], state=state)

# 2) Redirect URI'nize dönen istekte
code = kt.auth.parse_callback(request_url, state=state)
kt.auth.exchange_code(code, user="musteri-42")    # token bu anahtarla saklanır

# 3) O müşteri adına çağrı yapın
hesaplar = kt.as_user("musteri-42").tpp_accounts.account_list_v2()
```

Access token 1 saat, refresh token 24 saat geçerlidir. Süresi dolan access token otomatik
yenilenir; yenilenemiyorsa `AuthorizationRequiredError` fırlatılır ve müşterinin yeniden giriş
yapması gerekir.

Token'lar varsayılan olarak bellekte tutulur. Kalıcı saklamak için `FileTokenStore`
kullanabilir ya da `get` / `set` / `delete` metotlarını sağlayan kendi deponuzu (Redis,
veritabanı...) `token_store=` ile verebilirsiniz.

## Uç noktalar

23 kaynak altında 192 uç nokta hazır metot olarak gelir. Hazır metotlar kaynaklara ayrılmıştır: `kt.accounts`, `kt.tpp_accounts`, `kt.fx`, `kt.cards`,
`kt.treasury`... Tam liste: [ENDPOINTS.md](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/ENDPOINTS.md). Her metodun docstring'inde yolu,
kapsamı, akışı, parametreleri ve resmî dokümanın bağlantısı bulunur.

```python
from datetime import date

hareketler = kt.accounts.account_transactions_v3(
    suffix=1,
    begin_date=date(2025, 1, 1),
    end_date=date(2025, 1, 31),
    item_count=50,
)
for hareket in hareketler["accountActivities"]:
    print(hareket["date"], hareket["amount"], hareket["description"])
```

Tüm parametreler anahtar sözcükle verilir ve Python adlarıyla (`item_count`) yazılır; istekte
dokümandaki adlarıyla (`itemCount`) gönderilir. Verilmeyen isteğe bağlı parametreler gönderilmez.

### Yanıtlar

API yanıtları `{"value": ..., "success": ..., "results": [...]}` zarfıyla döner. Metotlar bir
`APIResponse` döndürür:

```python
yanit = kt.accounts.account_list_v3()
yanit.value          # zarfın içindeki asıl veri
yanit["accountList"] # value bir sözlükse kısayol
yanit.results        # uyarı / bilgi mesajları
yanit.data           # zarf dahil gövdenin tamamı
yanit.status_code, yanit.headers
```

Bir uç noktayı çağırabilmeniz için portaldaki uygulamanızda ilgili API ürününün (kapsamın)
etkin olması gerekir; değilse `AuthenticationError` (`invalid_scope`) ya da `ForbiddenError`
alırsınız. Dokümanda geçen bazı uç noktalar sandbox'ta bulunmayabilir (`NotFoundError`).

### Doküman eksikse ya da yanlışsa

Dokümanlar zaman zaman eksik ya da hatalı olabiliyor. Her metot bunun için üç kaçış yolu sunar:

```python
kt.accounts.account_list_v3(
    extra_query={"belgelenmemisParametre": 1},        # sorguya eklenir
    request_options={"timeout": 60, "flow": "authorization_code"},  # akışı/kapsamı/token'ı ezer
)
# gövdeli metotlarda ayrıca: extra_body={...}
```

Kütüphanede karşılığı olmayan bir uç noktayı doğrudan çağırabilirsiniz; token ve imza yine
otomatik eklenir:

```python
kt.request("GET", "/v4/accounts/{suffix}/transactions", scope="accounts",
           path_params={"suffix": 1}, query={"itemCount": 10})
kt.post("/v1/ornek", scope="public", body={"alan": "değer"})
```

## Örnek uygulamalar

[`examples/`](https://github.com/yilmazmuhammed/kuveytturk-api/tree/main/examples) klasöründe doğrudan çalıştırılabilen örnekler var:

| Örnek | Ne yapar |
| - | - |
| [`account_list.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/account_list.py) | Hesap listesi |
| [`account_transactions.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/account_transactions.py) | Bir hesabın hareketleri ve dekontu |
| [`exchange_rates.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/exchange_rates.py) | Döviz ve kıymetli maden kurları |
| [`iban_lookup.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/iban_lookup.py) | IBAN sahibini ve bankasını sorgulama |
| [`money_transfer.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/money_transfer.py) | Bir IBAN'a para transferi (önce alıcı doğrulama), durum sorgulama |
| [`async_usage.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/async_usage.py) | Asenkron istemci |
| [`web_app_flow.py`](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/web_app_flow.py) | Web uygulamasında müşteri girişi iskeleti |

```bash
python examples/account_list.py --only-open
python examples/account_transactions.py --suffix 1 --days 7 --receipt
```

Ayrıntılar: [examples/README.md](https://github.com/yilmazmuhammed/kuveytturk-api/blob/main/examples/README.md).

## Hata yönetimi

```python
from kuveytturk_api import APIError, AuthorizationRequiredError, BusinessError, TransportError

try:
    kt.fx.fx_currency_buy(account_suffix_from=1, account_suffix_to=101, buy_rate=40.1, exchange_amount=100)
except BusinessError as hata:            # HTTP 200 ama success: false
    print(hata.error_code, hata.error_message)
except APIError as hata:                 # 4xx / 5xx
    print(hata.status_code, hata.error_code, hata.error_message, hata.body)
except AuthorizationRequiredError:       # müşterinin (yeniden) giriş yapması gerekiyor
    ...
except TransportError:                   # ağ hatası / zaman aşımı
    ...
```

| İstisna | Ne zaman |
| - | - |
| `BadRequestError` / `UnauthorizedError` / `ForbiddenError` / `NotFoundError` / `RateLimitError` / `ServerError` | HTTP 400 / 401 / 403 / 404 / 429 / 5xx (hepsi `APIError`) |
| `BusinessError` | HTTP başarılı ama yanıtta `success: false` |
| `AuthenticationError` | Token alınamadı (yanlış client bilgisi, geçersiz kod...) |
| `AuthorizationRequiredError` | Müşteri token'ı yok, süresi dolmuş ya da kapsamı eksik |
| `TransportError` | İstek sunucuya ulaşamadı |
| `ConfigurationError` / `SignatureError` | Eksik ayar, okunamayan private key |

Hepsi `KuveytTurkError`'dan türer.

**Yeniden deneme:** Ağ hatalarında ve 5xx yanıtlarında yalnızca `GET` istekleri otomatik
yeniden denenir (`max_retries`, varsayılan 2). `POST` istekleri — para transferi, döviz alım
satımı gibi — **asla** kendiliğinden tekrarlanmaz; zaman aşımına uğrayan bir işlemin sonucunu
kendiniz sorgulamalısınız.

## Loglama ve hata ayıklama

Gönderilen her isteği ve dönen yanıtı görmek için:

```python
import kuveytturk_api

kuveytturk_api.enable_logging("debug")   # ya da "info": istek başına tek satır özet
```

Kod değiştirmeden, ortam değişkeniyle de açılabilir:

```bash
KUVEYTTURK_LOG=debug python examples/account_list.py
```

```text
kuveytturk_api DEBUG → GET https://prep-gateway.kuveytturk.com.tr/v3/accounts?onlyOpen=true
    Accept: application/json
    Authorization: Bearer <gizlendi, 1900 karakter>
    Signature: <gizlendi, 344 karakter>
kuveytturk_api DEBUG ← GET /v3/accounts -> 200 (0.42 sn)
    gövde: {"value":{"accountList":[...]},"success":true,...}
```

| Düzey | Ne yazılır |
| - | - |
| `info` | İstek başına tek satır: metot, yol, durum kodu, süre. Sorgu ve gövde yazılmaz. |
| `debug` | İsteğin tamamı (adres, başlıklar, gövde) ve yanıtın gövdesi; token istekleri dahil. |

Access token, imza, client secret, authorization code ve refresh token her iki düzeyde de
maskelenir. `debug` düzeyinde gövdeler olduğu gibi yazılır ve **müşteri verisi içerir** (IBAN,
bakiye, ad...); bu düzeyi yalnızca geliştirme sırasında kullanın.

Loglar standart `logging` modülüyle `"kuveytturk_api"` adlı logger'a yazılır; kendi log
yapılandırmanız varsa `enable_logging` yerine
`logging.getLogger("kuveytturk_api").setLevel(logging.DEBUG)` demeniz yeterlidir.

## Asenkron kullanım

```python
import asyncio
from kuveytturk_api import AsyncKuveytTurk

async def main():
    async with AsyncKuveytTurk.from_env(".env") as kt:
        kurlar, madenler = await asyncio.gather(
            kt.fx.fx_currency_rates(),
            kt.treasury.precious_metal_rates(),
        )

asyncio.run(main())
```

Arayüz senkron istemciyle aynıdır; ağa çıkan metotlar `await` edilir.

## Yapılandırma

| Argüman | Ortam değişkeni | Açıklama |
| - | - | - |
| `client_id` | `KUVEYTTURK_CLIENT_ID` | Uygulamanın Client ID değeri |
| `client_secret` | `KUVEYTTURK_CLIENT_SECRET` | Uygulamanın Client Secret değeri |
| `private_key` | `KUVEYTTURK_PRIVATE_KEY` | İmza anahtarı: dosya yolu ya da PEM içeriği |
| `private_key_password` | `KUVEYTTURK_PRIVATE_KEY_PASSWORD` | Anahtar şifreliyse parolası |
| `environment` | `KUVEYTTURK_ENVIRONMENT` | `sandbox` (varsayılan) ya da `production` |
| `redirect_uri` | `KUVEYTTURK_REDIRECT_URI` | Authorization code akışı için; portaldakiyle birebir aynı |
| `language_id` | `KUVEYTTURK_LANGUAGE_ID` | `LanguageId` başlığı (1: Türkçe, 2: İngilizce) |
| `device_id` | `KUVEYTTURK_DEVICE_ID` | `DeviceId` başlığı (isteğe bağlı) |
| `token_store` | – | Token deposu (varsayılan: bellek) |
| `timeout` | – | Saniye cinsinden zaman aşımı (varsayılan 30) |
| `max_retries` | – | GET isteklerinin yeniden deneme sayısı (varsayılan 2) |
| `raise_on_failure` | – | `success: false` yanıtında istisna fırlat (varsayılan açık) |
| `http_client` | – | Kendi `httpx.Client` / `httpx.AsyncClient` nesneniz (proxy vb.) |

## Geliştirme

```bash
git clone https://github.com/yilmazmuhammed/kuveytturk-api.git && cd kuveytturk-api
python -m venv venv && venv/bin/pip install -e ".[dev]"
venv/bin/python -m pytest -q
venv/bin/ruff check . && venv/bin/mypy
```

Uç nokta metotları dokümandan üretilir; `src/kuveytturk_api/resources/` altındaki dosyalar elle
düzenlenmez. Dokümanlar değiştiğinde:

```bash
python scripts/fetch_docs.py && python scripts/build_spec.py && python scripts/generate.py
```

## Lisans

MIT
