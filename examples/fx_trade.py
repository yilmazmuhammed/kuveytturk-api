"""Döviz (USD, EUR...) ve kıymetli maden (ALT, GMS, PLT) alım-satımı.

Kullanım::

    # Önce ne yapılacağını görün (varsayılan: hiçbir işlem gönderilmez)
    python examples/fx_trade.py buy USD 1 --tl-suffix 5 --fx-suffix 2 --corporate-user KULLANICI

    # Gerçekten göndermek için --execute ekleyin (onay sorulur)
    python examples/fx_trade.py buy USD 1 --tl-suffix 5 --fx-suffix 2 --corporate-user KULLANICI --execute
    python examples/fx_trade.py sell USD 1 --tl-suffix 5 --fx-suffix 2 --corporate-user KULLANICI --execute
    python examples/fx_trade.py buy ALT 1 --tl-suffix 5 --fx-suffix 25 --corporate-user KULLANICI --execute

Akış: güncel kur bankadan alınır (alışta ``buyRate``, satışta ``sellRate``), TL hesabının ve
döviz/maden hesabının para birimi kontrol edilir, özet gösterilir ve onaydan sonra işlem
gönderilir. ``--tl-suffix`` ve ``--fx-suffix`` değerlerini ``account_list.py`` çıktısındaki
"Ek No" ve "Döviz" sütunlarından seçin (TL için döviz kodu 0).

Dikkat edilecekler:

* İşlem isteği **asla otomatik tekrarlanmaz**. Zaman aşımı alırsanız işlem gerçekleşmiş olabilir;
  yeniden göndermeden önce hesap bakiyelerini kontrol edin.
* Kur, istek anında bankanın kuruyla uyuşmalı; aradan zaman geçerse banka reddedebilir.
* ``--corporate-user`` işlemi yapan kurumsal internet şubesi kullanıcı adıdır
  (``KUVEYTTURK_CORPORATE_USER`` ortam değişkeninden de okunur). Kıymetli madende zorunludur.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Mapping, Sequence
from decimal import Decimal, InvalidOperation
from typing import Any

from _common import as_list, create_client, run

from kuveytturk_api import KuveytTurk, TransportError

TL_FX_ID = 0


def positive_amount(text: str) -> Decimal:
    try:
        amount = Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"geçersiz miktar: {text!r}") from None
    if amount <= 0 or amount != amount.quantize(Decimal("0.001")):
        raise argparse.ArgumentTypeError(
            "miktar pozitif olmalı ve en fazla 3 ondalık basamak içermeli"
        )
    return amount


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Döviz ve kıymetli maden alım-satımı örneği.")
    parser.add_argument("side", choices=["buy", "sell"], help="buy: TL ile al, sell: TL'ye sat")
    parser.add_argument("code", help="döviz ya da maden kodu: USD, EUR, ALT, GMS, PLT...")
    parser.add_argument("amount", type=positive_amount, help="döviz/maden miktarı (ör. 1)")
    parser.add_argument("--tl-suffix", type=int, required=True, help="TL hesabının ek numarası")
    parser.add_argument(
        "--fx-suffix", type=int, required=True, help="döviz/maden hesabının ek numarası"
    )
    parser.add_argument(
        "--corporate-user",
        default=os.environ.get("KUVEYTTURK_CORPORATE_USER"),
        help="işlemi yapan kurumsal internet şubesi kullanıcı adı",
    )
    parser.add_argument("--execute", action="store_true", help="işlemi gerçekten gönder")
    parser.add_argument("--yes", action="store_true", help="onay sorma")
    parser.add_argument("--allow-production", action="store_true", help="canlı ortamda izin ver")
    return parser


def code_of(rate: Mapping[str, Any]) -> str:
    """Kurun kodu; maden kodları "ALT (gr)" biçiminde geldiği için yalnızca ilk sözcük."""
    parts = str(rate.get("fxCode") or "").upper().split()
    return parts[0] if parts else ""


def find_rate(kt: KuveytTurk, code: str) -> tuple[Mapping[str, Any], bool]:
    """Kodun güncel kurunu ve kıymetli maden olup olmadığını döndürür."""
    for rate in as_list(kt.fx.fx_currency_rates().value, "rateList"):
        if code_of(rate) == code:
            return rate, False
    for rate in as_list(kt.treasury.precious_metal_rates().value, "rateList"):
        if code_of(rate) == code:
            return rate, True
    raise SystemExit(f"Bankanın kur listesinde {code} yok.")


def check_accounts(kt: KuveytTurk, tl_suffix: int, fx_suffix: int, fx_id: Any) -> None:
    """İki hesabın var olduğunu ve para birimlerinin işlemle uyuştuğunu doğrular."""
    accounts = {
        a.get("suffix"): a for a in as_list(kt.accounts.account_list_v3().value, "accountList")
    }
    problems = []
    for suffix, expected, label in ((tl_suffix, TL_FX_ID, "TL"), (fx_suffix, fx_id, "döviz/maden")):
        account = accounts.get(suffix)
        if account is None:
            problems.append(f"ek no {suffix} bulunamadı")
        elif account.get("fxId") != expected:
            problems.append(
                f"ek no {suffix} {label} hesabı değil (döviz kodu {account.get('fxId')}, beklenen {expected})"
            )
    if problems:
        print("Hesaplar uygun değil: " + "; ".join(problems), file=sys.stderr)
        sys.exit(2)


def main(argv: Sequence[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    code = args.code.upper()
    buying = args.side == "buy"

    with create_client() as kt:
        rate_info, is_metal = find_rate(kt, code)
        if is_metal and not args.corporate_user:
            print("Kıymetli maden işleminde --corporate-user zorunlu.", file=sys.stderr)
            sys.exit(2)
        check_accounts(kt, args.tl_suffix, args.fx_suffix, rate_info.get("fxId"))

        # Alışta bankanın satış fiyatı (buyRate), satışta alış fiyatı (sellRate) kullanılır.
        rate = Decimal(str(rate_info["buyRate" if buying else "sellRate"]))
        source, target = (
            (args.tl_suffix, args.fx_suffix) if buying else (args.fx_suffix, args.tl_suffix)
        )
        params: dict[str, Any] = {
            "account_suffix_from": source,
            "account_suffix_to": target,
            "exchange_amount": args.amount,
            "corporate_web_user_name": args.corporate_user,
            ("buy_rate" if buying else "sell_rate"): rate,
        }
        if not params["corporate_web_user_name"]:
            del params["corporate_web_user_name"]

        print(f"Ortam    : {kt.environment.name}")
        print(f"İşlem    : {args.amount} {code} {'alış' if buying else 'satış'}")
        print(f"Kur      : {rate}  (yaklaşık {(args.amount * rate).quantize(Decimal('0.01'))} TL)")
        print(f"Hesaplar : ek no {source} -> ek no {target}")
        print("\nGönderilecek parametreler:")
        print(json.dumps(params, indent=2, ensure_ascii=False, default=str))

        if not args.execute:
            print("\nDeneme modu: işlem gönderilmedi. Göndermek için --execute ekleyin.")
            return
        if kt.environment.name == "production" and not args.allow_production:
            print("Canlı ortamda işlem için --allow-production da gerekir.", file=sys.stderr)
            sys.exit(2)
        if not args.yes and input("\nBu işlemi göndermek için EVET yazın: ").strip() != "EVET":
            print("Vazgeçildi; işlem gönderilmedi.")
            return

        if is_metal:
            method = kt.treasury.precious_metal_buy if buying else kt.treasury.precious_metal_sell
        else:
            method = kt.fx.fx_currency_buy if buying else kt.fx.fx_currency_sell
        try:
            response = method(**params)
        except TransportError as exc:
            print(
                f"İsteğin sonucu bilinmiyor ({exc}).\n"
                "Yeniden GÖNDERMEYİN; önce hesap bakiyelerini kontrol edin.",
                file=sys.stderr,
            )
            sys.exit(3)

    print("\nİşlem yanıtı:")
    print(json.dumps(response.value, indent=2, ensure_ascii=False, default=str))


if __name__ == "__main__":
    run(main)
