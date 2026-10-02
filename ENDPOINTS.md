# Uç nokta listesi

Kütüphanedeki 56 uç nokta, 9 kaynak altında. Bu dosya
`scripts/generate.py` tarafından üretilir; elle düzenlemeyin.

Akış sütunu: **CC** = client credentials (token otomatik alınır), 
**AC** = authorization code (müşteri girişi gerekir).

| Kaynak | Açıklama | Uç nokta |
| - | - | - |
| [`kt.accounts`](#ktaccounts) | Hesap yönetimi (kurumun kendi hesapları) | 6 |
| [`kt.cards`](#ktcards) | Kredi kartı işlemleri | 3 |
| [`kt.cash_management`](#ktcashmanagement) | Nakit yönetimi | 17 |
| [`kt.fx`](#ktfx) | Döviz işlemleri | 5 |
| [`kt.hgs`](#kthgs) | HGS servisleri | 1 |
| [`kt.tpp_accounts`](#kttppaccounts) | Hesap yönetimi (TPP - müşteri adına) | 4 |
| [`kt.transfers`](#kttransfers) | Para transferleri | 7 |
| [`kt.treasury`](#kttreasury) | Hazine servisleri (kıymetli maden, kur) | 5 |
| [`kt.vpos`](#ktvpos) | Sanal POS | 8 |

## kt.accounts

Hesap yönetimi (kurumun kendi hesapları)

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`account_list_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-v3) | `GET /v3/accounts` | accounts | CC |
| [`account_list_with_suffix_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-with-suffix-v3) | `GET /v3/accounts/{suffix}` | accounts | CC |
| [`account_transactions_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v3) | `GET /v3/accounts/{suffix}/transactions` | accounts | CC |
| [`account_transactions_v4_detail`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v4-detail) | `GET /v4/accounts/{suffix}/transactions` | accounts | CC |
| [`pdf_receipt_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/pdf-receipt-v3) | `POST /v3/accounts/transactions/pdfReceipts` | accounts | CC |
| [`receipt_v3`](https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-hesaplariniz/dekont-v3) | `POST /v3/accounts/transactions/receipts` | accounts | CC |

## kt.cards

Kredi kartı işlemleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`credit_card_list_v3`](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-list-v3) | `GET /v3/creditcard/cardlist` | cards | CC |
| [`credit_card_money_transfer`](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-money-transfer) | `POST /v1/moneytransfer/creditcardmoneytransfer` | transfers | CC |
| [`credit_card_transactions_list_v3`](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-transactions-list-v3) | `GET /v3/creditcard/{cardnumber}/transactions` | cards | CC |

## kt.cash_management

Nakit yönetimi

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`cheque_information_micro`](https://developer.kuveytturk.com.tr/documentation/cash-management/cheque-information-micro) | `POST /v1/cheque-information-micro` | public | CC |
| [`dijital_bankacilik_iadesi`](https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-iadesi) | `POST /v1/vpos/digitalPaymentRefund` | digital_payments | CC |
| [`dijital_bankacilik_islem_durumu`](https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-islem-durumu) | `POST /v1/vpos/digitalPaymentStatus` | digital_payments | CC |
| [`dijital_bankacilik_odeme`](https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-odeme) | `POST /v1/vpos/digitalPayment` | digital_payments | CC |
| [`school_installment_payment_system_active_registration_inquiry_api`](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-payment-system-active-registration-inquiry-api) | `POST /v1/school-installment/registration-inquiry` | loans | CC |
| [`school_installment_system_registration_and_installment_cancellation_api`](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-registration-and-installment-cancellation-api) | `POST /v1/school-installment/cancelation` | loans | CC |
| [`school_installment_system_school_guaranteed_registration_payment`](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-school-guaranteed-registration-payment) | `POST /v1/school-installment/transaction-information` | loans | CC |
| [`supplier_financing_buyer_order_confirmation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-confirmation) | `POST /v1/supplierfinance/approvefrompurchaserer` | loans | CC |
| [`supplier_financing_buyer_order_listing`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-listing) | `POST /v1/supplierfinance/getorderbypurchaser` | loans | CC |
| [`supplier_financing_invoice_cancellation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-invoice-cancellation) | `POST /v1/supplychainfinance/cancelinvoice` | loans | CC |
| [`supplier_financing_order_last_approval_by_supplier`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-order-last-approval-by-supplier) | `POST /v1/supplierfinance/lastapprovefromsupplier` | loans | CC |
| [`supplier_financing_vendor_company_invoice_approval`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-company-invoice-approval) | `POST /v1/supplychainfinance/supplierapproveinvoice` | loans | CC |
| [`supplier_financing_vendor_invoice_listing`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-invoice-listing) | `POST /v1/supplychainfinance/supplierinvoicelist` | loans | CC |
| [`supplier_financing_vendor_order_cancellation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-cancellation) | `POST /v1/supplierfinance/cancelFromSupplier` | loans | CC |
| [`supplier_financing_vendor_order_confirmation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-confirmation) | `POST /v1/supplierfinance/lastapprovefromsupplierer` | loans | CC |
| [`supplier_financing_vendor_order_initiation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-initiation) | `POST /supplierfinance/saveordersupplier` | loans | CC |
| [`tedarikci_finansman_geri_odeme_plani_hesaplamasi`](https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/tedarikci-finansman-geri-odeme-plani-hesaplamasi) | `POST /v1/supplierfinance/getpaybackplan` | loans | CC |

## kt.fx

Döviz işlemleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`fx_currency_buy`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-buy) | `POST /v1/fx/buy` | public | CC |
| [`fx_currency_list`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-list) | `GET /v1/data/fecs` | public | CC |
| [`fx_currency_rates`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-rates) | `GET /v2/fx/rates` | public | CC |
| [`fx_currency_sell`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-sell) | `POST /v1/fx/sell` | public | CC |
| [`fx_transaction_history`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-transaction-history) | `POST /v1/fx/fxtransactions` | public | CC |

## kt.hgs

HGS servisleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`hgs_balance_information`](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-balance-information) | `POST /v1/hgs/balance-info` | public | CC |

## kt.tpp_accounts

Hesap yönetimi (TPP - müşteri adına)

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`account_list_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-list-v2) | `GET /v2/accounts` | accounts | AC |
| [`account_list_with_suffix_v2`](https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-ucuncu-taraf-yazilim/ek-no-ile-hesap-listesi-v2) | `GET /v2/accounts/{suffix}` | accounts | AC |
| [`account_transactions_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-transactions-v2) | `GET /v2/accounts/{suffix}/transactions` | accounts | AC |
| [`receipt_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/receipt-v2) | `POST /v2/accounts/transactions/receipts` | accounts | AC |

## kt.transfers

Para transferleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`customer_iban_info_for_money_transfer`](https://developer.kuveytturk.com.tr/documentation/money-transfers/customer-iban-info-for-money-transfer) | `GET /v1/moneytransfer/{iban}/customeribaninfo` | transfers | CC |
| [`internal_money_transfer`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-veeraman) | `POST /v1/moneytransfer/interbankmoneytransfer` | transfers | CC |
| [`money_transfer_payment_type`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-payment-type) | `POST /v1/moneytransfer/paymenttype` | transfers | CC |
| [`money_transfer_state`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-state) | `GET /v1/moneytransfer-state` | transfers | CC |
| [`outgoing_money_transfer`](https://developer.kuveytturk.com.tr/documentation/para-transferleri/para-transferi-havale-eft-fast-virman) | `POST /v1/moneytransfer/outgoingmoneytransfer` | transfers | CC |
| [`outgoing_money_transfer_v2`](https://developer.kuveytturk.com.tr/documentation/money-transfers/outgoing-money-transfer-v2) | `POST /v2/moneytransfer/outgoingmoneytransfer` | transfers | AC |
| [`transaction_validation_list`](https://developer.kuveytturk.com.tr/documentation/money-transfers/transaction-validation-list) | `GET /v1/transactionvalidation/transactionlist` | public | CC |

## kt.treasury

Hazine servisleri (kıymetli maden, kur)

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`fx_and_precious_metal_rates`](https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metal-rates) | `GET /v1/fx/rates` | public | CC |
| [`fx_and_precious_metals_transaction_history`](https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metals-transaction-history) | `POST /v1/fx/fxtransactions` | public | CC |
| [`precious_metal_buy`](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-buy) | `POST /v1/preciousmetal/buy` | public | CC |
| [`precious_metal_rates`](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-rates) | `GET /v1/preciousmetal/rates` | public | CC |
| [`precious_metal_sell`](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-sell) | `POST /v1/preciousmetal/sell` | public | CC |

## kt.vpos

Sanal POS

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`_3_d_secure_odeme`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/3d-secure-odeme) | `POST /v1/vpos/threeDPayment` | public | CC |
| [`dijital_odeme_komisyon_mutabakati`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/dijital-odeme-komisyon-mutabakati) | `POST /v1/vpos/commissionReconciliation` | digital_payments | CC |
| [`duzenli_non_three_d_odeme`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/duzenli-nonthreed-odeme) | `POST /v1/vpos/recurringNonThreeDPayment` | public | CC |
| [`gelen_odeme_iptali`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/gelen-odeme-iptali) | `POST /v1/vpos/paymentOrderReversal` | public | CC |
| [`isyeri_onayli_non_three_d_odeme`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/isyeri-onayli-nonthreed-odeme) | `POST /v1/vpos/nonThreeDPaymentByMerchantSafe` | public | CC |
| [`merchant_safe_icin_kart_ekleme`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/merchant-safe-icin-kart-ekleme) | `POST /v1/vpos/addCardToMerchantSafe` | public | CC |
| [`on_provizyon`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/on-provizyon) | `POST /v1/vpos/preAuthorization` | public | CC |
| [`satis_islemi_iptal`](https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/satis-islemi-iptal) | `POST /v1/vpos/saleOrderReversal` | public | CC |
