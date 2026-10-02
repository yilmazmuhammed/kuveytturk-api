"""Döviz ve kıymetli maden kurları (müşteri girişi gerekmez).

Kullanım::

    python examples/exchange_rates.py
    python examples/exchange_rates.py --code USD --code EUR
"""

from __future__ import annotations

import argparse
from collections.abc import Mapping, Sequence
from typing import Any

from _common import as_list, create_client, print_table, run

COLUMNS = [("fxCode", "Kod"), ("fxName|name", "Ad"), ("buyRate", "Alış"), ("sellRate", "Satış")]


def code_of(rate: Mapping[str, Any]) -> str:
    parts = str(rate.get("fxCode") or "").upper().split()
    return parts[0] if parts else ""


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Döviz ve kıymetli maden kurlarını gösterir.")
    parser.add_argument(
        "--code", action="append", help="yalnızca bu kod(lar) (ör. USD); tekrarlanabilir"
    )
    args = parser.parse_args(argv)
    wanted = {code.upper() for code in args.code or []}

    with create_client() as kt:
        currencies = as_list(kt.fx.fx_currency_rates().value, "rateList")
        metals = as_list(kt.treasury.precious_metal_rates().value, "rateList")

    for title, rates in (("Döviz kurları", currencies), ("Kıymetli madenler", metals)):
        # Maden kodları "ALT (gr)" biçiminde gelir; karşılaştırmada yalnızca ilk sözcüğe bakılır.
        rows = [rate for rate in rates if not wanted or code_of(rate) in wanted]
        print(f"{title}:")
        print_table(rows, COLUMNS)
        print()


if __name__ == "__main__":
    run(main)
