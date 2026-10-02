"""Bir IBAN'a para transferi ve transfer durumu sorgulama.

Kullanım::

    # Önce ne gönderileceğini görün (varsayılan: hiçbir şey gönderilmez)
    python examples/money_transfer.py send --from-suffix 1 --iban TR330006100519786457841326 \\
        --amount 10.50 --corporate-user KULLANICI --description "Deneme"

    # Gerçekten göndermek için --execute ekleyin (onay sorulur)
    python examples/money_transfer.py send ... --execute

    # Bir transferin durumunu sorgulayın
    python examples/money_transfer.py state --type FAST --out-going-id 123456

Akış: IBAN yerel olarak doğrulanır, bankadan alıcının (maskeli) adı ve bankası sorgulanır,
özet gösterilir ve onaydan sonra ``POST /v1/moneytransfer/outgoingmoneytransfer`` çağrılır.

Dikkat edilecekler:

* Transfer isteği **asla otomatik tekrarlanmaz**. İstek zaman aşımına uğrarsa işlemin gerçekleşip
  gerçekleşmediği bilinmez; yeniden göndermeden önce hesap hareketlerini kontrol edin.
* ``--corporate-user`` işlemi yapan kurumsal internet şubesi kullanıcı adıdır
  (``KUVEYTTURK_CORPORATE_USER`` ortam değişkeninden de okunur). Sandbox'ta test kurumsal
  müşterilerinin kullanıcı adları geliştirici portalındaki test müşteri listesindedir.
* Resmî dokümandaki parametre listesi eksik: ``receiverIban`` ve ``corporateWebUserName``
  dokümanda yok ama API bunları zorunlu tutuyor. ``--transfer-type`` kodunun değerleri de
  dokümanda açıklanmıyor; gerekiyorsa değerini Kuveyt Türk API Market ekibinden teyit edin.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from collections.abc import Sequence
from decimal import Decimal, InvalidOperation

from _common import create_client, is_valid_iban, run

from kuveytturk_api import APIError, TransportError


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
    parser = argparse.ArgumentParser(description="IBAN'a para transferi örneği.")
    commands = parser.add_subparsers(dest="command", required=True)

    send = commands.add_parser("send", help="bir IBAN'a transfer")
    send.add_argument("--from-suffix", type=int, required=True, help="gönderen hesabın ek numarası")
    send.add_argument("--iban", required=True, help="alıcının IBAN'ı")
    send.add_argument("--amount", type=positive_amount, required=True, help="tutar (ör. 10.50)")
    send.add_argument(
        "--corporate-user",
        default=os.environ.get("KUVEYTTURK_CORPORATE_USER"),
        help="işlemi yapan kurumsal internet şubesi kullanıcı adı",
    )
    send.add_argument("--description", default="", help="açıklama")
    send.add_argument("--transfer-type", type=int, help="transfer türü kodu (isteğe bağlı)")
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
    iban = args.iban.replace(" ", "").upper()
    if not is_valid_iban(iban):
        print(f"Geçersiz IBAN: {args.iban}", file=sys.stderr)
        sys.exit(2)
    if not args.corporate_user:
        print("--corporate-user (ya da KUVEYTTURK_CORPORATE_USER) gerekli.", file=sys.stderr)
        sys.exit(2)

    transfer = {
        "sender_account_suffix": args.from_suffix,
        "receiver_iban": iban,
        "money_transfer_amount": args.amount,
        "corporate_web_user_name": args.corporate_user,
        "money_transfer_description": args.description or None,
        "transfer_type": args.transfer_type,
    }
    with create_client() as kt:
        environment = kt.environment.name
        try:
            # Alıcıyı göndermeden önce doğrula: banka maskeli adı ve bankayı döndürür.
            receiver = kt.transfers.customer_iban_info_for_money_transfer(iban=iban)
            owner = f"{receiver.get('customerName')} - {receiver.get('bankName')}"
        except APIError as exc:
            owner = f"sorgulanamadı ({exc.error_message or exc})"

        print(f"Ortam    : {environment}")
        print(f"Gönderen : ek no {args.from_suffix} ({args.corporate_user})")
        print(f"Alıcı    : {iban} ({owner})")
        print(f"Tutar    : {args.amount}")
        print(f"Açıklama : {args.description or '-'}")
        sent = {key: value for key, value in transfer.items() if value is not None}
        print("\nGönderilecek parametreler:")
        print(json.dumps(sent, indent=2, ensure_ascii=False, default=str))

        if not args.execute:
            print("\nDeneme modu: transfer gönderilmedi. Göndermek için --execute ekleyin.")
            return
        if environment == "production" and not args.allow_production:
            print("Canlı ortamda transfer için --allow-production da gerekir.", file=sys.stderr)
            sys.exit(2)
        if not args.yes and input("\nBu transferi göndermek için EVET yazın: ").strip() != "EVET":
            print("Vazgeçildi; transfer gönderilmedi.")
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
    print(f"İşlem no       : {response.get('moneyTransferTransactionId')}")
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
