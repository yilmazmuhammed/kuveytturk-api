# IBAN'a para transferi

!!! danger "Bu sayfayı okumadan transfer kodu yazmayın"
    - Transfer isteği **asla otomatik tekrarlanmaz**. Zaman aşımı aldıysanız işlem gerçekleşmiş
      olabilir; yeniden göndermeden önce hesap hareketlerini kontrol edin.
    - Resmî dokümandaki parametre listesi **eksiktir**. Aşağıdaki zorunlu alanlar sandbox'ın
      doğrulama hatalarından tespit edilmiştir.
    - Transferin para gönderen adımı bu kütüphanenin testlerinde gerçek sandbox'a karşı
      **çalıştırılmamıştır**. İlk kullanımda sandbox'ta deneyin.

!!! failure "Sandbox'ta şu an çalışmıyor (2026-10-07)"
    `outgoing_money_transfer` ve `money_transfer_payment_type` sandbox'ta zorunlu alanlar
    doldurulduğunda HTTP 500 `Object reference not set to an instance of an object.` dönüyor
    (para çıkmıyor). `LanguageId` / `DeviceId` başlıkları ve `transferType` eklemek sonucu
    değiştirmedi; sorun büyük olasılıkla bankanın sandbox tarafında ve API Market'e
    bildirilmesi gerekiyor. Durum: [Test durumu](../uc-noktalar/test-durumu.md).

## 1. Alıcıyı doğrulayın

Göndermeden önce IBAN'ın kime ait olduğunu sorgulayın. Banka maskeli adı ve bankayı döndürür:

```python
bilgi = kt.transfers.customer_iban_info_for_money_transfer(iban="TR...")
print(bilgi["customerName"], bilgi["bankName"])   # "SU***", "Kuveyt Türk Katılım Bankası A.Ş."
```

Bu adım para hareketi yapmaz; kullanıcıya "şu kişiye gönderiyorsunuz" diye göstermek için
uygundur.

## 2. Transferi gönderin

```python
from decimal import Decimal

yanit = kt.transfers.outgoing_money_transfer(
    sender_account_suffix=1,                  # gönderen hesabın ek numarası
    receiver_iban="TR...",
    money_transfer_amount=Decimal("10.50"),
    corporate_web_user_name="kullanici",      # işlemi yapan kurumsal kullanıcı
    money_transfer_description="Fatura 2026-041",
)
print(yanit["moneyTransferTransactionId"], yanit.execution_reference_id)
```

| Parametre | Zorunlu | Açıklama |
| - | - | - |
| `sender_account_suffix` | Evet | Tutarın çekileceği hesabın ek numarası |
| `receiver_iban` | Evet | Alıcının IBAN'ı. Dokümanda yok; API zorunlu tutuyor |
| `money_transfer_amount` | Evet | Tutar. Kuruş hatası olmaması için `Decimal` kullanın |
| `corporate_web_user_name` | Evet | İşlemi yapan kurumsal internet şubesi kullanıcı adı. Dokümanda yok; API zorunlu tutuyor |
| `money_transfer_description` | Hayır | Açıklama |
| `transfer_type` | Hayır | Tür kodu; değerleri dokümanda açıklanmıyor |

`corporate_web_user_name` neden gerekli: bu akışta kimse giriş yapmaz, uygulama kurum adına
işlem yapar; banka işlemi kurumsal internet şubesindeki hangi kullanıcının yaptığını bilmek
ister.

API ek bir alan isterse hangisinin eksik olduğunu hata mesajında söyler; onu `extra_body` ile
gönderebilirsiniz:

```python
kt.transfers.outgoing_money_transfer(..., extra_body={"eksikAlan": "değer"})
```

## 3. Hataları doğru ele alın

```python
from kuveytturk_api import APIError, BusinessError, TransportError

try:
    yanit = kt.transfers.outgoing_money_transfer(...)
except TransportError:
    # Yanıt alınamadı. İşlem bankaya ulaşmış ve gerçekleşmiş OLABİLİR.
    # Tekrar göndermeyin; hesap hareketlerinden durumu doğrulayın.
    raise
except BusinessError as hata:
    # Banka isteği aldı ve reddetti (yetersiz bakiye, limit vb.). Para çıkmadı.
    print(hata.error_code, hata.error_message)
except APIError as hata:
    # 400: eksik/hatalı alan. 403: kapsam yetkisi yok. Para çıkmadı.
    print(hata.status_code, hata.error_message)
```

## 4. Durumu sorgulayın

```python
durum = kt.transfers.money_transfer_state(transfer_type="FAST", out_going_id="123456")
print(durum["state"], durum["stateDescription"])
```

`transfer_type` olası değerleri: `VIRMAN`, `HAVALE`, `FAST`, `POS`. Virman için `virman_key`,
diğerleri için `out_going_id` verilir.

## Hazır örnek

`examples/money_transfer.py` bu akışın tamamını yapar ve varsayılan olarak **hiçbir şey
göndermez**; yalnızca gönderilecek isteği gösterir:

```bash
python examples/money_transfer.py send --from-suffix 1 --iban TR... --amount 10.50 \
    --corporate-user KULLANICI --description "Deneme"
```

Gerçekten göndermek için `--execute` eklenir ve onay sorulur; canlı ortamda ayrıca
`--allow-production` gerekir.

## Diğer transfer uç noktaları

| Metot | Durum |
| - | - |
| `internal_money_transfer` (virman) | Sandbox'ta `transfers` kapsamlı token ile 403 "Invalid Scope" döndü; denenemedi |
| `outgoing_money_transfer_v2` (müşteri girişiyle) | Dokümandaki parametreler başka bir sayfadan kopyalanmış; gerçek alanlar doğrulanamadı |
| `money_transfer_payment_type` | Zorunlu alanlar: `sender_account_suffix`, `receiver_iban`, `amount` |

Eski `/v1/transfers/ToIBAN` uç noktası dokümanda hâlâ görünür ama sunucudan kaldırılmıştır
(404); kütüphanede yer almaz.
