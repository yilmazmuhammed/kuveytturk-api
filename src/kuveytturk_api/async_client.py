"""Asenkron istemci: :class:`AsyncKuveytTurk`.

Davranış :class:`kuveytturk_api.KuveytTurk` ile aynıdır; ağa çıkan metotlar ``await`` edilir.
"""

from __future__ import annotations

import asyncio
import copy
import os
import time
import webbrowser
from collections.abc import Iterable, Mapping
from types import TracebackType
from typing import Any

import httpx

from . import _base, _logging
from ._base import DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT, DEFAULT_USER, Flow, RequestOptions
from .callback_server import wait_for_callback
from .environments import Environment
from .exceptions import (
    AuthenticationError,
    AuthorizationRequiredError,
    ConfigurationError,
    TransportError,
    UnauthorizedError,
)
from .resources import AsyncResourcesMixin
from .response import APIResponse
from .signature import PrivateKeySource
from .tokens import MemoryTokenStore, Token, TokenStore

__all__ = ["AsyncAuth", "AsyncKuveytTurk"]


class _AsyncShared:
    def __init__(
        self,
        config: _base.ClientConfig,
        store: TokenStore,
        http: httpx.AsyncClient,
        owns_http: bool,
    ) -> None:
        self.config = config
        self.store = store
        self.http = http
        self.owns_http = owns_http
        self._token_lock: asyncio.Lock | None = None

    @property
    def token_lock(self) -> asyncio.Lock:
        # Python 3.9'da Lock oluşturulduğu döngüye bağlanır; bu yüzden ilk kullanımda yaratılır.
        if self._token_lock is None:
            self._token_lock = asyncio.Lock()
        return self._token_lock


