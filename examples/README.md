# Örnek uygulamalar

Hepsi proje kökündeki `.env` dosyasını okur (`.env.example` dosyasını kopyalayıp doldurun) ve
proje kökünden çalıştırılır:

```bash
pip install -e .
python examples/account_list.py
```

| Dosya | Ne yapar | Akış |
| - | - | - |
| [`account_list.py`](account_list.py) | Hesap listesi (`--customer` ile müşteri girişiyle) | CC / AC |
| [`account_transactions.py`](account_transactions.py) | Bir hesabın hareketleri, `--receipt` ile son hareketin dekontu | CC / AC |
| [`exchange_rates.py`](exchange_rates.py) | Döviz ve kıymetli maden kurları | CC |
| [`iban_lookup.py`](iban_lookup.py) | IBAN'ın sahibini ve bankasını sorgular | CC |
| [`money_transfer.py`](money_transfer.py) | Hesaptan hesaba para transferi ve durum sorgulama | CC |
| [`async_usage.py`](async_usage.py) | Asenkron istemciyle eşzamanlı istekler | CC |
| [`web_app_flow.py`](web_app_flow.py) | Web uygulamasında müşteri girişi iskeleti | AC |

**CC** (client credentials): ek adım gerekmez. **AC** (authorization code): ilk çalıştırmada
tarayıcı açılır ve müşteri girişi istenir; bunun için uygulamanızın Redirect URI'si
`http://localhost:PORT/...` olmalıdır. Sandbox'ta giriş için geliştirici portalındaki test
müşterilerini kullanın. Alınan token `.kuveytturk/tokens.json` dosyasında saklanır.

## Para transferi hakkında

`money_transfer.py` varsayılan olarak **hiçbir şey göndermez**; yalnızca gönderilecek isteği
gösterir. Gerçekten göndermek için `--execute` gerekir ve onay sorulur; canlı ortamda ayrıca
`--allow-production` ister.

Güncel API dokümanında transfer isteği alıcıyı hesap numarası ve ek no ile tanımlıyor; alıcıyı
IBAN ile belirten alanlar dokümanda yer almıyor. Bu yüzden örnek IBAN'a transfer yapmaz.
`iban_lookup.py` ile bir IBAN'ın sahibini ve bankasını doğrulayabilirsiniz.
