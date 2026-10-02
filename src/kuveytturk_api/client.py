"""Senkron istemci: :class:`KuveytTurk`."""

from __future__ import annotations

import copy
import os
import threading
import time
import webbrowser
from collections.abc import Iterable, Mapping
from types import TracebackType
from typing import Any

import httpx

from . import _base
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
from .resources import ResourcesMixin
from .response import APIResponse
from .signature import PrivateKeySource
from .tokens import MemoryTokenStore, Token, TokenStore

__all__ = ["Auth", "KuveytTurk"]


class _Shared:
    """``as_user()`` ile türetilen istemcilerin ortak kullandığı durum."""

    def __init__(
        self, config: _base.ClientConfig, store: TokenStore, http: httpx.Client, owns_http: bool
    ) -> None:
        self.config = config
        self.store = store
        self.http = http
        self.owns_http = owns_http
        self.token_lock = threading.RLock()


class Auth:
    """OAuth2 işlemleri: token alma, yenileme ve saklama (``kt.auth``).

    İki akış vardır:

    * **Client credentials** — müşteri girişi gerektirmeyen uç noktalar. Token'lar ihtiyaç
      oldukça otomatik alınır ve süresi dolunca yenilenir; genelde hiçbir şey yapmanız gerekmez.
    * **Authorization code** — müşteri adına çalışan uç noktalar. Kullanıcıyı
      :meth:`authorization_url` adresine yönlendirir, dönen ``code`` değerini
      :meth:`exchange_code` ile token'a çevirirsiniz. Masaüstü betiklerinde hepsini
      :meth:`login` tek adımda yapar.
    """

    def __init__(self, client: KuveytTurk) -> None:
        self._shared = client._shared
        self._default_user = client._user

    def _user(self, user: str | None) -> str:
        return user or self._default_user or DEFAULT_USER

    # ----------------------------------------------------------- token uç noktası

    def _fetch(self, grant: Mapping[str, str], *, previous: Token | None = None) -> Token:
        url, headers, form = _base.build_token_request(self._shared.config, grant)
        try:
            response = self._shared.http.post(
                url, headers=headers, data=form, timeout=self._shared.config.timeout
            )
        except httpx.HTTPError as exc:
            raise TransportError(f"Token uç noktasına ulaşılamadı: {exc}") from exc
        return _base.parse_token_response(response.status_code, response.text, previous=previous)

    # ----------------------------------------------------------- client credentials

    def client_token(self, scope: str | Iterable[str], *, force: bool = False) -> Token:
        """Verilen kapsam için uygulama (client credentials) token'ını döndürür.

        Geçerli bir token saklıysa onu kullanır; yoksa ya da ``force=True`` ise yenisini alır.
        """
        key = _base.client_token_key(scope)
        with self._shared.token_lock:
            token = None if force else self._shared.store.get(key)
            if token is None or token.is_expired():
                try:
                    token = self._fetch(_base.client_credentials_grant(scope))
                except AuthenticationError as exc:
                    raise _base.explain_scope_error(exc, scope) from exc
                self._shared.store.set(key, token)
            return token

    # ----------------------------------------------------------- authorization code

    def authorization_url(
        self,
        scopes: str | Iterable[str],
        *,
        state: str | None = None,
        redirect_uri: str | None = None,
        ui_locales: str | None = None,
    ) -> str:
        """Müşteriyi giriş ve onay için yönlendireceğiniz adresi üretir.

        Args:
            scopes: İstenen kapsamlar. Refresh token almak için ``"offline_access"`` ekleyin.
            state: CSRF koruması için rastgele değer (:meth:`new_state` ile üretebilirsiniz);
                callback'te aynı değerin döndüğünü :meth:`parse_callback` ile doğrulayın.
            redirect_uri: İstemcideki varsayılanı ezer; portalda kayıtlı adresle birebir aynı olmalı.
            ui_locales: Giriş ekranının dili (``"tr"`` ya da ``"en"``).
        """
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

    def exchange_code(
        self, code: str, *, user: str | None = None, redirect_uri: str | None = None
    ) -> Token:
        """Authorization ``code`` değerini token'a çevirir ve ``user`` anahtarıyla saklar."""
        grant = _base.authorization_code_grant(self._shared.config, code, redirect_uri)
        with self._shared.token_lock:
            token = self._fetch(grant)
            self._shared.store.set(_base.user_token_key(self._user(user)), token)
            return token

    def refresh(self, *, user: str | None = None) -> Token:
        """Saklı refresh token ile yeni bir access token alır ve saklar."""
        key = _base.user_token_key(self._user(user))
        with self._shared.token_lock:
            current = self._shared.store.get(key)
            if current is None or not current.refresh_token:
                raise AuthorizationRequiredError(
                    f"{self._user(user)!r} için refresh token yok; müşterinin yeniden giriş "
                    "yapması gerekiyor.",
                    user=self._user(user),
                )
            try:
                token = self._fetch(_base.refresh_grant(current.refresh_token), previous=current)
            except AuthenticationError as exc:
                if exc.error == "invalid_grant":
                    self._shared.store.delete(key)
                    raise AuthorizationRequiredError(
                        "Refresh token geçersiz ya da süresi dolmuş; müşterinin yeniden giriş "
                        "yapması gerekiyor.",
                        user=self._user(user),
                    ) from exc
                raise
            self._shared.store.set(key, token)
            return token

    def user_token(self, *, user: str | None = None, scope: str | None = None) -> Token:
        """Müşteri için geçerli bir token döndürür; süresi dolmuşsa yeniler.

        Raises:
            AuthorizationRequiredError: Token yoksa, yenilenemiyorsa ya da ``scope`` eksikse.
        """
        name = self._user(user)
        with self._shared.token_lock:
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
                token = self.refresh(user=name)
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

    def login(
        self,
        scopes: str | Iterable[str],
        *,
        user: str | None = None,
        open_browser: bool = True,
        timeout: float = 300.0,
        ui_locales: str | None = None,
    ) -> Token:
        """Tarayıcıda giriş yaptırıp token'ı alır (masaüstü betikleri ve geliştirme için).

        ``redirect_uri`` ``http://localhost:PORT/...`` biçiminde olmalıdır: yöntem o portta
        geçici bir sunucu açar, tarayıcıyı giriş sayfasına yönlendirir, müşteri onay verince
        dönen kodu token'a çevirir ve saklar.
        """
        redirect_uri = self._shared.config.redirect_uri
        if not redirect_uri:
            raise ConfigurationError("login() için istemcide redirect_uri tanımlı olmalı.")
        state = _base.new_state()
        url = self.authorization_url(scopes, state=state, ui_locales=ui_locales)
        if not (open_browser and webbrowser.open(url)):
            print(f"Giriş için bu adresi tarayıcıda açın:\n{url}")
        callback = wait_for_callback(redirect_uri, timeout=timeout)
        return self.exchange_code(_base.parse_callback(callback, state=state), user=user)


