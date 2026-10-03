# Yetkilendirme

API Market iki OAuth2 akışı kullanır. Her uç noktanın hangi akışı ve hangi kapsamı (scope)
istediği dokümanda yazar; kütüphane bunu bilir ve doğru token'ı kendisi seçer.

| | Client credentials | Authorization code |
| - | - | - |
| Kim adına | Uygulamanın (kurumun) kendisi | Giriş yapan müşteri |
| Giriş ekranı | Yok | Müşteri bankanın sayfasında giriş yapar |
| Sizin yapmanız gereken | Hiçbir şey | Müşteriyi yönlendirmek, callback'i karşılamak |
| Örnek uç nokta | `kt.accounts.account_list_v3()` | `kt.tpp_accounts.account_list_v2()` |
| Token süresi | 1 saat, otomatik yenilenir | Access 1 saat, refresh 24 saat |

## Client credentials

Ek bir adım gerekmez:

```python
kt = KuveytTurk.from_env(".env")
hesaplar = kt.accounts.account_list_v3()
```

İstemci ilk çağrıda `accounts` kapsamı için token alır, bellekte saklar ve süresi dolmadan
yeniler. Her kapsam için ayrı token alınır.

!!! question "Kimse giriş yapmadıysa hangi hesaplar dönüyor?"
    Bu akışta dönen veriler, **API Market uygulamanızın bağlı olduğu müşteriye** aittir.
    Sandbox'ta bu, portalın uygulamanıza atadığı test kurumsal müşterisidir; canlıda API'yi
    kullanan kurumun kendisidir. Başka bir müşterinin verisine bu akışla erişilemez.

Uygulamanız bir kapsama yetkili değilse token alınamaz ve
`AuthenticationError` fırlatılır (`invalid_scope`). Portalda uygulamanıza ilgili API ürününü
eklemeniz gerekir.

## Authorization code (müşteri girişi)

Müşteri bankanın sayfasında oturum açıp uygulamanıza izin verir; banka tarayıcıyı bir `code`
ile sizin Redirect URI'nize geri yollar; siz bu kodu token'a çevirirsiniz.

### Betikler ve geliştirme: `login()`

Redirect URI'niz `http://localhost:PORT/...` biçimindeyse tek satır yeter. Tarayıcı açılır, o
portta geçici bir sunucu callback'i yakalar ve token alınır:

```python
from kuveytturk_api import FileTokenStore, KuveytTurk

kt = KuveytTurk.from_env(".env", token_store=FileTokenStore(".kuveytturk/tokens.json"))

if kt.auth.get_user_token() is None:
    kt.auth.login(["accounts", "offline_access"])

hesaplar = kt.tpp_accounts.account_list_v2()
```

`offline_access` kapsamı refresh token verilmesini sağlar. `FileTokenStore` sayesinde betiği
yeniden çalıştırdığınızda tekrar giriş istenmez (refresh token geçerli olduğu sürece).

Sandbox'ta giriş için geliştirici portalındaki test müşterilerini kullanın; giriş sonrası
istenen tek kullanımlık şifre için 6 haneli herhangi bir kod kabul edilir.

### Web uygulamaları

Yönlendirmeyi ve callback'i kendi rotalarınızda yaparsınız:

```python
# 1) Kullanıcıyı bankaya yönlendirin
state = kt.auth.new_state()                      # oturumda saklayın
url = kt.auth.authorization_url(["accounts", "offline_access"], state=state)

# 2) Redirect URI'nize dönen istekte
code = kt.auth.parse_callback(request_url, state=state)
kt.auth.exchange_code(code, user="musteri-42")   # token bu anahtarla saklanır

# 3) O müşteri adına çağrı yapın
hesaplar = kt.as_user("musteri-42").tpp_accounts.account_list_v2()
```

`state`, callback'in gerçekten sizin başlattığınız girişe ait olduğunu doğrular (CSRF koruması);
`parse_callback` uyuşmazlıkta `AuthenticationError` fırlatır. Çalışan tam bir örnek:
[Web uygulamasında müşteri girişi](kilavuzlar/web-uygulamasi.md).

### Token'ın ömrü

- Access token 1 saat geçerlidir. Süresi dolduğunda kütüphane refresh token ile yenisini alır;
  sizin bir şey yapmanız gerekmez.
- Refresh token 24 saat geçerlidir ve **her yenilemede değişir**. Kütüphane yenisini depoya
  yazar. Bu yüzden kalıcı bir depo kullanıyorsanız yazma işleminin güvenilir olması önemlidir:
  yeni refresh token kaydedilemeden kaybolursa müşterinin yeniden giriş yapması gerekir.
- Yenileme mümkün değilse `AuthorizationRequiredError` fırlatılır; müşteriyi yeniden giriş
  akışına yönlendirin.

## Çok kullanıcılı kullanım: `as_user()`

Müşteri token'ları bir kullanıcı anahtarıyla saklanır. `kt.as_user("anahtar")`, o müşterinin
token'ını kullanan hafif bir istemci görünümü döndürür; bağlantıları ve token deposunu ana
istemciyle paylaşır.

```python
kt.auth.exchange_code(code, user="ali")
kt.auth.exchange_code(baska_kod, user="veli")

kt.as_user("ali").tpp_accounts.account_list_v2()    # Ali'nin hesapları
kt.as_user("veli").tpp_accounts.account_list_v2()   # Veli'nin hesapları
```

Anahtar verilmezse `"default"` kullanılır; tek kullanıcılı betiklerde bunu düşünmeniz gerekmez.

## Token'ları saklamak

Token'lar varsayılan olarak yalnızca süreç belleğinde tutulur.

| Depo | Ne zaman |
| - | - |
| `MemoryTokenStore` (varsayılan) | Yalnızca client credentials kullanan ya da kısa ömürlü süreçler |
| `FileTokenStore("yol.json")` | Betikler ve masaüstü araçları; dosya `0600` izinleriyle yazılır |
| Kendi deponuz | Web uygulamaları, birden çok süreç ya da sunucu |

Kendi deponuz için üç metot yeterlidir:

```python
from kuveytturk_api import Token

class RedisTokenStore:
    def __init__(self, redis):
        self.redis = redis

    def get(self, key: str) -> Token | None:
        raw = self.redis.get(f"kt:{key}")
        return Token.from_dict(json.loads(raw)) if raw else None

    def set(self, key: str, token: Token) -> None:
        self.redis.set(f"kt:{key}", json.dumps(token.to_dict()))

    def delete(self, key: str) -> None:
        self.redis.delete(f"kt:{key}")

kt = KuveytTurk.from_env(token_store=RedisTokenStore(redis_client))
```

Anahtarlar `client:<kapsam>` (uygulama token'ları) ve `user:<kullanıcı>` (müşteri token'ları)
biçimindedir. Token'lar hesaba erişim sağlar; şifreli saklayın ve loglara yazmayın.

## Bir çağrıda akışı ya da token'ı değiştirmek

Doküman bir uç noktanın akışını yanlış belirtmişse ya da elinizde hazır bir token varsa
`request_options` ile ezebilirsiniz:

```python
kt.accounts.account_list_v3(request_options={"flow": "authorization_code", "user": "ali"})
kt.accounts.account_list_v3(request_options={"token": "hazir-access-token"})
```

Ayrıntı: [Doğrudan istek ve kaçış yolları](kilavuzlar/dogrudan-istek.md).
