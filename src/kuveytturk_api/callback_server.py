"""Authorization code akışında yönlendirmeyi yakalayan tek kullanımlık yerel sunucu.

Yalnızca masaüstü betikleri ve geliştirme içindir (``kt.auth.login()``). Web
uygulamalarında callback'i kendi çatınızın (Django, FastAPI...) rotasında karşılayıp
``kt.auth.exchange_code()`` çağırın.
"""

from __future__ import annotations

import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any
from urllib.parse import urlsplit

from .exceptions import AuthenticationError, ConfigurationError

__all__ = ["wait_for_callback"]

_LOCAL_HOSTS = {"localhost", "127.0.0.1"}

_PAGE = (
    "<!doctype html><html lang='tr'><head><meta charset='utf-8'><title>Kuveyt Türk API</title>"
    "</head><body style='font-family:system-ui;margin:3rem'><h2>{title}</h2><p>{text}</p>"
    "</body></html>"
)


def wait_for_callback(redirect_uri: str, *, timeout: float = 300.0) -> str:
    """``redirect_uri`` adresini dinler ve gelen ilk callback'in tam URL'sini döndürür.

    ``redirect_uri`` bu makineyi göstermelidir (``http://localhost:PORT/yol``); sunucu
    yalnızca yerel arayüze bağlanır.

    Raises:
        ConfigurationError: ``redirect_uri`` yerel bir http adresi değilse.
        AuthenticationError: ``timeout`` saniye içinde callback gelmezse.
    """
    parts = urlsplit(redirect_uri)
    if parts.scheme != "http" or (parts.hostname or "") not in _LOCAL_HOSTS:
        raise ConfigurationError(
            "Yerel callback sunucusu için redirect_uri 'http://localhost:PORT/...' biçiminde "
            f"olmalı (verilen: {redirect_uri!r})."
        )
    expected_path = parts.path or "/"
    captured: dict[str, str] = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if urlsplit(self.path).path != expected_path:
                self.send_error(404)
                return
            captured["url"] = f"{parts.scheme}://{parts.netloc}{self.path}"
            ok = "code=" in self.path
            body = _PAGE.format(
                title="Giriş tamamlandı" if ok else "Yetkilendirme tamamlanamadı",
                text="Bu sekmeyi kapatıp uygulamaya dönebilirsiniz.",
            ).encode("utf-8")
            self.send_response(200 if ok else 400)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: Any) -> None:
            return

    try:
        server = HTTPServer(("127.0.0.1", parts.port or 80), Handler)
    except OSError as exc:
        raise ConfigurationError(
            f"Yerel callback sunucusu {parts.port or 80} portunda başlatılamadı: {exc}"
        ) from exc
    deadline = time.monotonic() + timeout
    try:
        while "url" not in captured:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise AuthenticationError(
                    f"{timeout:.0f} saniye içinde giriş tamamlanmadı.", error="login_timeout"
                )
            server.timeout = min(remaining, 1.0)
            server.handle_request()
    finally:
        server.server_close()
    return captured["url"]
