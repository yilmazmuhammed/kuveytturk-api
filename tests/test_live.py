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
    """Sorgu dizgisi imzaya katılmazsa gateway "Client signature validation error" (400) döner."""
    try:
        response = kt.accounts.account_list_v3(only_open=True)
    except APIError as exc:
        assert "signature" not in str(exc).lower(), f"imza reddedildi: {exc}"
        pytest.skip(f"uygulamanın bu uç noktaya yetkisi yok: {exc}")
    assert response.status_code == 200
    assert isinstance(response["accountList"], list)


def test_gateway_rejects_a_wrong_signature(kt: KuveytTurk):
    """İmzanın gerçekten doğrulandığını gösterir: bozuk imza kabul edilmemeli."""
    from kuveytturk_api import _base

    config = kt._shared.config
    token = kt.auth.client_token("public").access_token
    # /v1 kullanılıyor: /v2/fx/rates bozuk imzada 400 yerine ilgisiz bir 404 dönüyor (gateway hatası).
    prepared = _base.prepare_request(config, "GET", "/v1/fx/rates", access_token=token)
    headers = dict(prepared.headers, Signature=config.signer.sign("baska-bir-veri"))
    response = kt._shared.http.get(prepared.url, headers=headers)
    assert response.status_code == 400
    assert "signature" in response.text.lower()


def test_read_only_endpoints_used_by_examples(kt: KuveytTurk):
    rates = kt.fx.fx_currency_rates()
    assert rates["rateList"] and {"fxCode", "buyRate", "sellRate"} <= set(rates["rateList"][0])
    metals = kt.treasury.precious_metal_rates()
    assert metals["rateList"]
