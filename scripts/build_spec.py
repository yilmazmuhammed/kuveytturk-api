#!/usr/bin/env python3
"""İndirilen dokümanlardan (apidocs/) uç nokta kataloğunu (spec/endpoints.json) üretir.

    python scripts/fetch_docs.py   # dokümanları indir
    python scripts/build_spec.py   # kataloğu üret
    python scripts/generate.py     # katalogdan Python kodunu üret

Dokümanlar elle yazıldığı için tutarsızlıklar içerir; bu betik onları olabildiğince
toparlar, toparlayamadıklarını spec/overrides.json ile düzeltmeye izin verir ve şüpheli
bulduğu her şeyi uyarı olarak raporlar.
"""

from __future__ import annotations

import argparse
import json
import keyword
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlsplit

import docstore

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "spec" / "endpoints.json"
OVERRIDES = ROOT / "spec" / "overrides.json"
DOC_SITE = "https://developer.kuveytturk.com.tr/documentation"

# Doküman kategorisi -> istemcideki özellik adı. Listede olmayanlar adından türetilir.
CATEGORY_RESOURCES = {
    "Account Management - Own": "accounts",
    "Account Management - TPP": "tpp_accounts",
    "Foreign Exchange Transactions": "fx",
    "Credit Card Transactions": "cards",
    "Treasury Services": "treasury",
    "Cash Management": "cash_management",
    "Payment Solutions": "payment_solutions",
    "Virtual POS (VPOS)": "vpos",
    "E-Commerce": "ecommerce",
    "Notification Services": "information",
    "Support management": "support",
    "Payments": "payments",
    "Financing Solutions": "financing",
    "Real Estate Services": "real_estate",
    "Your Banking": "your_banking",
    "Credibility": "credibility",
    "MoneyGram": "moneygram",
    "API-GoLive": "golive",
    "BKM": "bkm",
    "Chatbot": "chatbot",
    "Architecht": "architecht",
    "SGK": "sgk",
    "DMS": "dms",
    "SMS-OTP": "sms_otp",
    "Test": "test_data",
    "Other": "other",
    "Money Transfers": "transfers",
    "HGS Services": "hgs",
    "Donations": "donations",
    # Türkçe menüdeki karşılıkları (yalnızca Türkçe dokümanı olan uç noktalar için)
    "Hesap Yönetimi - Hesaplarınız": "accounts",
    "Hesap Yönetimi - Üçüncü Taraf Yazılım": "tpp_accounts",
    "Para Transferleri": "transfers",
    "Döviz İşlemleri": "fx",
    "Kredi Kart İşlemleri": "cards",
    "Hazine Hizmetleri": "treasury",
    "Nakit Yönetimi": "cash_management",
    "Sanal POS (VPOS)": "vpos",
    "HGS Hizmetleri": "hgs",
    "Ödeme Çözümleri": "payment_solutions",
    "Bağışlar": "donations",
    "Ödemeler": "payments",
    "Bilgi Hizmetleri": "information",
    "E-Ticaret": "ecommerce",
    "Finansal Çözümler": "financing",
    "Gayrimenkul Hizmetleri": "real_estate",
    "Kredibilite": "credibility",
    "Destek Hizmetleri": "support",
    "API - GoLive": "golive",
    "SMS - OTP": "sms_otp",
    "Diğer": "other",
}

# Aşağıdaki tüm anahtarlar fold() ile katlanmış biçimdedir (küçük harf, Türkçe karakterler ASCII).
HEADER_KEYS = {
    "url": "url",
    "method": "method",
    "metod": "method",
    "metot": "method",
    "yontem": "method",
    "version": "version",
    "versiyon": "version",
    "surum": "version",
    "scope": "scope",
    "kapsam": "scope",
    "authorization flow": "flow",
    "authorization": "flow",
    "yetkilendirme akisi": "flow",
    "active": "active",
    "aktif": "active",
}

