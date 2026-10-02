"""Hesap listesi.

    python examples/account_list.py                 # uygulamanın bağlı olduğu müşterinin hesapları
    python examples/account_list.py --only-open
    python examples/account_list.py --customer      # müşteri girişiyle (authorization code)

İki ayrı uç nokta vardır:

* ``GET /v3/accounts`` — client credentials; kurumun kendi hesapları için (``kt.accounts``).
* ``GET /v2/accounts`` — authorization code; giriş yapan müşterinin hesapları (``kt.tpp_accounts``).
"""

from __future__ import annotations

import argparse
from collections.abc import Sequence

from _common import as_list, create_client, ensure_login, print_table, run


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Hesap listesini gösterir.")
    parser.add_argument("--customer", action="store_true", help="müşteri girişiyle listele (/v2)")
    parser.add_argument("--only-open", action="store_true", help="yalnızca açık hesaplar")
    parser.add_argument("--suffix", type=int, help="yalnızca bu ek numaralı hesap")
    args = parser.parse_args(argv)

    filters = {"suffix": args.suffix, "only_open": True if args.only_open else None}
    with create_client() as kt:
        if args.customer:
            ensure_login(kt, ["accounts"])
            response = kt.tpp_accounts.account_list_v2(**filters)
        else:
            response = kt.accounts.account_list_v3(**filters)

    print_table(
        as_list(response.value, "accountList"),
        [
            ("suffix", "Ek No"),
            ("name", "Hesap Adı"),
            ("productType|type", "Tür"),
            ("fxCode|fxId", "Döviz"),
            ("balance", "Bakiye"),
            ("availableBalance|avaibleBalance", "Kullanılabilir"),
            ("iban", "IBAN"),
        ],
    )


if __name__ == "__main__":
    run(main)
