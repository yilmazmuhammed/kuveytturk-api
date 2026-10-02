#!/usr/bin/env python3
"""Kuveyt Türk API Market dokümanlarını yerel önbelleğe (.cache/kt-docs) indirir.

Geliştirici portalı dokümanları bir JSON API'sinden Markdown olarak sunar; bu betik menüyü
ve doküman sayfalarını (önce İngilizce, sonra Türkçe) indirir. Çıktı, scripts/generate.py'nin girdisidir.

    python scripts/fetch_docs.py            # yalnızca eksik sayfaları indirir
    python scripts/fetch_docs.py --refresh  # hepsini yeniden indirir

ÖNEMLİ: Sunucu hızlı/paralel istekleri engelliyor (bağlantıyı IP bazında, tüm
*.kuveytturk.com.tr adresleri için kesiyor). Bu yüzden istekler tek tek ve aralıklı
gönderilir; art arda hata alınırsa betik ısrar etmeden durur. --delay değerini düşürmeyin.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PORTAL_API = "https://prep-kuveytturk-portalapi.kuveytturk.com.tr"
ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "kt-docs"
MAX_CONSECUTIVE_FAILURES = 2


def fetch_json(path: str, *, language: str, timeout: float = 40.0) -> dict:
    request = urllib.request.Request(
        PORTAL_API + path,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Accept-Language": language,
            "languageId": language,
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--refresh", action="store_true", help="önbellekteki sayfaları da yeniden indir"
    )
    parser.add_argument(
        "--languages",
        default="en,tr",
        help="indirilecek diller, öncelik sırasıyla (varsayılan: en,tr)",
    )
    parser.add_argument("--delay", type=float, default=3.0, help="istekler arası bekleme (saniye)")
    parser.add_argument(
        "--limit", type=int, default=0, help="en fazla bu kadar sayfa indir (0: sınırsız)"
    )
    args = parser.parse_args()

    documents = CACHE / "documents"
    documents.mkdir(parents=True, exist_ok=True)
    menu_path = CACHE / "menu.json"

    if args.refresh or not menu_path.exists():
        try:
            menu = fetch_json("/api/v1/get-document-menu", language="en")
        except (urllib.error.URLError, OSError) as exc:
            print(f"Menü indirilemedi: {exc}", file=sys.stderr)
            return 1
        menu_path.write_text(json.dumps(menu, ensure_ascii=False, indent=1), encoding="utf-8")
        time.sleep(args.delay)
    menu = json.loads(menu_path.read_text(encoding="utf-8"))

    # Bazı İngilizce kategorilerin dil alanı boş geliyor; onlar İngilizce sayılır.
    languages = [code.strip() for code in args.languages.split(",") if code.strip()]
    pages = [
        (str(sub["id"]), language)
        for language in languages
        for category in menu["data"]
        if (category.get("languageId") or "en") == language
        for sub in category.get("subMenus") or []
    ]
    todo = [
        (doc_id, language)
        for doc_id, language in pages
        if args.refresh or not (documents / f"{doc_id}.json").exists()
    ]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(pages)} sayfa var, {len(todo)} tanesi indirilecek (istek arası {args.delay} sn).")

    failures = 0
    for index, (doc_id, language) in enumerate(todo, 1):
        try:
            payload = fetch_json(f"/api/v1/document/{doc_id}", language=language)
        except (urllib.error.URLError, OSError, ValueError) as exc:
            failures += 1
            print(f"[{index}/{len(todo)}] {doc_id}: HATA {exc}", file=sys.stderr)
            if failures >= MAX_CONSECUTIVE_FAILURES:
                print(
                    "Art arda hata alındı; sunucu büyük olasılıkla istekleri engelliyor. "
                    "Bir süre bekleyip betiği yeniden çalıştırın (kaldığı yerden devam eder).",
                    file=sys.stderr,
                )
                return 2
            time.sleep(args.delay * 5)
            continue
        failures = 0
        if payload.get("statusCode") == 200 and payload.get("data"):
            (documents / f"{doc_id}.json").write_text(
                json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8"
            )
            print(f"[{index}/{len(todo)}] {doc_id}: {payload['data'].get('title')}")
        else:
            print(
                f"[{index}/{len(todo)}] {doc_id}: atlandı (statusCode={payload.get('statusCode')})"
            )
        time.sleep(args.delay)
    return 0


if __name__ == "__main__":
    sys.exit(main())
