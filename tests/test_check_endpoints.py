"""scripts/check_endpoints.py: güvenlik listesi ve sonuç sınıflandırması."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

import httpx
import pytest

from conftest import Recorder, envelope, token_response
from kuveytturk_api import KuveytTurk

ROOT = Path(__file__).resolve().parent.parent
ENDPOINTS = json.loads((ROOT / "spec" / "endpoints.json").read_text(encoding="utf-8"))
BY_KEY = {f"{e['resource']}.{e['name']}": e for e in ENDPOINTS}

spec = importlib.util.spec_from_file_location(
    "check_endpoints", ROOT / "scripts" / "check_endpoints.py"
)
assert spec and spec.loader
checker = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = checker
spec.loader.exec_module(checker)

# İşlem yaptığını adından anladığımız uç noktalar asla otomatik çağrılmamalı. Ad, alt çizgiyle
# ayrılan sözcüklerine bölünüp bu sözcüklerle karşılaştırılır ("seller" "sell" sayılmaz).
WRITE_WORDS = frozenset(
    {
        "buy", "sell", "send", "create", "creation", "insert", "cancel", "cancellation", "refund",
        "reversal", "update", "reopen", "approval", "confirm", "confirmation", "initiation",
        "collect", "withdrawal", "token", "commission", "career", "consume", "lendings",
        "outgoing", "internal", "execute",
    }
)  # fmt: skip


def looks_like_transaction(name: str) -> bool:
    words = name.split("_")
    if WRITE_WORDS & set(words):
        return True
    # "...application" ve "..._payment" ile biten adlar başvuru/ödeme yapar; "..._list",
    # "..._status_query" gibi sorgular hariç.
    return words[-1] in ("application", "payment", "transaction") and "list" not in words


def test_read_only_list_only_names_catalog_endpoints():
    assert BY_KEY.keys() >= checker.READ_ONLY


@pytest.mark.parametrize("key", sorted(checker.READ_ONLY))
def test_read_only_list_contains_no_transaction_endpoint(key):
    assert not looks_like_transaction(key.split(".", 1)[1]), f"{key} işlem yapıyor gibi görünüyor"


def test_the_name_check_recognises_transaction_endpoints():
    for name in ("fx_currency_buy", "precious_metal_sell", "your_banking_account_application",
                 "pr_payment_transaction", "kt_incident_creation", "virtual_pos_non_three_d_payment"):  # fmt: skip
        assert looks_like_transaction(name), name
    for name in ("get_seller_order_details", "supplier_financing_buyer_order_listing",
                 "get_digital_channel_card_application_list_v2", "money_transfer_state"):  # fmt: skip
        assert not looks_like_transaction(name), name


def test_known_transaction_endpoints_are_never_called():
    for key in (
        "transfers.outgoing_money_transfer",
        "transfers.internal_money_transfer",
        "fx.fx_currency_buy",
        "treasury.precious_metal_sell",
        "vpos.non_3_d_payment",
        "sms_otp.pr_payment_transaction",
        "support.kt_incident_creation",
        "your_banking.your_banking_account_application",
        "fx.fx_transaction_history",  # dokümandaki gövde bir para transferi gövdesi
    ):
        assert key not in checker.READ_ONLY, key


def test_mask_hides_ibans_and_long_numbers():
    text = checker.mask("IBAN TR33 0006 1005 1978 6457 8413 26 hesap 40036812 için kayıt yok")
    assert "8413" not in text and "40036812" not in text
    assert checker.mask("x" * 500).endswith("…")


def run_check(
    handler: Any, key: str, private_pem: str, context: dict[str, Any] | None = None
) -> dict[str, Any]:
    recorder = Recorder(api=handler, token=lambda r: token_response())
    kt = KuveytTurk(
        "id", "secret", private_pem, max_retries=0,
        http_client=httpx.Client(transport=httpx.MockTransport(recorder)),
    )  # fmt: skip
    result = checker.check(kt, BY_KEY[key], context or {})
    result["_istekler"] = recorder.api_requests
    return result


@pytest.mark.parametrize(
    ("response", "durum", "sonuc"),
    [
        (envelope({"rateList": [{}, {}]}), "test edildi", "çalışıyor"),
        (httpx.Response(404, json={"code": 404, "message": "Path not found."}), "test edildi", "bu ortamda yok (404)"),
        (httpx.Response(400, json={"results": [{"errorMessage": "x zorunlu"}]}), "kısmen test edildi", "erişilebilir, parametre/iş kuralı hatası"),
        (envelope(None, success=False), "kısmen test edildi", "erişilebilir, parametre/iş kuralı hatası"),
        (httpx.Response(403, json={"code": 403, "message": "Invalid Scope"}), "test edilmedi", "uygulamanın kapsam yetkisi yok"),
        (httpx.Response(503, text="meşgul"), "test edildi", "sunucu hatası"),
    ],
)  # fmt: skip
def test_check_classifies_responses(private_pem, response, durum, sonuc):
    result = run_check(lambda r: response, "fx.fx_currency_rates", private_pem)
    assert (result["durum"], result["sonuc"]) == (durum, sonuc)


def test_check_reports_missing_scope_from_token_endpoint(private_pem):
    recorder = Recorder(token=lambda r: httpx.Response(400, json={"error": "invalid_scope"}))
    kt = KuveytTurk(
        "id",
        "secret",
        private_pem,
        http_client=httpx.Client(transport=httpx.MockTransport(recorder)),
    )
    result = checker.check(kt, BY_KEY["accounts.account_activity_list"], {})
    assert result["durum"] == "test edilmedi" and "kapsam" in result["sonuc"]


def test_unknown_required_values_are_left_out_of_the_request(private_pem):
    result = run_check(
        lambda r: httpx.Response(
            400,
            json={"results": [{"errorMessage": "Lütfen transactionReference alanını doldurun."}]},
        ),
        "accounts.receipt_v3",
        private_pem,
    )
    assert result["durum"] == "kısmen test edildi"
    assert json.loads(result["_istekler"][0].content) == {}


def test_known_values_fill_path_parameters_and_details_never_contain_them(private_pem):
    result = run_check(
        lambda r: envelope({"customerName": "SU***"}),
        "transfers.customer_iban_info_for_money_transfer",
        private_pem,
        context={"iban": "TR330006100519786457841326"},
    )
    assert result["_istekler"][0].url.path.endswith("/TR330006100519786457841326/customeribaninfo")
    assert result["durum"] == "test edildi"
    assert "TR33" not in result["ayrinti"] and "(iban)" in result["ayrinti"]


def test_missing_path_value_means_not_tested(private_pem):
    result = run_check(
        lambda r: envelope({}), "cards.credit_card_transactions_list_v3", private_pem
    )
    assert result["durum"] == "test edilmedi" and result["_istekler"] == []
