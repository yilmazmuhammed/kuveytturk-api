"""scripts/build_spec.py: doküman Markdown'unun uç nokta kataloğuna çevrilmesi."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parent.parent


def _load(name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


build_spec = _load("build_spec")

HEADER = """| URL | {url} |
| - | - |
| Method | {method} |
| Version | 1.0 |
| Scope | {scope} |
| Authorization Flow | {flow} |
## Description
Does **something** useful. See [guide](https://example.com).
"""


def parse(markdown: str, **header: str) -> tuple[dict[str, Any], list[str]]:
    values = {"url": "/v1/things", "method": "GET", "scope": "public", "flow": "client credentials"}
    values.update(header)
    doc = {
        "id": "1",
        "title": "Thing List (Beta)",
        "documentData": HEADER.format(**values) + markdown,
    }
    endpoint, warnings = build_spec.parse_endpoint(doc, "Some Category")
    assert endpoint is not None
    build_spec.assign_names([endpoint], {})
    return endpoint, warnings


def names(params: list[dict[str, Any]]) -> list[str]:
    return [p["wire"] + ("*" if p["required"] else "") for p in params]


def test_header_and_naming():
    endpoint, warnings = parse("", scope="Loans", flow="Client Credential")
    assert warnings == []
    assert (endpoint["method"], endpoint["path"]) == ("GET", "/v1/things")
    assert endpoint["scope"] == "loans"
    assert endpoint["flow"] == "client_credentials"
    assert endpoint["description"] == "Does something useful. See guide."
    assert endpoint["name"] == "thing_list"
    assert endpoint["resource"] == "some_category"
    assert endpoint["doc_url"].endswith("/documentation/some-category/thing-list-beta")


def test_flow_detection_and_url_normalisation():
    endpoint, _ = parse("", flow="authorization code", url="v2/accounts/{suffix?}")
    assert endpoint["flow"] == "authorization_code"
    assert endpoint["path"] == "/v2/accounts/{suffix}"
    assert names(endpoint["path_params"]) == ["suffix"]  # "?" -> isteğe bağlı yol parçası

    _, warnings = parse("", flow="???")
    assert any("akış" in w for w in warnings)


def test_pages_without_endpoint_header_are_skipped():
    doc = {"id": "1", "title": "Guide", "documentData": "## Introduction\nJust prose."}
    assert build_spec.parse_endpoint(doc, "Introduction") == (None, [])


def test_query_table_with_route_parameter_and_placeholder_row():
    markdown = """## Query Parameters
| Name | Type | Description | Required/Optional |
| - | - | - | - |
| cardNumber | string | Sent as a route parameter. | Required |
| beginDate | datetime | Lower bound. | Optional |
| itemCount | int | Max items. | Required |
| - | - | This endpoint does not require any other parameters. | - |
## Sample Query
```json
GET /v3/creditcard/123/transactions?beginDate=2020-01-01&extra=1
```
"""
    endpoint, warnings = parse(markdown, url="/v3/creditcard/{cardnumber}/transactions")
    assert names(endpoint["path_params"]) == ["cardnumber*"]
    assert endpoint["path_params"][0]["description"] == "Sent as a route parameter."
    assert names(endpoint["query_params"]) == ["beginDate", "itemCount*", "extra"]
    assert [p["type"] for p in endpoint["query_params"]] == ["datetime", "int", "str"]
    assert [p["name"] for p in endpoint["query_params"]] == ["begin_date", "item_count", "extra"]
    assert any("extra" in w for w in warnings)


def test_flat_body_uses_sample_casing_and_table_metadata():
    markdown = """## Request Parameters
| Name | Type | Description | Required/Optional |
| - | - | - | - |
| AccountSuffixFrom | short | Source. | Required |
| TLAmount | decimal | Amount. | Optional |
| notInSample | bool | Extra flag. | Optional |
## Sample Request
```json
{
  "AccountSuffixFrom": 1,
  "TLAmount": 650.0,
  "undocumented": "x",
}
```
"""
    endpoint, _ = parse(markdown, method="POST")
    assert endpoint["body_kind"] == "object" and endpoint["body_wrap"] == []
    assert names(endpoint["body_params"]) == [
        "AccountSuffixFrom*",
        "TLAmount",
        "undocumented",
        "notInSample",
    ]
    assert [p["type"] for p in endpoint["body_params"]] == ["int", "number", "str", "bool"]
    assert [p["name"] for p in endpoint["body_params"]] == [
        "account_suffix_from",
        "tl_amount",
        "undocumented",
        "not_in_sample",
    ]
    assert endpoint["query_params"] == []


def test_wrapped_body_is_flattened_and_nested_fields_are_not_parameters():
    markdown = """## Body Arguments
| Name | Type | Description | Required/Optional |
| - | - | - | - |
| request | object | Wrapper. | Required |
| contract | object | Contract. | Required |
| amount | decimal | Amount. | Required |
| items | list | Lines. | Optional |
| sku | string | Nested line field. | Required |
## Sample Body
```json
{"request": {"contract": {"amount": 10.5, "items": [{"sku": "a"}]}}}
```
"""
    endpoint, _ = parse(markdown, method="POST")
    assert endpoint["body_wrap"] == ["request", "contract"]
    assert names(endpoint["body_params"]) == ["amount*", "items"]
    assert [p["type"] for p in endpoint["body_params"]] == ["number", "array"]


def test_body_without_sample_or_with_array_sample():
    table = """## Request Parameters
| Name | Type | Description | Required/Optional |
| - | - | - | - |
| a | string | A. | Required |
"""
    endpoint, warnings = parse(table, method="POST")
    assert names(endpoint["body_params"]) == ["a*"]
    assert any("örnek gövde" in w for w in warnings)

    endpoint, _ = parse(table + '## Sample Request\n```json\n[{"a": "x"}]\n```\n', method="POST")
    assert endpoint["body_kind"] == "raw" and endpoint["body_params"] == []

    endpoint, _ = parse("", method="POST")
    assert endpoint["body_kind"] == "empty"


def test_response_fields_skip_envelope_keys():
    markdown = """## Response Parameters
| Name | Type | Description |
| - | - | - |
| value | object | Main. |
| accountList | array | Accounts. |
| success | bool | Flag. |
| results | array | Messages. |
"""
    endpoint, _ = parse(markdown)
    assert endpoint["response_fields"] == ["accountList"]


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("senderAccountSuffix", "sender_account_suffix"),
        ("TLAmount", "tl_amount"),
        ("IBAN", "iban"),
        ("class", "class_"),
        ("from", "from_"),
        ("3dSecure", "_3d_secure"),
        ("Müşteri No", "musteri_no"),
        ("request_options", "request_options_"),
    ],
)
def test_snake_case_names(raw, expected):
    assert build_spec.snake(raw) == expected


def test_duplicate_method_names_are_disambiguated():
    def endpoint(doc_id: str, path: str) -> dict[str, Any]:
        return {
            "id": doc_id,
            "title": "Account List",
            "category": "Other",
            "path": path,
            "path_params": [],
            "query_params": [],
            "body_params": [],
        }

    endpoints = [
        endpoint("1", "/v1/accounts"),
        endpoint("2", "/v2/accounts"),
        endpoint("3", "/v2/accounts"),
    ]
    build_spec.assign_names(endpoints, {"3": {"resource": "accounts"}})
    assert [(e["resource"], e["name"]) for e in endpoints] == [
        ("other", "account_list_v1"),
        ("other", "account_list_v2"),
        ("accounts", "account_list"),
    ]
