<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# Uç noktalar

Kütüphanede 23 kaynak altında 192 hazır metot var. Metotlar API Market dokümanından üretilir; her birinin sayfasında istek yolu, kapsamı, akışı, parametreleri ve resmî dokümanın bağlantısı bulunur.

- Parametreler anahtar sözcükle ve Python adlarıyla verilir (`item_count`); istekte dokümandaki adlarıyla (`itemCount`) gönderilir. Verilmeyen isteğe bağlı parametreler gönderilmez.
- Metot adlarındaki `_v2`, `_v3` gibi ekler API sürümünü gösterir.
- **CC**: client credentials, token otomatik alınır. **AC**: authorization code, müşteri girişi gerekir ([Yetkilendirme](../yetkilendirme.md)).
- Bir uç noktayı çağırabilmek için portaldaki uygulamanızda ilgili kapsamın etkin olması gerekir. Dokümandaki bazı uç noktalar sandbox'ta bulunmayabilir ([Sandbox notları](../sandbox-notlari.md)).

| Kaynak | Açıklama | Uç nokta |
| - | - | - |
| [`kt.accounts`](accounts.md) | Hesap yönetimi (kurumun kendi hesapları) | 8 |
| [`kt.architecht`](architecht.md) | Architecht | 3 |
| [`kt.cards`](cards.md) | Kredi kartı işlemleri | 4 |
| [`kt.cash_management`](cash_management.md) | Nakit yönetimi | 17 |
| [`kt.credibility`](credibility.md) | Kredibilite | 5 |
| [`kt.donations`](donations.md) | Bağışlar | 5 |
| [`kt.ecommerce`](ecommerce.md) | E-ticaret | 10 |
| [`kt.financing`](financing.md) | Finansman çözümleri | 16 |
| [`kt.fx`](fx.md) | Döviz işlemleri | 5 |
| [`kt.hgs`](hgs.md) | HGS servisleri | 3 |
| [`kt.information`](information.md) | Bilgi servisleri (şube, ATM, parametre sorguları...) | 12 |
| [`kt.moneygram`](moneygram.md) | MoneyGram | 6 |
| [`kt.other`](other.md) | Diğer | 9 |
| [`kt.payment_solutions`](payment_solutions.md) | Ödeme çözümleri | 15 |
| [`kt.payments`](payments.md) | Ödemeler | 15 |
| [`kt.sgk`](sgk.md) | SGK | 1 |
| [`kt.sms_otp`](sms_otp.md) | SMS / OTP | 5 |
| [`kt.support`](support.md) | Destek yönetimi | 14 |
| [`kt.tpp_accounts`](tpp_accounts.md) | Hesap yönetimi (TPP - müşteri adına) | 5 |
| [`kt.transfers`](transfers.md) | Para transferleri | 10 |
| [`kt.treasury`](treasury.md) | Hazine servisleri (kıymetli maden, kur) | 5 |
| [`kt.vpos`](vpos.md) | Sanal POS | 15 |
| [`kt.your_banking`](your_banking.md) | Senin Bankan | 4 |
