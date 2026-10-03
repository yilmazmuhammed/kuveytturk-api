# Asenkron kullanım

`AsyncKuveytTurk`, `KuveytTurk` ile aynı arayüzü sunar; ağa çıkan metotlar `await` edilir.

```python
import asyncio
from kuveytturk_api import AsyncKuveytTurk

async def main():
    async with AsyncKuveytTurk.from_env(".env") as kt:
        kurlar, madenler = await asyncio.gather(
            kt.fx.fx_currency_rates(),
            kt.treasury.precious_metal_rates(),
        )
        print(kurlar["rateList"], madenler["rateList"])

asyncio.run(main())
```

- Eşzamanlı istekler aynı kapsam için tek bir token isteği yapar.
- Müşteri girişi: `await kt.auth.exchange_code(code, user=...)`, `await kt.auth.login([...])`.
- Kapatma: `async with` kullanın ya da `await kt.aclose()` çağırın.
- Kendi `httpx.AsyncClient`'ınızı `http_client=` ile verebilirsiniz; bu durumda onu kapatmak
  sizin sorumluluğunuzdadır.

Token depoları asenkron istemciden de senkron çağrılır; kendi deponuzu yazıyorsanız metotları
hızlı olmalıdır.
