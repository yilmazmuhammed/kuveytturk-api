"""Senkron ve asenkron istemcilerin paylaştığı, ağ erişimi içermeyen mantık.

Burada yalnızca "istek nasıl kurulur" ve "yanıt nasıl yorumlanır" soruları yanıtlanır;
HTTP çağrısını yapan kod :mod:`kuveytturk_api.client` ve
:mod:`kuveytturk_api.async_client` içindedir. Böylece iki istemci aynı davranışı paylaşır.
"""

from __future__ import annotations

import base64
import datetime as _dt
import enum
import json
import os
import secrets
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path
from typing import Any, Literal, TypedDict
from urllib.parse import parse_qs, quote, urlencode, urlsplit

from ._version import __version__
from .environments import Environment, resolve_environment
from .exceptions import (
    APIError,
    AuthenticationError,
    BadRequestError,
    BusinessError,
    ConfigurationError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServerError,
    UnauthorizedError,
)
from .response import APIResponse, parse_results
from .signature import PrivateKeySource, Signer
from .tokens import Token, normalize_scopes

__all__ = ["DEFAULT_USER", "Flow", "RequestOptions"]

Flow = Literal["client_credentials", "authorization_code"]

#: ``user`` verilmediğinde müşteri token'ının saklandığı anahtar.
DEFAULT_USER = "default"
DEFAULT_TIMEOUT = 30.0
DEFAULT_MAX_RETRIES = 2
USER_AGENT = f"kuveytturk-api-python/{__version__}"

#: Yalnızca bu metotlar otomatik yeniden denenir; para hareketi yapan POST'lar asla.
IDEMPOTENT_METHODS = frozenset({"GET", "HEAD"})
RETRY_STATUS_CODES = frozenset({500, 502, 503, 504})
#: Gövdesi imzalanan metotlar. Diğerlerinde sorgu dizgisi imzalanır.
BODY_METHODS = frozenset({"POST", "PUT", "PATCH"})

ENV_PREFIX = "KUVEYTTURK_"


class RequestOptions(TypedDict, total=False):
    """Tek bir çağrıya özel ayarlar (her uç nokta metodunun ``request_options`` argümanı).

    Attributes:
        token: Hazır bir access token. Verilirse token yönetimi tamamen atlanır.
        user: Müşteri token'ı hangi kullanıcı anahtarından okunacak.
        flow: Uç noktanın dokümandaki yetkilendirme akışını ezer.
        scope: Uç noktanın dokümandaki kapsamını ezer.
        timeout: Saniye cinsinden zaman aşımı.
        headers: İsteğe eklenecek başlıklar.
        raise_on_failure: ``success: false`` yanıtında istisna fırlatılsın mı.
    """

    token: str | Token
    user: str
    flow: Flow
    scope: str
    timeout: float
    headers: Mapping[str, str]
    raise_on_failure: bool


@dataclass(frozen=True)
class ClientConfig:
    client_id: str
    client_secret: str
    signer: Signer
    environment: Environment
    redirect_uri: str | None
    language_id: int | None
    device_id: str | None
    timeout: float
    max_retries: int
    raise_on_failure: bool


@dataclass(frozen=True)
class PreparedRequest:
    """Gönderilmeye hazır, imzalanmış istek."""

    method: str
    url: str
    headers: dict[str, str]
    content: bytes | None


@dataclass(frozen=True)
class AuthPlan:
    """Bir çağrıda hangi token'ın kullanılacağı."""

    kind: Literal["explicit", "client", "user"]
    scope: str
    user: str
    token: str | None = None


# --------------------------------------------------------------------------- yapılandırma


def read_env_file(path: str | os.PathLike[str]) -> dict[str, str]:
    """Basit bir ``.env`` dosyasını (``ANAHTAR=değer`` satırları) okur. Dosya yoksa boş döner."""
    values: dict[str, str] = {}
    try:
        text = Path(os.fspath(path)).expanduser().read_text(encoding="utf-8")
    except FileNotFoundError:
        return values
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        if line.startswith("export "):
            line = line[len("export ") :]
        key, _, value = line.partition("=")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        values[key.strip()] = value
    return values


