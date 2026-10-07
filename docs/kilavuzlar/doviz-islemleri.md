# Döviz ve kıymetli maden alım-satımı

!!! danger "Gerçek işlem"
    Alış ve satış istekleri hesaplar arasında para hareketi yapar ve **asla otomatik
    tekrarlanmaz**. Zaman aşımı alırsanız yeniden göndermeden önce bakiyeleri kontrol edin.
    Bu uç noktalar bu kütüphanenin testlerinde gerçek sandbox'a karşı çalıştırılmamıştır;
    güncel durum için [Test durumu](../uc-noktalar/test-durumu.md) sayfasına bakın.

## Kurlar

```python
kurlar = kt.fx.fx_currency_rates()["rateList"]           # USD, EUR...
madenler = kt.treasury.precious_metal_rates()["rateList"]  # "ALT (gr)", "GMS (gr)", "PLT (gr)"
for kur in kurlar + madenler:
    print(kur["fxCode"], kur["fxId"], kur["buyRate"], kur["sellRate"])
```

`buyRate` sizin alırken ödediğiniz, `sellRate` satarken aldığınız kurdur. `fxId`, hesap
listesindeki para birimi koduyla aynıdır (TL `0`, USD `1`, EUR `19`, altın `24`).

## Alış ve satış

```python
from decimal import Decimal

usd = next(k for k in kt.fx.fx_currency_rates()["rateList"] if k["fxCode"] == "USD")

kt.fx.fx_currency_buy(
    account_suffix_from=5,            # TL hesabı (TL buradan çekilir)
    account_suffix_to=2,              # USD hesabı (döviz buraya yatar)
    buy_rate=Decimal(str(usd["buyRate"])),
    exchange_amount=Decimal("1"),
    corporate_web_user_name="kullanici",
)

kt.fx.fx_currency_sell(
    account_suffix_from=2,            # USD hesabı
    account_suffix_to=5,              # TL hesabı
    sell_rate=Decimal(str(usd["sellRate"])),
    exchange_amount=Decimal("1"),
    corporate_web_user_name="kullanici",
)
```

Kıymetli madende `kt.treasury.precious_metal_buy` / `precious_metal_sell` aynı biçimdedir;
orada `corporate_web_user_name` zorunludur.

- Kur, istek anındaki bankanın kuruyla uyuşmalıdır; kuru isteğin hemen öncesinde alın.
- Hesapların para birimini `account_list_v3()` yanıtındaki `fxId` ile doğrulayın: alışta kaynak
  TL hesabı, hedef döviz hesabı olmalıdır; satışta tersi.

## Hazır örnek

`examples/fx_trade.py` kuru alır, hesapların para birimini kontrol eder, özeti gösterir ve
varsayılan olarak **hiçbir işlem göndermez**:

```bash
python examples/fx_trade.py buy USD 1 --tl-suffix 5 --fx-suffix 2 --corporate-user KULLANICI
python examples/fx_trade.py buy USD 1 --tl-suffix 5 --fx-suffix 2 --corporate-user KULLANICI --execute
```
