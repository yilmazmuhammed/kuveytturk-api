"""Üretilen uç nokta metotlarının katalogla (spec/endpoints.json) tutarlılığı."""

from __future__ import annotations

import inspect
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from conftest import Recorder, body_json, envelope
from kuveytturk_api import AsyncKuveytTurk, KuveytTurk, Token

ROOT = Path(__file__).resolve().parent.parent
ENDPOINTS = json.loads((ROOT / "spec" / "endpoints.json").read_text(encoding="utf-8"))

SAMPLES: dict[str, Any] = {
    "str": "x y/ş",
    "int": 7,
    "number": 12.5,
    "bool": True,
    "datetime": "2025-01-02",
    "object": {"k": "v"},
    "array": [1, 2],
    "any": "any",
}


def endpoint_id(endpoint: dict[str, Any]) -> str:
    return f"{endpoint['resource']}.{endpoint['name']}"


def sample_kwargs(endpoint: dict[str, Any]) -> dict[str, Any]:
    """Tüm parametreler (isteğe bağlılar dahil) için türüne uygun örnek değerler."""
    kwargs = {}
    for group in ("path_params", "query_params", "body_params"):
        for param in endpoint[group]:
            kwargs[param["name"]] = SAMPLES[param["type"]]
    return kwargs


def test_generated_files_are_up_to_date():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate.py"), "--check"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_catalog_is_consistent():
    assert ENDPOINTS, "katalog boş"
    names = [endpoint_id(e) for e in ENDPOINTS]
    assert len(names) == len(set(names)), "aynı kaynakta yinelenen metot adı var"
    for endpoint in ENDPOINTS:
        assert endpoint["method"] in {"GET", "POST", "PUT", "PATCH", "DELETE"}
        assert endpoint["path"].startswith("/") and " " not in endpoint["path"]
        assert endpoint["flow"] in {"client_credentials", "authorization_code"}
        assert endpoint["name"].isidentifier() and endpoint["resource"].isidentifier()
        placeholders = {p["wire"] for p in endpoint["path_params"]}
        assert all("{" + name + "}" in endpoint["path"] for name in placeholders)
        python_names = [
            p["name"] for g in ("path_params", "query_params", "body_params") for p in endpoint[g]
        ]
        assert len(python_names) == len(set(python_names)), endpoint_id(endpoint)
        assert all(name.isidentifier() for name in python_names)
        if endpoint["method"] not in {"POST", "PUT", "PATCH"}:
            assert endpoint["body_kind"] == "none" and not endpoint["body_params"]


def test_sync_and_async_clients_expose_the_same_surface(private_pem):
    sync, asynchronous = KuveytTurk("i", "s", private_pem), AsyncKuveytTurk("i", "s", private_pem)
    for endpoint in ENDPOINTS:
        sync_method = getattr(getattr(sync, endpoint["resource"]), endpoint["name"])
        async_method = getattr(getattr(asynchronous, endpoint["resource"]), endpoint["name"])
        assert inspect.signature(sync_method) == inspect.signature(async_method)
        assert inspect.iscoroutinefunction(async_method)
        assert not inspect.iscoroutinefunction(sync_method)
        assert sync_method.__doc__ and endpoint["path"] in sync_method.__doc__
    sync.close()


def test_resources_are_cached_per_client_and_rebound_by_as_user(make_client):
    kt = make_client(Recorder())
    first = ENDPOINTS[0]["resource"]
    assert getattr(kt, first) is getattr(kt, first)
    ali = kt.as_user("ali")
    assert getattr(ali, first) is not getattr(kt, first)
    assert getattr(ali, first)._client is ali


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=endpoint_id)
def test_endpoint_method_builds_the_documented_request(endpoint, make_client, verify):
    recorder = Recorder(api=lambda r: envelope({"ok": True}))
    kt = make_client(recorder)
    kt.auth.set_user_token(Token(access_token="user-tok"))  # authorization_code uç noktaları için
    kwargs = sample_kwargs(endpoint)

    response = getattr(getattr(kt, endpoint["resource"]), endpoint["name"])(**kwargs)
    assert response.value == {"ok": True}

    request = recorder.last
    assert request.method == endpoint["method"]

    expected_path = endpoint["path"]
    for param in endpoint["path_params"]:
        expected_path = expected_path.replace(
            "{" + param["wire"] + "}", _escaped(kwargs[param["name"]])
        )
    raw_path, _, raw_query = request.url.raw_path.decode().partition("?")
    assert raw_path == expected_path
    assert set(request.url.params.keys()) == {p["wire"] for p in endpoint["query_params"]}

    expected_token = "user-tok" if endpoint["flow"] == "authorization_code" else "tok-1"
    assert request.headers["Authorization"] == f"Bearer {expected_token}"
    if endpoint["flow"] == "client_credentials":
        assert recorder.token_form()["scope"] == endpoint["scope"]

    if endpoint["body_kind"] == "none":
        assert request.content == b""
        signed = ("?" + raw_query if raw_query else "").encode()
    else:
        body = body_json(request)
        for key in endpoint["body_wrap"]:
            assert list(body) == [key]
            body = body[key]
        if endpoint["body_kind"] != "raw":
            assert body == {p["wire"]: kwargs[p["name"]] for p in endpoint["body_params"]}
        signed = request.content
    verify(request.headers["Signature"], expected_token.encode() + signed)


@pytest.mark.parametrize("endpoint", ENDPOINTS, ids=endpoint_id)
def test_optional_parameters_are_omitted_when_not_given(endpoint, make_client):
    recorder = Recorder()
    kt = make_client(recorder)
    kt.auth.set_user_token(Token(access_token="user-tok"))
    required = {
        p["name"]: SAMPLES[p["type"]]
        for group in ("path_params", "query_params", "body_params")
        for p in endpoint[group]
        if p["required"]
    }
    getattr(getattr(kt, endpoint["resource"]), endpoint["name"])(**required)

    request = recorder.last
    assert set(request.url.params.keys()) == {
        p["wire"] for p in endpoint["query_params"] if p["required"]
    }
    assert "{" not in request.url.path
    if endpoint["body_kind"] == "object":
        body = body_json(request)
        for key in endpoint["body_wrap"]:
            body = body[key]
        assert set(body) == {p["wire"] for p in endpoint["body_params"] if p["required"]}


def _escaped(value: Any) -> str:
    from urllib.parse import quote

    return quote(str(value), safe="")


def test_extra_query_and_extra_body_are_merged(make_client):
    recorder = Recorder()
    kt = make_client(recorder)
    with_body = next(e for e in ENDPOINTS if e["body_kind"] == "object" and not e["path_params"])
    required = {
        p["name"]: SAMPLES[p["type"]]
        for group in ("query_params", "body_params")
        for p in with_body[group]
        if p["required"]
    }
    getattr(getattr(kt, with_body["resource"]), with_body["name"])(
        **required,
        extra_query={"debug": 1},
        extra_body={"undocumentedField": "x"},
        request_options={"token": "explicit"},
    )
    request = recorder.last
    assert request.url.params["debug"] == "1"
    body = body_json(request)
    for key in with_body["body_wrap"]:
        body = body[key]
    assert body["undocumentedField"] == "x"
    assert request.headers["Authorization"] == "Bearer explicit"
