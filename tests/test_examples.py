"""examples/ altındaki örnek uygulamalar, dokümandaki örnek yanıtlara karşı çalıştırılır."""

from __future__ import annotations

import datetime as dt
import importlib
import json
import sys
from pathlib import Path
from typing import Any

import httpx
import pytest

from conftest import Recorder, envelope
from conftest import token_response as conftest_token
from kuveytturk_api import FileTokenStore, KuveytTurk, Token

EXAMPLES = Path(__file__).resolve().parent.parent / "examples"

# Sandbox'ın 2026-10-02'de döndürdüğü gerçek yanıt biçimleri (değerler uydurma).
TODAY = dt.date.today()


def days_ago(days: int, clock: str = "10:00:00") -> str:
    return f"{TODAY - dt.timedelta(days=days)}T{clock}"


ACCOUNTS_V3 = {
    "accountList": [
        {
            "name": "",
            "suffix": 1,
            "balance": 9955.0,
            "availableBalance": 9900.1,
            "fxId": 0,
            "iban": "TR12",
            "productType": "Cari Hesap",
        },
        {
            "name": "Altın",
            "suffix": 101,
            "balance": 5.0,
            "availableBalance": 5.0,
            "fxId": 24,
            "iban": "TR34",
            "productType": "Kıymetli Maden",
        },
        {
            "name": "Dolar",
            "suffix": 2,
            "balance": 10.0,
            "availableBalance": 10.0,
            "fxId": 1,
            "iban": "TR35",
            "productType": "Döviz Hesabı",
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
            "type": "Current Account",
        }
    ]
}
ACTIVITIES = {
    "accountActivities": [
        {
            "suffix": 1,
            "date": days_ago(1, "23:17:05.327"),
            "description": "Para Transferi",
            "amount": -22.54,
            "fxCode": "TL",
            "transactionReference": "ref-1",
        },
        {
            "suffix": 1,
            "date": days_ago(3, "01:32:29.64"),
            "description": "Nakit Yatırma",
            "amount": 10.0,
            "balance": 77.46,
            "fxCode": "TL",
            "transactionReference": "ref-2",
        },
        {
            "suffix": 1,
            "date": days_ago(400),
            "description": "Aralık dışı eski kayıt",
            "amount": 99.0,
            "fxCode": "TL",
            "transactionReference": "ref-eski",
        },
    ]
}
RECEIPT = {
    "title": "Nakit Yatan",
    "description": "Açıklama",
    "slipList": [{"key": "Hesap No", "value": "TR12"}],
}
EMPTY_RECEIPT = {"executionReferenceId": "x", "title": "", "description": "", "amount": 0.0}
RATES = {
    "rateList": [
        {
            "fxName": "Amerikan Doları",
            "fxCode": "USD",
            "fxId": 1,
            "buyRate": 45.73486,
            "sellRate": 44.71732,
        },
        {"fxName": "Euro", "fxCode": "EUR", "fxId": 19, "buyRate": 51.5129, "sellRate": 50.36568},
    ]
}
METALS = {
    "rateList": [
        {
            "fxName": "Altın",
            "fxCode": "ALT (gr)",
            "fxId": 24,
            "buyRate": 6082.12347,
            "sellRate": 6067.5,
        }
    ]
}
IBAN_INFO = {
    "customerName": "Fu**** Gö****",
    "bankName": "Kuveyt Türk Katılım Bankası A.Ş.",
    "bankId": 205,
    "fec": 0,
}
VALID_IBAN = "TR330006100519786457841326"

