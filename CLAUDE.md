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
venv/bin/python scripts/fetch_docs.py    # dokümanları apidocs/'a indirir (yavaş, kasıtlı; eksikleri tamamlar)
venv/bin/python scripts/build_spec.py    # apidocs/ -> spec/endpoints.json (+ uyarılar)
venv/bin/python scripts/generate.py      # spec -> resources/*.py, ENDPOINTS.md, docs/uc-noktalar/, mkdocs.yml nav
```

Doküman sitesi (MkDocs Material, Türkçe). Araçlar ayrı ortamda: `python3 -m venv .venv-docs &&
.venv-docs/bin/pip install -e ".[docs]"`. Önizleme `.claude/launch.json` -> "docs" (port 8001).

```bash
.venv-docs/bin/mkdocs build --strict     # CI'daki docs işi de bunu çalıştırır
```

Site https://dvty.tr/kuveytturk-api/ adresinde (github.io adresi oraya yönlenir; kullanıcının GitHub kullanıcı sitesindeki özel alan adı); `main`'e her gönderimde `.github/workflows/docs.yml` derleyip
GitHub Pages'e yükler.

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
  _logging.py       "kuveytturk_api" logger'ı: INFO tek satır özet, DEBUG istek/yanıtın tamamı
                    (token, imza, client secret, code, refresh token maskelenir); enable_logging()
                    ve KUVEYTTURK_LOG ortam değişkeni
  resources/        ÜRETİLEN uç nokta metotları (kt.accounts, kt.fx, ...). Elle düzenlenmez.
    _resource.py    Elle yazılan taban (Resource, AsyncResource, merge, tür takma adları)
spec/endpoints.json Uç nokta kataloğu (build_spec.py çıktısı; commit edilir)
spec/overrides.json Doküman hatalarını düzeltmek için elle yazılan düzeltmeler (doküman id -> alanlar)
apidocs/            İndirilen API Market dokümanları (Markdown; menu.json + <dil>/<kategori>/<başlık>-<id>.md).
                    Bu repoda DEĞİL: ayrı private repo `yilmazmuhammed/kuveytturk-api-apidocs`,
                    buraya klonlanır ve .gitignore'dadır (içerik Kuveyt Türk'e ait; public repoda
                    durmamalı). Yoksa: `gh repo clone yilmazmuhammed/kuveytturk-api-apidocs apidocs`.
                    fetch_docs.py ile güncelledikten sonra o repoda commit + push et.
                    Doküman hakkında bir şey ararken önce burada grep yap.
scripts/            fetch_docs.py, build_spec.py, generate.py, docstore.py (apidocs okuma/yazma)
ENDPOINTS.md        Üretilen uç nokta listesi
mkdocs.yml, docs/   Doküman sitesi. docs/uc-noktalar/ ve mkdocs.yml'deki uç nokta nav listesi
                    ÜRETİLİR (generate.py); diğer sayfalar elle yazılır. Sınıf referansı
                    (docs/referans/) docstring'lerden mkdocstrings ile gelir: docstring'lerde
                    reST rolleri (:class: vb.) ve "::" blokları değil Markdown kullan.
examples/           Çalıştırılabilir örnek uygulamalar (ortak yardımcılar: _common.py)
examples/web_app/   Müşteri girişi yapan Flask uygulaması (authorization code akışı). Önizleme:
                    .claude/launch.json -> "web-app-example" (port 8000 = Redirect URI'nin portu)
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
- **Gateway'in hata yanıtları** (sandbox'ta doğrulandı): imza hatası **400**
  `{"code":400,"message":"Client signature validation error"}`; yanlış akış 401
  `"Invalid grant type. Authorization Code is required."`; yanlış kapsam 403 `"Invalid Scope"`;
  olmayan yol 404 `"Path not found"`. İş kuralı hataları `results[]` içinde gelir.
- **Yanıt zarfı**: `{"value": ..., "success": bool, "results": [{errorCode, errorMessage}]}`.
  `success: false` -> `BusinessError`. Bazı uç noktalar zarf kullanmaz; `APIResponse.data` ham gövdedir.
  Gerçek yanıtlarda ayrıca üst düzeyde `errors: []` ve `executionReferenceId` bulunur.
- **Gerçek yanıtlar dokümandaki örneklerden farklı olabilir** (ör. kurlar `value.rateList[].fxName`
  ile gelir, doküman `value[].name` der; hesaplarda `productType`/`availableBalance`). Yanıt alanına
  dayanan bir şey yazarken sandbox'ta gerçek yanıta bak; dokümana güvenme.
- **Ortamlar**: sandbox `prep-identity` / `prep-gateway.kuveytturk.com.tr`; production
  `identity` / `gateway.kuveytturk.com.tr`.

### Hesap hareketleri: sandbox'ta ölçülenler (2026-10-03)

Müşteri girişli `tpp_accounts.account_transactions_v2` (22 kayıt) ve client credentials
`accounts.account_transactions_v3` (23 kayıt) üzerinde:

- Kayıtlar **yeniden eskiye** sıralıdır; `itemCount` en yeni N kaydı verir. Sayfalama yoktur.
  `amount` işaretlidir (giden eksi); `date` milisaniyelidir, kesir basamağı değişkendir.
- **`transactionReference` tekil değildir**: tek işlemin birden çok bacağı (v2'de üç bacaklı bir
  altın işlemi) aynı referansı ve `transactionId`yi paylaşır. Çağrılar arasında kararlıdır.
  Kaydı tekil yapan `(transactionId, seqNum)` çiftidir; v3'te aynı değer `businessKey` adıyla
  gelir. Mükerrer eleme bu çiftle yapılmalıdır.
- **Karşı tarafın IBAN'ı için alan yoktur.** v3'teki `iban` hesabın kendi IBAN'ıdır; v2'de alan
  hiç yoktur.
- **Sandbox veriyi maskeler**: `description` her kayıtta kelimesi kelimesine `Açıklama`'dır;
  `senderTCKNorVKN` / `receiverTCKNorVKN` (ve v3'te `senderIdentityNumber`) hep boştur. Bu
  alanların canlıda dolu gelip gelmediği **sandbox'tan anlaşılamaz**.
- v3'ün gerçek alanları dokümandakinden farklıdır (`reqNum` yok; `businessKey`, `seqNum`,
  `transactionCode`, kimlik alanları var; `balance` kayıtların yarısından azında). Düzeltme
  `spec/overrides.json`'da.
- `tpp_accounts.receipt_v2` denenen iki harekette de boş döndü (`slipList` yok, `amount` `"0.0"`).
  `tpp_accounts.receipt_v1` ise üç farklı hareketle 404 "Path not found" verdi.
- Müşteri girişli uç noktalar arasında karşı tarafı tanıtan başka bir kaynak yok: yanıtında
  IBAN / kimlik geçen diğer uç (`donations.account_transactions_for_the_organization`) yalnızca
  bağış kuruluşları içindir (kuruluş kodu + şifre ister) ve oradaki IBAN yine kuruluşun kendi
  hesabıdır.
- Test müşterisinin 58 hesabından yalnızca ek no 1'de hareket vardı (diğer on hesap boş döndü).
- `tpp_accounts.account_list_v2` dokümandaki alanlarla döner. Para birimi `fxId` / `fxCode` ile
  gelir: TL `0`, USD `1`, EUR `19`, altın `24` / `ALT (gr)`, gümüş `26` / `GMS (gr)`,
  platin `27` / `PLT (gr)`.
- **Refresh token her yenilemede değişir** (rotasyon); kütüphane yenisini depoya yazar. Depoya
  yazılamadan kaybolan bir yenileme, müşterinin yeniden giriş yapmasını gerektirir. 24 saatlik
  sürenin yenilemeyle uzayıp uzamadığı ölçülmedi.
- Sandbox uygulaması `account_activities` kapsamına yetkili değil (`invalid_scope`).

Bir isteğin sandbox'ta neden başarısız olduğunu anlamak için önce
`KUVEYTTURK_LOG=debug venv/bin/python examples/...` ile isteği ve yanıtı gör. Loglara yeni bir
alan eklerken sır sızdırmadığını `tests/test_logging.py`'deki gibi test et.

## Dokümanlar ve üreteç

- Doküman sitesi bir SPA; içerik `https://prep-kuveytturk-portalapi.kuveytturk.com.tr/api/v1/`
  altındaki JSON API'sinden Markdown olarak gelir (`get-document-menu`, `document/{id}`).
  `scripts/fetch_docs.py` bunu kullanır. Tarayıcıyla HTML kazımaya gerek yok.
