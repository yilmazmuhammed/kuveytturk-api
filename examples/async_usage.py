"""Asenkron kullanım: aynı arayüz, ağa çıkan metotlar ``await`` edilir.

Kullanım::

    python examples/async_usage.py
"""

from __future__ import annotations

import asyncio

from _common import ENV_FILE, as_list, print_table

from kuveytturk_api import AsyncKuveytTurk


async def main() -> None:
    async with AsyncKuveytTurk.from_env(ENV_FILE) as kt:
        # İki istek eşzamanlı gider; ikisi de aynı kapsamı kullandığı için tek token alınır.
        currencies, metals = await asyncio.gather(
            kt.fx.fx_currency_rates(),
            kt.treasury.precious_metal_rates(),
        )
    columns = [("fxCode", "Kod"), ("fxName|name", "Ad"), ("buyRate", "Alış"), ("sellRate", "Satış")]
    print_table(as_list(currencies.value, "rateList") + as_list(metals.value, "rateList"), columns)


if __name__ == "__main__":
    asyncio.run(main())
