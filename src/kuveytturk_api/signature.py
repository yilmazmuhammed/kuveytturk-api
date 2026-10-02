"""İstek imzalama (``Signature`` başlığı) ve RSA anahtar çifti üretimi.

Kuveyt Türk API Gateway her istekte bir ``Signature`` başlığı bekler. İmza,
uygulamanın private key'i ile RSA-SHA256 (PKCS#1 v1.5) kullanılarak üretilir ve
Base64 olarak gönderilir. İmzalanan veri:

* ``POST`` (ve gövdeli diğer metotlar): ``{access_token}{request_body}``
* ``GET``: ``{access_token}{query_string}`` — sorgu varsa ``?`` dahil
  (ör. ``{access_token}?beginDate=2025-01-01&itemCount=10``), yoksa yalnızca token.
"""

from __future__ import annotations

import base64
import os
from pathlib import Path
from typing import Union

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

from .exceptions import SignatureError

__all__ = ["PrivateKeySource", "Signer", "generate_key_pair"]

#: Private key için kabul edilen girdiler: dosya yolu, PEM metni/baytları ya da hazır anahtar nesnesi.
PrivateKeySource = Union[str, bytes, "os.PathLike[str]", rsa.RSAPrivateKey]

_PEM_MARKER = b"-----BEGIN"


def _read_pem(source: str | bytes | os.PathLike[str]) -> bytes:
    if isinstance(source, bytes):
        data = source
    elif isinstance(source, str) and _PEM_MARKER.decode() in source:
        # .env dosyalarında satır sonları çoğu zaman "\n" olarak kaçışlanır.
        data = source.replace("\\n", "\n").encode()
    else:
        path = Path(os.fspath(source)).expanduser()
        try:
            data = path.read_bytes()
        except OSError as exc:
            raise SignatureError(f"Private key dosyası okunamadı: {path} ({exc})") from exc
    if _PEM_MARKER not in data:
        raise SignatureError("Private key PEM biçiminde değil ('-----BEGIN ...' satırı yok).")
    return data


class Signer:
    """Bir RSA private key ile ``Signature`` başlığı üretir.

    Args:
        private_key: PEM dosyasının yolu, PEM içeriği (``str``/``bytes``) ya da
            ``cryptography`` ``RSAPrivateKey`` nesnesi. PKCS#1 ve PKCS#8 desteklenir.
        password: Anahtar şifreliyse parolası.
    """

    def __init__(
        self, private_key: PrivateKeySource, *, password: str | bytes | None = None
    ) -> None:
        if isinstance(private_key, rsa.RSAPrivateKey):
            self._key = private_key
            return
        pem = _read_pem(private_key)
        pwd = password.encode() if isinstance(password, str) else password
        try:
            key = serialization.load_pem_private_key(pem, password=pwd)
        except (ValueError, TypeError) as exc:
            raise SignatureError(f"Private key yüklenemedi: {exc}") from exc
        if not isinstance(key, rsa.RSAPrivateKey):
            raise SignatureError("Private key RSA türünde olmalı.")
        self._key = key

    def sign(self, access_token: str, payload: str | bytes = b"") -> str:
        """``access_token + payload`` verisini imzalar ve Base64 imzayı döndürür.

        ``payload``; POST için gönderilen gövdenin birebir kendisi, GET için ``?`` ile
        başlayan sorgu dizgisi (sorgu yoksa boş) olmalıdır.
        """
        body = payload.encode("utf-8") if isinstance(payload, str) else payload
        signature = self._key.sign(
            access_token.encode("utf-8") + body, padding.PKCS1v15(), hashes.SHA256()
        )
        return base64.b64encode(signature).decode("ascii")

    def public_key_pem(self) -> str:
        """Private key'e karşılık gelen public key (geliştirici portalına girilen değer)."""
        return (
            self._key.public_key()
            .public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
            .decode("ascii")
        )

    def __repr__(self) -> str:
        return f"<Signer RSA-{self._key.key_size}>"


def generate_key_pair(
    private_key_path: str | os.PathLike[str] | None = None,
    public_key_path: str | os.PathLike[str] | None = None,
    *,
    key_size: int = 2048,
) -> tuple[str, str]:
    """Yeni bir RSA anahtar çifti üretir ve ``(private_pem, public_pem)`` döndürür.

    Public key'i geliştirici portalındaki uygulamanıza ekleyin; private key'i gizli
    tutun ve kaynak koduna/commit'e koymayın. Yol verilirse dosyalar da yazılır
    (private key ``0600`` izinleriyle; var olan dosyanın üzerine yazılmaz).
    """
    key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
    private_pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_pem = key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    if private_key_path is not None:
        path = Path(os.fspath(private_key_path)).expanduser()
        try:
            fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            raise SignatureError(
                f"{path} zaten var; mevcut private key'in üzerine yazılmaz."
            ) from None
        with os.fdopen(fd, "wb") as fh:
            fh.write(private_pem)
    if public_key_path is not None:
        Path(os.fspath(public_key_path)).expanduser().write_bytes(public_pem)
    return private_pem.decode("ascii"), public_pem.decode("ascii")
