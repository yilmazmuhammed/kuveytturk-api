"""İndirilen API Market dokümanlarının repodaki deposu (``apidocs/``).

Düzen::

    apidocs/menu.json                                  menü (kategoriler ve sayfa listesi)
    apidocs/<dil>/<kategori>/<başlık>-<id>.md          sayfa: küçük bir üst bilgi + Markdown gövde

Sayfalar okunabilir Markdown olarak saklanır; böylece GitHub'da gezilebilir, ``grep`` ile
aranabilir ve doküman değişiklikleri ``git diff`` ile izlenebilir. ``fetch_docs.py`` buraya
yazar, ``build_spec.py`` buradan okur.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "apidocs"
MENU = DOCS / "menu.json"

_FOLD = str.maketrans("ığüşöçİĞÜŞÖÇ", "igusocIGUSOC")
_HEADER_KEYS = ("id", "title", "category", "language", "status")


def slugify(text: str) -> str:
    text = text.translate(_FOLD).lower()
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-") or "x"


def language_of(category: dict[str, Any]) -> str:
    """Kategorinin dili. Bazı İngilizce kategorilerin dil alanı boş gelir; onlar İngilizce sayılır."""
    return str(category.get("languageId") or "en")


def status_of(document: dict[str, Any]) -> str:
    """API yanıtındaki ``tags`` alanından sayfanın durumunu (ACTIVE, ...) çıkarır."""
    tags = document.get("tags")
    if isinstance(tags, str):
        try:
            tags = json.loads(tags)
        except json.JSONDecodeError:
            tags = None
    for tag in tags or []:
        if isinstance(tag, dict) and tag.get("group") == "Status":
            return str(tag.get("key") or "")
    return ""


# --------------------------------------------------------------------------- menü


def simplify_menu(payload: dict[str, Any]) -> list[dict[str, Any]]:
    """Menü yanıtından yalnızca gereken alanları alır (istek kimliği gibi değişken alanlar atılır)."""
    categories = []
    for category in payload.get("data") or []:
        categories.append(
            {
                "name": str(category.get("categoryName") or "").strip(),
                "language": language_of(category),
                "pages": [
                    {"id": str(sub["id"]), "title": str(sub.get("title") or "").strip()}
                    for sub in category.get("subMenus") or []
                ],
            }
        )
    return categories


def save_menu(categories: list[dict[str, Any]]) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    MENU.write_text(json.dumps(categories, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def load_menu() -> list[dict[str, Any]]:
    menu: list[dict[str, Any]] = json.loads(MENU.read_text(encoding="utf-8"))
    return menu


# --------------------------------------------------------------------------- sayfalar


def index() -> dict[str, Path]:
    """Depodaki sayfalar: ``{doküman id: dosya yolu}``."""
    pages: dict[str, Path] = {}
    for path in DOCS.glob("*/*/*.md"):
        match = re.search(r"-(\d+)\.md$", path.name)
        if match:
            pages[match.group(1)] = path
    return pages


def page_path(doc_id: str, title: str, category: str, language: str) -> Path:
    return DOCS / language / slugify(category) / f"{slugify(title)[:80]}-{doc_id}.md"


def save_page(
    *, doc_id: str, title: str, category: str, language: str, status: str, body: str
) -> Path:
    """Sayfayı yazar; aynı id eski bir yolda duruyorsa (kategori/başlık değiştiyse) onu siler."""
    path = page_path(doc_id, title, category, language)
    for stale in DOCS.glob(f"*/*/*-{doc_id}.md"):
        if stale != path:
            stale.unlink()
    path.parent.mkdir(parents=True, exist_ok=True)
    header = {
        "id": doc_id,
        "title": " ".join(title.split()),
        "category": category,
        "language": language,
        "status": status,
    }
    lines = ["---", *(f"{key}: {header[key]}" for key in _HEADER_KEYS), "---", ""]
    text = body.replace("\r\n", "\n").replace("\r", "\n").strip("\n")
    path.write_text("\n".join(lines) + text + "\n", encoding="utf-8")
    return path


def load_page(path: Path) -> dict[str, str]:
    """Sayfayı ``{id, title, category, language, status, body}`` sözlüğü olarak okur."""
    text = path.read_text(encoding="utf-8")
    page = dict.fromkeys(_HEADER_KEYS, "")
    if text.startswith("---\n"):
        head, _, body = text[4:].partition("\n---\n")
        for line in head.splitlines():
            key, _, value = line.partition(": ")
            if key in page:
                page[key] = value.strip()
    else:
        body = text
    page["body"] = body.lstrip("\n")
    return page
