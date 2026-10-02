"""scripts/generate.py: katalogdan üretilen kodun zor durumlardaki davranışı."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent


sys.path.insert(0, str(ROOT / "scripts"))


def _load(name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


generate = _load("generate")
build_spec = _load("build_spec")


def param(wire: str, type_: str = "str", required: bool = False) -> dict[str, Any]:
    return {"wire": wire, "type": type_, "required": required, "description": f"{wire} açıklaması"}


def endpoint(name: str, **fields: Any) -> dict[str, Any]:
    base: dict[str, Any] = {
        "id": name,
        "title": name.replace("_", " ").title() + ' "quoted" \\ title',
        "category": "Tricky",
        "doc_url": "https://example.com/doc",
        "status": "PASSIVE",
        "method": "GET",
        "path": "/v1/tricky",
        "version": "1.0",
        "scope": "public",
        "flow": "client_credentials",
        "description": 'Açıklama """üç tırnak""" ve \\ters eğik çizgi içerir.',
        "path_params": [],
        "query_params": [],
        "body_kind": "none",
        "body_wrap": [],
        "body_params": [],
        "response_fields": [f"field{i}" for i in range(40)],
        "resource": "tricky",
        "name": name,
    }
    base.update(fields)
    return base


class FakeClient:
    def __init__(self) -> None:
        self.calls: list[dict[str, Any]] = []

    def request(self, method: str, path: str, **kwargs: Any) -> str:
        self.calls.append({"method": method, "path": path, **kwargs})
        return "response"


def build(endpoints: list[dict[str, Any]]) -> Any:
    """Uç noktaları adlandırır, modülü üretir, çalıştırır ve senkron kaynak nesnesini döndürür."""
    build_spec.assign_names(
        endpoints, {e["id"]: {"resource": "tricky", "name": e["name"]} for e in endpoints}
    )
    source = generate.render_module("tricky", endpoints)
    compile(source, "tricky.py", "exec")
    path = ROOT / "src" / "kuveytturk_api" / "resources" / "_tricky_test_module.py"
    path.write_text(source, encoding="utf-8")
    try:
        spec = importlib.util.spec_from_file_location(
            "kuveytturk_api.resources._tricky_test_module", path
        )
        assert spec and spec.loader
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    finally:
        path.unlink()
    client = FakeClient()
    return module.Tricky(client), client, source


def test_parameters_named_like_locals_and_keywords_do_not_collide():
    resource, client, _ = build(
        [
            endpoint(
                "collide",
                method="POST",
                path="/v1/{path}/x",
                path_params=[param("path", required=True)],
                query_params=[param("query"), param("class"), param("body")],
                body_kind="object",
                body_wrap=["request"],
                body_params=[
                    param("query", "int"),
                    param("from", required=True),
                    param("extraBody"),
                ],
            )
        ]
    )
    result = resource.collide(
        path="p", from_="a", query="q1", class_="c", body_="b", query_=5, extra_body_="e"
    )
    assert result == "response"
    assert client.calls == [
        {
            "method": "POST",
            "path": "/v1/{path}/x",
            "scope": "public",
            "flow": "client_credentials",
            "path_params": {"path": "p"},
            "query": {"query": "q1", "class": "c", "body": "b"},
            "body": {"request": {"query": 5, "from": "a", "extraBody": "e"}},
            "options": None,
        }
    ]


def test_optional_path_segment_is_dropped_when_not_given():
    resource, client, _ = build(
        [
            endpoint(
                "optional_segment",
                path="/v2/{kind}/accounts/{suffix}",
                path_params=[param("kind", required=True), param("suffix", "int")],
            )
        ]
    )
    resource.optional_segment(kind="k")
    resource.optional_segment(kind="k", suffix=3)
    assert [(c["path"], c["path_params"]) for c in client.calls] == [
        ("/v2/{kind}/accounts", {"kind": "k"}),
        ("/v2/{kind}/accounts/{suffix}", {"kind": "k", "suffix": 3}),
    ]


def test_raw_and_empty_bodies():
    resource, client, _ = build(
        [
            endpoint("raw_body", method="POST", body_kind="raw"),
            endpoint("empty_body", method="POST", body_kind="empty"),
        ]
    )
    resource.raw_body(body=[{"a": 1}], request_options={"timeout": 5})
    resource.empty_body(extra_body={"x": 1})
    resource.empty_body()
    assert [c["body"] for c in client.calls] == [[{"a": 1}], {"x": 1}, {}]
    assert client.calls[0]["options"] == {"timeout": 5}


def test_docstring_escapes_and_metadata():
    resource, _, source = build(
        [endpoint("documented", query_params=[param("itemCount", "int", True)])]
    )
    doc = resource.documented.__doc__
    assert "``GET /v1/tricky``" in doc
    assert "Durum: PASSIVE" in doc
    assert "'''üç tırnak'''" in doc and "\\ters" in doc
    assert "item_count: (``itemCount``, sorgu, zorunlu) itemCount açıklaması" in doc
    assert "field29, ..." in doc and "field30" not in doc
    assert "class AsyncTricky(AsyncResource):" in source
    assert "return await self._client.request(" in source
