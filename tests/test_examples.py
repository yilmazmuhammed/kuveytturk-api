"""examples/ altındaki örnek uygulamalar, dokümandaki örnek yanıtlara karşı çalıştırılır."""

from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path
from typing import Any

import httpx
import pytest

from conftest import Recorder, envelope
from kuveytturk_api import FileTokenStore, KuveytTurk, Token

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"

ACCOUNTS_V3 = {
    "accountList": [
        {
            "name": "Cari",
            "suffix": 1,
            "balance": 9955.0,
            "avaibleBalance": 9900.1,
            "iban": "TR12",
            "type": "Cari Hesap",
        },
        {
            "name": "Altın",
            "suffix": 101,
            "balance": 5.0,
            "avaibleBalance": 5.0,
            "iban": "TR34",
            "type": "Altın",
        },
    ]
}
ACCOUNTS_V2 = {
    "accountList": [
        {
            "accountNumber": 123456,
            "name": "Müşteri Cari",
            "suffix": 2,
            "balance": 10.0,
            "availableBalance": 7.5,
            "fxCode": "TL",
            "iban": "TR56",
        }
    ]
}
ACTIVITIES = {
    "accountActivities": [
        {
            "suffix": 1,
            "date": "2020-03-19T00:00:00",
            "description": "Para Transferi",
            "amount": 22.54,
            "balance": 100,
            "transactionReference": "ref-1",
            "fxCode": "TL",
        },
        {
            "suffix": 1,
            "date": "2020-03-17T00:00:00",
            "description": "Nakit Yatırma",
            "amount": 10,
            "balance": 77.46,
            "transactionReference": "ref-2",
            "fxCode": "TL",
        },
    ]
}
RECEIPT = {
    "title": "Nakit Yatan",
    "description": "Açıklama",
    "slipList": [{"key": "Hesap No", "value": "TR12"}],
}
RATES = [
    {"name": "Amerikan Doları", "fxCode": "USD", "buyRate": 3.52537, "sellRate": 3.51042},
    {"name": "Euro", "fxCode": "EUR", "buyRate": 3.71738, "sellRate": 3.70032},
]
METALS = [{"name": "Altın", "fxCode": "ALT", "buyRate": 2571.43, "sellRate": 2377.05}]
IBAN_INFO = {
    "customerName": "Fu**** Gö****",
    "bankName": "Kuveyt Türk Katılım Bankası A.Ş.",
    "bankId": 205,
    "fec": 1,
}
VALID_IBAN = "TR330006100519786457841326"

ROUTES: dict[tuple[str, str], Any] = {
    ("GET", "/v3/accounts"): ACCOUNTS_V3,
    ("GET", "/v2/accounts"): ACCOUNTS_V2,
    ("GET", "/v3/accounts/1/transactions"): ACTIVITIES,
    ("GET", "/v2/accounts/1/transactions"): ACTIVITIES,
    ("POST", "/v3/accounts/transactions/receipts"): RECEIPT,
    ("POST", "/v2/accounts/transactions/receipts"): RECEIPT,
    ("GET", "/v2/fx/rates"): RATES,
    ("GET", "/v1/preciousmetal/rates"): METALS,
    ("GET", f"/v1/moneytransfer/{VALID_IBAN}/customeribaninfo"): IBAN_INFO,
    ("POST", "/v1/moneytransfer/outgoingmoneytransfer"): {
        "executionReferenceId": "exec-1",
        "moneyTransferTransactionId": 39284624,
    },
    ("GET", "/v1/moneytransfer-state"): {
        "transferType": "FAST",
        "state": "Completed",
        "stateDescription": "Tamamlandı",
    },
}


def route(request: httpx.Request) -> httpx.Response:
    return envelope(ROUTES[(request.method, request.url.path)])


@pytest.fixture
def recorder() -> Recorder:
    return Recorder(api=route)