PATH_SECTIONS = (
    "url parameters",
    "path parameters",
    "route parameters",
    "uri parameters",
    "url parametreleri",
    "yol parametreleri",
)
QUERY_SECTIONS = (
    "query parameters",
    "query string parameters",
    "querystring parameters",
    "sorgu parametreleri",
    "query parametreleri",
)
BODY_SECTIONS = (
    "request parameters",
    "body arguments",
    "body parameters",
    "request body",
    "request body parameters",
    "request",
    "input",
    "istek parametreleri",
    "body argumanlari",
    "govde argumanlari",
    "govde parametreleri",
)
SAMPLE_BODY_SECTIONS = (
    "sample request",
    "sample body",
    "sample request body",
    "request sample",
    "ornek istek",
    "ornek body",
    "ornek govde",
    "ornek request",
)
SAMPLE_QUERY_SECTIONS = (
    "sample query",
    "sample request",
    "sample url",
    "ornek sorgu",
    "ornek query",
    "ornek istek",
)
RESPONSE_SECTIONS = (
    "response parameters",
    "response",
    "response body",
    "output",
    "cevap parametreleri",
    "yanit parametreleri",
    "cevap",
    "yanit",
)
DESCRIPTION_SECTIONS = ("description", "aciklama")

NAME_COLUMNS = ("name", "parameter", "field", "ad", "adi", "parametre", "alan")
TYPE_COLUMNS = ("type", "tur", "turu", "tip", "tipi")
DESCRIPTION_COLUMNS = ("description", "aciklama")
REQUIREMENT_WORDS = ("required", "optional", "mandatory", "zorunlu", "gerekli", "opsiyonel")
REQUIRED_PREFIXES = ("req", "zorunlu", "gerekli", "mandatory", "yes", "evet", "true")
ENVELOPE_FIELDS = ("value", "success", "results", "errormessage", "errorcode")

# Türkçe dokümanlarda kapsam adları da çevrilmiş olabiliyor.
SCOPE_TRANSLATIONS = {
    "krediler": "loans",
    "hesaplar": "accounts",
    "transferler": "transfers",
    "kartlar": "cards",
    "odemeler": "payments",
    "bagislar": "donations",
    "genel": "public",
}

TYPE_MAP = {
    "string": "str",
    "str": "str",
    "text": "str",
    "char": "str",
    "guid": "str",
    "uuid": "str",
    "int": "int",
    "int16": "int",
    "int32": "int",
    "int64": "int",
    "integer": "int",
    "short": "int",
    "long": "int",
    "byte": "int",
    "number": "number",
    "numeric": "number",
    "decimal": "number",
    "double": "number",
    "float": "number",
    "money": "number",
    "bool": "bool",
    "boolean": "bool",
    "datetime": "datetime",
    "date": "datetime",
    "time": "str",
    "timestamp": "datetime",
    "object": "object",
    "dictionary": "object",
    "list": "array",
    "array": "array",
    "enum": "any",
}


# Üretilen metotların kendi argümanlarıyla çakışacak parametre adları ("_" eklenir).
RESERVED_NAMES = frozenset({"self", "body", "extra_query", "extra_body", "request_options"})

# --------------------------------------------------------------------------- yardımcılar


def slugify(text: str) -> str:
    table = str.maketrans("ığüşöçİĞÜŞÖÇ", "igusocIGUSOC")
    text = text.translate(table).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def snake(name: str) -> str:
    """camelCase / PascalCase / serbest metni snake_case Python adına çevirir."""
    table = str.maketrans("ığüşöçİĞÜŞÖÇ", "igusocIGUSOC")
    name = name.translate(table)
    name = re.sub(r"[^0-9A-Za-z]+", "_", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name)
    name = re.sub(r"_+", "_", name).strip("_").lower()
    if not name:
        name = "param"
    if name[0].isdigit():
        name = "_" + name
    if keyword.iskeyword(name) or name in RESERVED_NAMES:
        name += "_"
    return name


_FOLD = str.maketrans("ığüşöçİĞÜŞÖÇ", "igusocIGUSOC")


def fold(text: str) -> str:
    """Karşılaştırma için: Türkçe karakterleri ASCII'ye çevirir ve küçük harfe indirir."""
    return text.translate(_FOLD).lower().strip()


def pick(row: dict[str, str], columns: tuple[str, ...]) -> str:
    return next((row[c] for c in columns if row.get(c)), "")