def settings_from_env(env_file: str | os.PathLike[str] | None) -> dict[str, Any]:
    """``KUVEYTTURK_*`` ortam değişkenlerinden istemci argümanlarını toplar.

    Gerçek ortam değişkenleri ``env_file`` içindekilerden önceliklidir.
    """
    from_file = read_env_file(env_file) if env_file is not None else {}
    from_environ = {k: v for k, v in os.environ.items() if k.startswith(ENV_PREFIX) and v}

    def pick(name: str) -> str | None:
        key = ENV_PREFIX + name
        return from_environ.get(key) or from_file.get(key) or None

    settings: dict[str, Any] = {}
    for name in ("CLIENT_ID", "CLIENT_SECRET", "REDIRECT_URI", "ENVIRONMENT", "DEVICE_ID"):
        value = pick(name)
        if value is not None:
            settings[name.lower()] = value
    private_key = pick("PRIVATE_KEY")
    if private_key is not None:
        key_from_file = ENV_PREFIX + "PRIVATE_KEY" not in from_environ
        if key_from_file and env_file is not None and "-----BEGIN" not in private_key:
            # .env içindeki göreli anahtar yolu, .env dosyasının bulunduğu klasöre göredir.
            candidate = Path(private_key).expanduser()
            if not candidate.is_absolute():
                base_dir = Path(os.fspath(env_file)).expanduser().resolve().parent
                private_key = str(base_dir / candidate)
        settings["private_key"] = private_key
    password = pick("PRIVATE_KEY_PASSWORD")
    if password is not None:
        settings["private_key_password"] = password
    language_id = pick("LANGUAGE_ID")
    if language_id is not None:
        settings["language_id"] = int(language_id)
    return settings


def build_config(
    *,
    client_id: str | None,
    client_secret: str | None,
    private_key: PrivateKeySource | None,
    private_key_password: str | bytes | None,
    environment: str | Environment,
    redirect_uri: str | None,
    language_id: int | None,
    device_id: str | None,
    timeout: float,
    max_retries: int,
    raise_on_failure: bool,
) -> ClientConfig:
    missing = [
        name
        for name, value in (
            ("client_id", client_id),
            ("client_secret", client_secret),
            ("private_key", private_key),
        )
        if not value
    ]
    if missing:
        raise ConfigurationError(
            "Eksik yapılandırma: " + ", ".join(missing) + ". Değerleri argüman olarak verin ya da "
            f"{ENV_PREFIX}* ortam değişkenleriyle birlikte from_env() kullanın."
        )
    assert client_id is not None and client_secret is not None and private_key is not None
    if max_retries < 0:
        raise ConfigurationError("max_retries negatif olamaz.")
    return ClientConfig(
        client_id=client_id,
        client_secret=client_secret,
        signer=Signer(private_key, password=private_key_password),
        environment=resolve_environment(environment),
        redirect_uri=redirect_uri,
        language_id=language_id,
        device_id=device_id,
        timeout=timeout,
        max_retries=max_retries,
        raise_on_failure=raise_on_failure,
    )


# --------------------------------------------------------------------------- OAuth2


def client_token_key(scope: str | Iterable[str]) -> str:
    return "client:" + " ".join(normalize_scopes(scope))


def user_token_key(user: str) -> str:
    return f"user:{user}"


def new_state() -> str:
    """CSRF koruması için rastgele bir ``state`` değeri üretir."""
    return secrets.token_urlsafe(24)


def build_authorization_url(
    config: ClientConfig,
    scopes: str | Iterable[str],
    *,
    state: str | None,
    redirect_uri: str | None,
    ui_locales: str | None,
) -> str:
    redirect = redirect_uri or config.redirect_uri
    if not redirect:
        raise ConfigurationError(
            "Authorization code akışı için redirect_uri gerekli "
            "(istemciyi oluştururken ya da bu çağrıda verin)."
        )
    scope_list = normalize_scopes(scopes)
    if not scope_list:
        raise ConfigurationError("En az bir scope verilmelidir.")
    params = {
        "response_type": "code",
        "client_id": config.client_id,
        "redirect_uri": redirect,
        "scope": " ".join(scope_list),
        "state": state or "",
    }
    if ui_locales:
        params["ui_locales"] = ui_locales
    return f"{config.environment.authorize_url}?{urlencode(params, quote_via=quote)}"


