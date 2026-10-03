# Hesaplar ve hareketler

Hesap uç noktaları iki kaynakta toplanır:

| Kaynak | Akış | Kimin hesapları |
| - | - | - |
| [`kt.accounts`](../uc-noktalar/accounts.md) | Client credentials | Uygulamanın bağlı olduğu müşterinin (kurumun kendi hesapları) |
| [`kt.tpp_accounts`](../uc-noktalar/tpp_accounts.md) | Authorization code | Giriş yapan müşterinin |

## Hesap listesi

```python
yanit = kt.accounts.account_list_v3(only_open=True)
for hesap in yanit["accountList"]:
    print(hesap["suffix"], hesap["productType"], hesap["balance"], hesap["iban"])
```

`suffix` hesabın **ek numarasıdır**; hareket ve transfer çağrılarında hesabı bununla
belirtirsiniz.

Müşteri girişiyle:

```python
yanit = kt.tpp_accounts.account_list_v2()
```

Sandbox'ta dönen alanlar iki sürümde farklıdır:

| Bilgi | `account_list_v3` | `account_list_v2` |
| - | - | - |
| Hesap türü | `productType` | `type` |
| Para birimi | yalnızca `fxId` | `fxId` ve `fxCode` |
| Müşteri numarası | – | `accountNumber` |

`fxId` değerleri: TL `0`, USD `1`, EUR `19`, altın `24`, gümüş `26`, platin `27`.

## Hesap hareketleri

```python
from datetime import date, timedelta

bugun = date.today()
yanit = kt.accounts.account_transactions_v3(
    suffix=5,
    begin_date=bugun - timedelta(days=30),
    end_date=bugun,
    item_count=50,
)
for hareket in yanit["accountActivities"]:
    print(hareket["date"], hareket["amount"], hareket["fxCode"], hareket["description"])
```

Sandbox'ta ölçülen davranış:

- Kayıtlar **yeniden eskiye** sıralıdır; `item_count` en yeni N kaydı verir. Sayfalama yoktur.
- `amount` işaretlidir: giden tutarlar eksi gelir.
- `date` milisaniyeli ISO biçimindedir; kesir basamağı sayısı değişkendir.
- `balance` her kayıtta bulunmaz.
- Karşı tarafın IBAN'ı için bir alan yoktur. v3'teki `iban` hesabın kendi IBAN'ıdır.

!!! warning "Kayıtları tekilleştirirken `transactionReference` kullanmayın"
    Tek bir işlemin birden çok bacağı aynı `transactionReference` değerini paylaşır. Kaydı
    tekil yapan, v2'de `(transactionId, seqNum)` çifti, v3'te `businessKey` + `seqNum`'dır.
    Hareketleri kendi veritabanınıza aktarıyorsanız mükerrer kontrolünü bunlarla yapın.

!!! note "Sandbox veriyi maskeler"
    Sandbox'ta `description` her kayıtta `Açıklama` olarak gelir ve kimlik alanları
    (`senderTCKNorVKN`, `receiverTCKNorVKN`) boştur. Bu alanların canlıda nasıl dolduğu
    sandbox'tan anlaşılamaz.

Daha ayrıntılı alanlar için `account_transactions_v4_detail` kullanılabilir; bu uç nokta
yanıtını `value` yerine `accountTransactionListValueModel` anahtarında döndürür:

```python
yanit = kt.accounts.account_transactions_v4_detail(suffix=5, item_count=10)
hareketler = yanit.data["accountTransactionListValueModel"]["accountActivities"]
```

## Dekont

```python
dekont = kt.accounts.receipt_v3(transaction_reference=hareket["transactionReference"])
for satir in dekont.get("slipList") or []:
    print(satir["key"], satir["value"])
```

Sandbox'ta denenen hareketler için dekont içeriği boş döndü (`slipList` yok). Kodunuz boş
dekontu hata saymamalıdır. PDF için `kt.accounts.pdf_receipt_v3(...)` Base64 kodlu içerik
döndürür.

## Hazır örnekler

```bash
python examples/account_list.py --only-open
python examples/account_transactions.py --suffix 5 --days 60 --receipt
python examples/account_list.py --customer        # müşteri girişiyle
```
