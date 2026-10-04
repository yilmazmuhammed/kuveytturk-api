#!/usr/bin/env python3
"""Elle yapılan bir testin sonucunu spec/test_status.json'a işler ve doküman sayfalarını günceller.

Otomatik betiğin (check_endpoints.py) çağırmadığı uç noktalar için kullanılır: para transferi
gibi işlem yapan uçlar, müşteri girişi isteyen uçlar ve canlı ortam testleri.

    python scripts/record_test.py transfers.outgoing_money_transfer \\
        --durum "test edildi" --sonuc "çalışıyor" --ayrinti "1 TL, kendi hesaplar arası"

    python scripts/record_test.py fx.fx_currency_rates --environment production \\
        --durum "test edildi" --sonuc "çalışıyor"

Ayrıntıdaki IBAN ve uzun numaralar maskelenir; yine de müşteri verisi yazmayın.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
from pathlib import Path

import generate
from check_endpoints import NOT_TESTED, PARTIAL, SECTIONS, SPEC, STATUS, TESTED, mask

DURUMLAR = (TESTED, PARTIAL, NOT_TESTED)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("metot", help="kaynak.metot, ör. transfers.outgoing_money_transfer")
    parser.add_argument("--environment", default="sandbox", choices=sorted(SECTIONS))
    parser.add_argument("--durum", required=True, choices=DURUMLAR)
    parser.add_argument("--sonuc", required=True, help='kısa sonuç, ör. "çalışıyor"')
    parser.add_argument("--ayrinti", default="", help="isteğe bağlı açıklama")
    parser.add_argument("--tarih", default=dt.date.today().isoformat(), help="YYYY-MM-DD")
    parser.add_argument("--no-generate", action="store_true", help="doküman sayfalarını üretme")
    args = parser.parse_args(argv)

    endpoints = {f"{e['resource']}.{e['name']}": e for e in json.loads(SPEC.read_text("utf-8"))}
    if args.metot not in endpoints:
        close = [k for k in endpoints if args.metot.split(".")[-1] in k][:5]
        print(
            f"Bilinmeyen uç nokta: {args.metot}. Benzerleri: {', '.join(close) or '-'}",
            file=sys.stderr,
        )
        return 2
    dt.date.fromisoformat(args.tarih)

    endpoint = endpoints[args.metot]
    status = json.loads(STATUS.read_text("utf-8")) if STATUS.exists() else {"endpoints": {}}
    entry = status["endpoints"].setdefault(
        endpoint["id"],
        {
            "metot": args.metot,
            "istek": f"{endpoint['method']} {endpoint['path']}",
            "sandbox": {"durum": NOT_TESTED, "sonuc": "henüz denenmedi"},
            "canli": {"durum": NOT_TESTED, "sonuc": "henüz denenmedi"},
        },
    )
    result = {"durum": args.durum, "sonuc": mask(args.sonuc), "tarih": args.tarih}
    if args.ayrinti:
        result["ayrinti"] = mask(args.ayrinti)
    result["kaynak"] = "elle"
    entry[SECTIONS[args.environment]] = result
    Path(STATUS).write_text(json.dumps(status, ensure_ascii=False, indent=1) + "\n", "utf-8")
    print(f"{args.metot} [{args.environment}] -> {args.durum}: {result['sonuc']}")

    if not args.no_generate:
        sys.argv = ["generate.py"]
        return generate.main()
    return 0


if __name__ == "__main__":
    sys.exit(main())