- **Sunucu hızlı/paralel istekleri IP bazında engelliyor** ve engel sandbox dahil tüm
  `*.kuveytturk.com.tr` adreslerini kapsıyor. 4 paralel istekle ~130 sayfa çekmek bunu tetikledi ve
  engel yaklaşık iki saat sürdü. Belirtisi bir hata mesajı değil: sunucu TLS el sıkışmasında
  bağlantıyı sıfırlıyor (`curl: (35) Recv failure: Connection reset by peer`, HTTP yanıtı yok).
  İstekleri tek tek ve 4 sn arayla at (bu tempo sorunsuz çalıştı); engellenince ısrar etme, seyrek
  yokla. IP değiştirerek engeli aşmaya çalışma.
- `fetch_docs.py` önem sırasıyla indirir (yetkilendirme -> hesaplar/transferler -> diğer müşteri
  işlemleri -> ... -> şube/ATM gibi bilgi servisleri ve kurum içi servisler en son). Kullanıcı bu
  sırayı özellikle istedi; `PRIORITY` / `LAST` listelerini değiştirirken koru.
- Başlık tablosunda `Active | false` yazan sayfalar sunucudan kaldırılmış eski uç noktalardır
  (ör. `/v1/transfers/ToIBAN` -> 404 "Path not found"); kataloğa alınmaz.
