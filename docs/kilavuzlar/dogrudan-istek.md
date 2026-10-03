# Doğrudan istek ve kaçış yolları

Hazır metotlar API Market dokümanından üretilir. Doküman eksik ya da yanlış olduğunda
kullanabileceğiniz üç kaçış yolu vardır.

## Fazladan parametre: `extra_query`, `extra_body`

Her metot, dokümanda olmayan alanları göndermenize izin verir:

```python
kt.accounts.account_list_v3(extra_query={"belgelenmemisParametre": 1})
kt.transfers.outgoing_money_transfer(..., extra_body={"yeniAlan": "değer"})
```

## Çağrıya özel ayarlar: `request_options`

```python
kt.accounts.account_list_v3(request_options={
    "timeout": 60,                       # saniye
    "flow": "authorization_code",        # dokümandaki akışı ezer
    "scope": "accounts",                 # dokümandaki kapsamı ezer
    "user": "musteri-42",                # hangi müşterinin token'ı kullanılsın
    "token": "hazir-access-token",       # token yönetimini tamamen atla
    "headers": {"X-Izleme": "abc"},      # ek başlık
    "raise_on_failure": False,           # success: false yanıtında istisna fırlatma
})
```

## Herhangi bir uç nokta: `kt.request()`

Kütüphanede karşılığı olmayan bir uç noktayı doğrudan çağırabilirsiniz; token ve imza yine
otomatik eklenir:

```python
kt.request(
    "GET",
    "/v4/accounts/{suffix}/transactions",
    scope="accounts",
    path_params={"suffix": 1},
    query={"itemCount": 10},
)

kt.post("/v1/ornek", scope="public", body={"alan": "değer"})
kt.get("/v2/accounts", scope="accounts", flow="authorization_code")
```

Sorgu ve gövde kütüphane tarafından bir kez kodlanır ve imzalanan baytlar gönderilen baytlarla
birebir aynıdır; `None` değerli sorgu parametreleri gönderilmez.
