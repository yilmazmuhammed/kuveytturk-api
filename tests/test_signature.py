from __future__ import annotations

import os
import stat
from pathlib import Path

import pytest
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from kuveytturk_api import SignatureError, Signer, generate_key_pair


def test_sign_is_rsa_sha256_over_token_plus_payload(private_pem, verify):
    signer = Signer(private_pem)
    signature = signer.sign("TOKEN", '{"a":1}')
    verify(signature, b'TOKEN{"a":1}')
    with pytest.raises(InvalidSignature):
        verify(signature, b'TOKEN{"a":2}')


def test_sign_without_payload_signs_only_the_token(private_pem, verify):
    verify(Signer(private_pem).sign("TOKEN"), b"TOKEN")


def test_sign_handles_non_ascii_payload(private_pem, verify):
    signature = Signer(private_pem).sign("TOKEN", '{"açıklama":"Şişli"}')
    verify(signature, 'TOKEN{"açıklama":"Şişli"}'.encode())


def test_key_can_be_loaded_from_path_bytes_object_and_escaped_env_value(
    private_pem, private_key, tmp_path: Path, verify
):
    path = tmp_path / "key.pem"
    path.write_text(private_pem)
    escaped = private_pem.replace("\n", "\\n")  # .env dosyalarındaki tek satırlık biçim
    for source in (path, str(path), private_pem.encode(), private_key, escaped):
        verify(Signer(source).sign("T", "x"), b"Tx")


def test_pkcs1_key_is_supported(private_key, verify):
    pkcs1 = private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.TraditionalOpenSSL,
        serialization.NoEncryption(),
    )
    verify(Signer(pkcs1).sign("T"), b"T")


def test_encrypted_key_needs_password(private_key, verify):
    encrypted = private_key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.BestAvailableEncryption(b"parola"),
    )
    verify(Signer(encrypted, password="parola").sign("T"), b"T")
    with pytest.raises(SignatureError):
        Signer(encrypted)


def test_bad_inputs_raise_signature_error(tmp_path: Path):
    with pytest.raises(SignatureError, match="okunamadı"):
        Signer(tmp_path / "yok.pem")
    not_pem = tmp_path / "not.pem"
    not_pem.write_text("merhaba")
    with pytest.raises(SignatureError, match="PEM"):
        Signer(not_pem)
    ec_key = ec.generate_private_key(ec.SECP256R1()).private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )
    with pytest.raises(SignatureError, match="RSA"):
        Signer(ec_key)


def test_public_key_pem_matches_private_key(private_pem, private_key):
    expected = private_key.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
    )
    assert Signer(private_pem).public_key_pem().encode() == expected


def test_generate_key_pair_writes_files_and_never_overwrites(tmp_path: Path):
    private_path, public_path = tmp_path / "private.pem", tmp_path / "public.pem"
    private_pem, public_pem = generate_key_pair(private_path, public_path)

    assert private_path.read_text() == private_pem
    assert public_path.read_text() == public_pem
    assert Signer(private_path).public_key_pem() == public_pem
    if os.name == "posix":
        assert stat.S_IMODE(private_path.stat().st_mode) == 0o600

    with pytest.raises(SignatureError, match="zaten var"):
        generate_key_pair(private_path)
    assert private_path.read_text() == private_pem
