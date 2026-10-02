"""Para transferi (hesaptan hesaba) ve transfer durumu sorgulama.

    # Önce ne gönderileceğini görün (varsayılan: hiçbir şey gönderilmez)
    python examples/money_transfer.py send --from-suffix 1 --to-account 123456 --to-suffix 1 \\
        --amount 10.50 --transfer-type 2 --description "Deneme"

    # Gerçekten göndermek için --execute ekleyin (onay sorulur)
    python examples/money_transfer.py send ... --execute

    # Bir transferin durumunu sorgulayın
    python examples/money_transfer.py state --type FAST --out-going-id 123456

Dikkat edilecekler:

* Transfer isteği **asla otomatik tekrarlanmaz**. İstek zaman aşımına uğrarsa işlemin gerçekleşip
  gerçekleşmediği bilinmez; yeniden göndermeden önce hesap hareketlerini kontrol edin.
* ``--transfer-type`` değerinin anlamı (havale / EFT / FAST / virman) API dokümanında
  açıklanmıyor; uygulamanız için geçerli değeri Kuveyt Türk API Market ekibinden teyit edin.
* Dokümandaki istek gövdesi alıcıyı hesap numarası + ek no ile tanımlar; alıcıyı **IBAN ile**
  belirten alanlar güncel dokümanda yer almadığı için bu örnek IBAN'a transfer yapmaz.
  Alıcı IBAN'ını doğrulamak için ``iban_lookup.py`` örneğine bakın.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from decimal import Decimal, InvalidOperation

from _common import create_client, run

from kuveytturk_api import TransportError


def positive_amount(text: str) -> Decimal:
    try:
        amount = Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(f"geçersiz tutar: {text!r}") from None
    if amount <= 0 or amount != amount.quantize(Decimal("0.01")):
        raise argparse.ArgumentTypeError(
            "tutar pozitif olmalı ve en fazla 2 ondalık basamak içermeli"
        )
    return amount


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Para transferi örneği.")
    commands = parser.add_subparsers(dest="command", required=True)

    send = commands.add_parser("send", help="hesaptan hesaba transfer")
    send.add_argument("--from-suffix", type=int, required=True, help="gönderen hesabın ek numarası")
    send.add_argument("--to-account", type=int, required=True, help="alıcı müşteri/hesap numarası")
    send.add_argument("--to-suffix", type=int, required=True, help="alıcı hesabın ek numarası")
    send.add_argument("--amount", type=positive_amount, required=True, help="tutar (ör. 10.50)")
    send.add_argument("--transfer-type", type=int, required=True, help="transfer türü kodu")
    send.add_argument("--description", default="", help="açıklama")
    send.add_argument("--execute", action="store_true", help="isteği gerçekten gönder")
    send.add_argument("--yes", action="store_true", help="onay sorma")
    send.add_argument(
        "--allow-production", action="store_true", help="canlı ortamda göndermeye izin ver"
    )

    state = commands.add_parser("state", help="transfer durumu sorgula")
    state.add_argument("--type", required=True, help="VIRMAN, HAVALE, FAST, ...")
    state.add_argument("--out-going-id", help="giden transfer id'si (VIRMAN dışındakiler için)")
    state.add_argument("--virman-key", help="virman işlem anahtarı (VIRMAN için)")
    return parser


def send(args: argparse.Namespace) -> None:
    transfer = {
        "sender_account_suffix": args.from_suffix,
        "receiver_account_number": args.to_account,
        "receiver_account_suffix": args.to_suffix,
        "money_transfer_amount": args.amount,
        "transfer_type": args.transfer_type,
        "money_transfer_description": args.description or None,
    }
    with create_client() as kt:
        environment = kt.environment.name
        print(f"Ortam: {environment}")
        print(json.dumps(transfer, indent=2, ensure_ascii=False, default=str))

        if not args.execute:
            print("\nDeneme modu: istek gönderilmedi. Göndermek için --execute ekleyin.")
            return
        if environment == "production" and not args.allow_production:
            print("Canlı ortamda transfer için --allow-production da gerekir.", file=sys.stderr)
            sys.exit(2)
        if not args.yes and input("\nBu transferi göndermek için EVET yazın: ").strip() != "EVET":
            print("Vazgeçildi; istek gönderilmedi.")
            return

        try:
            response = kt.transfers.outgoing_money_transfer(**transfer)
        except TransportError as exc:
            # Yanıt alınamadı: işlem bankaya ulaşmış ve gerçekleşmiş olabilir.
            print(
                f"İsteğin sonucu bilinmiyor ({exc}).\n"
                "Yeniden GÖNDERMEYİN; önce hesap hareketlerinden işlemin durumunu kontrol edin.",
                file=sys.stderr,
            )
            sys.exit(3)

    print("\nTransfer talebi alındı.")
    print(f"İşlem no      : {response.get('moneyTransferTransactionId')}")
    print(f"İşlem referansı: {response.execution_reference_id}")


def state(args: argparse.Namespace) -> None:
    with create_client() as kt:
        response = kt.transfers.money_transfer_state(
            transfer_type=args.type,
            out_going_id=args.out_going_id,
            virman_key=args.virman_key,
        )
    print(f"Tür   : {response.get('transferType')}")
    print(f"Durum : {response.get('state')} - {response.get('stateDescription')}")


def main(argv: Sequence[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    if args.command == "send":
        send(args)
    else:
        state(args)


if __name__ == "__main__":
    run(main)