def clean(text: str) -> str:
    text = re.sub(r"<br\s*/?>", " ", text)
    text = re.sub(r"\*\*|__|`", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def split_sections(markdown: str) -> tuple[str, dict[str, str]]:
    """Markdown'u (başlık öncesi kısım, {küçük harfli başlık: içerik}) olarak böler."""
    parts = re.split(r"^#{1,4}\s+(.+?)\s*$", markdown, flags=re.M)
    sections: dict[str, str] = {}
    for title, body in zip(parts[1::2], parts[2::2]):
        key = fold(clean(title)).rstrip(":").strip()
        sections[key] = sections.get(key, "") + body
    return parts[0], sections


def parse_tables(text: str) -> list[list[dict[str, str]]]:
    """Metindeki Markdown tablolarını {sütun: değer} satır listelerine çevirir."""
    tables: list[list[dict[str, str]]] = []
    lines = text.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index].strip()
        is_header = (
            line.startswith("|")
            and index + 1 < len(lines)
            and re.fullmatch(r"\|?[\s:\-|]+\|?", lines[index + 1].strip() or "x")
        )
        if not is_header:
            index += 1
            continue
        columns = [fold(clean(c)) for c in line.strip("|").split("|")]
        rows: list[dict[str, str]] = []
        index += 2
        while index < len(lines) and "|" in lines[index]:
            cells = [clean(c) for c in lines[index].strip().strip("|").split("|")]
            if len(cells) > len(columns):  # açıklamada "|" geçiyorsa fazlalığı son hücreye kat
                cells = [*cells[: len(columns) - 1], " | ".join(cells[len(columns) - 1 :])]
            rows.append(dict(zip(columns, cells)))
            index += 1
        tables.append(rows)
    return tables


