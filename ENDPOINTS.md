# Uç nokta listesi

Kütüphanedeki 192 uç nokta, 23 kaynak altında. Bu dosya
`scripts/generate.py` tarafından üretilir; elle düzenlemeyin.

Akış sütunu: **CC** = client credentials (token otomatik alınır), 
**AC** = authorization code (müşteri girişi gerekir). Sandbox / Canlı sütunları
`spec/test_status.json`'dan gelir (bkz. docs/uc-noktalar/test-durumu.md).

| Kaynak | Açıklama | Uç nokta |
| - | - | - |
| [`kt.accounts`](#ktaccounts) | Hesap yönetimi (kurumun kendi hesapları) | 8 |
| [`kt.architecht`](#ktarchitecht) | Architecht | 3 |
| [`kt.cards`](#ktcards) | Kredi kartı işlemleri | 4 |
| [`kt.cash_management`](#ktcashmanagement) | Nakit yönetimi | 17 |
| [`kt.credibility`](#ktcredibility) | Kredibilite | 5 |
| [`kt.donations`](#ktdonations) | Bağışlar | 5 |
| [`kt.ecommerce`](#ktecommerce) | E-ticaret | 10 |
| [`kt.financing`](#ktfinancing) | Finansman çözümleri | 16 |
| [`kt.fx`](#ktfx) | Döviz işlemleri | 5 |
| [`kt.hgs`](#kthgs) | HGS servisleri | 3 |
| [`kt.information`](#ktinformation) | Bilgi servisleri (şube, ATM, parametre sorguları...) | 12 |
| [`kt.moneygram`](#ktmoneygram) | MoneyGram | 6 |
| [`kt.other`](#ktother) | Diğer | 9 |
| [`kt.payment_solutions`](#ktpaymentsolutions) | Ödeme çözümleri | 15 |
| [`kt.payments`](#ktpayments) | Ödemeler | 15 |
| [`kt.sgk`](#ktsgk) | SGK | 1 |
| [`kt.sms_otp`](#ktsmsotp) | SMS / OTP | 5 |
| [`kt.support`](#ktsupport) | Destek yönetimi | 14 |
| [`kt.tpp_accounts`](#kttppaccounts) | Hesap yönetimi (TPP - müşteri adına) | 5 |
| [`kt.transfers`](#kttransfers) | Para transferleri | 10 |
| [`kt.treasury`](#kttreasury) | Hazine servisleri (kıymetli maden, kur) | 5 |
| [`kt.vpos`](#ktvpos) | Sanal POS | 15 |
| [`kt.your_banking`](#ktyourbanking) | Senin Bankan | 4 |

## kt.accounts

Hesap yönetimi (kurumun kendi hesapları)

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`account_activity_list`](https://developer.kuveytturk.com.tr/documentation/other/account-activity-list) | `POST /v1/accountActivities` | account_activities | CC | test edilmedi | test edilmedi |
| [`account_list_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-v3) | `GET /v3/accounts` | accounts | CC | test edildi | test edilmedi |
| [`account_list_with_suffix_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-list-with-suffix-v3) | `GET /v3/accounts/{suffix}` | accounts | CC | test edildi | test edilmedi |
| [`account_transactions_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v3) | `GET /v3/accounts/{suffix}/transactions` | accounts | CC | test edildi | test edilmedi |
| [`account_transactions_v4_detail`](https://developer.kuveytturk.com.tr/documentation/account-management-own/account-transactions-v4-detail) | `GET /v4/accounts/{suffix}/transactions` | accounts | CC | test edildi | test edilmedi |
| [`account_verification_v2`](https://developer.kuveytturk.com.tr/documentation/other/prevalidation-data-provider) | `POST /v2/accounts/verification` | accounts | CC | test edilmedi | test edilmedi |
| [`pdf_receipt_v3`](https://developer.kuveytturk.com.tr/documentation/account-management-own/pdf-receipt-v3) | `POST /v3/accounts/transactions/pdfReceipts` | accounts | CC | kısmen test edildi | test edilmedi |
| [`receipt_v3`](https://developer.kuveytturk.com.tr/documentation/hesap-yonetimi-hesaplariniz/dekont-v3) | `POST /v3/accounts/transactions/receipts` | accounts | CC | test edildi | test edilmedi |

## kt.architecht

Architecht

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`architecht_career_change`](https://developer.kuveytturk.com.tr/documentation/architecht/architecht-career-change) | `POST /v1/architechtintegration/career/insertAssignment` | public | CC | test edilmedi | test edilmedi |
| [`customer_consent_cancellation`](https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-cancellation) | `POST /v1/airapi/revoke-consent` | accounts | CC | test edilmedi | test edilmedi |
| [`customer_consent_list`](https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-list) | `GET /v1/airapi/consent-list` | accounts | CC | test edildi | test edilmedi |

## kt.cards

Kredi kartı işlemleri

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`credit_card_list_v3`](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-list-v3) | `GET /v3/creditcard/cardlist` | cards | CC | test edildi | test edilmedi |
| [`credit_card_money_transfer`](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-money-transfer) | `POST /v1/moneytransfer/creditcardmoneytransfer` | transfers | CC | test edilmedi | test edilmedi |
| [`credit_card_transactions_list_v3`](https://developer.kuveytturk.com.tr/documentation/credit-card-transactions/credit-card-transactions-list-v3) | `GET /v3/creditcard/{cardnumber}/transactions` | cards | CC | test edilmedi | test edilmedi |
| [`virtual_card_limit_update`](https://developer.kuveytturk.com.tr/documentation/other/virtual-card-limit-update) | `POST /v1/cards/virtualcardlimitupdate` | cards | AC | test edilmedi | test edilmedi |

## kt.cash_management

Nakit yönetimi

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`cheque_information_micro`](https://developer.kuveytturk.com.tr/documentation/cash-management/cheque-information-micro) | `POST /v1/cheque-information-micro` | public | CC | kısmen test edildi | test edilmedi |
| [`digital_banking_payment`](https://developer.kuveytturk.com.tr/documentation/cash-management/digital-banking-payment) | `POST /v1/vpos/digitalPayment` | digital_payments | CC | test edilmedi | test edilmedi |
| [`digital_banking_refund`](https://developer.kuveytturk.com.tr/documentation/cash-management/digital-banking-refund) | `POST /v1/vpos/digitalPaymentRefund` | digital_payments | CC | test edilmedi | test edilmedi |
| [`digital_banking_transaction_status`](https://developer.kuveytturk.com.tr/documentation/cash-management/digital-banking-transaction-status) | `POST /v1/vpos/digitalPaymentStatus` | digital_payments | CC | test edilmedi | test edilmedi |
| [`school_installment_payment_system_active_registration_inquiry`](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-payment-system-active-registration-inquiry-api) | `POST /v1/school-installment/registration-inquiry` | loans | CC | test edildi | test edilmedi |
| [`school_installment_system_registration_and_installment_cancellation`](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-registration-and-installment-cancellation-api) | `POST /v1/school-installment/cancelation` | loans | CC | test edilmedi | test edilmedi |
| [`school_installment_system_school_guaranteed_registration_payment`](https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-school-guaranteed-registration-payment) | `POST /v1/school-installment/transaction-information` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_buyer_order_confirmation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-confirmation) | `POST /v1/supplierfinance/approvefrompurchaserer` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_buyer_order_listing`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-listing) | `POST /v1/supplierfinance/getorderbypurchaser` | loans | CC | test edildi | test edilmedi |
| [`supplier_financing_invoice_cancellation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-invoice-cancellation) | `POST /v1/supplychainfinance/cancelinvoice` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_order_last_approval_by_supplier`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-order-last-approval-by-supplier) | `POST /v1/supplierfinance/lastapprovefromsupplier` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_repayment_plan_calculation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-repayment-plan-calculation) | `POST /v1/supplierfinance/getpaybackplan` | loans | CC | kısmen test edildi | test edilmedi |
| [`supplier_financing_vendor_company_invoice_approval`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-company-invoice-approval) | `POST /v1/supplychainfinance/supplierapproveinvoice` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_vendor_invoice_listing`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-invoice-listing) | `POST /v1/supplychainfinance/supplierinvoicelist` | loans | CC | kısmen test edildi | test edilmedi |
| [`supplier_financing_vendor_order_cancellation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-cancellation) | `POST /v1/supplierfinance/cancelFromSupplier` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_vendor_order_confirmation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-confirmation) | `POST /v1/supplierfinance/lastapprovefromsupplierer` | loans | CC | test edilmedi | test edilmedi |
| [`supplier_financing_vendor_order_initiation`](https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-initiation) | `POST /supplierfinance/saveordersupplier` | loans | CC | test edilmedi | test edilmedi |

## kt.credibility

Kredibilite

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`customer_overall_limit_values`](https://developer.kuveytturk.com.tr/documentation/credibility/customer-overall-limit-values) | `POST /v1/Loans/LastAllotmentTopLimit` | loans | CC | test edildi | test edilmedi |
| [`final_credit_decision_recommendation`](https://developer.kuveytturk.com.tr/documentation/credibility/final-credit-decision-recommendation) | `POST /v1/Loans/AllotmentFinalDecision` | loans | CC | test edilmedi | test edilmedi |
| [`send_invoice_detail_v2`](https://developer.kuveytturk.com.tr/documentation/credibility/send-invoice-detail-v2) | `POST /v2/purchase/invoice` | payments | CC | test edilmedi | test edilmedi |
| [`tardes_agricultural_score_inquiry`](https://developer.kuveytturk.com.tr/documentation/credibility/tardes-agricultural-score-inquiry) | `POST /v1/inquiry/gettardesscore` | loans | CC | kısmen test edildi | test edilmedi |
| [`taxpayer_gib_identity_information`](https://developer.kuveytturk.com.tr/documentation/credibility/taxpayer-gib-identity-information) | `POST /v1/inquiry/gib-tax-payer` | loans | CC | test edildi | test edilmedi |

## kt.donations

Bağışlar

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`account_transactions_for_the_organization`](https://developer.kuveytturk.com.tr/documentation/other/account-transactions-for-the-organization) | `POST /v1/donations/transactions` | donations | AC | test edilmedi | test edilmedi |
| [`campaign_list_for_organization`](https://developer.kuveytturk.com.tr/documentation/donations/campaign-list-for-organization) | `POST /v1/donations/campaignList` | donations | AC | test edilmedi | test edilmedi |
| [`donation_list_for_organization`](https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization) | `POST /v1/donations/donationList` | donations | CC | test edildi | test edilmedi |
| [`donation_list_for_organization_tdv`](https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization-tdv) | `POST /v1/donations/donationListTdv` | donations | CC | test edilmedi | test edilmedi |
| [`external_payments_list`](https://developer.kuveytturk.com.tr/documentation/donations/external-payments-list) | `POST /v1/donations/externalPayments` | donations | AC | test edilmedi | test edilmedi |

## kt.ecommerce

E-ticaret

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`ecommerce_application_refund_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund) | `POST /v1/lendings/{applicationId}/refund` | digital_payments | CC | test edilmedi | test edilmedi |
| [`ecommerce_application_refund_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund) | `POST /v1/lendings/{applicationId}/refund` | digital_payments | CC | test edilmedi | test edilmedi |
| [`ecommerce_get_lending_information_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information) | `GET /v1/lendings/{applicationId}` | digital_payments | CC | test edilmedi | test edilmedi |
| [`ecommerce_get_lending_information_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information) | `GET /v1/lendings/{applicationId}` | digital_payments | CC | test edilmedi | test edilmedi |
| [`ecommerce_lendings_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings) | `POST /v1/lendings` | digital_payments | CC | test edilmedi | test edilmedi |
| [`ecommerce_lendings_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings) | `POST /v1/lendings` | digital_payments | CC | test edilmedi | test edilmedi |
| [`ecommerce_monthly_payments_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments) | `POST /v1/query/monthly-payments` | digital_payments | CC | test edildi | test edilmedi |
| [`ecommerce_monthly_payments_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments) | `POST /v1/query/monthly-payments` | digital_payments | CC | test edildi | test edilmedi |
| [`ecommerce_pre_approved_monthly_payments_v1`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments) | `POST /v1/query/pre-approved-monthly-payments` | digital_payments | CC | test edildi | test edilmedi |
| [`ecommerce_pre_approved_monthly_payments_v1_2`](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments) | `POST /v1/query/pre-approved-monthly-payments` | digital_payments | CC | test edildi | test edilmedi |

## kt.financing

Finansman çözümleri

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`corporate_app_agreement_v2`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-app-agreement-v2) | `GET /v2/corporateAppAgreementData` | cards | CC | test edilmedi | test edilmedi |
| [`corporate_credit_card_application`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-credit-card-application) | `POST /v2/corporateCreditCardApplication` | cards | CC | test edilmedi | test edilmedi |
| [`credit_limit_request`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/credit-limit-request) | `GET /v1/loans/allotmentLimit` | loans | AC | test edilmedi | test edilmedi |
| [`customer_current_credit_allocation_flow_information`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-current-credit-allocation-flow-information) | `POST /v1/Loans/GetLatestRouteHistoryByAccountNumber` | loans | CC | test edildi | test edilmedi |
| [`customer_suited_card_list`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-suited-card-list) | `GET /v2/customerSuitedCardList` | cards | CC | kısmen test edildi | test edilmedi |
| [`get_digital_channel_card_application_list_v2`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/get-digital-channel-card-application-list-v2) | `GET /v2/cardApplicationList` | cards | CC | kısmen test edildi | test edilmedi |
| [`individual_app_agreement_v2`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-app-agreement-v2) | `GET /v2/individualAppAgreement` | cards | CC | test edilmedi | test edilmedi |
| [`individual_credit_card_application_v2`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-credit-card-application-v2) | `POST /v2/individualCreditCardApplication` | cards | CC | test edilmedi | test edilmedi |
| [`loan_finance_calculation`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-calculation) | `GET /v1/calculations/loan` | public | CC | test edildi | test edilmedi |
| [`loan_finance_info`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-info) | `GET /v1/loans/{projectNumber}/info` | loans | AC | test edilmedi | test edilmedi |
| [`loan_finance_installments`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-installments) | `GET /v1/loans/{projectNumber}/installments` | loans | AC | test edilmedi | test edilmedi |
| [`loan_finance_list`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-list) | `GET /v1/loans` | loans | AC | test edilmedi | test edilmedi |
| [`loans_price_list`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loans-price-list) | `GET /v1/loans/pricelist` | loans | CC | kısmen test edildi | test edilmedi |
| [`send_leasing_confirmation_form`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-confirmation-form) | `POST /v1/leasing/confirmation-form` | loans | CC | test edilmedi | test edilmedi |
| [`send_leasing_current_account_file`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-current-account-file) | `POST /v1/leasing/current-documents` | loans | CC | test edilmedi | test edilmedi |
| [`send_leasing_release_documents`](https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-release-documents) | `POST /v1/leasing/exit-documents` | loans | CC | test edilmedi | test edilmedi |

## kt.fx

Döviz işlemleri

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`fx_currency_buy`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-buy) | `POST /v1/fx/buy` | public | CC | test edilmedi | test edilmedi |
| [`fx_currency_list`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-list) | `GET /v1/data/fecs` | public | CC | test edildi | test edilmedi |
| [`fx_currency_rates`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-rates) | `GET /v2/fx/rates` | public | CC | test edildi | test edilmedi |
| [`fx_currency_sell`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-currency-sell) | `POST /v1/fx/sell` | public | CC | test edilmedi | test edilmedi |
| [`fx_transaction_history`](https://developer.kuveytturk.com.tr/documentation/foreign-exchange-transactions/fx-transaction-history) | `POST /v1/fx/fxtransactions` | public | CC | test edilmedi | test edilmedi |

## kt.hgs

HGS servisleri

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`hgs_balance_information`](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-balance-information) | `POST /v1/hgs/balance-info` | public | CC | kısmen test edildi | test edilmedi |
| [`hgs_product_information`](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-product-information) | `POST /v1/hgs/product-info` | public | CC | kısmen test edildi | test edilmedi |
| [`hgs_usage_transactions`](https://developer.kuveytturk.com.tr/documentation/hgs-services/hgs-usage-transactions) | `POST /v1/hgs/usage-transactions` | public | CC | kısmen test edildi | test edilmedi |

## kt.information

Bilgi servisleri (şube, ATM, parametre sorguları...)

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`bank_branch_list`](https://developer.kuveytturk.com.tr/documentation/notification-services/bank-branch-list) | `GET /v1/data/banks/{bankId}/branches` | public | CC | test edilmedi | test edilmedi |
| [`bank_list`](https://developer.kuveytturk.com.tr/documentation/notification-services/bank-list) | `GET /v1/data/banks` | public | CC | test edildi | test edilmedi |
| [`calculate_profit_share_rate`](https://developer.kuveytturk.com.tr/documentation/notification-services/calculate-profit-share-rate) | `POST /v1/calculateprofitsharerate` | public | CC | test edildi | test edilmedi |
| [`central_notification`](https://developer.kuveytturk.com.tr/documentation/notification-services/central-notification) | `POST /v1/notification/sendInfEng` | public | CC | test edilmedi | test edilmedi |
| [`collect_installment`](https://developer.kuveytturk.com.tr/documentation/notification-services/collect-installment) | `POST /v1/collections/collectInstallment` | loans | CC | test edilmedi | test edilmedi |
| [`collection_list`](https://developer.kuveytturk.com.tr/documentation/notification-services/collection-list) | `POST /v1/collections` | loans | CC | test edildi | test edilmedi |
| [`get_class_info`](https://developer.kuveytturk.com.tr/documentation/notification-services/get-class-info) | `POST /v1/erp/lms/getClassInfo` | public | CC | test edildi | test edilmedi |
| [`iban_validation_utility`](https://developer.kuveytturk.com.tr/documentation/notification-services/iban-validation-utility) | `POST /v1/validation/ibanvalidator` | public | CC | test edildi | test edilmedi |
| [`kuveyt_turk_atm_list`](https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-atm-list) | `GET /v1/data/atms` | public | CC | test edildi | test edilmedi |
| [`kuveyt_turk_branch_list`](https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-branch-list) | `GET /v1/data/branches` | public | CC | test edildi | test edilmedi |
| [`kuveyt_turk_xtm_list`](https://developer.kuveytturk.com.tr/documentation/notification-services/kuveyt-turk-xtm-list) | `GET /v1/data/xtms` | public | CC | test edildi | test edilmedi |
| [`loan_finance_calculation_parameter`](https://developer.kuveytturk.com.tr/documentation/notification-services/loan-finance-calculation-parameter) | `GET /v1/data/loans` | public | CC | test edilmedi | test edilmedi |

## kt.moneygram

MoneyGram

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`money_gram_country_list`](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-country-list) | `GET /v1/moneygram/countrylist` | public | CC | test edildi | test edilmedi |
| [`money_gram_currency_list`](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-currency-list) | `GET /v1/moneygram/currencylist` | public | CC | test edildi | test edilmedi |
| [`money_gram_get_fee`](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-get-fee) | `POST /v1/moneygram/getfee` | transfers | AC | test edilmedi | test edilmedi |
| [`money_gram_query_fee`](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-fee) | `GET /v1/moneygram/queryfee` | transfers | CC | test edildi | test edilmedi |
| [`money_gram_query_reference`](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-query-reference) | `POST /v1/moneygram/queryreference` | transfers | AC | test edilmedi | test edilmedi |
| [`money_gram_send`](https://developer.kuveytturk.com.tr/documentation/moneygram/moneygram-send) | `POST /v1/moneygram/send` | transfers | AC | test edilmedi | test edilmedi |

## kt.other

Diğer

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`calculate_welcome_participation_account_profit_share`](https://developer.kuveytturk.com.tr/documentation/other/calculate-welcome-participation-account-profit-share) | `POST /v1/welcomeprofitsharecalculation` | public | CC | test edildi | test edilmedi |
| [`credi_tech_intelligence_inquiry_by_credit_allocation_status`](https://developer.kuveytturk.com.tr/documentation/other/creditech-intelligence-inquiry-by-credit-allocation-status) | `POST /v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber` | loans | CC | test edilmedi | test edilmedi |
| [`credit_tech_pos`](https://developer.kuveytturk.com.tr/documentation/other/credittech-pos-api) | `POST /v1/data/credittechpos` | payments | CC | test edilmedi | test edilmedi |
| [`fraud_notifications_exists`](https://developer.kuveytturk.com.tr/documentation/other/fraud-notifications-exists) | `POST /v1/inquiry/is-fraud-notification-exists` | public | CC | test edildi | test edilmedi |
| [`get_fraud_notifications_last_day`](https://developer.kuveytturk.com.tr/documentation/other/get-fraud-notifications-last-day) | `POST /v1/inquiry/get-fraud-notifications-daily` | public | CC | test edildi | test edilmedi |
| [`get_process_design_xml_by_business_process_id`](https://developer.kuveytturk.com.tr/documentation/other/get-process-design-xml-by-business-process-id) | `POST /v1/bpm/post/grcprocessdesignxml` | public | CC | test edildi | test edilmedi |
| [`saglam_pay_get_customer_full_info`](https://developer.kuveytturk.com.tr/documentation/other/saglam-pay-get-customer-full-info) | `GET /v1/get-customer-info-by-customerId-full` | public | CC | test edilmedi | test edilmedi |
| [`visa_payment_status_notification`](https://developer.kuveytturk.com.tr/documentation/other/visa-payment-status-notification) | `POST /v1/StatusNotify` | public | CC | test edilmedi | test edilmedi |
| [`visa_statement_delivery`](https://developer.kuveytturk.com.tr/documentation/other/visa-statement-delivery) | `POST /v1/StatementDelivery` | public | CC | test edilmedi | test edilmedi |

## kt.payment_solutions

Ödeme çözümleri

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`digital_payment_get_token`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-get-token) | `POST /v1/vpos/digitalPaymentGetToken` | digital_payments | CC | test edilmedi | test edilmedi |
| [`digital_payment_query`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-query) | `POST /v1/vpos/digitalPaymentQuery` | digital_payments | CC | test edildi | test edilmedi |
| [`digital_payment_refund`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-refund) | `POST /v1/vpos/digitalPaymentDoRefund` | digital_payments | CC | test edilmedi | test edilmedi |
| [`digital_payment_send_document`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-send-document) | `POST /v1/vpos/sendDocument` | digital_payments | CC | test edilmedi | test edilmedi |
| [`pos_merchant_number_list`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-merchant-number-list) | `GET /v1/pos/merchant-number` | public | CC | test edildi | test edilmedi |
| [`pos_transaction_details_for_tpp_v2`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-for-tpp-third-party-provider-v2) | `POST /v2/pos/detail-transactions` | cards | AC | test edilmedi | test edilmedi |
| [`pos_transaction_details_v3`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-v3) | `POST /v3/pos/detail-transactions` | cards | CC | kısmen test edildi | test edilmedi |
| [`pos_transactions_summary_for_tpp_v2`](https://developer.kuveytturk.com.tr/documentation/odeme-cozumleri/ucuncu-taraf-saglayici-tpp-icin-pos-islemleri-ozeti-v2) | `POST /v2/pos/transactions` | cards | AC | test edilmedi | test edilmedi |
| [`pos_transactions_summary_v3`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transactions-summary-v3) | `POST /v3/pos/transactions` | cards | CC | kısmen test edildi | test edilmedi |
| [`send_order_distribution_detail_v2`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/send-order-distribution-detail-v2) | `POST /v3/purchase/orderdistribution` | payments | CC | test edilmedi | test edilmedi |
| [`virtual_pos`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos) | `POST /v1/vpos` | cards | CC | test edilmedi | test edilmedi |
| [`virtual_pos_end_day_all_list`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-enddayall-list) | `POST /v1/vpos/endDayAllList` | cards | AC | test edilmedi | test edilmedi |
| [`virtual_pos_end_of_day`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-endofday) | `POST /v1/vpos/endOfDay` | cards | AC | test edilmedi | test edilmedi |
| [`virtual_pos_general_transaction`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-general-transaction) | `POST /v1/vpos/transaction` | cards | AC | test edilmedi | test edilmedi |
| [`virtual_pos_order_filter`](https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-order-filter) | `POST /v1/vpos/orderFilter` | cards | AC | test edilmedi | test edilmedi |

## kt.payments

Ödemeler

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`account_validation_by_account_number_for_group_money_transfer`](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-account-number-for-group-money-transfer) | `POST /v1/groupmoneytransfer/accountvalidation` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`account_validation_by_iban_for_group_money_transfer`](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer) | `POST /v1/groupmoneytransfer/account` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`account_validation_by_iban_for_group_money_transfer_v2`](https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer-v2) | `POST /v2/groupmoneytransfer/account` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`cancel_money_transfers_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/cancel-money-transfers-from-ktbank-to-kuveyt-turk) | `POST /v1/groupmoneytransfer/incomingtransfer/cancellist` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`check_money_transfers_status_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/check-money-transfers-status-from-ktbank-to-kuveytturk) | `POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist` | intrabank_money_transfers | AC | test edilmedi | test edilmedi |
| [`do_stamp_duty_tax_payment_offline`](https://developer.kuveytturk.com.tr/documentation/other/do-stamp-duty-tax-payment-offline) | `POST /v1/tax/do-stamp-duty-tax-payment-offline` | payments | CC | test edilmedi | test edilmedi |
| [`insert_money_transfers_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/insert-money-transfers-from-kt-bank-to-kuveyt-turk) | `POST /v1/groupmoneytransfer/incomingtransfer/insertlist` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`invoice_company_list`](https://developer.kuveytturk.com.tr/documentation/payments/invoice-company-list) | `GET /v1/invoices/companies` | payments | AC | test edilmedi | test edilmedi |
| [`kt_bank_error_message_list`](https://developer.kuveytturk.com.tr/documentation/payments/kt-bank-error-message-list) | `GET /v1/groupmoneytransfer/errormessagelist` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`kuveyt_turk_branch_list_for_group_money_transfer`](https://developer.kuveytturk.com.tr/documentation/payments/kuveyt-turk-branch-list-for-group-money-transfer) | `GET /v1/groupmoneytransfer/branchlist` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`return_money_transfers_from_kt_bank_to_kuveyt_turk`](https://developer.kuveytturk.com.tr/documentation/payments/return-money-transfers-from-ktbank-to-kuveyt-turk) | `POST /v1/groupmoneytransfer/incomingtransfer/returnlist` | intrabank_money_transfers | CC | test edilmedi | test edilmedi |
| [`send_multiple_invoice_v2`](https://developer.kuveytturk.com.tr/documentation/payments/send-multiple-invoice-v2) | `POST /v2/purchase/multipleinvoice` | payments | CC | test edilmedi | test edilmedi |
| [`send_offer_vendor_detail`](https://developer.kuveytturk.com.tr/documentation/payments/send-offer-vendor-detail) | `POST /v1/purchase/offervendor` | payments | CC | test edilmedi | test edilmedi |
| [`send_order_distribution_detail`](https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail) | `POST /v1/purchase/orderdistribution` | payments | CC | test edilmedi | test edilmedi |
| [`send_order_distribution_detail_v2`](https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail-v2) | `POST /v3/purchase/orderdistribution` | payments | CC | test edilmedi | test edilmedi |

## kt.sgk

SGK

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`consume_insurance_queue`](https://developer.kuveytturk.com.tr/documentation/sgk/consume-insurance-queue) | `POST /v1/insurance/consumeQueue` | public | CC | test edilmedi | test edilmedi |

## kt.sms_otp

SMS / OTP

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`pr_customer_validation`](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-customer-validation) | `POST /v1/paymentrequest/customerValidation` | public | CC | test edilmedi | test edilmedi |
| [`pr_get_account_details_by_iban`](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-account-details-by-iban) | `POST /v1/paymentrequest/getAccountByIban` | accounts | CC | test edilmedi | test edilmedi |
| [`pr_get_fast_result`](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-get-fast-result) | `GET /v1/paymentrequest/getFastResult` | public | CC | test edildi | test edilmedi |
| [`pr_payment_request_control`](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-request-control) | `POST /v1/paymentrequest/paymentControl` | public | CC | test edilmedi | test edilmedi |
| [`pr_payment_transaction`](https://developer.kuveytturk.com.tr/documentation/sms-otp/pr-payment-transaction) | `POST /v1/paymentrequest/transfer` | transfers | CC | test edilmedi | test edilmedi |

## kt.support

Destek yönetimi

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`kt_incident_activity_type_list`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-activity-type-list) | `GET /v1/incident/activityTypes` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_cancel`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-cancel) | `POST /v1/incident/cancel` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_creation`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation) | `POST /v1/incident/operation/create` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_creation_by_company`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-creation-by-company) | `POST /v1/company/incident/create` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_defined_document_list`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-defined-document-list) | `GET /v1/incident/defiendDocuments` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_info`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-info) | `POST /v1/incident/information/info` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_insert_activity`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-activity) | `POST /v1/incident/insertActivity` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_insert_document`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-insert-document) | `POST /v1/incident/insertDocument` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_neova_info`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-info) | `POST /v1/incident/neova/info` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_neova_list`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-list) | `POST /v1/incident/neova/list` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_neova_update`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-neova-update) | `POST /v1/incident/neova/update` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_optional_field_list`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-optional-field-list) | `POST /v1/incident/optionalFieldList` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_product_list`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-product-list) | `GET /v1/incident/information/products` | incident_operations | CC | test edilmedi | test edilmedi |
| [`kt_incident_reopen`](https://developer.kuveytturk.com.tr/documentation/support-management/kt-incident-reopen) | `POST /v1/incident/reopen` | incident_operations | CC | test edilmedi | test edilmedi |

## kt.tpp_accounts

Hesap yönetimi (TPP - müşteri adına)

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`account_list_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-list-v2) | `GET /v2/accounts` | accounts | AC | test edildi | test edilmedi |
| [`account_list_with_suffix_v2`](https://developer.kuveytturk.com.tr/documentation/other/account-list-v2-withouth-suffix) | `GET /v2/accounts/{suffix}` | accounts | AC | test edilmedi | test edilmedi |
| [`account_transactions_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/account-transactions-v2) | `GET /v2/accounts/{suffix}/transactions` | accounts | AC | test edildi | test edilmedi |
| [`receipt_v1`](https://developer.kuveytturk.com.tr/documentation/other/receipt) | `GET /v1/accounts/{suffix}/transactions/{businessKey}` | accounts | AC | test edildi | test edilmedi |
| [`receipt_v2`](https://developer.kuveytturk.com.tr/documentation/account-management-tpp/receipt-v2) | `POST /v2/accounts/transactions/receipts` | accounts | AC | test edildi | test edilmedi |

## kt.transfers

Para transferleri

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`cash_withdrawal_from_atm_via_qr_code`](https://developer.kuveytturk.com.tr/documentation/other/cash-withdrawal-from-atm-via-qr-code) | `POST /v1/transfers/fromATMByQRCode` | transfers | AC | test edilmedi | test edilmedi |
| [`customer_iban_info_for_money_transfer`](https://developer.kuveytturk.com.tr/documentation/money-transfers/customer-iban-info-for-money-transfer) | `GET /v1/moneytransfer/{iban}/customeribaninfo` | transfers | CC | test edildi | test edilmedi |
| [`internal_money_transfer`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-veeraman) | `POST /v1/moneytransfer/interbankmoneytransfer` | transfers | CC | test edilmedi | test edilmedi |
| [`investment_account_activities_report`](https://developer.kuveytturk.com.tr/documentation/other/money-transfer-report-for-kuveyt-turk-investment-securities-inc) | `POST /v1/investment/report-for-account-activities` | transfers | CC | test edildi | test edilmedi |
| [`money_transfer_payment_type`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-payment-type) | `POST /v1/moneytransfer/paymenttype` | transfers | CC | kısmen test edildi | test edilmedi |
| [`money_transfer_state`](https://developer.kuveytturk.com.tr/documentation/money-transfers/money-transfer-state) | `GET /v1/moneytransfer-state` | transfers | CC | test edildi | test edilmedi |
| [`money_transfer_to_gsm`](https://developer.kuveytturk.com.tr/documentation/other/money-transfer-to-gsm) | `POST /v1/transfers/toGSM` | transfers | AC | test edilmedi | test edilmedi |
| [`outgoing_money_transfer`](https://developer.kuveytturk.com.tr/documentation/para-transferleri/para-transferi-havale-eft-fast-virman) | `POST /v1/moneytransfer/outgoingmoneytransfer` | transfers | CC | kısmen test edildi | test edilmedi |
| [`outgoing_money_transfer_v2`](https://developer.kuveytturk.com.tr/documentation/money-transfers/outgoing-money-transfer-v2) | `POST /v2/moneytransfer/outgoingmoneytransfer` | transfers | AC | test edilmedi | test edilmedi |
| [`transaction_validation_list`](https://developer.kuveytturk.com.tr/documentation/money-transfers/transaction-validation-list) | `GET /v1/transactionvalidation/transactionlist` | public | CC | kısmen test edildi | test edilmedi |

## kt.treasury

Hazine servisleri (kıymetli maden, kur)

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`fx_and_precious_metal_rates`](https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metal-rates) | `GET /v1/fx/rates` | public | CC | test edildi | test edilmedi |
| [`fx_and_precious_metals_transaction_history`](https://developer.kuveytturk.com.tr/documentation/treasury-services/fx-and-precious-metals-transaction-history) | `POST /v1/fx/fxtransactions` | public | CC | test edilmedi | test edilmedi |
| [`precious_metal_buy`](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-buy) | `POST /v1/preciousmetal/buy` | public | CC | test edilmedi | test edilmedi |
| [`precious_metal_rates`](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-rates) | `GET /v1/preciousmetal/rates` | public | CC | test edildi | test edilmedi |
| [`precious_metal_sell`](https://developer.kuveytturk.com.tr/documentation/treasury-services/precious-metal-sell) | `POST /v1/preciousmetal/sell` | public | CC | test edilmedi | test edilmedi |

## kt.vpos

Sanal POS

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`add_card_to_merchant_safe`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/addcardtomerchantsafe) | `POST /v1/vpos/addCardToMerchantSafe` | public | CC | test edilmedi | test edilmedi |
| [`digital_payment_commission_reconciliation`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/digital-payment-commission-reconciliation) | `POST /v1/vpos/commissionReconciliation` | digital_payments | CC | test edilmedi | test edilmedi |
| [`get_customer_by_safe_key`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/getcustomerbysafekey) | `POST /v1/vpos/getCustomerBySafeKey` | public | CC | test edilmedi | test edilmedi |
| [`get_seller_order_details`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/get-seller-order-details) | `POST /v1/vpos/getMerchantOrderDetail` | public | CC | kısmen test edildi | test edilmedi |
| [`non_3_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/non-3d-payment) | `POST /v1/vpos/non3DPayment` | public | CC | test edilmedi | test edilmedi |
| [`non_three_d_payment_by_merchant_safe`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/nonthreedpaymentbymerchantsafe) | `POST /v1/vpos/nonThreeDPaymentByMerchantSafe` | public | CC | test edilmedi | test edilmedi |
| [`order_detail_with_payment_id`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/order-detail-with-payment-id) | `POST /v1/vpos/orderDetailWithPaymentId` | public | CC | kısmen test edildi | test edilmedi |
| [`payment_order_reversal`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/paymentorderreversal) | `POST /v1/vpos/paymentOrderReversal` | public | CC | test edilmedi | test edilmedi |
| [`pre_authorization`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/preauthorization) | `POST /v1/vpos/preAuthorization` | public | CC | test edilmedi | test edilmedi |
| [`recurring_non_three_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/recurringnonthreedpayment) | `POST /v1/vpos/recurringNonThreeDPayment` | public | CC | test edilmedi | test edilmedi |
| [`sale_order_reversal`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/saleorderreversal) | `POST /v1/vpos/saleOrderReversal` | public | CC | test edilmedi | test edilmedi |
| [`secure_partner_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/secure-partner-payment) | `POST /v1/vpos/secureCommonPaymentToken` | public | CC | test edilmedi | test edilmedi |
| [`threee_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/threeed-payment) | `POST /v1/vpos/threeDPayment` | public | CC | test edilmedi | test edilmedi |
| [`virtual_pos_non_three_d_payment`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/virtual-pos-nonthreed-payment-masked-card) | `POST /v1/vpos/nonThreeDPayment` | cards | CC | test edilmedi | test edilmedi |
| [`virtual_pos_sale_reversal`](https://developer.kuveytturk.com.tr/documentation/virtual-pos-vpos/virtual-pos-sale-reversal-masked) | `POST /v1/vpos/saleReversal` | cards | CC | test edilmedi | test edilmedi |

## kt.your_banking

Senin Bankan

| Metot | İstek | Kapsam | Akış | Sandbox | Canlı |
| - | - | - | - | - | - |
| [`your_banking_account_application`](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application) | `POST /v1/yourbank/accountApplications` | accounts | CC | test edilmedi | test edilmedi |
| [`your_banking_account_application_documents`](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-documents) | `POST /v1/yourbank/accountApplicationDocuments` | accounts | CC | test edilmedi | test edilmedi |
| [`your_banking_account_application_sms_validation`](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-sms-validation) | `POST /v1/yourbank/accountSmsOtp` | accounts | CC | test edilmedi | test edilmedi |
| [`your_banking_account_application_status_query`](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-status-query) | `POST /v1/yourbank/accountApplicationStatus` | accounts | CC | test edildi | test edilmedi |
