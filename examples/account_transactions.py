"""Bir hesabın hareketleri ve (istenirse) son hareketin dekontu.

    python examples/account_transactions.py --suffix 1
    python examples/account_transactions.py --suffix 1 --days 7 --count 20
    python examples/account_transactions.py --suffix 1 --receipt     # son hareketin dekontu
    python examples/account_transactions.py --suffix 1 --customer    # müşteri girişiyle

``--suffix`` hesabın ek numarasıdır; ``account_list.py`` çıktısındaki "Ek No" sütunu.
"""

from __future__ import annotations

import argparse
import datetime as dt
from collections.abc import Sequence

from _common import as_list, create_client, ensure_login, print_table, run


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Hesap hareketlerini gösterir.")
    parser.add_argument("--suffix", type=int, required=True, help="hesap ek numarası")
    parser.add_argument(
        "--days", type=int, default=30, help="kaç gün geriye gidilsin (varsayılan 30)"
    )
    parser.add_argument(
        "--count", type=int, default=50, help="en fazla kaç hareket (varsayılan 50)"
    )
    parser.add_argument("--customer", action="store_true", help="müşteri girişiyle sorgula (/v2)")
    parser.add_argument("--receipt", action="store_true", help="son hareketin dekontunu da göster")
    args = parser.parse_args(argv)

    end = dt.date.today()
    begin = end - dt.timedelta(days=args.days)
    query = {"suffix": args.suffix, "begin_date": begin, "end_date": end, "item_count": args.count}

    with create_client() as kt:
        if args.customer:
            ensure_login(kt, ["accounts"])
            response = kt.tpp_accounts.account_transactions_v2(**query)
        else:
            response = kt.accounts.account_transactions_v3(**query)

        activities = as_list(response.value, "accountActivities")
        print(f"{begin} - {end} arası {len(activities)} hareket (ek no {args.suffix}):\n")
        print_table(
            activities,
            [
                ("date", "Tarih"),
                ("amount", "Tutar"),
                ("fxCode", "Döviz"),
                ("balance", "Bakiye"),
                ("description", "Açıklama"),
            ],
        )

        if args.receipt and activities:
            reference = activities[0].get("transactionReference")
            if not reference:
                print("\nSon harekette transactionReference yok; dekont alınamıyor.")
                return
            if args.customer:
                receipt = kt.tpp_accounts.receipt_v2(transaction_reference=reference)
            else:
                receipt = kt.accounts.receipt_v3(transaction_reference=reference)
            print(f"\nDekont: {receipt.get('title')} - {receipt.get('description')}")
            print_table(as_list(receipt.value, "slipList"), [("key", "Alan"), ("value", "Değer")])


if __name__ == "__main__":
    run(main)
