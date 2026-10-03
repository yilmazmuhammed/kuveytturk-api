# Kurulum ve ilk istek

## 1. Geliştirici portalında uygulama oluşturun

[Geliştirici portalına](https://developer.kuveytturk.com.tr) kaydolup **Uygulamalarım** sayfasından
yeni bir uygulama oluşturun. Uygulama sayfasında iki değer bulunur:

- **Client ID**
- **Client Secret**

Uygulamayı oluştururken kullanacağınız API ürünlerini seçersiniz. Bir uç noktayı çağırabilmeniz
için o uç noktanın kapsamını (scope) içeren ürünün uygulamanızda etkin olması gerekir.

Müşteri girişi (authorization code akışı) kullanacaksanız bir **Redirect URI** de girmelisiniz;
geliştirme için `http://localhost:8000/callback` uygundur.

## 2. İmza anahtarı

Her istek, uygulamanıza ait bir RSA private key ile imzalanır. Portal, uygulama oluştururken
anahtar çifti üretebilir. Kendiniz üretmek isterseniz:

```python
from kuveytturk_api import generate_key_pair

private_pem, public_pem = generate_key_pair("private_key.pem", "public_key.pem")
print(public_pem)  # bunu portaldaki uygulamanızın public key alanına yapıştırın
```

!!! danger "Private key gizli kalmalı"
    Private key'i kaynak koduna, sürüm kontrolüne ya da istemci tarafı uygulamalara koymayın.
    `generate_key_pair` dosyayı yalnızca sahibinin okuyabileceği izinlerle yazar ve var olan bir
    anahtarın üzerine yazmaz.

Portalda kayıtlı public key ile kullandığınız private key eşleşmezse API
`Client signature validation error` (HTTP 400) döner.

## 3. Ayarları tanımlayın

Değerleri doğrudan verebilirsiniz:

```python
from kuveytturk_api import KuveytTurk

kt = KuveytTurk(
    client_id="...",
    client_secret="...",
    private_key="private_key.pem",   # dosya yolu ya da PEM içeriği
    environment="sandbox",           # canlı ortam için "production"
    redirect_uri="http://localhost:8000/callback",  # yalnızca müşteri girişi için
)
```

Ya da ortam değişkenlerinden okutabilirsiniz. Bir `.env` dosyası:

```ini
KUVEYTTURK_CLIENT_ID=...
KUVEYTTURK_CLIENT_SECRET=...
KUVEYTTURK_PRIVATE_KEY=private_key.pem
KUVEYTTURK_REDIRECT_URI=http://localhost:8000/callback
KUVEYTTURK_ENVIRONMENT=sandbox
```

```python
kt = KuveytTurk.from_env(".env")   # dosyadan
kt = KuveytTurk.from_env()         # yalnızca ortam değişkenlerinden
```

Gerçek ortam değişkenleri dosyadakilerden önceliklidir. `.env` içindeki göreli anahtar yolu,
`.env` dosyasının bulunduğu klasöre göre çözülür.

| Argüman | Ortam değişkeni | Açıklama |
| - | - | - |
| `client_id` | `KUVEYTTURK_CLIENT_ID` | Uygulamanın Client ID değeri |
| `client_secret` | `KUVEYTTURK_CLIENT_SECRET` | Uygulamanın Client Secret değeri |
| `private_key` | `KUVEYTTURK_PRIVATE_KEY` | İmza anahtarı: dosya yolu ya da PEM içeriği |
| `private_key_password` | `KUVEYTTURK_PRIVATE_KEY_PASSWORD` | Anahtar şifreliyse parolası |
| `environment` | `KUVEYTTURK_ENVIRONMENT` | `sandbox` (varsayılan) ya da `production` |
| `redirect_uri` | `KUVEYTTURK_REDIRECT_URI` | Müşteri girişi için; portaldakiyle birebir aynı |
| `language_id` | `KUVEYTTURK_LANGUAGE_ID` | `LanguageId` başlığı (1: Türkçe, 2: İngilizce) |
| `device_id` | `KUVEYTTURK_DEVICE_ID` | `DeviceId` başlığı (isteğe bağlı) |
| `token_store` | – | Token deposu (varsayılan: bellek) |
| `timeout` | – | Saniye cinsinden zaman aşımı (varsayılan 30) |
| `max_retries` | – | GET isteklerinin yeniden deneme sayısı (varsayılan 2) |
| `raise_on_failure` | – | `success: false` yanıtında istisna fırlat (varsayılan açık) |
| `http_client` | – | Kendi `httpx.Client` / `httpx.AsyncClient` nesneniz (proxy vb.) |

## 4. İlk istek

```python
from kuveytturk_api import KuveytTurk

with KuveytTurk.from_env(".env") as kt:
    kurlar = kt.fx.fx_currency_rates()
    for kur in kurlar["rateList"]:
        print(kur["fxCode"], kur["buyRate"], kur["sellRate"])
```

Token almanıza ya da imza üretmenize gerek yoktur. İstemci, uç noktanın gerektirdiği kapsam için
token'ı alır, saklar ve süresi dolunca yeniler.

Metotlar bir [`APIResponse`](referans/yanitlar.md) döndürür:

```python
yanit = kt.accounts.account_list_v3()
yanit.value            # yanıt zarfının içindeki asıl veri
yanit["accountList"]   # value bir sözlükse kısayol
yanit.results          # uyarı / bilgi mesajları
yanit.data             # zarf dahil gövdenin tamamı
yanit.status_code
```

Bir şey beklediğiniz gibi çalışmazsa isteği ve yanıtı görmek için:

```bash
KUVEYTTURK_LOG=debug python betiginiz.py
```

Ayrıntı: [Loglama](kilavuzlar/loglama.md).

## Ortamlar

| Ortam | Kimlik sunucusu | API gateway |
| - | - | - |
| `sandbox` | `https://prep-identity.kuveytturk.com.tr` | `https://prep-gateway.kuveytturk.com.tr` |
| `production` | `https://identity.kuveytturk.com.tr` | `https://gateway.kuveytturk.com.tr` |

Portalda oluşturulan uygulamalar önce sandbox'ta çalışır. Canlı ortama geçmek için portaldaki
**Go Live** sürecini tamamlamanız gerekir.