def parse_callback(url: str, *, state: str | None = None) -> str:
    """Yönlendirme (callback) URL'sinden authorization ``code`` değerini çıkarır.

    Args:
        url: Kullanıcının yönlendirildiği tam URL ya da yalnızca sorgu dizgisi.
        state: Yetkilendirme isteğinde gönderilen değer; verilirse eşleşme doğrulanır.

    Raises:
        AuthenticationError: Kullanıcı reddettiyse, ``code`` yoksa ya da ``state`` uyuşmuyorsa.
    """
    query = urlsplit(url).query if ("://" in url or "?" in url) else url
    params = {k: v[0] for k, v in parse_qs(query, keep_blank_values=True).items()}
    if "error" in params:
        raise AuthenticationError(
            f"Yetkilendirme reddedildi: {params['error']}",
            error=params["error"],
            error_description=params.get("error_description"),
        )
    if state is not None and params.get("state") != state:
        raise AuthenticationError(
            "Callback'teki state değeri gönderilenle uyuşmuyor (olası CSRF).",
            error="state_mismatch",
        )
    code = params.get("code")
    if not code:
        raise AuthenticationError(
            "Callback URL'sinde 'code' parametresi yok.", error="missing_code"
        )
    return code


def build_token_request(
    config: ClientConfig, grant: Mapping[str, str]
) -> tuple[str, dict[str, str], dict[str, str]]:
    """Token uç noktası için ``(url, headers, form)`` üçlüsünü kurar."""
    credentials = f"{config.client_id}:{config.client_secret}".encode()
    headers = {
        "Authorization": "Basic " + base64.b64encode(credentials).decode("ascii"),
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    return config.environment.token_url, headers, dict(grant)


def client_credentials_grant(scope: str | Iterable[str]) -> dict[str, str]:
    return {"grant_type": "client_credentials", "scope": " ".join(normalize_scopes(scope))}


def authorization_code_grant(
    config: ClientConfig, code: str, redirect_uri: str | None
) -> dict[str, str]:
    redirect = redirect_uri or config.redirect_uri
    if not redirect:
        raise ConfigurationError("Kodu token ile değiştirmek için redirect_uri gerekli.")
    return {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect}


def refresh_grant(refresh_token: str) -> dict[str, str]:
    return {"grant_type": "refresh_token", "refresh_token": refresh_token}


def parse_token_response(status_code: int, text: str, *, previous: Token | None = None) -> Token:
    """Token uç noktasının yanıtını ``Token``'a çevirir; hata ise ``AuthenticationError`` fırlatır."""
    try:
        data = json.loads(text) if text else {}
    except json.JSONDecodeError:
        data = {}
    if status_code >= 400 or not isinstance(data, dict) or "access_token" not in data:
        error = data.get("error") if isinstance(data, dict) else None
        description = data.get("error_description") if isinstance(data, dict) else None
        detail = " - ".join(str(p) for p in (error, description) if p) or text[:200] or "yanıt boş"
        raise AuthenticationError(
            f"Token alınamadı (HTTP {status_code}): {detail}",
            error=str(error) if error else None,
            error_description=str(description) if description else None,
            status_code=status_code,
        )
    token = Token.from_response(data)
    if previous is not None and token.refresh_token is None and previous.refresh_token:
        # Sunucu yeni refresh token dönmediyse eskisi geçerliliğini korur.
        token = Token(
            access_token=token.access_token,
            token_type=token.token_type,
            expires_at=token.expires_at,
            refresh_token=previous.refresh_token,
            refresh_expires_at=previous.refresh_expires_at,
            scope=token.scope or previous.scope,
        )
    return token


def explain_scope_error(
    error: AuthenticationError, scope: str | Iterable[str]
) -> AuthenticationError:
    """``invalid_scope`` hatasını, hangi kapsamın eksik olduğunu söyleyen bir hataya çevirir."""
    if error.error != "invalid_scope":
        return error
    wanted = " ".join(normalize_scopes(scope))
    return AuthenticationError(
        f"Uygulamanız {wanted!r} kapsamı için yetkili değil (invalid_scope). Geliştirici "
        "portalında uygulamanıza bu kapsamı içeren API ürününü ekleyin.",
        error=error.error,
        error_description=error.error_description,
        status_code=error.status_code,
    )


def plan_auth(
    options: Mapping[str, Any], *, scope: str, flow: str, default_user: str | None
) -> AuthPlan:
    """Çağrı için hangi token'ın kullanılacağına karar verir."""
    scope = str(options.get("scope") or scope)
    user = options.get("user") or default_user or DEFAULT_USER
    explicit = options.get("token")
    if explicit is not None:
        token = explicit.access_token if isinstance(explicit, Token) else str(explicit)
        return AuthPlan(kind="explicit", scope=scope, user=user, token=token)
    flow = str(options.get("flow") or flow)
    if flow == "authorization_code":
        return AuthPlan(kind="user", scope=scope, user=user)
    if flow == "client_credentials":
        if not normalize_scopes(scope):
            raise ConfigurationError("Client credentials akışı için bir scope gerekli.")
        return AuthPlan(kind="client", scope=scope, user=user)
    raise ConfigurationError(
        f"Bilinmeyen akış: {flow!r}. 'client_credentials' ya da 'authorization_code' olmalı."
    )


# --------------------------------------------------------------------------- istek kurma


def _scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, enum.Enum):
        return _scalar(value.value)
    if isinstance(value, (_dt.datetime, _dt.date, _dt.time)):
        return value.isoformat()
    return str(value)


