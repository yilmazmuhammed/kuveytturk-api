# Değişiklikler

## 0.1.0 (yayınlanmadı)

İlk sürüm.

- `KuveytTurk` (senkron) ve `AsyncKuveytTurk` (asenkron) istemcileri
- OAuth2: client credentials (kapsam başına otomatik token), authorization code
  (`authorization_url`, `exchange_code`, otomatik yenileme, `login()` ile yerel tarayıcı akışı)
- İsteklerin RSA-SHA256 ile imzalanması; `generate_key_pair` ile anahtar üretimi
- Token depoları: `MemoryTokenStore`, `FileTokenStore`, özel depolar için `TokenStore` protokolü
- Çok kullanıcılı kullanım için `as_user()`
- API Market dokümanından üretilen uç nokta metotları (bkz. `ENDPOINTS.md`)
- Hata sınıfları ve yalnızca GET istekleri için otomatik yeniden deneme