@pytest.fixture
def example(
    recorder: Recorder, private_pem: str, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> Any:
    """Örnek modülünü yükleyen ve istemcisini sahte sunucuya bağlayan yükleyici."""
    monkeypatch.syspath_prepend(str(EXAMPLES))
    for name in [n for n in sys.modules if n == "_common" or (EXAMPLES / f"{n}.py").exists()]:
        monkeypatch.delitem(sys.modules, name)
    common = importlib.import_module("_common")
    store = FileTokenStore(tmp_path / "tokens.json")

    def create_client(**overrides: Any) -> KuveytTurk:
        overrides.setdefault("environment", "sandbox")
        return KuveytTurk(
            "client-id",
            "client-secret",
            private_pem,
            redirect_uri="http://localhost:8000/callback",
            token_store=store,
            http_client=httpx.Client(transport=httpx.MockTransport(recorder)),
            **overrides,
        )

    monkeypatch.setattr(common, "create_client", create_client)

    def load(name: str) -> Any:
        return importlib.import_module(name)

    load.store = store  # type: ignore[attr-defined]
    load.common = common  # type: ignore[attr-defined]
    load.create_client = create_client  # type: ignore[attr-defined]
    return load


def test_account_list(example, recorder, capsys):
    example("account_list").main(["--only-open"])
    out = capsys.readouterr().out
    assert recorder.last.url.raw_path == b"/v3/accounts?onlyOpen=true"
    assert "Cari Hesap" in out and "9,900.10" in out and "TR34" in out
    assert out.splitlines()[0].split() == [
        "Ek",
        "No",
        "Hesap",
        "Adı",
        "Tür",
        "Döviz",
        "Bakiye",
        "Kullanılabilir",
        "IBAN",
    ]


def test_account_list_as_customer_uses_stored_login(example, recorder, capsys):
    example.store.set(
        "user:default", Token(access_token="musteri-tok", scope="accounts offline_access")
    )
    example("account_list").main(["--customer", "--suffix", "2"])
    out = capsys.readouterr().out
    assert recorder.last.url.raw_path == b"/v2/accounts?suffix=2"
    assert recorder.last.headers["Authorization"] == "Bearer musteri-tok"
    assert "Müşteri Cari" in out and "7.50" in out


def test_customer_flag_triggers_login_when_no_token(example, monkeypatch, capsys):
    logins: list[list[str]] = []

    def fake_login(self: Any, scopes: Any, **kwargs: Any) -> Token:
        logins.append(list(scopes))
        token = Token(access_token="yeni-tok", scope="accounts offline_access")
        self.set_user_token(token)
        return token

    monkeypatch.setattr("kuveytturk_api.client.Auth.login", fake_login)
    example("account_list").main(["--customer"])
    assert logins == [["accounts", "offline_access"]]
    assert "tarayıcı açılıyor" in capsys.readouterr().out


def test_account_transactions_with_receipt(example, recorder, capsys):
    example("account_transactions").main(
        ["--suffix", "1", "--days", "7", "--count", "20", "--receipt"]
    )
    out = capsys.readouterr().out
    listing, receipt = recorder.api_requests
    assert listing.url.path == "/v3/accounts/1/transactions"
    assert listing.url.params["itemCount"] == "20"
    assert {"beginDate", "endDate", "itemCount"} == set(listing.url.params.keys())
    assert json.loads(receipt.content) == {"transactionReference": "ref-1"}
    assert "2 hareket" in out and "Nakit Yatırma" in out and "22.54" in out
    assert "Dekont: Nakit Yatan" in out and "Hesap No" in out


def test_account_transactions_as_customer(example, recorder, capsys):
    example.store.set("user:default", Token(access_token="musteri-tok", scope="accounts"))
    example("account_transactions").main(["--suffix", "1", "--customer", "--receipt"])
    assert [r.url.path for r in recorder.api_requests] == [
        "/v2/accounts/1/transactions",
        "/v2/accounts/transactions/receipts",
    ]
    assert "Para Transferi" in capsys.readouterr().out


def test_exchange_rates_filter(example, capsys):
    example("exchange_rates").main(["--code", "usd", "--code", "ALT"])
    out = capsys.readouterr().out
    assert "Amerikan Doları" in out and "Altın" in out
    assert "Euro" not in out


def test_iban_lookup(example, recorder, capsys):
    module = example("iban_lookup")
    module.main(["tr33 0006 1005 1978 6457 8413 26"])
    assert recorder.last.url.path == f"/v1/moneytransfer/{VALID_IBAN}/customeribaninfo"
    assert "Fu**** Gö****" in capsys.readouterr().out

    with pytest.raises(SystemExit) as info:
        module.main(["TR330006100519786457841327"])  # kontrol basamağı hatalı
    assert info.value.code == 2
    assert len(recorder.api_requests) == 1  # geçersiz IBAN için istek atılmadı


def test_is_valid_iban(example):
    is_valid_iban = example.common.is_valid_iban
    assert is_valid_iban(VALID_IBAN)
    assert is_valid_iban("GB82 WEST 1234 5698 7654 32")
    assert not is_valid_iban("TR33000610051978645784132")  # eksik hane
    assert not is_valid_iban("TR33-0006")
    assert not is_valid_iban("")


SEND = [
    "send",
    "--from-suffix",
    "1",
    "--to-account",
    "123456",
    "--to-suffix",
    "2",
    "--amount",
    "10.50",
    "--transfer-type",
    "2",
]


def test_money_transfer_is_a_dry_run_by_default(example, recorder, capsys):
    example("money_transfer").main([*SEND, "--description", "Kira"])
    out = capsys.readouterr().out
    assert recorder.api_requests == [] and recorder.token_requests == []
    assert "Deneme modu" in out and '"money_transfer_amount": "10.50"' in out


def test_money_transfer_execute_needs_typed_confirmation(example, recorder, monkeypatch, capsys):
    module = example("money_transfer")
    monkeypatch.setattr("builtins.input", lambda prompt: "evet")  # tam olarak EVET değil
    module.main([*SEND, "--execute"])
    assert recorder.api_requests == []
    assert "Vazgeçildi" in capsys.readouterr().out

    monkeypatch.setattr("builtins.input", lambda prompt: "EVET")
    module.main([*SEND, "--execute", "--description", "Kira"])
    assert json.loads(recorder.last.content) == {
        "senderAccountSuffix": 1,
        "receiverAccountNumber": 123456,
        "receiverAccountSuffix": 2,
        "moneyTransferDescription": "Kira",
        "moneyTransferAmount": 10.5,
        "transferType": 2,
    }
    out = capsys.readouterr().out
    assert "39284624" in out and "exec-1" in out
    assert len(recorder.api_requests) == 1


def test_money_transfer_refuses_production_without_flag(example, recorder, monkeypatch, capsys):
    module = example("money_transfer")
    monkeypatch.setattr(
        module, "create_client", lambda: example.create_client(environment="production")
    )
    with pytest.raises(SystemExit) as info:
        module.main([*SEND, "--execute", "--yes"])
    assert info.value.code == 2
    assert recorder.api_requests == []
    assert "--allow-production" in capsys.readouterr().err


def test_money_transfer_timeout_is_reported_not_retried(example, recorder, capsys):
    def timeout(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("zaman aşımı")

    recorder.api = timeout
    with pytest.raises(SystemExit) as info:
        example("money_transfer").main([*SEND, "--execute", "--yes"])
    assert info.value.code == 3
    assert len(recorder.api_requests) == 1
    assert "Yeniden GÖNDERMEYİN" in capsys.readouterr().err


@pytest.mark.parametrize("amount", ["0", "-5", "1.005", "abc"])
def test_money_transfer_rejects_bad_amounts(example, amount, capsys):
    arguments = [a if a != "10.50" else amount for a in SEND]
    with pytest.raises(SystemExit):
        example("money_transfer").main(arguments)
    capsys.readouterr()


def test_money_transfer_state(example, recorder, capsys):
    example("money_transfer").main(["state", "--type", "FAST", "--out-going-id", "123456"])
    assert (
        recorder.last.url.raw_path == b"/v1/moneytransfer-state?outGoingId=123456&transferType=FAST"
    )
    assert "Completed - Tamamlandı" in capsys.readouterr().out


def test_run_reports_api_errors(example, recorder, capsys):
    recorder.api = lambda r: httpx.Response(
        403, json={"results": [{"errorCode": "Forbidden", "errorMessage": "Yetkiniz yok"}]}
    )
    module = example("account_list")
    with pytest.raises(SystemExit) as info:
        example.common.run(lambda: module.main([]))
    assert info.value.code == 1
    assert "HTTP 403" in capsys.readouterr().err


async def test_async_usage(private_pem, monkeypatch, capsys):
    monkeypatch.syspath_prepend(str(EXAMPLES))
    for name in ("_common", "async_usage"):
        monkeypatch.delitem(sys.modules, name, raising=False)
    module = importlib.import_module("async_usage")
    recorder = Recorder(api=route)

    class FakeAsyncKuveytTurk:
        @staticmethod
        def from_env(env_file: Any) -> Any:
            from kuveytturk_api import AsyncKuveytTurk

            return AsyncKuveytTurk(
                "id",
                "secret",
                private_pem,
                http_client=httpx.AsyncClient(transport=httpx.MockTransport(recorder)),
            )

    monkeypatch.setattr(module, "AsyncKuveytTurk", FakeAsyncKuveytTurk)
    await module.main()
    out = capsys.readouterr().out
    assert "USD" in out and "ALT" in out
    assert len(recorder.token_requests) == 1


def test_every_example_compiles():
    for path in EXAMPLES.glob("*.py"):
        compile(path.read_text(encoding="utf-8"), str(path), "exec")