- Doküman yanlışsa gerçeği sandbox'tan öğrenmenin güvenli yolu: uç noktaya **boş gövde** (`{}`)
  göndermek; API zorunlu alanları doğrulama hatası olarak listeler (para transferinin gerçek
  alanları — `receiverIban`, `corporateWebUserName` — böyle bulundu). Dolu/geçerli gövdeyle para
  hareketi yapan bir uç noktayı deneme amaçlı çağırma; onu kullanıcı çalıştırır.
- Dokümanlar elle yazılmış ve hatalı olabilir (yanlış akış/kapsam, eksik parametre, başka uç
  noktadan kopyalanmış gövde). Düzeltmeler koda değil `spec/overrides.json`'a yazılır. Her üretilen
  metot bu yüzden `extra_query` / `extra_body` / `request_options` kabul eder; hiçbir karşılığı
  olmayan uç nokta için `kt.request()` vardır.
- Gövde tablolarında iç içe alanlar düz listelenir; hangi alanın üst düzey olduğu örnek JSON'dan
  çıkarılır ve `{"request": {"contract": {...}}}` gibi tek anahtarlı sarmalayıcılar açılır
  (`body_wrap`). Ayrıntı: `scripts/build_spec.py::build_body`.

## Sırlar ve kişisel bilgiler

- Kullanıcı e-posta adresinin hiçbir yerde görünmesini istemiyor: `pyproject.toml` yazar
  bilgisine, README'ye, örneklere ya da commit'lere e-posta yazma. Bu repoda commit'ler GitHub
  noreply adresiyle atılır (repo-yerel `git config user.email`).

- Sandbox uygulama bilgileri `.env`'de, imza anahtarı `.secrets/private_key.pem`'de, test müşteri
  bilgileri `.secrets/test_customers.txt`'de. Hepsi `.gitignore`'da; **asla commit etme, koda ya
  da teste gömme, çıktıya yazdırma**.
- sdist içeriği `pyproject.toml`'da `only-include` ile sınırlı. Yayından önce
  `tar tzf dist/*.tar.gz` ile içerikte sır olmadığını doğrula.
