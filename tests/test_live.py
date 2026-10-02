"""Kuveyt Türk sandbox'ına gerçek istek atan testler.

Varsayılan olarak atlanır. Çalıştırmak için proje kökünde dolu bir ``.env`` olmalı:

    KUVEYTTURK_LIVE=1 pytest -m live

Yalnızca okuma yapan uç noktalar çağrılır; para hareketi yapan hiçbir uç nokta buraya eklenmez.
Sandbox istekleri hız sınırına takıldığı için testler bilerek az sayıda istek atar.
"""

from __future__ import annotations

import os
from collections.abc import Iterator
from pathlib import Path

import pytest

from kuveytturk_api import APIError, KuveytTurk

ROOT = Path(__file__).resolve().parent.parent

pytestmark = [
    pytest.mark.live,
    pytest.mark.skipif(
        os.environ.get("KUVEYTTURK_LIVE") != "1", reason="canlı testler için KUVEYTTURK_LIVE=1"
    ),
]


@pytest.fixture(scope="module")
def kt() -> Iterator[KuveytTurk]:
    with KuveytTurk.from_env(ROOT / ".env", max_retries=1) as client:
        yield client


def test_client_credentials_token(kt: KuveytTurk):
    token = kt.auth.client_token("public")
    assert token.access_token
    assert not token.is_expired()
    assert kt.auth.client_token("public") is token  # ikinci çağrı saklı token'ı döndürür


def test_signed_get_without_query(kt: KuveytTurk):
    response = kt.fx.fx_currency_rates()
    assert response.status_code == 200
    assert response.success


def test_signed_get_with_query_string(kt: KuveytTurk):
    """Sorgu dizgisi imzaya dahil edilmezse gateway isteği 401 ile reddeder."""
    try:
        response = kt.accounts.account_list_v3(only_open=True)
    except APIError as exc:
        assert exc.status_code != 401, f"imza reddedildi: {exc}"
        pytest.skip(f"uygulamanın bu uç noktaya yetkisi yok: {exc}")
    assert response.status_code == 200