class AsyncAuth:
    """OAuth2 işlemlerinin asenkron hali (``kt.auth``). Ayrıntılar için :class:`~kuveytturk_api.Auth`."""

    def __init__(self, client: AsyncKuveytTurk) -> None:
        self._shared = client._shared
        self._default_user = client._user

    def _user(self, user: str | None) -> str:
        return user or self._default_user or DEFAULT_USER

    async def _fetch(self, grant: Mapping[str, str], *, previous: Token | None = None) -> Token:
        url, headers, form = _base.build_token_request(self._shared.config, grant)
        _logging.log_token_request(url, form)
        started = time.perf_counter()
        try:
            response = await self._shared.http.post(
                url, headers=headers, data=form, timeout=self._shared.config.timeout
            )
        except httpx.HTTPError as exc:
            _logging.log_failure("POST", url, exc, time.perf_counter() - started, 0)
            raise TransportError(f"Token uç noktasına ulaşılamadı: {exc}") from exc
        _logging.log_token_response(
            url, response.status_code, response.text, time.perf_counter() - started
        )
        return _base.parse_token_response(response.status_code, response.text, previous=previous)

    async def client_token(self, scope: str | Iterable[str], *, force: bool = False) -> Token:
        """Verilen kapsam için uygulama (client credentials) token'ını döndürür."""
        key = _base.client_token_key(scope)
        async with self._shared.token_lock:
            token = None if force else self._shared.store.get(key)
            if token is None or token.is_expired():
                try:
                    token = await self._fetch(_base.client_credentials_grant(scope))
                except AuthenticationError as exc:
                    raise _base.explain_scope_error(exc, scope) from exc
                self._shared.store.set(key, token)
            return token

    def authorization_url(
        self,
        scopes: str | Iterable[str],
        *,
        state: str | None = None,
        redirect_uri: str | None = None,
        ui_locales: str | None = None,
    ) -> str:
        """Müşteriyi giriş ve onay için yönlendireceğiniz adresi üretir."""
        return _base.build_authorization_url(
            self._shared.config,
            scopes,
            state=state,
            redirect_uri=redirect_uri,
            ui_locales=ui_locales,
        )

    @staticmethod
    def new_state() -> str:
        """``state`` parametresi için tahmin edilemez bir değer üretir."""
        return _base.new_state()

    @staticmethod
    def parse_callback(url: str, *, state: str | None = None) -> str:
        """Callback URL'sinden ``code`` değerini çıkarır; ``state`` verilirse doğrular."""
        return _base.parse_callback(url, state=state)

    async def exchange_code(
        self, code: str, *, user: str | None = None, redirect_uri: str | None = None
    ) -> Token:
        """Authorization ``code`` değerini token'a çevirir ve ``user`` anahtarıyla saklar."""
        grant = _base.authorization_code_grant(self._shared.config, code, redirect_uri)
        async with self._shared.token_lock:
            token = await self._fetch(grant)
            self._shared.store.set(_base.user_token_key(self._user(user)), token)
            return token

    async def _refresh_locked(self, name: str) -> Token:
        key = _base.user_token_key(name)
        current = self._shared.store.get(key)
        if current is None or not current.refresh_token:
            raise AuthorizationRequiredError(
                f"{name!r} için refresh token yok; müşterinin yeniden giriş yapması gerekiyor.",
                user=name,
            )
        try:
            token = await self._fetch(_base.refresh_grant(current.refresh_token), previous=current)
        except AuthenticationError as exc:
            if exc.error == "invalid_grant":
                self._shared.store.delete(key)
                raise AuthorizationRequiredError(
                    "Refresh token geçersiz ya da süresi dolmuş; müşterinin yeniden giriş "
                    "yapması gerekiyor.",
                    user=name,
                ) from exc
            raise
        self._shared.store.set(key, token)
        return token

    async def refresh(self, *, user: str | None = None) -> Token:
        """Saklı refresh token ile yeni bir access token alır ve saklar."""
        async with self._shared.token_lock:
            return await self._refresh_locked(self._user(user))

    async def user_token(self, *, user: str | None = None, scope: str | None = None) -> Token:
        """Müşteri için geçerli bir token döndürür; süresi dolmuşsa yeniler."""
        name = self._user(user)
        async with self._shared.token_lock:
            token = self._shared.store.get(_base.user_token_key(name))
            if token is None:
                raise AuthorizationRequiredError(
                    f"{name!r} için müşteri token'ı yok. Önce auth.login() ya da "
                    "auth.authorization_url() + auth.exchange_code() ile giriş yaptırın.",
                    scope=scope,
                    user=name,
                )
            if token.is_expired():
                if not token.can_refresh():
                    raise AuthorizationRequiredError(
                        f"{name!r} için token'ın süresi dolmuş ve yenilenemiyor "
                        "(refresh token almak için 'offline_access' kapsamını isteyin).",
                        scope=scope,
                        user=name,
                    )
                token = await self._refresh_locked(name)
            if scope and not token.has_scope(scope):
                raise AuthorizationRequiredError(
                    f"{name!r} token'ında {scope!r} kapsamı yok (verilenler: {token.scope!r}). "
                    "Bu kapsamı da isteyerek yeniden giriş yaptırın.",
                    scope=scope,
                    user=name,
                )
            return token

    def get_user_token(self, *, user: str | None = None) -> Token | None:
        """Saklı müşteri token'ını (yenilemeye çalışmadan) döndürür."""
        return self._shared.store.get(_base.user_token_key(self._user(user)))

    def set_user_token(self, token: Token, *, user: str | None = None) -> None:
        """Başka bir yerde alınmış/saklanmış müşteri token'ını istemciye tanıtır."""
        self._shared.store.set(_base.user_token_key(self._user(user)), token)

    def forget_user(self, *, user: str | None = None) -> None:
        """Müşterinin saklı token'ını siler."""
        self._shared.store.delete(_base.user_token_key(self._user(user)))

    async def login(
        self,
        scopes: str | Iterable[str],
        *,
        user: str | None = None,
        open_browser: bool = True,
        timeout: float = 300.0,
        ui_locales: str | None = None,
    ) -> Token:
        """Tarayıcıda giriş yaptırıp token'ı alır (masaüstü betikleri ve geliştirme için)."""
        redirect_uri = self._shared.config.redirect_uri
        if not redirect_uri:
            raise ConfigurationError("login() için istemcide redirect_uri tanımlı olmalı.")
        state = _base.new_state()
        url = self.authorization_url(scopes, state=state, ui_locales=ui_locales)
        if not (open_browser and webbrowser.open(url)):
            print(f"Giriş için bu adresi tarayıcıda açın:\n{url}")
        loop = asyncio.get_running_loop()
        callback = await loop.run_in_executor(
            None, lambda: wait_for_callback(redirect_uri, timeout=timeout)
        )
        return await self.exchange_code(_base.parse_callback(callback, state=state), user=user)


