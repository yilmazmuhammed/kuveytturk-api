# Uç nokta listesi

Kütüphanedeki 116 uç nokta, 16 kaynak altında. Bu dosya
`scripts/generate.py` tarafından üretilir; elle düzenlemeyin.

Akış sütunu: **CC** = client credentials (token otomatik alınır), 
**AC** = authorization code (müşteri girişi gerekir).

| Kaynak | Açıklama | Uç nokta |
| - | - | - |
| [`kt.accounts`](#ktaccounts) | Hesap yönetimi (kurumun kendi hesapları) | 6 |
| [`kt.cards`](#ktcards) | Kredi kartı işlemleri | 3 |
| [`kt.cash_management`](#ktcashmanagement) | Nakit yönetimi | 17 |
| [`kt.donations`](#ktdonations) | Bağışlar | 4 |
| [`kt.ecommerce`](#ktecommerce) | E-ticaret | 10 |
| [`kt.financing`](#ktfinancing) | Finansman çözümleri | 4 |
| [`kt.fx`](#ktfx) | Döviz işlemleri | 5 |
| [`kt.hgs`](#kthgs) | HGS servisleri | 3 |
| [`kt.information`](#ktinformation) | Bilgi servisleri (şube, ATM, parametre sorguları...) | 1 |
| [`kt.other`](#ktother) | Diğer | 2 |
| [`kt.payment_solutions`](#ktpaymentsolutions) | Ödeme çözümleri | 14 |
| [`kt.payments`](#ktpayments) | Ödemeler | 14 |
| [`kt.tpp_accounts`](#kttppaccounts) | Hesap yönetimi (TPP - müşteri adına) | 5 |
| [`kt.transfers`](#kttransfers) | Para transferleri | 8 |
| [`kt.treasury`](#kttreasury) | Hazine servisleri (kıymetli maden, kur) | 5 |
| [`kt.vpos`](#ktvpos) | Sanal POS | 15 |

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

## kt.donations

Bağışlar

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`campaign_list_for_organization`](https://developer.kuveytturk.com.tr/documentation/donations/campaign-list-for-organization) | `POST /v1/donations/campaignList` | donations | AC |
| [`donation_list_for_organization`](https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization) | `POST /v1/donations/donationList` | donations | CC |
| [`donation_list_for_organization_tdv`](https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization-tdv) | `POST /v1/donations/donationListTdv` | donations | CC |
| [`external_payments_list`](https://developer.kuveytturk.com.tr/documentation/donations/external-payments-list) | `POST /v1/donations/externalPayments` | donations | AC |

## kt.ecommerce

E-ticaret

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`ecommerce_application_refund_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund) | `POST /v1/lendings/{applicationId}/refund` | digital_payments | CC |
| [`ecommerce_application_refund_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund) | `POST /v1/lendings/{applicationId}/refund` | digital_payments | CC |
| [`ecommerce_get_lending_information_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information) | `GET /v1/lendings/{applicationId}` | digital_payments | CC |
| [`ecommerce_get_lending_information_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information) | `GET /v1/lendings/{applicationId}` | digital_payments | CC |
| [`ecommerce_lendings_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings) | `POST /v1/lendings` | digital_payments | CC |
| [`ecommerce_lendings_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings) | `POST /v1/lendings` | digital_payments | CC |
| [`ecommerce_monthly_payments_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments) | `POST /v1/query/monthly-payments` | digital_payments | CC |
| [`ecommerce_monthly_payments_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments) | `POST /v1/query/monthly-payments` | digital_payments | CC |
| [`ecommerce_pre_approved_monthly_payments_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments) | `POST /v1/query/pre-approved-monthly-payments` | digital_payments | CC |
| [`ecommerce_pre_approved_monthly_payments_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments) | `POST /v1/query/pre-approved-monthly-payments` | digital_payments | CC |

## kt.financing

Finansman çözümleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`corporate_credit_card_application`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-credit-card-application) | `POST /v2/corporateCreditCardApplication` | cards | CC |
| [`customer_suited_card_list`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-suited-card-list) | `GET /v2/customerSuitedCardList` | cards | CC |
| [`get_digital_channel_card_application_list_v2`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/get-digital-channel-card-application-list-v2) | `GET /v2/cardApplicationList` | cards | CC |
| [`individual_credit_card_application_v2`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-credit-card-application-v2) | `POST /v2/individualCreditCardApplication` | cards | CC |

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
| [`hgs_product_information`](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-product-information) | `POST /v1/hgs/product-info` | public | CC |
| [`hgs_usage_transactions`](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-usage-transactions) | `POST /v1/hgs/usage-transactions` | public | CC |

## kt.information

Bilgi servisleri (şube, ATM, parametre sorguları...)

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`central_notification`](https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification) | `POST /v1/notification/sendInfEng` | public | CC |

## kt.other

Diğer

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`money_transfer_report_for_kuveyt_turk_investment_securities_inc`](https://developer.kuveytturk.com.tr/documentation/other/money-transfer-report-for-kuveyt-turk-investment-securities-inc) | `POST /v1/investment/report-for-account-activities` | transfers | CC |
| [`virtual_card_limit_update`](https://developer.kuveytturk.com.tr/documentation/other/virtual-card-limit-update) | `POST /v1/cards/virtualcardlimitupdate` | cards | AC |

## kt.payment_solutions

Ödeme çözümleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`digital_payment_get_token`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-get-token) | `POST /v1/vpos/digitalPaymentGetToken` | digital_payments | CC |
| [`digital_payment_query`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-query) | `POST /v1/vpos/digitalPaymentQuery` | digital_payments | CC |
| [`digital_payment_refund`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-refund) | `POST /v1/vpos/digitalPaymentDoRefund` | digital_payments | CC |
| [`digital_payment_send_document`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-send-document) | `POST /v1/vpos/sendDocument` | digital_payments | CC |
| [`pos_merchant_number_list`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-merchant-number-list) | `GET /v1/pos/merchant-number` | public | CC |
| [`pos_transaction_details_for_tpp_v2`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-for-tpp-third-party-provider-v2) | `POST /v2/pos/detail-transactions` | cards | AC |
| [`pos_transaction_details_v3`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-v3) | `POST /v3/pos/detail-transactions` | cards | CC |
| [`pos_transactions_summary_v3`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transactions-summary-v3) | `POST /v3/pos/transactions` | cards | CC |
| [`send_order_distribution_detail_v2`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/send-order-distribution-detail-v2) | `POST /v3/purchase/orderdistribution` | payments | CC |
| [`virtual_pos`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos) | `POST /v1/vpos` | cards | CC |
| [`virtual_pos_end_day_all_list`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-enddayall-list) | `POST /v1/vpos/endDayAllList` | cards | AC |
| [`virtual_pos_end_of_day`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-endofday) | `POST /v1/vpos/endOfDay` | cards | AC |
| [`virtual_pos_general_transaction`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-general-transaction) | `POST /v1/vpos/transaction` | cards | AC |
| [`virtual_pos_order_filter`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-order-filter) | `POST /v1/vpos/orderFilter` | cards | AC |

## kt.payments

Ödemeler

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`account_validation_by_account_number_for_group_money_transfer`](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-account-number-for-group-money-transfer) | `POST /v1/groupmoneytransfer/accountvalidation` | intrabank_money_transfers | CC |
| [`account_validation_by_iban_for_group_money_transfer`](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer) | `POST /v1/groupmoneytransfer/account` | intrabank_money_transfers | CC |
| [`account_validation_by_iban_for_group_money_transfer_v2`](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer-v2) | `POST /v2/groupmoneytransfer/account` | intrabank_money_transfers | CC |
| [`cancel_money_transfers_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/cancel-money-transfers-from-ktbank-to-kuveyt-turk) | `POST /v1/groupmoneytransfer/incomingtransfer/cancellist` | intrabank_money_transfers | CC |
| [`check_money_transfers_status_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/check-money-transfers-status-from-ktbank-to-kuveytturk) | `POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist` | intrabank_money_transfers | AC |
| [`insert_money_transfers_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/insert-money-transfers-from-kt-bank-to-kuveyt-turk) | `POST /v1/groupmoneytransfer/incomingtransfer/insertlist` | intrabank_money_transfers | CC |
| [`invoice_company_list`](https://developer.kuveytturk.com.tr/documentation/payments/invoice-company-list) | `GET /v1/invoices/companies` | payments | AC |
| [`kt_bank_error_message_list`](https://developer.kuveytturk.com.tr/documentation/payments/kt-bank-error-message-list) | `GET /v1/groupmoneytransfer/errormessagelist` | intrabank_money_transfers | CC |
| [`kuveyt_turk_branch_list_for_group_money_transfer`](https://developer.kuveytturk.com.tr/documentation/payments/kuveyt-turk-branch-list-for-group-money-transfer) | `GET /v1/groupmoneytransfer/branchlist` | intrabank_money_transfers | CC |
| [`return_money_transfers_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/return-money-transfers-from-ktbank-to-kuveyt-turk) | `POST /v1/groupmoneytransfer/incomingtransfer/returnlist` | intrabank_money_transfers | CC |
| [`send_multiple_invoice_v2`](https://developer.kuveytturk.com.tr/documentation/payments/send-multiple-invoice-v2) | `POST /v2/purchase/multipleinvoice` | payments | CC |
| [`send_offer_vendor_detail`](https://developer.kuveytturk.com.tr/documentation/payments/send-offer-vendor-detail) | `POST /v1/purchase/offervendor` | payments | CC |
| [`send_order_distribution_detail`](https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail) | `POST /v1/purchase/orderdistribution` | payments | CC |
| [`send_order_distribution_detail_v2`](https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail-v2) | `POST /v3/purchase/orderdistribution` | payments | CC |

## kt.tpp_accounts

Hesap yönetimi (TPP - müşteri adına)

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`account_list_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-list-v2) | `GET /v2/accounts` | accounts | AC |
| [`account_list_with_suffix_v2`](https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-ucuncu-taraf-yazilim/ek-no-ile-hesap-listesi-v2) | `GET /v2/accounts/{suffix}` | accounts | AC |
| [`account_transactions_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-transactions-v2) | `GET /v2/accounts/{suffix}/transactions` | accounts | AC |
| [`receipt_v1`](https://developer.kuveytturk.com.tr/documentation/other/receipt) | `GET /v1/accounts/{suffix}/transactions/{businessKey}` | accounts | AC |
| [`receipt_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/receipt-v2) | `POST /v2/accounts/transactions/receipts` | accounts | AC |

## kt.transfers

Para transferleri

| Metot | İstek | Kapsam | Akış |
| - | - | - | - |
| [`customer_iban_info_for_money_transfer`](https://developer.kuveytturk.com.tr/documentation/money-transfers/customer-iban-info-for-money-transfer) | `GET /v1/moneytransfer/{iban}/customeribaninfo` | transfers | CC |
| [`internal_money_transfer`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-veeraman) | `POST /v1/moneytransfer/interbankmoneytransfer` | transfers | CC |
| [`money_transfer_payment_type`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-payment-type) | `POST /v1/moneytransfer/paymenttype` | transfers | CC |
| [`money_transfer_state`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-state) | `GET /v1/moneytransfer-state` | transfers | CC |
| [`money_transfer_to_gsm`](https://developer.kuveytturk.com.tr/documentation/other/money-transfer-to-gsm) | `POST /v1/transfers/toGSM` | transfers | AC |
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
| [`add_card_to_merchant_safe`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/addcardtomerchantsafe) | `POST /v1/vpos/addCardToMerchantSafe` | public | CC |
| [`digital_payment_commission_reconciliation`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/digital-payment-commission-reconciliation) | `POST /v1/vpos/commissionReconciliation` | digital_payments | CC |
| [`get_customer_by_safe_key`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/getcustomerbysafekey) | `POST /v1/vpos/getCustomerBySafeKey` | public | CC |
| [`get_seller_order_details`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/get-seller-order-details) | `POST /v1/vpos/getMerchantOrderDetail` | public | CC |
| [`non_3_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/non-3d-payment) | `POST /v1/vpos/non3DPayment` | public | CC |
| [`non_three_d_payment_by_merchant_safe`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/nonthreedpaymentbymerchantsafe) | `POST /v1/vpos/nonThreeDPaymentByMerchantSafe` | public | CC |
| [`order_detail_with_payment_id`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/order-detail-with-payment-id) | `POST /v1/vpos/orderDetailWithPaymentId` | public | CC |
| [`payment_order_reversal`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/paymentorderreversal) | `POST /v1/vpos/paymentOrderReversal` | public | CC |
| [`pre_authorization`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/preauthorization) | `POST /v1/vpos/preAuthorization` | public | CC |
| [`recurring_non_three_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/recurringnonthreedpayment) | `POST /v1/vpos/recurringNonThreeDPayment` | public | CC |
| [`sale_order_reversal`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/saleorderreversal) | `POST /v1/vpos/saleOrderReversal` | public | CC |
| [`secure_partner_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/secure-partner-payment) | `POST /v1/vpos/secureCommonPaymentToken` | public | CC |
| [`threee_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/threeed-payment) | `POST /v1/vpos/threeDPayment` | public | CC |
| [`virtual_pos_non_three_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/virtual-pos-nonthreed-payment-masked-card) | `POST /v1/vpos/nonThreeDPayment` | cards | CC |
| [`virtual_pos_sale_reversal`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/virtual-pos-sale-reversal-masked) | `POST /v1/vpos/saleReversal` | cards | CC |