def encode_query(params: Mapping[str, Any] | None) -> str:
    """Sorgu parametrelerini (baştaki ``?`` olmadan) kodlar. ``None`` değerler atlanır."""
    if not params:
        return ""
    pairs: list[tuple[str, str]] = []
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple, set, frozenset)):
            pairs.extend((key, _scalar(item)) for item in value if item is not None)
        else:
            pairs.append((key, _scalar(value)))
    return urlencode(pairs, quote_via=quote, safe="")


def format_path(path: str, path_params: Mapping[str, Any] | None) -> str:
    """``/v2/accounts/{suffix}`` gibi bir şablondaki yer tutucuları doldurur."""
    if not path.startswith("/"):
        path = "/" + path
    if not path_params:
        return path
    for name, value in path_params.items():
        placeholder = "{" + name + "}"
        if placeholder not in path:
            raise ConfigurationError(f"{path!r} yolunda {placeholder} yer tutucusu yok.")
        if value is None:
            raise ConfigurationError(f"Yol parametresi {name!r} boş olamaz.")
        path = path.replace(placeholder, quote(_scalar(value), safe=""))
    return path


def _json_default(value: Any) -> Any:
    if isinstance(value, Decimal):
        return int(value) if value == value.to_integral_value() else float(value)
    if isinstance(value, (_dt.datetime, _dt.date, _dt.time)):
        return value.isoformat()
    if isinstance(value, enum.Enum):
        return value.value
    if isinstance(value, (set, frozenset, tuple)):
        return list(value)
    if isinstance(value, bytes):
        return base64.b64encode(value).decode("ascii")
    raise TypeError(f"{type(value).__name__} türü JSON'a çevrilemiyor")


def encode_body(body: Any) -> bytes:
    """Gövdeyi, imzalanan ve gönderilen baytların birebir aynı olacağı şekilde JSON'a çevirir."""
    if isinstance(body, bytes):
        return body
    if isinstance(body, str):
        return body.encode("utf-8")
    return json.dumps(
        body, ensure_ascii=False, separators=(",", ":"), default=_json_default
    ).encode("utf-8")


def drop_none(data: Mapping[str, Any] | None) -> dict[str, Any]:
    """Üst düzeydeki ``None`` değerleri atar (verilmeyen isteğe bağlı parametreler)."""
    return {k: v for k, v in (data or {}).items() if v is not None}


