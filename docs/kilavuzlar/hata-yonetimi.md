# Hata yönetimi

Kütüphanenin fırlattığı tüm istisnalar `KuveytTurkError`'dan türer.

```python
from kuveytturk_api import (
    APIError, AuthenticationError, AuthorizationRequiredError, BusinessError, TransportError,
)

try:
    yanit = kt.accounts.account_list_v3()
except BusinessError as hata:          # HTTP 200 ama yanıtta success: false
    print(hata.error_code, hata.error_message)
except APIError as hata:               # 4xx / 5xx
    print(hata.status_code, hata.error_code, hata.error_message, hata.body)
except AuthorizationRequiredError:     # müşterinin (yeniden) giriş yapması gerekiyor
    ...
except AuthenticationError as hata:    # token alınamadı (ör. invalid_scope)
    print(hata.error, hata.error_description)
except TransportError:                 # ağ hatası, zaman aşımı
    ...
```

| İstisna | Ne zaman |
| - | - |
| `BadRequestError` | HTTP 400: eksik/hatalı parametre ya da **imza hatası** |
| `UnauthorizedError` | HTTP 401: token geçersiz ya da uç nokta başka bir akış istiyor |
| `ForbiddenError` | HTTP 403: token'ın kapsamı uç noktaya uymuyor |
| `NotFoundError` | HTTP 404: uç nokta ya da kayıt yok |
| `RateLimitError` | HTTP 429 |
| `ServerError` | HTTP 5xx |
| `BusinessError` | HTTP başarılı ama yanıtta `success: false` |
| `AuthenticationError` | Kimlik sunucusu token vermedi |
| `AuthorizationRequiredError` | Müşteri token'ı yok, süresi dolmuş ya da kapsamı eksik |
| `TransportError` | İstek sunucuya ulaşamadı |
| `ConfigurationError`, `SignatureError` | Eksik ayar, okunamayan private key |

`APIError` ve alt sınıflarında: `status_code`, `error_code`, `error_message`, `results`
(tüm mesajlar), `body` (ham yanıt), `method`, `url`.

## Gateway'in sık görülen yanıtları

| Yanıt | Anlamı | Ne yapmalı |
| - | - | - |
| 400 `Client signature validation error` | İmza doğrulanamadı | Portaldaki public key ile kullanılan private key eşleşiyor mu? |
| 400 `Signature header parameter is empty.` | İmza başlığı yok | Kütüphane her zaman ekler; isteği elle mi gönderiyorsunuz? |
| 401 `Invalid grant type. Authorization Code is required.` | Uç nokta müşteri girişi istiyor | `flow="authorization_code"` ile çağırın |
| 403 `Invalid Scope` | Token'ın kapsamı uç noktaya uymuyor | Uç noktanın kapsamını kontrol edin |
| 404 `Path not found` | Uç nokta sunucuda yok | Doküman eskimiş olabilir |
| Token: `invalid_scope` | Uygulamanız bu kapsama yetkili değil | Portalda ilgili API ürününü ekleyin |

## Yeniden deneme

| Durum | Davranış |
| - | - |
| GET + ağ hatası ya da 500/502/503/504 | `max_retries` kez (varsayılan 2) artan aralıklarla yeniden denenir |
| POST, PUT, PATCH | **Asla** otomatik yeniden denenmez |
| 401 | Token bir kez yenilenip istek tekrarlanır (istek işlenmediği için POST'ta da güvenlidir) |

Para transferi gibi bir POST zaman aşımına uğrarsa işlemin gerçekleşip gerçekleşmediği bilinmez;
yeniden göndermeden önce durumu sorgulayın.
