"""IBAN sorgulama: transferden önce alıcının (maskeli) adını ve bankasını doğrulamak için.

Kullanım::

    python examples/iban_lookup.py TR450020900000067395000006
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

from _common import create_client, is_valid_iban, run


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Bir IBAN'ın sahibini ve bankasını sorgular.")
    parser.add_argument("iban")
    args = parser.parse_args(argv)

    iban = args.iban.replace(" ", "").upper()
    if not is_valid_iban(iban):
        # Hatalı yazılmış bir IBAN için bankaya istek atmaya gerek yok.
        print(f"Geçersiz IBAN: {args.iban}", file=sys.stderr)
        sys.exit(2)

    with create_client() as kt:
        info = kt.transfers.customer_iban_info_for_money_transfer(iban=iban)

    print(f"IBAN       : {iban}")
    print(f"Hesap sahibi: {info.get('customerName')}")
    print(f"Banka      : {info.get('bankName')} ({info.get('bankId')})")
    print(f"Döviz kodu : {info.get('fec')}")


if __name__ == "__main__":
    run(main)