def parse_header(preamble: str) -> dict[str, str]:
    header: dict[str, str] = {}
    for line in preamble.splitlines():
        cells = [clean(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 2 and fold(cells[0]) in HEADER_KEYS:
            header.setdefault(HEADER_KEYS[fold(cells[0])], cells[1])
    return header


def code_blocks(text: str) -> list[str]:
    return [m.group(1).strip() for m in re.finditer(r"```[a-zA-Z]*\s*\n(.*?)```", text, flags=re.S)]


def load_json_lenient(text: str) -> Any:
    for candidate in (text, re.sub(r",(\s*[}\]])", r"\1", text)):
        try:
            return json.loads(candidate)
        except json.JSONDecodeError:
            continue
    return None


def first_section(sections: dict[str, str], names: tuple[str, ...]) -> str:
    for name in names:
        if name in sections:
            return sections[name]
    return ""


def normalize_type(raw: str) -> str:
    key = re.sub(r"[^a-z0-9]", "", raw.lower().split("<")[0].split("(")[0].split("[")[0])
    if raw.strip().endswith("[]") or raw.lower().startswith(("list", "array", "ienumerable")):
        return "array"
    return TYPE_MAP.get(key, "any")


def infer_type(value: Any) -> str:
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "str"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "any"


def is_required(text: str) -> bool:
    return fold(text).startswith(REQUIRED_PREFIXES)


def param_rows(text: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for table in parse_tables(text):
        for row in table:
            name = pick(row, NAME_COLUMNS).strip()
            if not name or set(name) <= {"-"} or not re.fullmatch(r"[\w.\[\]\- ]+", name):
                continue
            requirement = next(
                (v for k, v in row.items() if any(word in k for word in REQUIREMENT_WORDS)), ""
            )
            raw_type = pick(row, TYPE_COLUMNS)
            rows.append(
                {
                    "wire": name.split(".")[-1].strip().replace(" ", ""),
                    "type": normalize_type(raw_type),
                    "raw_type": raw_type,
                    "required": is_required(requirement),
                    "description": pick(row, DESCRIPTION_COLUMNS),
                }
            )
    return rows


def nested_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            keys.add(key)
            keys |= nested_keys(item)
    elif isinstance(value, list):
        for item in value:
            keys |= nested_keys(item)
    return keys


# --------------------------------------------------------------------------- uç nokta çözümleme


def build_body(
    rows: list[dict[str, Any]], sample: Any, warnings: list[str]
) -> tuple[str, list[str], list[dict[str, Any]]]:
    """Gövde parametrelerini çıkarır: (tür, sarmalayıcı yol, parametreler).

    Tablolar iç içe alanları düz liste olarak verir; hangi alanın üst düzey olduğu örnek
    gövdeden anlaşılır. ``{"request": {"contract": {...}}}`` gibi tek anahtarlı sarmalayıcılar
    açılır ve en içteki alanlar parametre yapılır.
    """
    if isinstance(sample, list):
        return "raw", [], []
    if not isinstance(sample, dict):
        if rows:
            warnings.append("örnek gövde çözümlenemedi; tüm tablo satırları üst düzey sayıldı")
        return ("object" if rows else "empty"), [], _dedupe(rows)

    wrap: list[str] = []
    leaf = sample
    while len(leaf) == 1:
        ((key, value),) = leaf.items()
        if not isinstance(value, dict) or not value:
            break
        wrap.append(key)
        leaf = value

    by_lower = {row["wire"].lower(): row for row in reversed(rows)}
    deeper = {k.lower() for k in nested_keys(leaf)} - {k.lower() for k in leaf}
    wrappers = {w.lower() for w in wrap}
    params: list[dict[str, Any]] = []
    for key, value in leaf.items():
        row = by_lower.get(key.lower())
        params.append(
            {
                "wire": key,
                "type": row["type"] if row and row["type"] != "any" else infer_type(value),
                "required": bool(row and row["required"]),
                "description": row["description"] if row else "",
            }
        )
    seen = {p["wire"].lower() for p in params}
    for row in rows:
        lower = row["wire"].lower()
        if lower in seen or lower in wrappers or lower in deeper:
            continue
        seen.add(lower)
        # Örnekte hiç geçmeyen alan: büyük olasılıkla örnekte atlanmış isteğe bağlı üst düzey alan.
        params.append({k: row[k] for k in ("wire", "type", "required", "description")})
    return "object", wrap, params


def _dedupe(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    unique = []
    for row in rows:
        if row["wire"].lower() in seen:
            continue
        seen.add(row["wire"].lower())
        unique.append({k: row[k] for k in ("wire", "type", "required", "description")})
    return unique


def parse_endpoint(page: dict[str, Any], category: str) -> tuple[dict[str, Any] | None, list[str]]:
    """Bir doküman sayfasını (``docstore.load_page`` çıktısı) uç nokta kaydına çevirir.

    Sayfa bir uç nokta anlatmıyorsa ``None`` döner.
    """
    warnings: list[str] = []
    markdown = page.get("body") or ""
    _, sections = split_sections(markdown)
    # Başlık tablosu ilk "##" bölümünden önce gelir; bazı sayfalar ondan önce bir "# Başlık" satırı taşır.
    header = parse_header(re.split(r"^#{2,4}\s", markdown, maxsplit=1, flags=re.M)[0])
    if "url" not in header or "method" not in header:
        return None, warnings

    method = re.split(r"[\s/,]+", header["method"].strip().upper())[0]
    if method not in {"GET", "POST", "PUT", "PATCH", "DELETE"}:
        warnings.append(f"bilinmeyen metot {header['method']!r}")
        return None, warnings

    raw_url = header["url"].strip()
    raw_url = re.sub(r"^https?://[^/]+", "", raw_url)
    raw_url = re.split(r"\?(?!\})", raw_url)[
        0
    ].strip()  # sorguyu at; "{suffix?}" içindeki "?" kalır
    raw_url = re.sub(r"\{\{[^}]*\}\}", "", raw_url)
    path = "/" + raw_url.strip("/ ")
    if " " in path or len(path) < 2:
        warnings.append(f"şüpheli URL {header['url']!r}")
        return None, warnings

    flow_text = fold(header.get("flow", ""))
    if "code" in flow_text or "kod" in flow_text:
        flow = "authorization_code"
    else:
        flow = "client_credentials"
        if not any(word in flow_text for word in ("client", "credential", "istemci")):
            warnings.append(
                f"akış anlaşılamadı ({header.get('flow')!r}); client_credentials varsayıldı"
            )
    scopes = {fold(part) for part in re.split(r"[\s,;/]+", header.get("scope", "")) if part}
    scopes = {SCOPE_TRANSLATIONS.get(part, part) for part in scopes}
    scope = " ".join(sorted(scopes))
    if not scope:
        warnings.append("scope yok")
    elif not re.fullmatch(r"[a-z0-9_. ]+", scope):
        warnings.append(f"şüpheli scope {header.get('scope')!r}")

    path_rows = param_rows(first_section(sections, PATH_SECTIONS))
    query_rows = param_rows(first_section(sections, QUERY_SECTIONS))
    body_rows = param_rows(first_section(sections, BODY_SECTIONS))
    has_body = method in {"POST", "PUT", "PATCH"}
    if not has_body:
        query_rows += body_rows
        body_rows = []

    # Yol parametreleri: URL'deki yer tutucular. Açıklamaları hangi tabloda geçiyorsa oradan alınır.
    described = {row["wire"].lower(): row for row in reversed(path_rows + query_rows + body_rows)}
    path_params = []
    placeholders = re.findall(r"\{([^{}]+)\}", path)
    for placeholder in placeholders:
        name = placeholder.rstrip("?").strip()
        optional = placeholder.strip().endswith("?")
        row = described.get(name.lower(), {})
        path_params.append(
            {
                "wire": name,
                "type": row.get("type") if row.get("type") not in (None, "any") else "str",
                "required": not optional,
                "description": row.get("description", ""),
            }
        )
        path = path.replace("{" + placeholder + "}", "{" + name + "}")
    in_path = {p["wire"].lower() for p in path_params}

    query_params = [row for row in _dedupe(query_rows) if row["wire"].lower() not in in_path]
    known_query = {row["wire"].lower() for row in query_params}
    for block in code_blocks(first_section(sections, SAMPLE_QUERY_SECTIONS)):
        match = re.search(r"\?(\S+)", block.splitlines()[0]) if block else None
        if not match or block.lstrip().startswith("{"):
            continue
        for key, value in parse_qsl(urlsplit("x?" + match.group(1)).query, keep_blank_values=True):
            if key.lower() not in known_query and re.fullmatch(r"[A-Za-z_][\w.]*", key):
                known_query.add(key.lower())
                query_params.append(
                    {"wire": key, "type": "str", "required": False, "description": ""}
                )
                warnings.append(f"sorgu parametresi {key!r} yalnızca örnekte geçiyor")
            del value

    body_kind, body_wrap, body_params = "none", [], []
    if has_body:
        sample = None
        for block in code_blocks(first_section(sections, SAMPLE_BODY_SECTIONS)):
            start = min((i for i in (block.find("{"), block.find("[")) if i >= 0), default=-1)
            if start >= 0:
                sample = load_json_lenient(block[start:])
                if sample is not None:
                    break
        body_rows = [row for row in body_rows if row["wire"].lower() not in in_path]
        body_kind, body_wrap, body_params = build_body(body_rows, sample, warnings)

    response_fields = [
        row["wire"]
        for row in _dedupe(param_rows(first_section(sections, RESPONSE_SECTIONS)))
        if row["wire"].lower() not in ENVELOPE_FIELDS
    ]

    # Başlık tablosunda "Active | false" yazan sayfalar sunucudan kaldırılmış eski uç noktalardır
    # (çağrıldıklarında 404 "Path not found" döner).
    active = fold(header.get("active", "true")) not in ("false", "hayir", "no", "0", "pasif")
    description = clean(first_section(sections, DESCRIPTION_SECTIONS).split("```")[0])
    title = clean(page.get("title") or "")
    endpoint = {
        "id": str(page.get("id") or ""),
        "title": title,
        "category": category,
        "doc_url": f"{DOC_SITE}/{slugify(category)}/{slugify(title)}",
        "status": str(page.get("status") or ""),
        "active": active,
        "method": method,
        "path": path,
        "version": header.get("version", ""),
        "scope": scope,
        "flow": flow,
        "description": description,
        "path_params": path_params,
        "query_params": query_params,
        "body_kind": body_kind,
        "body_wrap": body_wrap,
        "body_params": body_params,
        "response_fields": response_fields,
    }
    return endpoint, warnings


# --------------------------------------------------------------------------- adlandırma


def method_name(title: str) -> str:
    title = re.sub(r"\(.*?\)", " ", title)
    name = snake(title) or "call"
    # "... Inquiry API" gibi başlıklardaki anlamsız son eki at.
    return name[: -len("_api")] if name.endswith("_api") and len(name) > len("_api") else name


def assign_names(endpoints: list[dict[str, Any]], overrides: dict[str, Any]) -> None:
    for endpoint in endpoints:
        override = overrides.get(endpoint["id"], {})
        endpoint.update({k: v for k, v in override.items() if k not in ("resource", "name")})
        endpoint["resource"] = override.get("resource") or CATEGORY_RESOURCES.get(
            endpoint["category"], snake(endpoint["category"])
        )
        endpoint["name"] = override.get("name") or method_name(endpoint["title"])

    by_resource: dict[str, list[dict[str, Any]]] = {}
    for endpoint in endpoints:
        by_resource.setdefault(endpoint["resource"], []).append(endpoint)
    for group in by_resource.values():
        counts = Counter(e["name"] for e in group)
        for name, count in counts.items():
            if count == 1:
                continue
            clashing = [e for e in group if e["name"] == name]
            # Aynı adlı uç noktaları önce sürümle, o da yetmezse sıra numarasıyla ayır.
            for endpoint in clashing:
                version = endpoint["path"].split("/")[1] if endpoint["path"].count("/") > 1 else ""
                if re.fullmatch(r"v\d+", version) and not name.endswith("_" + version):
                    endpoint["name"] = f"{name}_{version}"
            taken: Counter[str] = Counter()
            for endpoint in clashing:
                taken[endpoint["name"]] += 1
                if taken[endpoint["name"]] > 1:
                    endpoint["name"] = f"{endpoint['name']}_{taken[endpoint['name']]}"

    for endpoint in endpoints:
        used: set[str] = set()
        for group_name in ("path_params", "query_params", "body_params"):
            for param in endpoint[group_name]:
                name = snake(param["wire"])
                while name in used:
                    name += "_"
                used.add(name)
                param["name"] = name


# --------------------------------------------------------------------------- ana akış


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--quiet", action="store_true", help="uyarıları yazdırma")
    args = parser.parse_args()

    if not docstore.MENU.exists():
        print("Önce scripts/fetch_docs.py çalıştırın.", file=sys.stderr)
        return 1
    menu = docstore.load_menu()
    pages = docstore.index()
    overrides = json.loads(OVERRIDES.read_text(encoding="utf-8")) if OVERRIDES.exists() else {}
    overrides = {k: v for k, v in overrides.items() if not k.startswith("_")}

    endpoints: list[dict[str, Any]] = []
    missing = skipped = translated = inactive = 0
    report: list[str] = []
    seen: set[tuple[str, str]] = set()
    # Menüde aynı uç noktanın İngilizce ve Türkçe sayfaları ayrı kayıtlardır. İngilizce esas
    # alınır; yalnızca Türkçe sayfası olan uç noktalar sonradan eklenir.
    for language in ("en", "tr"):
        known = set(seen)
        for category in menu:
            if category["language"] != language:
                continue
            for entry in category["pages"]:
                doc_id = entry["id"]
                if doc_id not in pages:
                    missing += 1
                    continue
                page = docstore.load_page(pages[doc_id])
                page["id"] = doc_id
                endpoint, warnings = parse_endpoint(page, category["name"])
                if overrides.get(doc_id, {}).get("skip"):
                    skipped += 1
                    if endpoint is not None:
                        # Atlanan uç noktanın öbür dildeki sayfası da kataloğa girmesin.
                        seen.add((endpoint["method"], endpoint["path"].lower()))
                    continue
                if endpoint is None:
                    skipped += 1
                    if warnings:
                        report.append(
                            f"[{doc_id}] {entry['title']}: ATLANDI - {'; '.join(warnings)}"
                        )
                    continue
                if not endpoint.pop("active"):
                    inactive += 1
                    continue
                key = (endpoint["method"], endpoint["path"].lower())
                if language == "tr" and key in known:
                    translated += 1
                    continue
                seen.add(key)
                endpoint["language"] = language
                endpoints.append(endpoint)
                report.extend(f"[{doc_id}] {endpoint['title']}: {w}" for w in warnings)

    assign_names(endpoints, overrides)
    endpoints.sort(key=lambda e: (e["resource"], e["name"]))

    duplicates = Counter((e["method"], e["path"]) for e in endpoints)
    for (method, path), count in sorted(duplicates.items()):
        if count > 1:
            report.append(f"{method} {path}: {count} farklı dokümanda geçiyor")

    SPEC.parent.mkdir(parents=True, exist_ok=True)
    SPEC.write_text(json.dumps(endpoints, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    if not args.quiet:
        for line in report:
            print("UYARI", line)
    resources = Counter(e["resource"] for e in endpoints)
    print(
        f"{len(endpoints)} uç nokta, {len(resources)} kaynak -> {SPEC.relative_to(ROOT)} "
        f"(atlananlar: uç nokta olmayan {skipped}, pasif {inactive}, İngilizcesi bulunan "
        f"{translated} Türkçe sayfa; {missing} sayfa henüz indirilmedi; "
        f"{len(report)} uyarı)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
