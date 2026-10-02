# Örnek web uygulaması: Kuveyt Türk ile bağlan

Müşteri girişinin (authorization code akışı) bir web uygulamasında nasıl kurulduğunu gösteren
küçük bir [Flask](https://flask.palletsprojects.com/) uygulaması. Ziyaretçi bankada giriş yapıp
izin verir; uygulama onun hesaplarını ve hesap hareketlerini gösterir.

## Çalıştırma

Proje kökünden:

```bash
pip install -e . flask
python examples/web_app/app.py
```

Ardından tarayıcıda `http://localhost:8000/` adresini açın (port, `.env` dosyasındaki
`KUVEYTTURK_REDIRECT_URI` adresinden alınır).

Gerekenler:

- Dolu bir `.env` dosyası (bkz. `.env.example`).
- `KUVEYTTURK_REDIRECT_URI`, geliştirici portalındaki uygulamanızın Redirect URI'siyle **birebir
  aynı** olmalı (ör. `http://localhost:8000/callback`). Uygulama callback'i bu adresin yolunda
  karşılar.
- Sandbox'ta giriş için portaldaki test müşterilerini kullanın; istenen OTP için 6 haneli
  herhangi bir kod girilebilir.

## Sayfalar

| Adres | Ne yapar | Akış |
| - | - | - |
| `/` | Bağlantı durumu ve "Kuveyt Türk ile bağlan" düğmesi | – |
| `/login` | `state` üretir, ziyaretçiyi bankanın giriş sayfasına yönlendirir | AC |
| Redirect URI'nin yolu (ör. `/callback`) | `state`'i doğrular, `code`'u token'a çevirir | AC |
| `/accounts` | Giriş yapan müşterinin hesapları | AC |
| `/accounts/<ek no>/transactions` | Hesap hareketleri (`?days=7` gibi) | AC |
| `/rates` | Döviz kurları; giriş gerektirmez | CC |
| `/logout` (POST) | Saklanan token'ı siler | – |

## Akışın koddaki karşılığı

```python
# 1) Yönlendirme
session["oauth_state"] = kt.auth.new_state()
return redirect(kt.auth.authorization_url(SCOPES, state=session["oauth_state"]))

# 2) Callback
code = kt.auth.parse_callback(request.url, state=session.pop("oauth_state"))
kt.auth.exchange_code(code, user=visitor())  # token bu ziyaretçinin anahtarıyla saklanır

# 3) Müşteri adına çağrı
kt.as_user(visitor()).tpp_accounts.account_list_v2()
```

- **`state`** her girişte yeniden üretilir ve callback'te doğrulanır; başka bir sitenin
  ziyaretçiyi sahte bir callback'e yollamasını (CSRF) engeller. Kullanıldıktan sonra oturumdan
  silinir.
- **Token tarayıcıya gitmez.** Oturum çerezinde yalnızca rastgele bir ziyaretçi anahtarı durur;
  access ve refresh token sunucudaki depoda saklanır.
- **Süre dolunca** kütüphane access token'ı refresh token ile kendisi yeniler. Yenilenemezse
  (`AuthorizationRequiredError`) uygulama ziyaretçiyi yeniden bağlanmaya yönlendirir.
- **Her ziyaretçinin token'ı ayrıdır**; `kt.as_user(...)` hangi müşteri adına çağrı yapıldığını
  belirler. Tek bir `KuveytTurk` istemcisi tüm istekler için yeterlidir.

## Gerçek bir uygulamaya taşırken

- **Token deposu:** Örnek, token'ları `.kuveytturk/web_tokens.json` dosyasında tutar. Birden çok
  süreç ya da sunucu varsa `get` / `set` / `delete` metotlarını sağlayan kendi deponuzu
  (veritabanı, Redis) `token_store=` ile verin ve token'ları şifreli saklayın.
- **Kullanıcı kimliği:** Örnekteki rastgele ziyaretçi anahtarı yerine kendi üyelik sisteminizdeki
  kullanıcı kimliğini kullanın.
- **Oturum anahtarı:** `FLASK_SECRET_KEY` ortam değişkeniyle sabit ve gizli bir değer verin;
  verilmezse her başlatmada yenilenir ve açık oturumlar düşer.
- **HTTPS:** Canlıda Redirect URI `https://` olmalı ve oturum çerezi `Secure` işaretlenmeli.
  Uygulamayı Flask'ın geliştirme sunucusuyla değil, gunicorn gibi bir WSGI sunucusuyla çalıştırın.
- **Refresh token 24 saat geçerlidir;** müşteri en geç o zaman yeniden giriş yapar.