- `.legacy/` eski deneme kodlarını ve eski doküman kazımalarını tutar (git'e girmez); içinde
  gömülü sırlar var. Kullanılmıyor, kullanıcı isterse silinebilir.

## Uç noktaların ortamlarda denenmesi

- `spec/test_status.json`: her uç noktanın (doküman id'siyle) `sandbox` ve `canli` test durumu
  (`test edildi` | `kısmen test edildi` | `test edilmedi`, sonuç, tarih, maskelenmiş ayrıntı).
  Doküman sitesindeki "Test durumu" sayfası ve uç nokta sayfalarındaki tablolar buradan üretilir.
- `scripts/check_endpoints.py [--environment production]` dosyayı günceller. **Yalnızca**
  betikteki `READ_ONLY` listesinde elle onaylanmış okuma uç noktalarını çağırır; para hareketi,
  ödeme, başvuru, kayıt oluşturma/iptal, bildirim ya da SMS gönderen uç noktalara asla istek
  atmaz. Listeye bir uç nokta eklemeden önce dokümanını oku; `tests/test_check_endpoints.py`
  işlem yapan adları listeye karşı denetler. Müşteri girişi isteyen uçlar çağrılmaz.
- Betik yalnızca çağırdığı uçların kaydını değiştirir; elle girilen kayıtlar (ör. müşteri
  girişiyle yapılan testler, canlı testler) korunur. Dosyayı değiştirince `generate.py` çalıştır.
- Canlı ortamda (Go Live sonrası) aynı betik `--environment production` ile çalıştırılır.
- Elle yapılan testler `scripts/record_test.py METOT --durum ... --sonuc ... [--environment production]`
  ile işlenir (doküman sayfalarını da üretir). Para transferi, döviz/altın alım-satımı, ödeme gibi
  işlem yapan uçları Claude çalıştırmaz (sandbox'ta da); kullanıcı çalıştırır, sonucu bu araçla işler.

## Testler

- Birim testleri `httpx.MockTransport` ile çalışır (`tests/conftest.py::Recorder`); ağa çıkmaz.
- `tests/test_generated.py` katalogdaki her uç nokta için üretilen metodun doğru isteği
  kurduğunu ve imzanın gönderilen baytlarla eşleştiğini doğrular; ayrıca üretilen dosyaların
  güncel olduğunu (`generate.py --check`) denetler.
- `tests/test_examples.py` örnek uygulamaları dokümandaki örnek yanıtlarla çalıştırır. Uç nokta
  adları (özellikle `spec/overrides.json`'daki adlar) değişirse örnekler ve README de güncellenir.
- `tests/test_web_app.py` web uygulamasını Flask test istemcisiyle uçtan uca sınar (Flask yoksa
  atlanır). Girişin banka sayfasındaki adımı (müşteri no + parola) otomatik denenemez; onu
  kullanıcı tarayıcıda yapar.
- Para hareketi yapan örnekler varsayılan olarak deneme modunda çalışır (`--execute` olmadan
  istek atmaz); bu davranışı koru. Dokümanda olmayan gövde alanlarını tahminle ekleme.
- Canlı testler (`-m live`) yalnızca `KUVEYTTURK_LIVE=1` iken çalışır ve `.env` ister. Yalnızca
  okuma yapan uç noktaları çağırır; para hareketi yapan uç noktalar canlı testlere eklenmez.
  Sandbox'ta `.env`'deki uygulama client credentials ile `accounts`, `public`, `transfers`
  kapsamlarında çalışıyor (hareketi olan test hesabı: ek no 5).

## Yayın

Paket PyPI'da `kuveytturk-api` adıyla yayınlanır. Repo public (2026-10-03); eski geçmişi taşıyan
private `kuveytturk-api-eski` reposu yalnızca arşivdir, oraya bir şey gönderme. Yükleme, PyPI
Trusted Publishing ile `.github/workflows/publish.yml` üzerinden yapılır; token yoktur.

1. `src/kuveytturk_api/_version.py` ve `CHANGELOG.md` güncellenir (sürüm + tarih).
2. `pytest`, `ruff`, `mypy`, `generate.py --check` temiz; `main` dalında CI yeşil olmalı.
3. `python -m build`, `twine check --strict dist/*`; sdist içinde sır ve `apidocs/` olmadığına bak.
4. `gh release create vX.Y.Z` -> iş akışı etiketin sürümle eşleştiğini doğrulayıp yükler.
   **Geri alınamaz** (bir sürüm numarası PyPI'da bir kez kullanılır); release'i oluşturmadan önce
   kullanıcıdan açık onay al.
5. Yayından sonra temiz bir ortamda `pip install kuveytturk-api==X.Y.Z` ile doğrula.
