"""İsteklerin ve yanıtların loglanması.

Kütüphane standart ``logging`` modülüyle ``"kuveytturk_api"`` adlı logger'a yazar:

* ``INFO``  — her istek için tek satırlık özet: metot, yol, durum kodu, süre. Sorgu dizgisi ve
  gövde yazılmaz; canlı ortamda açık bırakılabilir.
* ``DEBUG`` — gönderilen isteğin tamamı (adres, başlıklar, gövde) ve dönen yanıtın gövdesi.
  Access token, imza, client secret, authorization code ve refresh token **maskelenir**; ama
  gövdeler olduğu gibi yazılır ve müşteri verisi (IBAN, bakiye, ad...) içerir. Yalnızca
  geliştirme sırasında açın.

Açmanın en kısa yolu :func:`enable_logging` ya da ``KUVEYTTURK_LOG=debug`` ortam değişkenidir.
"""

from __future__ import annotations

import json
import logging
import os
import sys
from collections.abc import Mapping
from typing import IO
from urllib.parse import urlsplit

__all__ = ["enable_logging", "logger"]

logger = logging.getLogger("kuveytturk_api")

#: DEBUG loglarında bir gövdenin en fazla bu kadar karakteri yazılır.
MAX_BODY_CHARS = 4000
_SECRET_HEADERS = frozenset({"authorization", "signature"})
_SECRET_FORM_FIELDS = frozenset({"code", "refresh_token", "client_secret", "password"})
_SECRET_TOKEN_FIELDS = frozenset({"access_token", "refresh_token", "id_token"})
_HANDLER_FLAG = "_kuveytturk_api_handler"
_LEVELS = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING}


def enable_logging(level: str | int = "debug", *, stream: IO[str] | None = None) -> None:
    """Kütüphanenin loglarını ekrana (varsayılan: stderr) yazdırır.

    Args:
        level: ``"info"`` (istek başına tek satır özet) ya da ``"debug"`` (istek ve yanıtın
            tamamı; token ve imza maskelenir, gövdeler müşteri verisi içerir).
        stream: Logların yazılacağı akış.

    Kendi ``logging`` yapılandırmanız varsa bunu çağırmanız gerekmez;
    ``logging.getLogger("kuveytturk_api").setLevel(logging.DEBUG)`` yeterlidir.
    Tekrar çağrılırsa yalnızca düzeyi (ve verilmişse akışı) günceller.
    """
    if isinstance(level, str):
        try:
            level = _LEVELS[level.strip().lower()]
        except KeyError:
            raise ValueError(
                f"Bilinmeyen log düzeyi: {level!r} (debug, info ya da warning)"
            ) from None
    for handler in list(logger.handlers):
        if getattr(handler, _HANDLER_FLAG, False):
            logger.removeHandler(handler)
    handler = logging.StreamHandler(stream if stream is not None else sys.stderr)
    handler.setFormatter(logging.Formatter("%(asctime)s kuveytturk_api %(levelname)s %(message)s"))
    setattr(handler, _HANDLER_FLAG, True)
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False  # kök logger da yapılandırılmışsa satırlar iki kez yazılmasın


def enable_from_environment() -> None:
    """``KUVEYTTURK_LOG`` ortam değişkeni ``debug`` / ``info`` ise loglamayı açar."""
    level = os.environ.get("KUVEYTTURK_LOG", "").strip().lower()
    if level in _LEVELS:
        enable_logging(level)


# --------------------------------------------------------------------------- yardımcılar


def _masked(value: str) -> str:
    scheme, _, rest = value.partition(" ")
    if rest and scheme.lower() in ("bearer", "basic"):
        return f"{scheme} <gizlendi, {len(rest)} karakter>"
    return f"<gizlendi, {len(value)} karakter>"


def _body_text(content: bytes | str | None) -> str:
    if not content:
        return "(boş)"
    text = content.decode("utf-8", errors="replace") if isinstance(content, bytes) else content
    if len(text) > MAX_BODY_CHARS:
        return f"{text[:MAX_BODY_CHARS]}… (+{len(text) - MAX_BODY_CHARS} karakter)"
    return text


def _attempt(attempt: int) -> str:
    return f" (deneme {attempt + 1})" if attempt else ""


# --------------------------------------------------------------------------- API istekleri


def log_request(
    method: str, url: str, headers: Mapping[str, str], content: bytes | None, attempt: int
) -> None:
    if not logger.isEnabledFor(logging.DEBUG):
        return
    lines = [f"→ {method} {url}{_attempt(attempt)}"]
    for name, value in headers.items():
        shown = _masked(value) if name.lower() in _SECRET_HEADERS else value
        lines.append(f"    {name}: {shown}")
    if content is not None:
        lines.append(f"    gövde: {_body_text(content)}")
    logger.debug("\n".join(lines))


def log_response(
    method: str, url: str, status_code: int, content: bytes, elapsed: float, attempt: int
) -> None:
    if not logger.isEnabledFor(logging.INFO):
        return
    summary = (
        f"{method} {urlsplit(url).path} -> {status_code} ({elapsed:.2f} sn){_attempt(attempt)}"
    )
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug("← %s\n    gövde: %s", summary, _body_text(content))
    else:
        logger.info(summary)


def log_failure(method: str, url: str, error: BaseException, elapsed: float, attempt: int) -> None:
    logger.warning(
        "%s %s -> ağ hatası (%.2f sn)%s: %s",
        method,
        urlsplit(url).path,
        elapsed,
        _attempt(attempt),
        error,
    )


# --------------------------------------------------------------------------- token istekleri


def log_token_request(url: str, form: Mapping[str, str]) -> None:
    if not logger.isEnabledFor(logging.DEBUG):
        return
    fields = ", ".join(
        f"{key}={_masked(value) if key in _SECRET_FORM_FIELDS else value}"
        for key, value in form.items()
    )
    logger.debug("→ POST %s\n    Authorization: Basic <gizlendi>\n    form: %s", url, fields)


def log_token_response(url: str, status_code: int, text: str, elapsed: float) -> None:
    if not logger.isEnabledFor(logging.INFO):
        return
    summary = f"POST {urlsplit(url).path} -> {status_code} ({elapsed:.2f} sn)"
    if not logger.isEnabledFor(logging.DEBUG):
        logger.info(summary)
        return
    try:
        payload = json.loads(text)
    except ValueError:
        payload = None
    if isinstance(payload, dict):
        shown = ", ".join(
            f"{key}={_masked(str(value)) if key in _SECRET_TOKEN_FIELDS else value}"
            for key, value in payload.items()
        )
    else:
        shown = _body_text(text)
    logger.debug("← %s\n    yanıt: %s", summary, shown)
