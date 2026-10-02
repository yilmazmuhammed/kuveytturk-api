#!/usr/bin/env python3
"""spec/endpoints.json kataloğundan uç nokta metotlarını ve ENDPOINTS.md dosyasını üretir.

    python scripts/generate.py          # dosyaları yeniden yazar
    python scripts/generate.py --check  # üretilen dosyalar güncel değilse 1 döner (CI için)

src/kuveytturk_api/resources/ altındaki ``_resource.py`` dışındaki her şey bu betiğin
çıktısıdır; elle düzenlemeyin, kataloğu ya da bu betiği değiştirip yeniden üretin.
"""

from __future__ import annotations

import argparse
import json
import sys
import textwrap
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "spec" / "endpoints.json"
OUT = ROOT / "src" / "kuveytturk_api" / "resources"
ENDPOINTS_MD = ROOT / "ENDPOINTS.md"
KEEP = {"_resource.py"}

BANNER = '"""{doc}\n\nBu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.\n"""'

PY_TYPES = {
    "str": "str",
    "int": "int",
    "number": "Number",
    "bool": "bool",
    "datetime": "DateLike",
    "object": "Mapping[str, Any]",
    "array": "Sequence[Any]",
    "any": "Any",
}

FLOW_LABELS = {
    "client_credentials": "client credentials",
    "authorization_code": "authorization code (müşteri girişi gerekir)",
}

# Kaynakların sınıf belgelerinde ve ENDPOINTS.md'de görünen açıklamaları.
RESOURCE_TITLES = {
    "accounts": "Hesap yönetimi (kurumun kendi hesapları)",
    "tpp_accounts": "Hesap yönetimi (TPP - müşteri adına)",
    "fx": "Döviz işlemleri",
    "cards": "Kredi kartı işlemleri",
    "treasury": "Hazine servisleri (kıymetli maden, kur)",
    "transfers": "Para transferleri",
    "cash_management": "Nakit yönetimi",
    "payment_solutions": "Ödeme çözümleri",
    "vpos": "Sanal POS",
    "ecommerce": "E-ticaret",
    "information": "Bilgi servisleri (şube, ATM, parametre sorguları...)",
    "hgs": "HGS servisleri",
    "donations": "Bağışlar",
    "support": "Destek yönetimi",
    "payments": "Ödemeler",
    "financing": "Finansman çözümleri",
    "real_estate": "Gayrimenkul servisleri",
    "your_banking": "Senin Bankan",
    "credibility": "Kredibilite",
    "moneygram": "MoneyGram",
    "golive": "API Go-Live",
    "bkm": "BKM",
    "chatbot": "Chatbot",
    "architecht": "Architecht",
    "sgk": "SGK",
    "dms": "Doküman yönetimi (DMS)",
    "sms_otp": "SMS / OTP",
    "test_data": "Test verileri",
    "other": "Diğer",
}


def class_name(resource: str) -> str:
    return "".join(part.capitalize() for part in resource.split("_"))


def wrap(text: str, indent: str, width: int = 96) -> list[str]:
    return textwrap.wrap(
        text,
        width=width,
        initial_indent=indent,
        subsequent_indent=indent,
        break_long_words=False,
        break_on_hyphens=False,
    )


def escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"""', "'''")


def all_params(endpoint: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    groups = (("path", "path_params"), ("query", "query_params"), ("body", "body_params"))
    return [(kind, param) for kind, key in groups for param in endpoint[key]]


def signature(endpoint: dict[str, Any]) -> list[str]:
    """Metodun parametre satırları: önce zorunlular, sonra isteğe bağlılar; hepsi anahtar sözcüklü."""
    params = all_params(endpoint)
    required = [p for kind, p in params if p["required"]]
    optional = [p for kind, p in params if not p["required"]]
    lines = [f"{p['name']}: {PY_TYPES[p['type']]}," for p in required]
    lines += [f"{p['name']}: {PY_TYPES[p['type']]} | None = None," for p in optional]
    if endpoint["body_kind"] == "raw":
        lines.append("body: Any = None,")
    lines.append("extra_query: Mapping[str, Any] | None = None,")
    if endpoint["body_kind"] in ("object", "empty"):
        lines.append("extra_body: Mapping[str, Any] | None = None,")
    lines.append("request_options: RequestOptions | None = None,")
    return lines


def docstring(endpoint: dict[str, Any]) -> list[str]:
    indent = " " * 8
    lines = [f'{indent}"""{escape(endpoint["title"])}.', ""]
    lines.append(f"{indent}``{endpoint['method']} {endpoint['path']}``")
    lines.append("")
    meta = f"Kapsam: ``{endpoint['scope'] or '-'}`` · Akış: {FLOW_LABELS[endpoint['flow']]}"
    if endpoint.get("status") and endpoint["status"].upper() != "ACTIVE":
        meta += f" · Durum: {endpoint['status']}"
    lines.append(indent + meta)
    if endpoint["description"]:
        lines.append("")
        lines += wrap(escape(endpoint["description"]), indent)
    params = all_params(endpoint)
    if params or endpoint["body_kind"] == "raw":
        lines += ["", f"{indent}Args:"]
        for kind, param in params:
            where = {"path": "yol", "query": "sorgu", "body": "gövde"}[kind]
            wire = f"``{param['wire']}``" if param["wire"] != param["name"] else ""
            head = ", ".join(x for x in (wire, where, "zorunlu" if param["required"] else "") if x)
            text = f"{param['name']}: ({head}) {escape(param['description'])}".rstrip()
            wrapped = wrap(text, indent + "    ")
            lines.append(wrapped[0])
            lines += [indent + "        " + line.strip() for line in wrapped[1:]]
        if endpoint["body_kind"] == "raw":
            lines.append(f"{indent}    body: İstek gövdesi (dokümandaki örneğe göre hazırlanır).")
    if endpoint["body_wrap"]:
        path = " -> ".join(f"``{w}``" for w in endpoint["body_wrap"])
        lines += [
            "",
            *wrap(f"Gövde alanları istekte {path} nesnesinin içine yerleştirilir.", indent),
        ]
    if endpoint["response_fields"]:
        fields = ", ".join(endpoint["response_fields"][:30])
        if len(endpoint["response_fields"]) > 30:
            fields += ", ..."
        lines += ["", *wrap(f"Yanıt alanları: {escape(fields)}", indent)]
    lines += ["", f"{indent}Doküman: {endpoint['doc_url']}", f'{indent}"""']
    return lines


def merge_statement(target: str, params: list[dict[str, Any]], extra: str) -> list[str]:
    """``hedef = merge({...}, extra)`` atamasını üretir; sözlük uzunsa satırlara böler."""
    indent = " " * 8
    if not params:
        return [f"{indent}{target} = merge({{}}, {extra})"]
    lines = [f"{indent}{target} = merge(", f"{indent}    {{"]
    lines += [f'{indent}        "{p["wire"]}": {p["name"]},' for p in params]
    lines += [f"{indent}    }},", f"{indent}    {extra},", f"{indent})"]
    return lines


