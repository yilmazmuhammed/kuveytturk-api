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
    """Sözlük listesini hizalı bir tablo olarak yazdırır.

    ``columns``: (anahtar, başlık) çiftleri. API sürümleri aynı bilgiyi farklı adlarla
    döndürebildiği için anahtar ``"productType|type"`` gibi seçenekli yazılabilir; ilk dolu
    olan kullanılır. Hiçbir satırda değeri olmayan sütunlar gösterilmez.
    """
    if not rows:
        print("(kayıt yok)")
        return
    table = [[format_cell(value_of(row, key)) for key, _ in columns] for row in rows]
    shown = [i for i in range(len(columns)) if any(line[i] for line in table)]
    titles = [columns[i][1] for i in shown]
    table = [[line[i] for i in shown] for line in table]
    widths = [max(len(title), *(len(line[i]) for line in table)) for i, title in enumerate(titles)]
    print("  ".join(title.ljust(width) for title, width in zip(titles, widths)))
    print("  ".join("-" * width for width in widths))
    for line in table:
        print("  ".join(cell.ljust(width) for cell, width in zip(line, widths)))


def value_of(row: Mapping[str, Any], key: str) -> Any:
    """``"a|b"`` biçimindeki anahtardaki seçeneklerden satırda dolu olan ilkinin değeri."""
    for option in key.split("|"):
        if row.get(option) not in (None, ""):
            return row[option]
    return None


def format_cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        # Tutarlar 2 basamakla, kurlar gerektiği kadar (en çok 5) basamakla gösterilir.
        whole, _, fraction = f"{value:,.5f}".partition(".")
        return f"{whole}.{fraction.rstrip('0').ljust(2, '0')}"
    return str(value)


def as_list(value: Any, key: str) -> list[Any]:
    """Yanıttaki listeyi döndürür: ``value[key]`` ya da ``value`` doğrudan liste ise kendisi."""
    if isinstance(value, Mapping):
        value = value.get(key)
    return list(value) if isinstance(value, list) else []


def within_dates(activities: Iterable[Mapping[str, Any]], begin: Any, end: Any) -> list[Any]:
    """Hareketleri tarihlerine göre [begin, end] aralığına süzer.

    Sandbox ``beginDate`` / ``endDate`` filtrelerini tutarlı uygulamıyor (aralık dışındaki
    kayıtlar da dönebiliyor); bu yüzden aralık istemci tarafında da uygulanır.
    """
    first, last = begin.isoformat(), end.isoformat()
    return [a for a in activities if first <= str(a.get("date") or "")[:10] <= last]


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
