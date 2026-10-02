# kuveytturk-api

Kuveyt Türk API Market (https://developer.kuveytturk.com.tr) için gayriresmî Python istemcisi.
PyPI'da `kuveytturk-api` adıyla yayınlanacak; import adı `kuveytturk_api`.
(`kuveytturk` adı PyPI'da başkasına ait, 2019'dan kalma terk edilmiş bir pakete ait; kullanılamaz.)

Kullanıcıyla iletişim dili Türkçe. Docstring'ler, hata mesajları, README ve yorumlar Türkçe;
tanımlayıcılar (sınıf/fonksiyon/değişken adları) İngilizce. Uç nokta açıklamaları dokümandan
İngilizce geldiği gibi bırakılır.

## Komutlar

Ortam: `venv/` (Python 3.9 — desteklenen en düşük sürüm; kod 3.9'da çalışmak zorunda).

```bash
venv/bin/python -m pytest -q                 # testler (ağ gerektirmez)
KUVEYTTURK_LIVE=1 venv/bin/python -m pytest -q -m live   # sandbox'a gerçek istek atan testler
venv/bin/ruff check src tests scripts && venv/bin/ruff format src tests scripts
venv/bin/mypy                                # strict; yalnızca src/
venv/bin/python -m build && venv/bin/twine check dist/*
```

Uç noktaları dokümandan yeniden üretmek (üç adım, sırayla):

```bash
venv/bin/python scripts/fetch_docs.py    # dokümanları .cache/kt-docs'a indirir (yavaş, kasıtlı)
venv/bin/python scripts/build_spec.py    # .cache -> spec/endpoints.json (+ uyarılar)
venv/bin/python scripts/generate.py      # spec -> src/kuveytturk_api/resources/*.py + ENDPOINTS.md
```

## Mimari

```
src/kuveytturk_api/
  _base.py          Ağ erişimi olmayan ortak mantık: yapılandırma, OAuth istek/yanıtları,
                    istek kurma + imzalama (prepare_request), yanıt çözme (parse_response),
                    yeniden deneme kararı. Davranış değişikliği önce buraya yapılır.
  client.py         KuveytTurk + Auth (senkron, httpx.Client)
  async_client.py   AsyncKuveytTurk + AsyncAuth (aynı davranış, httpx.AsyncClient)
  signature.py      Signer (RSA-SHA256 imza), generate_key_pair
  tokens.py         Token, TokenStore protokolü, MemoryTokenStore, FileTokenStore
  response.py       APIResponse (zarf: value/success/results), ResultItem
  exceptions.py     KuveytTurkError hiyerarşisi
  environments.py   SANDBOX / PRODUCTION adresleri
  callback_server.py  auth.login() için tek kullanımlık yerel callback sunucusu
  resources/        ÜRETİLEN uç nokta metotları (kt.accounts, kt.fx, ...). Elle düzenlenmez.
    _resource.py    Elle yazılan taban (Resource, AsyncResource, merge, tür takma adları)
spec/endpoints.json Uç nokta kataloğu (build_spec.py çıktısı; commit edilir)
spec/overrides.json Doküman hatalarını düzeltmek için elle yazılan düzeltmeler (doküman id -> alanlar)
scripts/            fetch_docs.py, build_spec.py, generate.py
ENDPOINTS.md        Üretilen uç nokta listesi
examples/           Çalıştırılabilir örnek uygulamalar (ortak yardımcılar: _common.py)
```

Senkron ve asenkron istemci aynı davranmak zorunda: ortak mantık `_base.py`'de durur, iki
istemci yalnızca G/Ç'yi yapar. Birine eklenen davranış diğerine de eklenir ve ikisi de test edilir.

## API'nin bilinmesi gereken kuralları

- **İmza** (`Signature` başlığı): RSA-SHA256 / PKCS#1 v1.5, Base64. İmzalanan veri POST'ta
  `access_token + gövde`, GET'te `access_token + "?" + sorgu dizgisi` (sorgu yoksa yalnızca token).
  İmzalanan baytlar ile gönderilen baytlar birebir aynı olmalı; bu yüzden gövde ve sorgu
  `_base.py`'de bir kez kodlanır ve httpx'e hazır hâliyle verilir. Bunu bozacak şekilde
  httpx'in `params=`/`json=` argümanlarına geçme.
- **Token'lar**: client credentials token'ı kapsam (scope) başına ayrı alınır ve saklanır.
  Authorization code token'ı kullanıcı anahtarıyla saklanır (`as_user()`); access token 1 saat,
  refresh token 24 saat geçerli.
- **Yeniden deneme**: yalnızca GET, ağ hatası ve 5xx'te. POST'lar (para transferi vb.) asla
  otomatik tekrarlanmaz — bunu değiştirme. 401'de token bir kez yenilenip istek tekrarlanır.
- **Yanıt zarfı**: `{"value": ..., "success": bool, "results": [{errorCode, errorMessage}]}`.
  `success: false` -> `BusinessError`. Bazı uç noktalar zarf kullanmaz; `APIResponse.data` ham gövdedir.
- **Ortamlar**: sandbox `prep-identity` / `prep-gateway.kuveytturk.com.tr`; production
  `identity` / `gateway.kuveytturk.com.tr`.

## Dokümanlar ve üreteç

- Doküman sitesi bir SPA; içerik `https://prep-kuveytturk-portalapi.kuveytturk.com.tr/api/v1/`
  altındaki JSON API'sinden Markdown olarak gelir (`get-document-menu`, `document/{id}`).
  `scripts/fetch_docs.py` bunu kullanır. Tarayıcıyla HTML kazımaya gerek yok.
- **Sunucu hızlı/paralel istekleri IP bazında engelliyor** ve engel sandbox dahil tüm
  `*.kuveytturk.com.tr` adreslerini kapsıyor (TLS'te "connection reset"). 4 paralel istek bunu
  tetikledi. İstekleri tek tek ve birkaç saniye arayla at; engellenince ısrar etme, bekle.
- Dokümanlar elle yazılmış ve hatalı olabilir (yanlış akış/kapsam, eksik parametre, başka uç
  noktadan kopyalanmış gövde). Düzeltmeler koda değil `spec/overrides.json`'a yazılır. Her üretilen
  metot bu yüzden `extra_query` / `extra_body` / `request_options` kabul eder; hiçbir karşılığı
  olmayan uç nokta için `kt.request()` vardır.
- Gövde tablolarında iç içe alanlar düz listelenir; hangi alanın üst düzey olduğu örnek JSON'dan
  çıkarılır ve `{"request": {"contract": {...}}}` gibi tek anahtarlı sarmalayıcılar açılır
  (`body_wrap`). Ayrıntı: `scripts/build_spec.py::build_body`.

## Sırlar

- Sandbox uygulama bilgileri `.env`'de, imza anahtarı `.secrets/private_key.pem`'de, test müşteri
  bilgileri `.secrets/test_customers.txt`'de. Hepsi `.gitignore`'da; **asla commit etme, koda ya
  da teste gömme, çıktıya yazdırma**.
- sdist içeriği `pyproject.toml`'da `only-include` ile sınırlı. Yayından önce
  `tar tzf dist/*.tar.gz` ile içerikte sır olmadığını doğrula.
- `.legacy/` eski deneme kodlarını ve eski doküman kazımalarını tutar (git'e girmez); içinde
  gömülü sırlar var. Kullanılmıyor, kullanıcı isterse silinebilir.

## Testler

- Birim testleri `httpx.MockTransport` ile çalışır (`tests/conftest.py::Recorder`); ağa çıkmaz.
- `tests/test_generated.py` katalogdaki her uç nokta için üretilen metodun doğru isteği
  kurduğunu ve imzanın gönderilen baytlarla eşleştiğini doğrular; ayrıca üretilen dosyaların
  güncel olduğunu (`generate.py --check`) denetler.
- `tests/test_examples.py` örnek uygulamaları dokümandaki örnek yanıtlarla çalıştırır. Uç nokta
  adları (özellikle `spec/overrides.json`'daki adlar) değişirse örnekler ve README de güncellenir.
- Para hareketi yapan örnekler varsayılan olarak deneme modunda çalışır (`--execute` olmadan
  istek atmaz); bu davranışı koru. Dokümanda olmayan gövde alanlarını tahminle ekleme.
- Canlı testler (`-m live`) yalnızca `KUVEYTTURK_LIVE=1` iken çalışır ve `.env` ister. Yalnızca
  okuma yapan uç noktaları çağırır; para hareketi yapan uç noktalar canlı testlere eklenmez.

## Yayın

1. `src/kuveytturk_api/_version.py` ve `CHANGELOG.md` güncellenir.
2. `pytest`, `ruff`, `mypy`, `generate.py --check` temiz olmalı.
3. `python -m build`, `twine check dist/*`, sdist içeriği gözle kontrol edilir.
4. `twine upload dist/*` — PyPI token'ı kullanıcıdadır; yüklemeyi kullanıcı yapar ya da açıkça onaylar.