class KuveytTurk(ResourcesMixin):
    """Kuveyt Türk API Market istemcisi (senkron).

    Örnek::

        from kuveytturk_api import KuveytTurk

        kt = KuveytTurk(
            client_id="...",
            client_secret="...",
            private_key="private_key.pem",
            environment="sandbox",
        )
        rates = kt.request("GET", "/v1/fx/rates", scope="public").value

    Args:
        client_id: Geliştirici portalındaki uygulamanın Client ID değeri.
        client_secret: Uygulamanın Client Secret değeri.
        private_key: İstekleri imzalayan RSA private key — dosya yolu, PEM içeriği ya da
            ``cryptography`` anahtar nesnesi. Karşılığı olan public key portalda kayıtlı olmalı.
        environment: ``"sandbox"`` (varsayılan), ``"production"`` ya da bir
            :class:`~kuveytturk_api.Environment`.
        redirect_uri: Authorization code akışı için; portalda kayıtlı adresle birebir aynı.
        token_store: Token'ların saklanacağı yer. Varsayılan bellektir; betiklerde
            :class:`~kuveytturk_api.FileTokenStore` kullanışlıdır.
        timeout: Saniye cinsinden varsayılan zaman aşımı.
        max_retries: Ağ hatası ve 5xx yanıtlarında **yalnızca GET** isteklerinin kaç kez
            yeniden deneneceği. POST'lar (para transferi vb.) asla otomatik tekrarlanmaz.
        language_id: ``LanguageId`` başlığı (1: Türkçe, 2: İngilizce).
        device_id: ``DeviceId`` başlığı (denetim kayıtları için isteğe bağlı).
        raise_on_failure: Yanıt zarfında ``success: false`` gelirse
            :class:`~kuveytturk_api.BusinessError` fırlatılsın mı.
        http_client: Kendi ``httpx.Client`` nesneniz (proxy, özel sertifika vb. için).
        private_key_password: Private key şifreliyse parolası.
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
        http_client: httpx.Client | None = None,
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
        self._shared = _Shared(
            config,
            token_store if token_store is not None else MemoryTokenStore(),
            http_client if http_client is not None else httpx.Client(timeout=timeout),
            owns_http=http_client is None,
        )
        self._user: str | None = None

    @classmethod
    def from_env(
        cls, env_file: str | os.PathLike[str] | None = None, **overrides: Any
    ) -> KuveytTurk:
        """İstemciyi ``KUVEYTTURK_*`` ortam değişkenlerinden kurar.

        Okunan değişkenler: ``KUVEYTTURK_CLIENT_ID``, ``KUVEYTTURK_CLIENT_SECRET``,
        ``KUVEYTTURK_PRIVATE_KEY`` (dosya yolu ya da PEM içeriği),
        ``KUVEYTTURK_PRIVATE_KEY_PASSWORD``, ``KUVEYTTURK_REDIRECT_URI``,
        ``KUVEYTTURK_ENVIRONMENT``, ``KUVEYTTURK_LANGUAGE_ID``, ``KUVEYTTURK_DEVICE_ID``.

        Args:
            env_file: Verilirse bu ``.env`` dosyası da okunur (gerçek ortam değişkenleri önceliklidir).
            **overrides: Yapıcıya doğrudan geçirilecek, ortamdaki değerleri ezen argümanlar.
        """
        settings = _base.settings_from_env(env_file)
        settings.update(overrides)
        return cls(**settings)

    # ----------------------------------------------------------- özellikler

    @property
    def environment(self) -> Environment:
        return self._shared.config.environment

    @property
    def auth(self) -> Auth:
        """OAuth2 işlemleri (bkz. :class:`Auth`)."""
        return Auth(self)

    def as_user(self, user: str) -> KuveytTurk:
        """Müşteri token'ı ``user`` anahtarından okunan bir istemci görünümü döndürür.

        Çok kullanıcılı uygulamalarda her müşteri için ayrı token saklamak içindir. Dönen
        nesne bağlantıları ve token deposunu bu istemciyle paylaşır::

            kt.auth.exchange_code(code, user="musteri-42")
            hesaplar = kt.as_user("musteri-42").request(
                "GET", "/v2/accounts", scope="accounts", flow="authorization_code"
            )
        """
        if not user:
            raise ConfigurationError("user boş olamaz.")
        clone = copy.copy(self)
        clone._user = user
        clone.__dict__.pop("_resource_cache", None)
        return clone

    # ----------------------------------------------------------- istekler

    def _access_token(self, plan: _base.AuthPlan, *, force: bool = False) -> str:
        if plan.kind == "explicit":
            assert plan.token is not None
            return plan.token
        if plan.kind == "client":
            return self.auth.client_token(plan.scope, force=force).access_token
        if force:
            return self.auth.refresh(user=plan.user).access_token
        return self.auth.user_token(user=plan.user, scope=plan.scope).access_token

    def _send(self, prepared: _base.PreparedRequest, timeout: float) -> httpx.Response:
        config = self._shared.config
        attempt = 0
        while True:
            try:
                response = self._shared.http.request(
                    prepared.method,
                    prepared.url,
                    headers=prepared.headers,
                    content=prepared.content,
                    timeout=timeout,
                )
            except httpx.HTTPError as exc:
                _base.log_exchange(prepared, None, attempt)
                if _base.should_retry(prepared.method, attempt, config.max_retries, None):
                    time.sleep(_base.retry_delay(attempt))
                    attempt += 1
                    continue
                raise TransportError(f"{prepared.method} isteği gönderilemedi: {exc}") from exc
            _base.log_exchange(prepared, response.status_code, attempt)
            if _base.should_retry(
                prepared.method, attempt, config.max_retries, response.status_code
            ):
                time.sleep(_base.retry_delay(attempt))
                attempt += 1
                continue
            return response

    def request(
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
        """Herhangi bir uç noktayı çağırır; token ve imza otomatik eklenir.

        Hazır uç nokta metotları da bunu kullanır. Kütüphanede henüz karşılığı olmayan bir
        uç nokta için doğrudan çağırabilirsiniz::

            kt.request("GET", "/v4/accounts/{suffix}/transactions", scope="accounts",
                       path_params={"suffix": 1}, query={"itemCount": 10})

        Args:
            method: HTTP metodu.
            path: Gateway'e göre yol; ``{ad}`` yer tutucuları ``path_params`` ile doldurulur.
            scope: Uç noktanın dokümanındaki kapsam (ör. ``"accounts"``).
            flow: ``"client_credentials"`` ya da ``"authorization_code"``.
            query: Sorgu parametreleri; ``None`` değerler gönderilmez.
            body: JSON gövdesi (POST/PUT/PATCH).
            options: Bu çağrıya özel ayarlar (bkz. :class:`~kuveytturk_api.RequestOptions`).

        Raises:
            APIError: API hata yanıtı döndürdüyse (alt sınıflarına bakın).
            AuthorizationRequiredError: Müşteri girişi gerekiyorsa.
            TransportError: İstek sunucuya ulaşamadıysa.
        """
        opts: Mapping[str, Any] = options or {}
        config = self._shared.config
        plan = _base.plan_auth(opts, scope=scope, flow=flow, default_user=self._user)
        timeout = float(opts.get("timeout", config.timeout))
        raise_on_failure = bool(opts.get("raise_on_failure", config.raise_on_failure))

        def attempt(force_token: bool) -> APIResponse:
            prepared = _base.prepare_request(
                config,
                method,
                path,
                access_token=self._access_token(plan, force=force_token),
                path_params=path_params,
                query=query,
                body=body,
                headers=opts.get("headers"),
            )
            response = self._send(prepared, timeout)
            return _base.parse_response(
                prepared,
                status_code=response.status_code,
                headers=response.headers,
                content=response.content,
                raise_on_failure=raise_on_failure,
            )

        try:
            return attempt(False)
        except UnauthorizedError:
            # Saklı token sunucu tarafında geçersiz kılınmış olabilir: bir kez yenileyip dene.
            # 401, isteğin işlenmediği anlamına geldiği için POST'larda da güvenlidir.
            if plan.kind == "explicit":
                raise
            if plan.kind == "user":
                current = self.auth.get_user_token(user=plan.user)
                if current is None or not current.can_refresh():
                    raise
            return attempt(True)

    def get(
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
        return self.request(
            "GET",
            path,
            scope=scope,
            flow=flow,
            path_params=path_params,
            query=query,
            options=options,
        )

    def post(
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
        return self.request(
            "POST",
            path,
            scope=scope,
            flow=flow,
            path_params=path_params,
            query=query,
            body=body,
            options=options,
        )

    # ----------------------------------------------------------- yaşam döngüsü

    def close(self) -> None:
        """Açık bağlantıları kapatır (istemci kendi ``httpx.Client``'ını oluşturduysa)."""
        if self._shared.owns_http:
            self._shared.http.close()

    def __enter__(self) -> KuveytTurk:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def __repr__(self) -> str:
        user = f" user={self._user!r}" if self._user else ""
        return f"<KuveytTurk environment={self.environment.name!r}{user}>"
