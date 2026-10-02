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
| [`money_transfer.py`](money_transfer.py) | Bir IBAN'a para transferi ve durum sorgulama | CC |
| [`async_usage.py`](async_usage.py) | Asenkron istemciyle eşzamanlı istekler | CC |
| [`web_app_flow.py`](web_app_flow.py) | Web uygulamasında müşteri girişi iskeleti | AC |

**CC** (client credentials): ek adım gerekmez. **AC** (authorization code): ilk çalıştırmada
tarayıcı açılır ve müşteri girişi istenir; bunun için uygulamanızın Redirect URI'si
`http://localhost:PORT/...` olmalıdır. Sandbox'ta giriş için geliştirici portalındaki test
müşterilerini kullanın. Alınan token `.kuveytturk/tokens.json` dosyasında saklanır.

## Para transferi hakkında

```bash
python examples/money_transfer.py send --from-suffix 1 --iban TR... --amount 10.50 \
    --corporate-user KULLANICI --description "Deneme"
```

`money_transfer.py` önce IBAN'ı yerel olarak doğrular, bankadan alıcının (maskeli) adını ve
bankasını sorgular ve gönderilecek isteği gösterir. Varsayılan olarak **transfer göndermez**;
gerçekten göndermek için `--execute` gerekir ve onay sorulur. Canlı ortamda ayrıca
`--allow-production` ister.

`--corporate-user`, işlemi yapan kurumsal internet şubesi kullanıcı adıdır
(`KUVEYTTURK_CORPORATE_USER` ortam değişkeninden de okunur).

Resmî dokümandaki parametre listesi eksik: `receiverIban` ve `corporateWebUserName` dokümanda
yok, ama API bunları zorunlu tutuyor (sandbox'ın doğrulama hatalarından tespit edildi).
Transferin kendisi otomatik testlerde gerçek sandbox'a karşı çalıştırılmadı; ilk kullanımda
sandbox'ta `--execute` ile deneyin.