ROUTES: dict[tuple[str, str], Any] = {
    ("GET", "/v3/accounts"): ACCOUNTS_V3,
    ("GET", "/v2/accounts"): ACCOUNTS_V2,
    ("GET", "/v3/accounts/1/transactions"): ACTIVITIES,
    ("GET", "/v2/accounts/1/transactions"): ACTIVITIES,
    ("POST", "/v3/accounts/transactions/receipts"): RECEIPT,
    ("POST", "/v2/accounts/transactions/receipts"): EMPTY_RECEIPT,
    ("GET", "/v2/fx/rates"): RATES,
    ("GET", "/v1/preciousmetal/rates"): METALS,
    ("GET", f"/v1/moneytransfer/{VALID_IBAN}/customeribaninfo"): IBAN_INFO,
    ("POST", "/v1/fx/buy"): {"ExecutionReferenceId": "fx-1", "FxRate": 45.73486},
    ("POST", "/v1/fx/sell"): {"ExecutionReferenceId": "fx-2", "FxRate": 44.71732},
    ("POST", "/v1/preciousmetal/buy"): {"ExecutionReferenceId": "pm-1"},
    ("POST", "/v1/preciousmetal/sell"): {"ExecutionReferenceId": "pm-2"},
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
    assert "Kıymetli Maden" in out and "9,900.10" in out and "TR34" in out
    assert out.splitlines()[0].split() == [
        "Ek", "No", "Hesap", "Adı", "Tür", "Döviz", "Bakiye", "Kullanılabilir", "IBAN",
    ]  # fmt: skip


def test_account_list_as_customer_uses_stored_login(example, recorder, capsys):
    example.store.set(
        "user:default", Token(access_token="musteri-tok", scope="accounts offline_access")
    )
    example("account_list").main(["--customer", "--suffix", "2"])
    out = capsys.readouterr().out
    assert recorder.last.url.raw_path == b"/v2/accounts?suffix=2"
    assert recorder.last.headers["Authorization"] == "Bearer musteri-tok"
    assert "Müşteri Cari" in out and "7.50" in out and "Current Account" in out


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
    assert "2 hareket" in out and "Nakit Yatırma" in out and "-22.54" in out
    assert "Aralık dışı eski kayıt" not in out  # banka döndürse de aralık dışı gösterilmez
    assert "Dekont: Nakit Yatan" in out and "Hesap No" in out


def test_account_transactions_as_customer_with_empty_receipt(example, recorder, capsys):
    example.store.set("user:default", Token(access_token="musteri-tok", scope="accounts"))
    example("account_transactions").main(["--suffix", "1", "--customer", "--receipt"])
    assert [r.url.path for r in recorder.api_requests] == [
        "/v2/accounts/1/transactions",
        "/v2/accounts/transactions/receipts",
    ]
    out = capsys.readouterr().out
    assert "Para Transferi" in out and "dekont ayrıntısı dönmedi" in out


def test_exchange_rates_filter(example, capsys):
    example("exchange_rates").main(["--code", "usd", "--code", "ALT"])
    out = capsys.readouterr().out
    assert "Amerikan Doları" in out and "45.73486" in out
    assert "Altın" in out and "6,067.50" in out  # "ALT (gr)" kodu ALT ile eşleşir
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


def test_print_table_hides_empty_columns_and_formats_numbers(example, capsys):
    example.common.print_table(
        [{"a": 1.5, "b": "", "x": 45.73486}, {"a": 1234.0, "c": "son"}],
        [("a", "A"), ("b", "B"), ("c|x", "C")],
    )
    lines = capsys.readouterr().out.splitlines()
    assert lines[0].split() == ["A", "C"]  # B hiçbir satırda dolu değil
    assert lines[2].split() == ["1.50", "45.73486"]
    assert lines[3].split() == ["1,234.00", "son"]


SEND = [
    "send", "--from-suffix", "1", "--iban", VALID_IBAN, "--amount", "10.50",
    "--corporate-user", "kurumsal",
]  # fmt: skip


def transfer_requests(recorder: Recorder) -> list[httpx.Request]:
    return [r for r in recorder.api_requests if r.url.path.endswith("/outgoingmoneytransfer")]


def test_money_transfer_is_a_dry_run_by_default(example, recorder, capsys):
    example("money_transfer").main([*SEND, "--description", "Kira"])
    out = capsys.readouterr().out
    assert transfer_requests(recorder) == []
    assert "Deneme modu" in out and '"money_transfer_amount": "10.50"' in out
    assert "Fu**** Gö****" in out  # alıcı gönderilmeden önce sorgulandı


def test_money_transfer_execute_needs_typed_confirmation(example, recorder, monkeypatch, capsys):
    module = example("money_transfer")
    monkeypatch.setattr("builtins.input", lambda prompt: "evet")  # tam olarak EVET değil
    module.main([*SEND, "--execute"])
    assert transfer_requests(recorder) == []
    assert "Vazgeçildi" in capsys.readouterr().out

    monkeypatch.setattr("builtins.input", lambda prompt: "EVET")
    module.main([*SEND, "--execute", "--description", "Kira"])
    (request,) = transfer_requests(recorder)
    assert request.url.path == "/v1/moneytransfer/outgoingmoneytransfer"
    assert json.loads(request.content) == {
        "senderAccountSuffix": 1,
        "receiverIban": VALID_IBAN,
        "moneyTransferAmount": 10.5,
        "corporateWebUserName": "kurumsal",
        "moneyTransferDescription": "Kira",
    }
    out = capsys.readouterr().out
    assert "39284624" in out and "exec-1" in out


def test_money_transfer_validates_inputs_before_any_request(example, recorder, monkeypatch, capsys):
    module = example("money_transfer")
    monkeypatch.delenv("KUVEYTTURK_CORPORATE_USER", raising=False)
    bad_iban = [a if a != VALID_IBAN else "TR330006100519786457841327" for a in SEND]
    no_user = SEND[:-2]
    for arguments in (bad_iban, no_user):
        with pytest.raises(SystemExit) as info:
            module.main([*arguments, "--execute", "--yes"])
        assert info.value.code == 2
    assert recorder.api_requests == []
    capsys.readouterr()


def test_money_transfer_refuses_production_without_flag(example, recorder, monkeypatch, capsys):
    module = example("money_transfer")
    monkeypatch.setattr(
        module, "create_client", lambda: example.create_client(environment="production")
    )
    recorder.api = lambda r: route(r) if "gateway" in r.url.host else conftest_token()
    with pytest.raises(SystemExit) as info:
        module.main([*SEND, "--execute", "--yes"])
    assert info.value.code == 2
    assert transfer_requests(recorder) == []
    assert "--allow-production" in capsys.readouterr().err


def test_money_transfer_timeout_is_reported_not_retried(example, recorder, capsys):
    def flaky(request: httpx.Request) -> httpx.Response:
        if request.method == "POST":
            raise httpx.ReadTimeout("zaman aşımı")
        return route(request)

    recorder.api = flaky
    with pytest.raises(SystemExit) as info:
        example("money_transfer").main([*SEND, "--execute", "--yes"])
    assert info.value.code == 3
    assert len(transfer_requests(recorder)) == 1
    assert "Yeniden GÖNDERMEYİN" in capsys.readouterr().err


def test_money_transfer_continues_when_iban_lookup_fails(example, recorder, capsys):
    def lookup_forbidden(request: httpx.Request) -> httpx.Response:
        if "customeribaninfo" in request.url.path:
            return httpx.Response(403, json={"code": 403, "message": "Invalid Scope"})
        return route(request)

    recorder.api = lookup_forbidden
    example("money_transfer").main(SEND)
    out = capsys.readouterr().out
    assert "sorgulanamadı" in out and "Deneme modu" in out


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
    recorder.api = lambda r: httpx.Response(403, json={"code": 403, "message": "Invalid Scope"})
    module = example("account_list")
    with pytest.raises(SystemExit) as info:
        example.common.run(lambda: module.main([]))
    assert info.value.code == 1
    err = capsys.readouterr().err
    assert "HTTP 403" in err and "Invalid Scope" in err


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


# --------------------------------------------------------------------------- fx_trade.py

TRADE_PATHS = ("/v1/fx/buy", "/v1/fx/sell", "/v1/preciousmetal/buy", "/v1/preciousmetal/sell")


def trade_requests(recorder: Recorder) -> list[httpx.Request]:
    return [r for r in recorder.api_requests if r.url.path in TRADE_PATHS]


def test_fx_trade_is_a_dry_run_by_default(example, recorder, capsys):
    example("fx_trade").main(
        ["buy", "USD", "1", "--tl-suffix", "1", "--fx-suffix", "2", "--corporate-user", "k"]
    )
    out = capsys.readouterr().out
    assert trade_requests(recorder) == []
    assert "1 USD alış" in out and "45.73486" in out and "Deneme modu" in out


def test_fx_trade_buy_uses_the_bank_buy_rate_and_tl_as_source(
    example, recorder, monkeypatch, capsys
):
    monkeypatch.setattr("builtins.input", lambda prompt: "EVET")
    example("fx_trade").main(
        [
            "buy",
            "usd",
            "1.5",
            "--tl-suffix",
            "1",
            "--fx-suffix",
            "2",
            "--corporate-user",
            "k",
            "--execute",
        ]
    )
    (request,) = trade_requests(recorder)
    assert request.url.path == "/v1/fx/buy"
    assert json.loads(request.content) == {
        "AccountSuffixFrom": 1,
        "AccountSuffixTo": 2,
        "CorporateWebUserName": "k",
        "BuyRate": 45.73486,
        "ExchangeAmount": 1.5,
    }
    assert "fx-1" in capsys.readouterr().out


def test_fx_trade_sell_metal_uses_sell_rate_and_metal_account_as_source(example, recorder, capsys):
    example("fx_trade").main(
        [
            "sell",
            "ALT",
            "2",
            "--tl-suffix",
            "1",
            "--fx-suffix",
            "101",
            "--corporate-user",
            "k",
            "--execute",
            "--yes",
        ]
    )
    (request,) = trade_requests(recorder)
    assert request.url.path == "/v1/preciousmetal/sell"
    body = json.loads(request.content)
    assert (body["AccountSuffixFrom"], body["AccountSuffixTo"], body["SellRate"]) == (
        101,
        1,
        6067.5,
    )
    capsys.readouterr()


@pytest.mark.parametrize(
    "arguments",
    [
        [
            "buy",
            "EUR",
            "1",
            "--tl-suffix",
            "1",
            "--fx-suffix",
            "2",
            "--corporate-user",
            "k",
        ],  # 2 USD hesabı
        [
            "buy",
            "USD",
            "1",
            "--tl-suffix",
            "2",
            "--fx-suffix",
            "2",
            "--corporate-user",
            "k",
        ],  # 2 TL değil
        [
            "buy",
            "USD",
            "1",
            "--tl-suffix",
            "1",
            "--fx-suffix",
            "99",
            "--corporate-user",
            "k",
        ],  # hesap yok
        ["buy", "ALT", "1", "--tl-suffix", "1", "--fx-suffix", "101"],  # madende kullanıcı zorunlu
    ],
)
def test_fx_trade_refuses_mismatched_accounts_before_any_trade(
    example, recorder, monkeypatch, arguments, capsys
):
    monkeypatch.delenv("KUVEYTTURK_CORPORATE_USER", raising=False)
    with pytest.raises(SystemExit) as info:
        example("fx_trade").main([*arguments, "--execute", "--yes"])
    assert info.value.code == 2
    assert trade_requests(recorder) == []
    capsys.readouterr()


def test_fx_trade_needs_typed_confirmation_and_allow_production(
    example, recorder, monkeypatch, capsys
):
    module = example("fx_trade")
    monkeypatch.setattr("builtins.input", lambda prompt: "evet")
    module.main(
        [
            "buy",
            "USD",
            "1",
            "--tl-suffix",
            "1",
            "--fx-suffix",
            "2",
            "--corporate-user",
            "k",
            "--execute",
        ]
    )
    assert trade_requests(recorder) == [] and "Vazgeçildi" in capsys.readouterr().out

    monkeypatch.setattr(
        module, "create_client", lambda: example.create_client(environment="production")
    )
    recorder.api = lambda r: route(r) if "gateway" in r.url.host else conftest_token()
    with pytest.raises(SystemExit) as info:
        module.main(
            [
                "buy",
                "USD",
                "1",
                "--tl-suffix",
                "1",
                "--fx-suffix",
                "2",
                "--corporate-user",
                "k",
                "--execute",
                "--yes",
            ]
        )
    assert info.value.code == 2 and trade_requests(recorder) == []
    assert "--allow-production" in capsys.readouterr().err


def test_fx_trade_timeout_is_reported_not_retried(example, recorder, capsys):
    def flaky(request: httpx.Request) -> httpx.Response:
        if request.url.path in TRADE_PATHS:
            raise httpx.ReadTimeout("zaman aşımı")
        return route(request)

    recorder.api = flaky
    with pytest.raises(SystemExit) as info:
        example("fx_trade").main(
            [
                "sell",
                "USD",
                "1",
                "--tl-suffix",
                "1",
                "--fx-suffix",
                "2",
                "--corporate-user",
                "k",
                "--execute",
                "--yes",
            ]
        )
    assert info.value.code == 3 and len(trade_requests(recorder)) == 1
    assert "Yeniden GÖNDERMEYİN" in capsys.readouterr().err