def call(endpoint: dict[str, Any], *, is_async: bool) -> list[str]:
    indent = " " * 8
    lines: list[str] = []

    def mapping(params: list[dict[str, Any]]) -> str:
        return "{" + ", ".join(f'"{p["wire"]}": {p["name"]}' for p in params) + "}"

    args = [f'"{endpoint["method"]}"', f'"{endpoint["path"]}"', f'scope="{endpoint["scope"]}"']
    args.append(f'flow="{endpoint["flow"]}"')

    optional_path = [p for p in endpoint["path_params"] if not p["required"]]
    if optional_path:
        # İsteğe bağlı yol parçası verilmediyse şablondan çıkar (ör. /v2/accounts/{suffix?}).
        param = optional_path[-1]
        lines.append(f'{indent}_path = "{endpoint["path"]}"')
        lines.append(f"{indent}if {param['name']} is None:")
        lines.append(f'{indent}    _path = _path.replace("/{{{param["wire"]}}}", "")')
        args[1] = "_path"
        required_map = mapping([p for p in endpoint["path_params"] if p["required"]])
        lines.append(f"{indent}_path_params: dict[str, Any] = {required_map}")
        lines.append(f"{indent}if {param['name']} is not None:")
        lines.append(f'{indent}    _path_params["{param["wire"]}"] = {param["name"]}')
        args.append("path_params=_path_params")
    elif endpoint["path_params"]:
        args.append(f"path_params={mapping(endpoint['path_params'])}")

    lines += merge_statement("_query", endpoint["query_params"], "extra_query")
    args.append("query=_query")

    if endpoint["body_kind"] in ("object", "empty"):
        lines += merge_statement("_body: Any", endpoint["body_params"], "extra_body")
        for key in reversed(endpoint["body_wrap"]):
            lines.append(f'{indent}_body = {{"{key}": _body}}')
        args.append("body=_body")
    elif endpoint["body_kind"] == "raw":
        args.append("body=body")
    args.append("options=request_options")

    prefix = "return await" if is_async else "return"
    lines.append(f"{indent}{prefix} self._client.request(")
    lines += [f"{indent}    {arg}," for arg in args]
    lines.append(f"{indent})")
    return lines


def render_method(endpoint: dict[str, Any], *, is_async: bool) -> list[str]:
    keyword = "async def" if is_async else "def"
    lines = [f"    {keyword} {endpoint['name']}(", "        self,", "        *,"]
    lines += [f"        {line}" for line in signature(endpoint)]
    lines.append("    ) -> APIResponse:")
    lines += docstring(endpoint)
    lines += call(endpoint, is_async=is_async)
    return lines


def render_module(resource: str, endpoints: list[dict[str, Any]]) -> str:
    title = RESOURCE_TITLES.get(resource, resource)
    cls = class_name(resource)
    used_types = {PY_TYPES[p["type"]] for e in endpoints for _, p in all_params(e)}
    lines = [
        BANNER.format(doc=f"{title} uç noktaları (``kt.{resource}``)."),
        "",
        "from __future__ import annotations",
        "",
        "from collections.abc import Mapping"
        + (", Sequence" if "Sequence[Any]" in used_types else ""),
        "from typing import Any",
        "",
        "from .._base import RequestOptions",
        "from ..response import APIResponse",
    ]
    helpers = [name for name in ("DateLike", "Number") if name in used_types]
    lines.append(
        "from ._resource import "
        + ", ".join([*sorted(["AsyncResource", "Resource", *helpers]), "merge"])
    )
    exported = ", ".join(f'"{name}"' for name in sorted([cls, f"Async{cls}"]))
    lines += ["", f"__all__ = [{exported}]"]
    for is_async in (False, True):
        name = f"Async{cls}" if is_async else cls
        base = "AsyncResource" if is_async else "Resource"
        lines += ["", "", f"class {name}({base}):"]
        suffix = " (asenkron)" if is_async else ""
        lines.append(f'    """{title}{suffix} - ``kt.{resource}``."""')
        for endpoint in endpoints:
            lines.append("")
            lines += render_method(endpoint, is_async=is_async)
    return "\n".join(lines) + "\n"