def prepare_request(
    config: ClientConfig,
    method: str,
    path: str,
    *,
    access_token: str,
    path_params: Mapping[str, Any] | None = None,
    query: Mapping[str, Any] | None = None,
    body: Any = None,
    headers: Mapping[str, str] | None = None,
) -> PreparedRequest:
    """URL'yi, gövdeyi ve imza dahil tüm başlıkları üretir."""
    method = method.upper()
    url = config.environment.gateway_url + format_path(path, path_params)
    query_string = encode_query(query)
    if query_string:
        url += ("&" if "?" in url else "?") + query_string

    content: bytes | None = None
    if method in BODY_METHODS:
        content = encode_body({} if body is None else body)
        signed_payload: bytes = content
    else:
        if body is not None:
            raise ConfigurationError(f"{method} isteklerinde gövde gönderilemez.")
        _, sep, raw_query = url.partition("?")
        signed_payload = (sep + raw_query).encode("utf-8")

    final_headers = {
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
        "Authorization": f"Bearer {access_token}",
        "Signature": config.signer.sign(access_token, signed_payload),
    }
    if content is not None:
        final_headers["Content-Type"] = "application/json"
    if config.language_id is not None:
        final_headers["LanguageId"] = str(config.language_id)
    if config.device_id:
        final_headers["DeviceId"] = config.device_id
    for key, value in (headers or {}).items():
        if key.lower() in ("authorization", "signature"):
            raise ConfigurationError(
                f"{key} başlığı kütüphane tarafından üretilir, elle verilemez."
            )
        final_headers[key] = value
    return PreparedRequest(method=method, url=url, headers=final_headers, content=content)


# --------------------------------------------------------------------------- yanıt çözme

_STATUS_ERRORS: dict[int, type[APIError]] = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    429: RateLimitError,
}


def decode_body(content: bytes) -> Any:
    if not content or not content.strip():
        return None
    text = content.decode("utf-8", errors="replace")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def _error_detail(data: Any) -> str:
    results = parse_results(data)
    if results:
        return "; ".join(str(r) for r in results if str(r)) or "bilinmeyen hata"
    if isinstance(data, Mapping):
        errors = data.get("errors")
        if isinstance(errors, list) and errors:
            return json.dumps(errors, ensure_ascii=False)[:300]
        for key in ("message", "Message", "error_description", "error", "title", "detail"):
            if data.get(key):
                return str(data[key])
        return json.dumps(data, ensure_ascii=False)[:300]
    if isinstance(data, str) and data.strip():
        return data.strip()[:300]
    return "yanıt gövdesi boş"


def parse_response(
    request: PreparedRequest,
    *,
    status_code: int,
    headers: Mapping[str, str],
    content: bytes,
    raise_on_failure: bool,
) -> APIResponse:
    """HTTP yanıtını ``APIResponse``'a çevirir; hata yanıtlarında uygun istisnayı fırlatır."""
    data = decode_body(content)
    # İmzalı URL'deki sorgu müşteri verisi içerebilir; hata mesajına yalnızca yolu koy.
    target = f"{request.method} {urlsplit(request.url).path}"
    if status_code >= 400:
        error_cls = _STATUS_ERRORS.get(status_code, ServerError if status_code >= 500 else APIError)
        raise error_cls(
            f"{target} -> HTTP {status_code}: {_error_detail(data)}",
            status_code=status_code,
            method=request.method,
            url=request.url,
            body=data,
            results=parse_results(data),
        )
    response = APIResponse(status_code=status_code, headers=headers, data=data)
    if raise_on_failure and isinstance(data, Mapping) and data.get("success") is False:
        raise BusinessError(
            f"{target} başarısız: {_error_detail(data)}",
            status_code=status_code,
            method=request.method,
            url=request.url,
            body=data,
            results=response.results,
        )
    return response


def should_retry(method: str, attempt: int, max_retries: int, status_code: int | None) -> bool:
    """``attempt`` (0'dan başlar) sonrası isteğin yeniden denenip denenmeyeceği."""
    if attempt >= max_retries or method.upper() not in IDEMPOTENT_METHODS:
        return False
    return status_code is None or status_code in RETRY_STATUS_CODES


def retry_delay(attempt: int) -> float:
    return float(min(0.5 * (2**attempt), 8.0))
