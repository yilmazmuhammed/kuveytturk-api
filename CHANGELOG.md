# Değişiklikler

## Yayınlanmadı

- `accounts.account_transactions_v3` belgesindeki yanıt alanı listesi sandbox'ın gerçek yanıtına
  göre düzeltildi: dokümandaki `reqNum` gelmiyor; `businessKey`, `seqNum`, `transactionCode` ve
  kimlik alanları geliyor. Kodda davranış değişikliği yok.

## 0.1.1 (2026-10-03)

- Paket meta verisinden yazarın e-posta adresi kaldırıldı. Kodda değişiklik yok.

## 0.1.0 (2026-10-02)

İlk sürüm.

- `KuveytTurk` (senkron) ve `AsyncKuveytTurk` (asenkron) istemcileri
- OAuth2: client credentials (kapsam başına otomatik token), authorization code
  (`authorization_url`, `exchange_code`, otomatik yenileme, `login()` ile yerel tarayıcı akışı)
- İsteklerin RSA-SHA256 ile imzalanması; `generate_key_pair` ile anahtar üretimi
- Token depoları: `MemoryTokenStore`, `FileTokenStore`, özel depolar için `TokenStore` protokolü
- Çok kullanıcılı kullanım için `as_user()`
- API Market dokümanından üretilen uç nokta metotları: 23 kaynak altında 192 uç nokta
  (bkz. `ENDPOINTS.md`). Portalda yalnızca "bizimle iletişime geçin" yazan ve sunucudan
  kaldırılmış (pasif) sayfalar kapsam dışıdır.
- Sandbox'ta doğrulananlar: token alma, imzalı GET/POST, hesap listesi ve hareketleri, kurlar,
  IBAN sorgulama, şube/ATM listeleri. Dokümanı hatalı olan para transferi uç noktasının zorunlu
  alanları sandbox'tan tespit edildi.
- Çalıştırılabilir örnek uygulamalar (`examples/`), müşteri girişi yapan örnek bir web
  uygulaması dahil (`examples/web_app`)
- Hata sınıfları ve yalnızca GET istekleri için otomatik yeniden deneme
- İstek/yanıt logları: `enable_logging("debug")` ya da `KUVEYTTURK_LOG=debug`; token ve imza
  maskelenir
