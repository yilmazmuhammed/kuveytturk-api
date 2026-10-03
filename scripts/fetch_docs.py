#!/usr/bin/env python3
"""Kuveyt Türk API Market dokümanlarını ``apidocs/`` klasörüne indirir.

``apidocs/`` ayrı bir private repodur (bkz. scripts/docstore.py); indirmeden sonra değişiklikleri
orada commit'leyin.

Geliştirici portalı dokümanları bir JSON API'sinden Markdown olarak sunar; bu betik menüyü ve
doküman sayfalarını indirir. Çıktı, scripts/build_spec.py'nin girdisidir.

    python scripts/fetch_docs.py                 # yalnızca eksik sayfaları indirir
    python scripts/fetch_docs.py --refresh       # hepsini yeniden indirir
    python scripts/fetch_docs.py --match iban    # başlığında "iban" geçen sayfalar

İndirme sırası önem sırasına göredir: önce yetkilendirme ve genel kurallar, sonra hesaplar
ve para transferleri, sonra döviz/kart/hazine, en son geri kalan her şey. Böylece indirme
yarıda kesilirse en çok gereken sayfalar elde olur.

ÖNEMLİ: Sunucu hızlı/paralel istekleri engelliyor (IP bazında, sandbox dahil tüm
*.kuveytturk.com.tr adresleri için yaklaşık iki saat). Bu yüzden istekler tek tek ve aralıklı
gönderilir; art arda hata alınırsa betik ısrar etmeden durur. --delay değerini düşürmeyin.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.error
import urllib.request
from typing import Any

import docstore

PORTAL_API = "https://prep-kuveytturk-portalapi.kuveytturk.com.tr"
MAX_CONSECUTIVE_FAILURES = 2

# İndirme önceliği. Her satır bir basamaktır; kategori adında ya da sayfa başlığında (ASCII'ye
# katlanmış hâlinde) o basamağın sözcüklerinden biri geçen sayfalar o sırada indirilir.
# Mantık: önce yetkilendirme, sonra müşterinin hesabıyla ilgili işlemler, sonra diğer
# bankacılık işlemleri; şube/ATM listesi gibi bilgi servisleri ve kurum içi servisler en sonda.
PRIORITY: tuple[tuple[str, ...], ...] = (
    # 1) Yetkilendirme, imza, başlık parametreleri, test müşterileri
    ("introduction", "baslarken", "api integration", "api entegrasyon", "authorization", "test"),
    # 2) Hesaplar, hesap hareketleri, dekontlar, para transferleri
    (
        "account management",
        "hesap yonetimi",
        "money transfer",
        "para transfer",
        "iban",
        "receipt",
        "dekont",
    ),
    # 3) Müşterinin diğer işlemleri: döviz, kıymetli maden, kartlar, ödemeler
    ("foreign exchange", "doviz", "treasury", "hazine", "card", "kart", "payments", "odemeler"),
    # 4) Eski/sınıflandırılmamış müşteri işlemleri ve diğer işlem servisleri
    ("other", "diger", "cash management", "nakit yonetimi", "payment solutions", "odeme cozumleri"),
    (
        "vpos",
        "e commerce",
        "e ticaret",
        "donations",
        "bagislar",
        "hgs",
        "moneygram",
        "your banking",
    ),
    ("financing", "finansal", "credibility", "kredibilite"),
)
# Bunlar her zaman en sona kalır (müşteri işlemi olmayan bilgi ve kurum içi servisler).
LAST: tuple[str, ...] = (
    "notification services",
    "bilgi hizmetleri",
    "support",
    "destek",
    "real estate",
    "gayrimenkul",
    "golive",
    "bkm",
    "chatbot",
    "architecht",
    "sgk",
    "dms",
    "sms",
)


def fold(text: str) -> str:
    return docstore.slugify(text).replace("-", " ")


def priority(category: str, title: str) -> int:
    folded_category = fold(category)
    if any(keyword in folded_category for keyword in LAST):
        return len(PRIORITY) + 1
    haystack = f"{folded_category} | {fold(title)}"
    for rank, keywords in enumerate(PRIORITY):
        if any(keyword in haystack for keyword in keywords):
            return rank
    return len(PRIORITY)


def fetch_json(path: str, *, language: str, timeout: float = 40.0) -> dict[str, Any]:
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
        payload: dict[str, Any] = json.loads(response.read().decode("utf-8"))
        return payload


def main() -> int:
    parser = argparse.ArgumentParser(description=(__doc__ or "").splitlines()[0])
    parser.add_argument("--refresh", action="store_true", help="eldeki sayfaları da yeniden indir")
    parser.add_argument(
        "--languages",
        default="en,tr",
        help="indirilecek diller, öncelik sırasıyla (varsayılan: en,tr)",
    )
    parser.add_argument("--delay", type=float, default=4.0, help="istekler arası bekleme (saniye)")
    parser.add_argument(
        "--limit", type=int, default=0, help="en fazla bu kadar sayfa (0: sınırsız)"
    )
    parser.add_argument(
        "--match", default="", help="yalnızca başlığında bu metin geçen sayfalar (harf duyarsız)"
    )
    args = parser.parse_args()

    if args.refresh or not docstore.MENU.exists():
        try:
            payload = fetch_json("/api/v1/get-document-menu", language="en")
        except (urllib.error.URLError, OSError, ValueError) as exc:
            print(f"Menü indirilemedi: {exc}", file=sys.stderr)
            return 1
        docstore.save_menu(docstore.simplify_menu(payload))
        time.sleep(args.delay)
    menu = docstore.load_menu()

    languages = [code.strip() for code in args.languages.split(",") if code.strip()]
    ranked = []
    order = 0
    for category in menu:
        for page in category["pages"]:
            order += 1
            if category["language"] not in languages:
                continue
            if args.match.lower() not in page["title"].lower():
                continue
            rank = (
                priority(category["name"], page["title"]),
                languages.index(category["language"]),
                order,
            )
            ranked.append((rank, category, page))
    ranked.sort(key=lambda item: item[0])

    have = docstore.index()
    todo = [
        (category, page) for _, category, page in ranked if args.refresh or page["id"] not in have
    ]
    if args.limit:
        todo = todo[: args.limit]
    print(f"{len(ranked)} sayfa var, {len(todo)} tanesi indirilecek (istek arası {args.delay} sn).")

    failures = 0
    for number, (category, page) in enumerate(todo, 1):
        label = f"[{number}/{len(todo)}] {page['id']}"
        try:
            payload = fetch_json(f"/api/v1/document/{page['id']}", language=category["language"])
        except (urllib.error.URLError, OSError, ValueError) as exc:
            failures += 1
            print(f"{label}: HATA {exc}", file=sys.stderr)
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
        document = payload.get("data")
        if payload.get("statusCode") == 200 and isinstance(document, dict):
            docstore.save_page(
                doc_id=page["id"],
                title=str(document.get("title") or page["title"]),
                category=category["name"],
                language=category["language"],
                status=docstore.status_of(document),
                body=str(document.get("documentData") or ""),
            )
            print(f"{label}: {category['name']} / {page['title']}", flush=True)
        else:
            print(f"{label}: atlandı (statusCode={payload.get('statusCode')})", flush=True)
        time.sleep(args.delay)
    return 0


if __name__ == "__main__":
    sys.exit(main())