class AsyncKuveytTurk(AsyncResourcesMixin):
    """Kuveyt Türk API Market istemcisi (asenkron).

    Argümanlar :class:`~kuveytturk_api.KuveytTurk` ile aynıdır; ``http_client`` olarak
    ``httpx.AsyncClient`` alır::

        async with AsyncKuveytTurk.from_env(".env") as kt:
            rates = (await kt.request("GET", "/v1/fx/rates", scope="public")).value
    """

    def __init__(
        self,
        client_id: str | None = None,
        client_secret: str | None = None,
        private_key: PrivateKeySource | None = None,
        *,
        environment: str | Environment = "sandbox",
        redirect_uri: str | None = None,
        token_store: TokenStore | None = None,
        timeout: float = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        language_id: int | None = None,
        device_id: str | None = None,
        raise_on_failure: bool = True,
        http_client: httpx.AsyncClient | None = None,
        private_key_password: str | bytes | None = None,
    ) -> None:
        config = _base.build_config(
            client_id=client_id,
            client_secret=client_secret,
            private_key=private_key,
            private_key_password=private_key_password,
            environment=environment,
            redirect_uri=redirect_uri,
            language_id=language_id,
            device_id=device_id,
            timeout=timeout,
            max_retries=max_retries,
            raise_on_failure=raise_on_failure,
        )
        self._shared = _AsyncShared(
            config,
            token_store if token_store is not None else MemoryTokenStore(),
            http_client if http_client is not None else httpx.AsyncClient(timeout=timeout),
            owns_http=http_client is None,
        )
        self._user: str | None = None

    @classmethod
    def from_env(
        cls, env_file: str | os.PathLike[str] | None = None, **overrides: Any
    ) -> AsyncKuveytTurk:
        """İstemciyi ``KUVEYTTURK_*`` ortam değişkenlerinden kurar (bkz. ``KuveytTurk.from_env``)."""
        settings = _base.settings_from_env(env_file)
        settings.update(overrides)
        return cls(**settings)

    @property
    def environment(self) -> Environment:
        return self._shared.config.environment

    @property
    def redirect_uri(self) -> str | None:
        """Authorization code akışında kullanılan yönlendirme adresi (tanımlıysa)."""
        return self._shared.config.redirect_uri

    @property
    def auth(self) -> AsyncAuth:
        """OAuth2 işlemleri (bkz. :class:`AsyncAuth`)."""
        return AsyncAuth(self)

    def as_user(self, user: str) -> AsyncKuveytTurk:
        """Müşteri token'ı ``user`` anahtarından okunan bir istemci görünümü döndürür."""
        if not user:
            raise ConfigurationError("user boş olamaz.")
        clone = copy.copy(self)
        clone._user = user
        clone.__dict__.pop("_resource_cache", None)
        return clone

    async def _access_token(self, plan: _base.AuthPlan, *, force: bool = False) -> str:
        if plan.kind == "explicit":
            assert plan.token is not None
            return plan.token
        if plan.kind == "client":
            return (await self.auth.client_token(plan.scope, force=force)).access_token
        if force:
            return (await self.auth.refresh(user=plan.user)).access_token
        return (await self.auth.user_token(user=plan.user, scope=plan.scope)).access_token

    async def _send(self, prepared: _base.PreparedRequest, timeout: float) -> httpx.Response:
        config = self._shared.config
        attempt = 0
        while True:
            _logging.log_request(
                prepared.method, prepared.url, prepared.headers, prepared.content, attempt
            )
            started = time.perf_counter()
            try:
                response = await self._shared.http.request(
                    prepared.method,
                    prepared.url,
                    headers=prepared.headers,
                    content=prepared.content,
                    timeout=timeout,
                )
            except httpx.HTTPError as exc:
                _logging.log_failure(
                    prepared.method, prepared.url, exc, time.perf_counter() - started, attempt
                )
                if _base.should_retry(prepared.method, attempt, config.max_retries, None):
                    await asyncio.sleep(_base.retry_delay(attempt))
                    attempt += 1
                    continue
                raise TransportError(f"{prepared.method} isteği gönderilemedi: {exc}") from exc
            _logging.log_response(
                prepared.method,
                prepared.url,
                response.status_code,
                response.content,
                time.perf_counter() - started,
                attempt,
            )
            if _base.should_retry(
                prepared.method, attempt, config.max_retries, response.status_code
            ):
                await asyncio.sleep(_base.retry_delay(attempt))
                attempt += 1
                continue
            return response

    async def request(
        self,
        method: str,
        path: str,
        *,
        scope: str = "",
        flow: Flow = "client_credentials",
        path_params: Mapping[str, Any] | None = None,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        options: RequestOptions | None = None,
    ) -> APIResponse:
        """Herhangi bir uç noktayı çağırır (bkz. ``KuveytTurk.request``)."""
        opts: Mapping[str, Any] = options or {}
        config = self._shared.config
        plan = _base.plan_auth(opts, scope=scope, flow=flow, default_user=self._user)
        timeout = float(opts.get("timeout", config.timeout))
        raise_on_failure = bool(opts.get("raise_on_failure", config.raise_on_failure))

        async def attempt(force_token: bool) -> APIResponse:
            prepared = _base.prepare_request(
                config,
                method,
                path,
                access_token=await self._access_token(plan, force=force_token),
                path_params=path_params,
                query=query,
                body=body,
                headers=opts.get("headers"),
            )
            response = await self._send(prepared, timeout)
            return _base.parse_response(
                prepared,
                status_code=response.status_code,
                headers=response.headers,
                content=response.content,
                raise_on_failure=raise_on_failure,
            )

        try:
            return await attempt(False)
        except UnauthorizedError:
            if plan.kind == "explicit":
                raise
            if plan.kind == "user":
                current = self.auth.get_user_token(user=plan.user)
                if current is None or not current.can_refresh():
                    raise
            return await attempt(True)

    async def get(
        self,
        path: str,
        *,
        scope: str = "",
        flow: Flow = "client_credentials",
        path_params: Mapping[str, Any] | None = None,
        query: Mapping[str, Any] | None = None,
        options: RequestOptions | None = None,
    ) -> APIResponse:
        """``request("GET", ...)`` kısayolu."""
        return await self.request(
            "GET",
            path,
            scope=scope,
            flow=flow,
            path_params=path_params,
            query=query,
            options=options,
        )

    async def post(
        self,
        path: str,
        *,
        scope: str = "",
        flow: Flow = "client_credentials",
        path_params: Mapping[str, Any] | None = None,
        query: Mapping[str, Any] | None = None,
        body: Any = None,
        options: RequestOptions | None = None,
    ) -> APIResponse:
        """``request("POST", ...)`` kısayolu."""
        return await self.request(
            "POST",
            path,
            scope=scope,
            flow=flow,
            path_params=path_params,
            query=query,
            body=body,
            options=options,
        )

    async def aclose(self) -> None:
        """Açık bağlantıları kapatır (istemci kendi ``httpx.AsyncClient``'ını oluşturduysa)."""
        if self._shared.owns_http:
            await self._shared.http.aclose()

    async def __aenter__(self) -> AsyncKuveytTurk:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    def __repr__(self) -> str:
        user = f" user={self._user!r}" if self._user else ""
        return f"<AsyncKuveytTurk environment={self.environment.name!r}{user}>"
