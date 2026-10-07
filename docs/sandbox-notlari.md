# Sandbox notları

Resmî API dokümanı ile gerçek davranış her zaman örtüşmüyor. Bu sayfa, sandbox'a gerçek
isteklerle yapılan denemelerde görülenleri toplar. Kütüphanenin hazır metotları bu bulgulara
göre düzeltildi; kendi kodunuzu yazarken de bunları göz önünde bulundurun.

## Neler denendi

Her uç noktanın sandbox ve canlı ortamdaki durumu ayrıntılı olarak
[Test durumu](uc-noktalar/test-durumu.md) sayfasında. Özetle:

| Konu | Durum |
| - | - |
| Client credentials token, imzalı GET ve POST | Denendi, çalışıyor |
| Kurumun hesap listesi ve hareketleri (`kt.accounts`) | Denendi, çalışıyor |
| Müşteri girişiyle hesap listesi ve hareketleri (`kt.tpp_accounts`) | Denendi, çalışıyor |
| Kurlar, IBAN sorgulama, şube/ATM listeleri | Denendi, çalışıyor |
| IBAN'a transferin gönderim adımı | Denendi: zorunlu alanlar doluyken **500** dönüyor, para çıkmıyor |
| Diğer uç noktaların çoğu | Denenmedi; uygulamanın kapsam yetkisine bağlı |

## Dokümandan farklı olanlar

- **İmza kuralı:** GET isteklerinde sorgu dizgisi `?` dahil imzalanır
  (`{access_token}?a=1&b=2`). Sorgu imzaya katılmazsa istek reddedilir.
- **İmza hatası 400 döner**, 401 değil: `{"code":400,"message":"Client signature validation error"}`.
- **Para transferi:** `POST /v1/moneytransfer/outgoingmoneytransfer` dokümanda alıcıyı hesap
  numarasıyla tanımlar; API ise `receiverIban` ve `corporateWebUserName` alanlarını zorunlu tutar.
  Ayrıntı: [IBAN'a para transferi](kilavuzlar/para-transferi.md).
- **Yanıt alanları:** kurlar `value.rateList[].fxName` ile gelir (doküman `value[].name` der);
  hesap listesi v3'te `productType` ve `availableBalance` gelir (doküman `type` ve
  `avaibleBalance` der); hareketler v3'te `reqNum` gelmez, `businessKey`, `seqNum`,
  `transactionCode` gelir.
- **Yanıt zarfı:** gerçek yanıtlarda `value`, `success`, `results` yanında üst düzeyde `errors`
  ve `executionReferenceId` de bulunur. `account_transactions_v4_detail` veriyi `value` yerine
  `accountTransactionListValueModel` anahtarında döndürür.
- **Hesap hareketlerinde tarih filtresi:** `beginDate` uygulanmıyor, `endDate` yalnızca tek
  başına verildiğinde uygulanıyor; ikisi birlikte verilince aralık dışındaki kayıtlar da
  dönebiliyor. `itemCount` uygulanıyor. Ayrıntı: [Hesaplar ve hareketler](kilavuzlar/hesaplar.md).
- **Refresh token rotasyonu:** her yenilemede yeni bir refresh token verilir.
- **Kaldırılmış uç noktalar:** dokümanda "Active: false" işaretli sayfalar sunucuda yoktur
  (404 "Path not found"); kütüphaneye alınmadı. Pasif işaretli olmadığı hâlde sandbox'ta 404
  dönenler de var (ör. MoneyGram listeleri, `tpp_accounts.receipt_v1`).
- **Erişilemeyen dokümanlar:** portaldaki sayfaların yaklaşık yarısında yalnızca "Please contact
  us to use this product." yazar; bu ürünler kütüphanede yer almaz.

## Sandbox verisinin sınırları

- Hareket açıklamaları her kayıtta `Açıklama` olarak gelir; kimlik alanları boştur.
- Dekont uç noktaları denenen hareketlerde boş içerik döndü.
- Test müşterisinin hesaplarının çoğunda hareket yoktur.

Bu alanların canlı ortamda nasıl dolduğu sandbox'tan anlaşılamaz.

## Hız sınırı { #hiz-siniri }

Geliştirici portalının sunucuları kısa sürede çok istek gelince IP adresini yaklaşık iki saat
engelliyor; engel sandbox dahil tüm `*.kuveytturk.com.tr` adreslerini kapsıyor. Belirtisi bir
hata mesajı değil, bağlantının kesilmesidir (`Connection reset by peer`). Toplu deneme ya da
tarama yaparken istekleri aralıklı gönderin.
