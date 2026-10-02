"""Örnek uygulamaların ortak yardımcıları: istemci kurulumu, müşteri girişi, tablo çıktısı."""

from __future__ import annotations

import sys
from collections.abc import Iterable, Mapping, Sequence
from pathlib import Path
from typing import Any

from kuveytturk_api import (
    APIError,
    AuthorizationRequiredError,
    FileTokenStore,
    KuveytTurk,
    KuveytTurkError,
)

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
#: Müşteri token'ları burada saklanır; böylece her çalıştırmada yeniden giriş gerekmez.
TOKEN_FILE = ROOT / ".kuveytturk" / "tokens.json"


def create_client(**overrides: Any) -> KuveytTurk:
    """İstemciyi proje kökündeki ``.env`` dosyasından (ve ortam değişkenlerinden) kurar."""
    overrides.setdefault("token_store", FileTokenStore(TOKEN_FILE))
    return KuveytTurk.from_env(ENV_FILE, **overrides)


def ensure_login(kt: KuveytTurk, scopes: Iterable[str]) -> None:
    """Geçerli bir müşteri token'ı yoksa tarayıcıda giriş yaptırır.

    Sandbox'ta giriş için geliştirici portalındaki test müşterilerini kullanın.
    ``offline_access`` kapsamı refresh token verilmesini sağlar.
    """
    wanted = list(scopes)
    try:
        kt.auth.user_token(scope=" ".join(wanted))
    except AuthorizationRequiredError:
        print("Müşteri girişi gerekiyor; tarayıcı açılıyor...")
        kt.auth.login([*wanted, "offline_access"])


def print_table(rows: Sequence[Mapping[str, Any]], columns: Sequence[tuple[str, str]]) -> None:
    """Sözlük listesini hizalı bir tablo olarak yazdırır. ``columns``: (anahtar, başlık) çiftleri."""
    if not rows:
        print("(kayıt yok)")
        return
    cells = [[format_cell(row.get(key)) for key, _ in columns] for row in rows]
    widths = [
        max(len(title), *(len(line[index]) for line in cells))
        for index, (_, title) in enumerate(columns)
    ]
    print("  ".join(title.ljust(width) for (_, title), width in zip(columns, widths)))
    print("  ".join("-" * width for width in widths))
    for line in cells:
        print("  ".join(cell.ljust(width) for cell, width in zip(line, widths)))


def format_cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:,.2f}"
    return str(value)


def as_list(value: Any, key: str) -> list[Any]:
    """Yanıttaki listeyi döndürür: ``value[key]`` ya da ``value`` doğrudan liste ise kendisi."""
    if isinstance(value, Mapping):
        value = value.get(key)
    return list(value) if isinstance(value, list) else []


def is_valid_iban(iban: str) -> bool:
    """IBAN'ın biçimini ve kontrol basamaklarını (mod 97) doğrular; ağa çıkmaz."""
    compact = iban.replace(" ", "").upper()
    if not (15 <= len(compact) <= 34 and compact.isalnum() and compact[:2].isalpha()):
        return False
    if compact.startswith("TR") and len(compact) != 26:
        return False
    rearranged = compact[4:] + compact[:4]
    digits = "".join(str(int(char, 36)) for char in rearranged)
    return int(digits) % 97 == 1


def run(main: Any) -> None:
    """Örneği çalıştırır; kütüphane hatalarını okunur bir mesaja çevirip 1 ile çıkar."""
    try:
        main()
    except APIError as exc:
        print(f"API hatası (HTTP {exc.status_code}): {exc}", file=sys.stderr)
        for result in exc.results:
            print(f"  - {result}", file=sys.stderr)
        sys.exit(1)
    except KuveytTurkError as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        sys.exit(1)
