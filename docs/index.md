# kuveytturk-api

[Kuveyt Türk API Market](https://developer.kuveytturk.com.tr) için Python istemcisi. Token
almayı, istekleri imzalamayı ve hata yönetimini üstlenir; siz yalnızca çağırmak istediğiniz
işlemi yazarsınız.

```python
from kuveytturk_api import KuveytTurk

kt = KuveytTurk.from_env(".env")

for hesap in kt.accounts.account_list_v3()["accountList"]:
    print(hesap["suffix"], hesap["iban"], hesap["balance"])
```

!!! warning "Gayriresmî kütüphane"
    Bu kütüphane Kuveyt Türk tarafından geliştirilmemekte ve desteklenmemektedir. Sürüm 0.1
    "alpha" düzeyindedir; neyin gerçek sandbox'ta denendiği [Sandbox notları](sandbox-notlari.md)
    sayfasında yazıyor.

## Neler sağlar

- **OAuth2 token yönetimi.** Client credentials token'ını kapsam başına kendisi alır, saklar ve
  yeniler. Müşteri girişi (authorization code) için yönlendirme adresini üretir, dönen kodu
  token'a çevirir, süresi dolan token'ı yeniler.
- **İstek imzalama.** Her isteğe RSA-SHA256 ile `Signature` başlığını ekler.
- **Hazır metotlar.** API Market dokümanındaki 192 uç nokta, 23 kaynak altında tip ipuçlu ve
  belgeli metotlar olarak gelir: [Uç noktalar](uc-noktalar/index.md).
- **Senkron ve asenkron istemci.** `KuveytTurk` ve `AsyncKuveytTurk` aynı arayüzü sunar.
- **Güvenli varsayılanlar.** Para hareketi yapan istekler asla kendiliğinden tekrarlanmaz;
  loglarda token ve imza maskelenir.

## Kurulum

```bash
pip install kuveytturk-api
```

Python 3.9 ve üzeri gerekir.

## Nereden başlamalı

| Yapmak istediğiniz | Sayfa |
| - | - |
| Uygulama açıp ilk isteği atmak | [Kurulum ve ilk istek](baslangic.md) |
| Hangi akışın ne zaman kullanıldığını anlamak | [Yetkilendirme](yetkilendirme.md) |
| Hesapları ve hareketleri çekmek | [Hesaplar ve hareketler](kilavuzlar/hesaplar.md) |
| Bir IBAN'a para göndermek | [IBAN'a para transferi](kilavuzlar/para-transferi.md) |
| Web sitenize "Kuveyt Türk ile bağlan" eklemek | [Web uygulamasında müşteri girişi](kilavuzlar/web-uygulamasi.md) |
| Bir isteğin neden başarısız olduğunu görmek | [Loglama](kilavuzlar/loglama.md), [Hata yönetimi](kilavuzlar/hata-yonetimi.md) |