def render_init(resources: dict[str, list[dict[str, Any]]]) -> str:
    names = sorted(resources)
    lines = [
        BANNER.format(doc="Uç nokta grupları ve istemcilere eklenen kaynak özellikleri."),
        "",
        "from __future__ import annotations",
        "",
        "from ._resource import AsyncResource, Resource, ResourceHost",
    ]
    for name in names:
        cls = class_name(name)
        lines.append(f"from .{name} import " + ", ".join(sorted([cls, f"Async{cls}"])))
    exported = sorted(
        ["AsyncResource", "AsyncResourcesMixin", "Resource", "ResourcesMixin"]
        + [f"{prefix}{class_name(n)}" for n in names for prefix in ("", "Async")]
    )
    lines += ["", "__all__ = ["]
    lines += [f'    "{item}",' for item in exported]
    lines.append("]")
    for is_async in (False, True):
        mixin = "AsyncResourcesMixin" if is_async else "ResourcesMixin"
        kind = "Asenkron" if is_async else "Senkron"
        lines += ["", "", f"class {mixin}(ResourceHost):"]
        lines.append(f'    """{kind} istemcinin kaynak özellikleri (``kt.accounts`` gibi)."""')
        if not names:
            continue
        for name in names:
            cls = ("Async" if is_async else "") + class_name(name)
            count = len(resources[name])
            lines += [
                "",
                "    @property",
                f"    def {name}(self) -> {cls}:",
                f'        """{RESOURCE_TITLES.get(name, name)} ({count} uç nokta)."""',
                f'        return self._resource("{name}", {cls})',
            ]
    return "\n".join(lines) + "\n"


def render_endpoints_md(resources: dict[str, list[dict[str, Any]]]) -> str:
    total = sum(len(v) for v in resources.values())
    lines = [
        "# Uç nokta listesi",
        "",
        f"Kütüphanedeki {total} uç nokta, {len(resources)} kaynak altında. Bu dosya",
        "`scripts/generate.py` tarafından üretilir; elle düzenlemeyin.",
        "",
        "Akış sütunu: **CC** = client credentials (token otomatik alınır), ",
        "**AC** = authorization code (müşteri girişi gerekir).",
        "",
        "| Kaynak | Açıklama | Uç nokta |",
        "| - | - | - |",
    ]
    for name in sorted(resources):
        title = RESOURCE_TITLES.get(name, name)
        lines.append(
            f"| [`kt.{name}`](#kt{name.replace('_', '')}) | {title} | {len(resources[name])} |"
        )
    for name in sorted(resources):
        lines += ["", f"## kt.{name}", "", RESOURCE_TITLES.get(name, name), ""]
        lines += ["| Metot | İstek | Kapsam | Akış |", "| - | - | - | - |"]
        for endpoint in resources[name]:
            flow = "AC" if endpoint["flow"] == "authorization_code" else "CC"
            lines.append(
                f"| [`{endpoint['name']}`]({endpoint['doc_url']}) | "
                f"`{endpoint['method']} {endpoint['path']}` | {endpoint['scope'] or '-'} | {flow} |"
            )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="yazma; yalnızca güncelliği denetle")
    args = parser.parse_args()

    endpoints = json.loads(SPEC.read_text(encoding="utf-8"))
    resources: dict[str, list[dict[str, Any]]] = {}
    for endpoint in endpoints:
        resources.setdefault(endpoint["resource"], []).append(endpoint)

    files = {OUT / f"{name}.py": render_module(name, items) for name, items in resources.items()}
    files[OUT / "__init__.py"] = render_init(resources)
    files[ENDPOINTS_MD] = render_endpoints_md(resources)
    stale = [p for p in OUT.glob("*.py") if p.name not in KEEP and p not in files]

    if args.check:
        outdated = [
            p for p, text in files.items() if not p.exists() or p.read_text("utf-8") != text
        ]
        for path in [*outdated, *stale]:
            print(f"güncel değil: {path.relative_to(ROOT)}", file=sys.stderr)
        return 1 if outdated or stale else 0

    for path in stale:
        path.unlink()
    for path, text in files.items():
        path.write_text(text, encoding="utf-8")
    print(f"{len(endpoints)} uç nokta, {len(resources)} kaynak modülü üretildi.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
