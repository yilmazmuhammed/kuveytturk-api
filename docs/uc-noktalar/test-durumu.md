<!-- Bu sayfa scripts/generate.py tarafından spec/test_status.json'dan üretildi. -->

# Test durumu

Her uç noktanın sandbox'ta ve canlı ortamda denenip denenmediği. Kaynak dosya `spec/test_status.json`; ayrıntılar her uç noktanın kendi sayfasında.

| Durum | Anlamı |
| - | - |
| test edildi | Uç noktaya istek atıldı ve anlamlı bir yanıt alındı (çalışıyor ya da bu ortamda bulunmadığı görüldü). |
| kısmen test edildi | Uç nokta var ve uygulamanın yetkisi yeterli, ama gerçek parametre değerleri olmadığı için yalnızca doğrulama hatası alındı. |
| test edilmedi | İstek atılmadı: işlem yapan uç nokta (para hareketi, ödeme, başvuru, kayıt oluşturma, bildirim), müşteri girişi gerekiyor, uygulamanın kapsam yetkisi yok ya da parametre değeri bilinmiyor. |

- **Sandbox:** kısmen test edildi: 17, test edildi: 48, test edilmedi: 127
- **Canlı:** test edilmedi: 192

!!! info "İşlem yapan uç noktalar otomatik denenmez"
    Para hareketi, ödeme, başvuru, kayıt oluşturma/iptal, bildirim ya da SMS gönderen uç noktalara test betiği hiç istek atmaz. Bunları denemek isteyen, sonuçlarını bilerek elle dener ve `spec/test_status.json`'daki kaydı elle günceller.

## Nasıl güncellenir

```bash
python scripts/check_endpoints.py                         # sandbox
python scripts/check_endpoints.py --environment production # canlı (Go Live sonrası)
python scripts/generate.py                                # bu sayfayı yeniden üretir
```

Elle yapılan bir testi (işlem yapan uçlar, müşteri girişli uçlar, canlı testler) işlemek için:

```bash
python scripts/record_test.py transfers.outgoing_money_transfer \
    --durum "test edildi" --sonuc "çalışıyor" --ayrinti "1 TL, kendi hesaplar arası"
python scripts/record_test.py fx.fx_currency_rates --environment production \
    --durum "test edildi" --sonuc "çalışıyor"
```

Betik yalnızca elle onaylanmış okuma uç noktalarını çağırır ve yalnızca çağırdıklarının kaydını değiştirir; elle girilmiş kayıtlar korunur.

## Uç noktalar

| Metot | İstek | Sandbox | Canlı |
| - | - | - | - |
| [`accounts.account_activity_list`](accounts.md#account_activity_list) | `POST /v1/accountActivities` | test edilmedi | test edilmedi |
| [`accounts.account_list_v3`](accounts.md#account_list_v3) | `GET /v3/accounts` | test edildi | test edilmedi |
| [`accounts.account_list_with_suffix_v3`](accounts.md#account_list_with_suffix_v3) | `GET /v3/accounts/{suffix}` | test edildi | test edilmedi |
| [`accounts.account_transactions_v3`](accounts.md#account_transactions_v3) | `GET /v3/accounts/{suffix}/transactions` | test edildi | test edilmedi |
| [`accounts.account_transactions_v4_detail`](accounts.md#account_transactions_v4_detail) | `GET /v4/accounts/{suffix}/transactions` | test edildi | test edilmedi |
| [`accounts.account_verification_v2`](accounts.md#account_verification_v2) | `POST /v2/accounts/verification` | test edilmedi | test edilmedi |
| [`accounts.pdf_receipt_v3`](accounts.md#pdf_receipt_v3) | `POST /v3/accounts/transactions/pdfReceipts` | kısmen test edildi | test edilmedi |
| [`accounts.receipt_v3`](accounts.md#receipt_v3) | `POST /v3/accounts/transactions/receipts` | test edildi | test edilmedi |
| [`architecht.architecht_career_change`](architecht.md#architecht_career_change) | `POST /v1/architechtintegration/career/insertAssignment` | test edilmedi | test edilmedi |
| [`architecht.customer_consent_cancellation`](architecht.md#customer_consent_cancellation) | `POST /v1/airapi/revoke-consent` | test edilmedi | test edilmedi |
| [`architecht.customer_consent_list`](architecht.md#customer_consent_list) | `GET /v1/airapi/consent-list` | test edildi | test edilmedi |
| [`cards.credit_card_list_v3`](cards.md#credit_card_list_v3) | `GET /v3/creditcard/cardlist` | test edildi | test edilmedi |
| [`cards.credit_card_money_transfer`](cards.md#credit_card_money_transfer) | `POST /v1/moneytransfer/creditcardmoneytransfer` | test edilmedi | test edilmedi |
| [`cards.credit_card_transactions_list_v3`](cards.md#credit_card_transactions_list_v3) | `GET /v3/creditcard/{cardnumber}/transactions` | test edilmedi | test edilmedi |
| [`cards.virtual_card_limit_update`](cards.md#virtual_card_limit_update) | `POST /v1/cards/virtualcardlimitupdate` | test edilmedi | test edilmedi |
| [`cash_management.cheque_information_micro`](cash_management.md#cheque_information_micro) | `POST /v1/cheque-information-micro` | kısmen test edildi | test edilmedi |
| [`cash_management.digital_banking_payment`](cash_management.md#digital_banking_payment) | `POST /v1/vpos/digitalPayment` | test edilmedi | test edilmedi |
| [`cash_management.digital_banking_refund`](cash_management.md#digital_banking_refund) | `POST /v1/vpos/digitalPaymentRefund` | test edilmedi | test edilmedi |
| [`cash_management.digital_banking_transaction_status`](cash_management.md#digital_banking_transaction_status) | `POST /v1/vpos/digitalPaymentStatus` | test edilmedi | test edilmedi |
| [`cash_management.school_installment_payment_system_active_registration_inquiry`](cash_management.md#school_installment_payment_system_active_registration_inquiry) | `POST /v1/school-installment/registration-inquiry` | test edildi | test edilmedi |
| [`cash_management.school_installment_system_registration_and_installment_cancellation`](cash_management.md#school_installment_system_registration_and_installment_cancellation) | `POST /v1/school-installment/cancelation` | test edilmedi | test edilmedi |
| [`cash_management.school_installment_system_school_guaranteed_registration_payment`](cash_management.md#school_installment_system_school_guaranteed_registration_payment) | `POST /v1/school-installment/transaction-information` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_buyer_order_confirmation`](cash_management.md#supplier_financing_buyer_order_confirmation) | `POST /v1/supplierfinance/approvefrompurchaserer` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_buyer_order_listing`](cash_management.md#supplier_financing_buyer_order_listing) | `POST /v1/supplierfinance/getorderbypurchaser` | test edildi | test edilmedi |
| [`cash_management.supplier_financing_invoice_cancellation`](cash_management.md#supplier_financing_invoice_cancellation) | `POST /v1/supplychainfinance/cancelinvoice` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_order_last_approval_by_supplier`](cash_management.md#supplier_financing_order_last_approval_by_supplier) | `POST /v1/supplierfinance/lastapprovefromsupplier` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_repayment_plan_calculation`](cash_management.md#supplier_financing_repayment_plan_calculation) | `POST /v1/supplierfinance/getpaybackplan` | kısmen test edildi | test edilmedi |
| [`cash_management.supplier_financing_vendor_company_invoice_approval`](cash_management.md#supplier_financing_vendor_company_invoice_approval) | `POST /v1/supplychainfinance/supplierapproveinvoice` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_vendor_invoice_listing`](cash_management.md#supplier_financing_vendor_invoice_listing) | `POST /v1/supplychainfinance/supplierinvoicelist` | kısmen test edildi | test edilmedi |
| [`cash_management.supplier_financing_vendor_order_cancellation`](cash_management.md#supplier_financing_vendor_order_cancellation) | `POST /v1/supplierfinance/cancelFromSupplier` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_vendor_order_confirmation`](cash_management.md#supplier_financing_vendor_order_confirmation) | `POST /v1/supplierfinance/lastapprovefromsupplierer` | test edilmedi | test edilmedi |
| [`cash_management.supplier_financing_vendor_order_initiation`](cash_management.md#supplier_financing_vendor_order_initiation) | `POST /supplierfinance/saveordersupplier` | test edilmedi | test edilmedi |
| [`credibility.customer_overall_limit_values`](credibility.md#customer_overall_limit_values) | `POST /v1/Loans/LastAllotmentTopLimit` | test edildi | test edilmedi |
| [`credibility.final_credit_decision_recommendation`](credibility.md#final_credit_decision_recommendation) | `POST /v1/Loans/AllotmentFinalDecision` | test edilmedi | test edilmedi |
| [`credibility.send_invoice_detail_v2`](credibility.md#send_invoice_detail_v2) | `POST /v2/purchase/invoice` | test edilmedi | test edilmedi |
| [`credibility.tardes_agricultural_score_inquiry`](credibility.md#tardes_agricultural_score_inquiry) | `POST /v1/inquiry/gettardesscore` | kısmen test edildi | test edilmedi |
| [`credibility.taxpayer_gib_identity_information`](credibility.md#taxpayer_gib_identity_information) | `POST /v1/inquiry/gib-tax-payer` | test edildi | test edilmedi |
| [`donations.account_transactions_for_the_organization`](donations.md#account_transactions_for_the_organization) | `POST /v1/donations/transactions` | test edilmedi | test edilmedi |
| [`donations.campaign_list_for_organization`](donations.md#campaign_list_for_organization) | `POST /v1/donations/campaignList` | test edilmedi | test edilmedi |
| [`donations.donation_list_for_organization`](donations.md#donation_list_for_organization) | `POST /v1/donations/donationList` | test edildi | test edilmedi |
| [`donations.donation_list_for_organization_tdv`](donations.md#donation_list_for_organization_tdv) | `POST /v1/donations/donationListTdv` | test edilmedi | test edilmedi |
| [`donations.external_payments_list`](donations.md#external_payments_list) | `POST /v1/donations/externalPayments` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_application_refund_v1`](ecommerce.md#ecommerce_application_refund_v1) | `POST /v1/lendings/{applicationId}/refund` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_application_refund_v1_2`](ecommerce.md#ecommerce_application_refund_v1_2) | `POST /v1/lendings/{applicationId}/refund` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_get_lending_information_v1`](ecommerce.md#ecommerce_get_lending_information_v1) | `GET /v1/lendings/{applicationId}` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_get_lending_information_v1_2`](ecommerce.md#ecommerce_get_lending_information_v1_2) | `GET /v1/lendings/{applicationId}` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_lendings_v1`](ecommerce.md#ecommerce_lendings_v1) | `POST /v1/lendings` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_lendings_v1_2`](ecommerce.md#ecommerce_lendings_v1_2) | `POST /v1/lendings` | test edilmedi | test edilmedi |
| [`ecommerce.ecommerce_monthly_payments_v1`](ecommerce.md#ecommerce_monthly_payments_v1) | `POST /v1/query/monthly-payments` | test edildi | test edilmedi |
| [`ecommerce.ecommerce_monthly_payments_v1_2`](ecommerce.md#ecommerce_monthly_payments_v1_2) | `POST /v1/query/monthly-payments` | test edildi | test edilmedi |
| [`ecommerce.ecommerce_pre_approved_monthly_payments_v1`](ecommerce.md#ecommerce_pre_approved_monthly_payments_v1) | `POST /v1/query/pre-approved-monthly-payments` | test edildi | test edilmedi |
| [`ecommerce.ecommerce_pre_approved_monthly_payments_v1_2`](ecommerce.md#ecommerce_pre_approved_monthly_payments_v1_2) | `POST /v1/query/pre-approved-monthly-payments` | test edildi | test edilmedi |
| [`financing.corporate_app_agreement_v2`](financing.md#corporate_app_agreement_v2) | `GET /v2/corporateAppAgreementData` | test edilmedi | test edilmedi |
| [`financing.corporate_credit_card_application`](financing.md#corporate_credit_card_application) | `POST /v2/corporateCreditCardApplication` | test edilmedi | test edilmedi |
| [`financing.credit_limit_request`](financing.md#credit_limit_request) | `GET /v1/loans/allotmentLimit` | test edilmedi | test edilmedi |
| [`financing.customer_current_credit_allocation_flow_information`](financing.md#customer_current_credit_allocation_flow_information) | `POST /v1/Loans/GetLatestRouteHistoryByAccountNumber` | test edildi | test edilmedi |
| [`financing.customer_suited_card_list`](financing.md#customer_suited_card_list) | `GET /v2/customerSuitedCardList` | kısmen test edildi | test edilmedi |
| [`financing.get_digital_channel_card_application_list_v2`](financing.md#get_digital_channel_card_application_list_v2) | `GET /v2/cardApplicationList` | kısmen test edildi | test edilmedi |
| [`financing.individual_app_agreement_v2`](financing.md#individual_app_agreement_v2) | `GET /v2/individualAppAgreement` | test edilmedi | test edilmedi |
| [`financing.individual_credit_card_application_v2`](financing.md#individual_credit_card_application_v2) | `POST /v2/individualCreditCardApplication` | test edilmedi | test edilmedi |
| [`financing.loan_finance_calculation`](financing.md#loan_finance_calculation) | `GET /v1/calculations/loan` | test edildi | test edilmedi |
| [`financing.loan_finance_info`](financing.md#loan_finance_info) | `GET /v1/loans/{projectNumber}/info` | test edilmedi | test edilmedi |
| [`financing.loan_finance_installments`](financing.md#loan_finance_installments) | `GET /v1/loans/{projectNumber}/installments` | test edilmedi | test edilmedi |
| [`financing.loan_finance_list`](financing.md#loan_finance_list) | `GET /v1/loans` | test edilmedi | test edilmedi |
| [`financing.loans_price_list`](financing.md#loans_price_list) | `GET /v1/loans/pricelist` | kısmen test edildi | test edilmedi |
| [`financing.send_leasing_confirmation_form`](financing.md#send_leasing_confirmation_form) | `POST /v1/leasing/confirmation-form` | test edilmedi | test edilmedi |
| [`financing.send_leasing_current_account_file`](financing.md#send_leasing_current_account_file) | `POST /v1/leasing/current-documents` | test edilmedi | test edilmedi |
| [`financing.send_leasing_release_documents`](financing.md#send_leasing_release_documents) | `POST /v1/leasing/exit-documents` | test edilmedi | test edilmedi |
| [`fx.fx_currency_buy`](fx.md#fx_currency_buy) | `POST /v1/fx/buy` | test edilmedi | test edilmedi |
| [`fx.fx_currency_list`](fx.md#fx_currency_list) | `GET /v1/data/fecs` | test edildi | test edilmedi |
| [`fx.fx_currency_rates`](fx.md#fx_currency_rates) | `GET /v2/fx/rates` | test edildi | test edilmedi |
| [`fx.fx_currency_sell`](fx.md#fx_currency_sell) | `POST /v1/fx/sell` | test edilmedi | test edilmedi |
| [`fx.fx_transaction_history`](fx.md#fx_transaction_history) | `POST /v1/fx/fxtransactions` | test edilmedi | test edilmedi |
| [`hgs.hgs_balance_information`](hgs.md#hgs_balance_information) | `POST /v1/hgs/balance-info` | kısmen test edildi | test edilmedi |
| [`hgs.hgs_product_information`](hgs.md#hgs_product_information) | `POST /v1/hgs/product-info` | kısmen test edildi | test edilmedi |
| [`hgs.hgs_usage_transactions`](hgs.md#hgs_usage_transactions) | `POST /v1/hgs/usage-transactions` | kısmen test edildi | test edilmedi |
| [`information.bank_branch_list`](information.md#bank_branch_list) | `GET /v1/data/banks/{bankId}/branches` | test edilmedi | test edilmedi |
| [`information.bank_list`](information.md#bank_list) | `GET /v1/data/banks` | test edildi | test edilmedi |
| [`information.calculate_profit_share_rate`](information.md#calculate_profit_share_rate) | `POST /v1/calculateprofitsharerate` | test edildi | test edilmedi |
| [`information.central_notification`](information.md#central_notification) | `POST /v1/notification/sendInfEng` | test edilmedi | test edilmedi |
| [`information.collect_installment`](information.md#collect_installment) | `POST /v1/collections/collectInstallment` | test edilmedi | test edilmedi |
| [`information.collection_list`](information.md#collection_list) | `POST /v1/collections` | test edildi | test edilmedi |
| [`information.get_class_info`](information.md#get_class_info) | `POST /v1/erp/lms/getClassInfo` | test edildi | test edilmedi |
| [`information.iban_validation_utility`](information.md#iban_validation_utility) | `POST /v1/validation/ibanvalidator` | test edildi | test edilmedi |
| [`information.kuveyt_turk_atm_list`](information.md#kuveyt_turk_atm_list) | `GET /v1/data/atms` | test edildi | test edilmedi |
| [`information.kuveyt_turk_branch_list`](information.md#kuveyt_turk_branch_list) | `GET /v1/data/branches` | test edildi | test edilmedi |
| [`information.kuveyt_turk_xtm_list`](information.md#kuveyt_turk_xtm_list) | `GET /v1/data/xtms` | test edildi | test edilmedi |
| [`information.loan_finance_calculation_parameter`](information.md#loan_finance_calculation_parameter) | `GET /v1/data/loans` | test edilmedi | test edilmedi |
| [`moneygram.money_gram_country_list`](moneygram.md#money_gram_country_list) | `GET /v1/moneygram/countrylist` | test edildi | test edilmedi |
| [`moneygram.money_gram_currency_list`](moneygram.md#money_gram_currency_list) | `GET /v1/moneygram/currencylist` | test edildi | test edilmedi |
| [`moneygram.money_gram_get_fee`](moneygram.md#money_gram_get_fee) | `POST /v1/moneygram/getfee` | test edilmedi | test edilmedi |
| [`moneygram.money_gram_query_fee`](moneygram.md#money_gram_query_fee) | `GET /v1/moneygram/queryfee` | test edildi | test edilmedi |
| [`moneygram.money_gram_query_reference`](moneygram.md#money_gram_query_reference) | `POST /v1/moneygram/queryreference` | test edilmedi | test edilmedi |
| [`moneygram.money_gram_send`](moneygram.md#money_gram_send) | `POST /v1/moneygram/send` | test edilmedi | test edilmedi |
| [`other.calculate_welcome_participation_account_profit_share`](other.md#calculate_welcome_participation_account_profit_share) | `POST /v1/welcomeprofitsharecalculation` | test edildi | test edilmedi |
| [`other.credi_tech_intelligence_inquiry_by_credit_allocation_status`](other.md#credi_tech_intelligence_inquiry_by_credit_allocation_status) | `POST /v1/Loans/GetInquiryPermissionCheckByCreditechtReportNumber` | test edilmedi | test edilmedi |
| [`other.credit_tech_pos`](other.md#credit_tech_pos) | `POST /v1/data/credittechpos` | test edilmedi | test edilmedi |
| [`other.fraud_notifications_exists`](other.md#fraud_notifications_exists) | `POST /v1/inquiry/is-fraud-notification-exists` | test edildi | test edilmedi |
| [`other.get_fraud_notifications_last_day`](other.md#get_fraud_notifications_last_day) | `POST /v1/inquiry/get-fraud-notifications-daily` | test edildi | test edilmedi |
| [`other.get_process_design_xml_by_business_process_id`](other.md#get_process_design_xml_by_business_process_id) | `POST /v1/bpm/post/grcprocessdesignxml` | test edildi | test edilmedi |
| [`other.saglam_pay_get_customer_full_info`](other.md#saglam_pay_get_customer_full_info) | `GET /v1/get-customer-info-by-customerId-full` | test edilmedi | test edilmedi |
| [`other.visa_payment_status_notification`](other.md#visa_payment_status_notification) | `POST /v1/StatusNotify` | test edilmedi | test edilmedi |
| [`other.visa_statement_delivery`](other.md#visa_statement_delivery) | `POST /v1/StatementDelivery` | test edilmedi | test edilmedi |
| [`payment_solutions.digital_payment_get_token`](payment_solutions.md#digital_payment_get_token) | `POST /v1/vpos/digitalPaymentGetToken` | test edilmedi | test edilmedi |
| [`payment_solutions.digital_payment_query`](payment_solutions.md#digital_payment_query) | `POST /v1/vpos/digitalPaymentQuery` | test edildi | test edilmedi |
| [`payment_solutions.digital_payment_refund`](payment_solutions.md#digital_payment_refund) | `POST /v1/vpos/digitalPaymentDoRefund` | test edilmedi | test edilmedi |
| [`payment_solutions.digital_payment_send_document`](payment_solutions.md#digital_payment_send_document) | `POST /v1/vpos/sendDocument` | test edilmedi | test edilmedi |
| [`payment_solutions.pos_merchant_number_list`](payment_solutions.md#pos_merchant_number_list) | `GET /v1/pos/merchant-number` | test edildi | test edilmedi |
| [`payment_solutions.pos_transaction_details_for_tpp_v2`](payment_solutions.md#pos_transaction_details_for_tpp_v2) | `POST /v2/pos/detail-transactions` | test edilmedi | test edilmedi |
| [`payment_solutions.pos_transaction_details_v3`](payment_solutions.md#pos_transaction_details_v3) | `POST /v3/pos/detail-transactions` | kısmen test edildi | test edilmedi |
| [`payment_solutions.pos_transactions_summary_for_tpp_v2`](payment_solutions.md#pos_transactions_summary_for_tpp_v2) | `POST /v2/pos/transactions` | test edilmedi | test edilmedi |
| [`payment_solutions.pos_transactions_summary_v3`](payment_solutions.md#pos_transactions_summary_v3) | `POST /v3/pos/transactions` | kısmen test edildi | test edilmedi |
| [`payment_solutions.send_order_distribution_detail_v2`](payment_solutions.md#send_order_distribution_detail_v2) | `POST /v3/purchase/orderdistribution` | test edilmedi | test edilmedi |
| [`payment_solutions.virtual_pos`](payment_solutions.md#virtual_pos) | `POST /v1/vpos` | test edilmedi | test edilmedi |
| [`payment_solutions.virtual_pos_end_day_all_list`](payment_solutions.md#virtual_pos_end_day_all_list) | `POST /v1/vpos/endDayAllList` | test edilmedi | test edilmedi |
| [`payment_solutions.virtual_pos_end_of_day`](payment_solutions.md#virtual_pos_end_of_day) | `POST /v1/vpos/endOfDay` | test edilmedi | test edilmedi |
| [`payment_solutions.virtual_pos_general_transaction`](payment_solutions.md#virtual_pos_general_transaction) | `POST /v1/vpos/transaction` | test edilmedi | test edilmedi |
| [`payment_solutions.virtual_pos_order_filter`](payment_solutions.md#virtual_pos_order_filter) | `POST /v1/vpos/orderFilter` | test edilmedi | test edilmedi |
| [`payments.account_validation_by_account_number_for_group_money_transfer`](payments.md#account_validation_by_account_number_for_group_money_transfer) | `POST /v1/groupmoneytransfer/accountvalidation` | test edilmedi | test edilmedi |
| [`payments.account_validation_by_iban_for_group_money_transfer`](payments.md#account_validation_by_iban_for_group_money_transfer) | `POST /v1/groupmoneytransfer/account` | test edilmedi | test edilmedi |
| [`payments.account_validation_by_iban_for_group_money_transfer_v2`](payments.md#account_validation_by_iban_for_group_money_transfer_v2) | `POST /v2/groupmoneytransfer/account` | test edilmedi | test edilmedi |
| [`payments.cancel_money_transfers_from_kt_bank_to_kuveyt_turk`](payments.md#cancel_money_transfers_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/cancellist` | test edilmedi | test edilmedi |
| [`payments.check_money_transfers_status_from_kt_bank_to_kuveyt_turk`](payments.md#check_money_transfers_status_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist` | test edilmedi | test edilmedi |
| [`payments.do_stamp_duty_tax_payment_offline`](payments.md#do_stamp_duty_tax_payment_offline) | `POST /v1/tax/do-stamp-duty-tax-payment-offline` | test edilmedi | test edilmedi |
| [`payments.insert_money_transfers_from_kt_bank_to_kuveyt_turk`](payments.md#insert_money_transfers_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/insertlist` | test edilmedi | test edilmedi |
| [`payments.invoice_company_list`](payments.md#invoice_company_list) | `GET /v1/invoices/companies` | test edilmedi | test edilmedi |
| [`payments.kt_bank_error_message_list`](payments.md#kt_bank_error_message_list) | `GET /v1/groupmoneytransfer/errormessagelist` | test edilmedi | test edilmedi |
| [`payments.kuveyt_turk_branch_list_for_group_money_transfer`](payments.md#kuveyt_turk_branch_list_for_group_money_transfer) | `GET /v1/groupmoneytransfer/branchlist` | test edilmedi | test edilmedi |
| [`payments.return_money_transfers_from_kt_bank_to_kuveyt_turk`](payments.md#return_money_transfers_from_kt_bank_to_kuveyt_turk) | `POST /v1/groupmoneytransfer/incomingtransfer/returnlist` | test edilmedi | test edilmedi |
| [`payments.send_multiple_invoice_v2`](payments.md#send_multiple_invoice_v2) | `POST /v2/purchase/multipleinvoice` | test edilmedi | test edilmedi |
| [`payments.send_offer_vendor_detail`](payments.md#send_offer_vendor_detail) | `POST /v1/purchase/offervendor` | test edilmedi | test edilmedi |
| [`payments.send_order_distribution_detail`](payments.md#send_order_distribution_detail) | `POST /v1/purchase/orderdistribution` | test edilmedi | test edilmedi |
| [`payments.send_order_distribution_detail_v2`](payments.md#send_order_distribution_detail_v2) | `POST /v3/purchase/orderdistribution` | test edilmedi | test edilmedi |
| [`sgk.consume_insurance_queue`](sgk.md#consume_insurance_queue) | `POST /v1/insurance/consumeQueue` | test edilmedi | test edilmedi |
| [`sms_otp.pr_customer_validation`](sms_otp.md#pr_customer_validation) | `POST /v1/paymentrequest/customerValidation` | test edilmedi | test edilmedi |
| [`sms_otp.pr_get_account_details_by_iban`](sms_otp.md#pr_get_account_details_by_iban) | `POST /v1/paymentrequest/getAccountByIban` | test edilmedi | test edilmedi |
| [`sms_otp.pr_get_fast_result`](sms_otp.md#pr_get_fast_result) | `GET /v1/paymentrequest/getFastResult` | test edildi | test edilmedi |
| [`sms_otp.pr_payment_request_control`](sms_otp.md#pr_payment_request_control) | `POST /v1/paymentrequest/paymentControl` | test edilmedi | test edilmedi |
| [`sms_otp.pr_payment_transaction`](sms_otp.md#pr_payment_transaction) | `POST /v1/paymentrequest/transfer` | test edilmedi | test edilmedi |
| [`support.kt_incident_activity_type_list`](support.md#kt_incident_activity_type_list) | `GET /v1/incident/activityTypes` | test edilmedi | test edilmedi |
| [`support.kt_incident_cancel`](support.md#kt_incident_cancel) | `POST /v1/incident/cancel` | test edilmedi | test edilmedi |
| [`support.kt_incident_creation`](support.md#kt_incident_creation) | `POST /v1/incident/operation/create` | test edilmedi | test edilmedi |
| [`support.kt_incident_creation_by_company`](support.md#kt_incident_creation_by_company) | `POST /v1/company/incident/create` | test edilmedi | test edilmedi |
| [`support.kt_incident_defined_document_list`](support.md#kt_incident_defined_document_list) | `GET /v1/incident/defiendDocuments` | test edilmedi | test edilmedi |
| [`support.kt_incident_info`](support.md#kt_incident_info) | `POST /v1/incident/information/info` | test edilmedi | test edilmedi |
| [`support.kt_incident_insert_activity`](support.md#kt_incident_insert_activity) | `POST /v1/incident/insertActivity` | test edilmedi | test edilmedi |
| [`support.kt_incident_insert_document`](support.md#kt_incident_insert_document) | `POST /v1/incident/insertDocument` | test edilmedi | test edilmedi |
| [`support.kt_incident_neova_info`](support.md#kt_incident_neova_info) | `POST /v1/incident/neova/info` | test edilmedi | test edilmedi |
| [`support.kt_incident_neova_list`](support.md#kt_incident_neova_list) | `POST /v1/incident/neova/list` | test edilmedi | test edilmedi |
| [`support.kt_incident_neova_update`](support.md#kt_incident_neova_update) | `POST /v1/incident/neova/update` | test edilmedi | test edilmedi |
| [`support.kt_incident_optional_field_list`](support.md#kt_incident_optional_field_list) | `POST /v1/incident/optionalFieldList` | test edilmedi | test edilmedi |
| [`support.kt_incident_product_list`](support.md#kt_incident_product_list) | `GET /v1/incident/information/products` | test edilmedi | test edilmedi |
| [`support.kt_incident_reopen`](support.md#kt_incident_reopen) | `POST /v1/incident/reopen` | test edilmedi | test edilmedi |
| [`tpp_accounts.account_list_v2`](tpp_accounts.md#account_list_v2) | `GET /v2/accounts` | test edildi | test edilmedi |
| [`tpp_accounts.account_list_with_suffix_v2`](tpp_accounts.md#account_list_with_suffix_v2) | `GET /v2/accounts/{suffix}` | test edilmedi | test edilmedi |
| [`tpp_accounts.account_transactions_v2`](tpp_accounts.md#account_transactions_v2) | `GET /v2/accounts/{suffix}/transactions` | test edildi | test edilmedi |
| [`tpp_accounts.receipt_v1`](tpp_accounts.md#receipt_v1) | `GET /v1/accounts/{suffix}/transactions/{businessKey}` | test edildi | test edilmedi |
| [`tpp_accounts.receipt_v2`](tpp_accounts.md#receipt_v2) | `POST /v2/accounts/transactions/receipts` | test edildi | test edilmedi |
| [`transfers.cash_withdrawal_from_atm_via_qr_code`](transfers.md#cash_withdrawal_from_atm_via_qr_code) | `POST /v1/transfers/fromATMByQRCode` | test edilmedi | test edilmedi |
| [`transfers.customer_iban_info_for_money_transfer`](transfers.md#customer_iban_info_for_money_transfer) | `GET /v1/moneytransfer/{iban}/customeribaninfo` | test edildi | test edilmedi |
| [`transfers.internal_money_transfer`](transfers.md#internal_money_transfer) | `POST /v1/moneytransfer/interbankmoneytransfer` | test edilmedi | test edilmedi |
| [`transfers.investment_account_activities_report`](transfers.md#investment_account_activities_report) | `POST /v1/investment/report-for-account-activities` | test edildi | test edilmedi |
| [`transfers.money_transfer_payment_type`](transfers.md#money_transfer_payment_type) | `POST /v1/moneytransfer/paymenttype` | test edilmedi | test edilmedi |
| [`transfers.money_transfer_state`](transfers.md#money_transfer_state) | `GET /v1/moneytransfer-state` | test edildi | test edilmedi |
| [`transfers.money_transfer_to_gsm`](transfers.md#money_transfer_to_gsm) | `POST /v1/transfers/toGSM` | test edilmedi | test edilmedi |
| [`transfers.outgoing_money_transfer`](transfers.md#outgoing_money_transfer) | `POST /v1/moneytransfer/outgoingmoneytransfer` | kısmen test edildi | test edilmedi |
| [`transfers.outgoing_money_transfer_v2`](transfers.md#outgoing_money_transfer_v2) | `POST /v2/moneytransfer/outgoingmoneytransfer` | test edilmedi | test edilmedi |
| [`transfers.transaction_validation_list`](transfers.md#transaction_validation_list) | `GET /v1/transactionvalidation/transactionlist` | kısmen test edildi | test edilmedi |
| [`treasury.fx_and_precious_metal_rates`](treasury.md#fx_and_precious_metal_rates) | `GET /v1/fx/rates` | test edildi | test edilmedi |
| [`treasury.fx_and_precious_metals_transaction_history`](treasury.md#fx_and_precious_metals_transaction_history) | `POST /v1/fx/fxtransactions` | test edilmedi | test edilmedi |
| [`treasury.precious_metal_buy`](treasury.md#precious_metal_buy) | `POST /v1/preciousmetal/buy` | test edilmedi | test edilmedi |
| [`treasury.precious_metal_rates`](treasury.md#precious_metal_rates) | `GET /v1/preciousmetal/rates` | test edildi | test edilmedi |
| [`treasury.precious_metal_sell`](treasury.md#precious_metal_sell) | `POST /v1/preciousmetal/sell` | test edilmedi | test edilmedi |
| [`vpos.add_card_to_merchant_safe`](vpos.md#add_card_to_merchant_safe) | `POST /v1/vpos/addCardToMerchantSafe` | test edilmedi | test edilmedi |
| [`vpos.digital_payment_commission_reconciliation`](vpos.md#digital_payment_commission_reconciliation) | `POST /v1/vpos/commissionReconciliation` | test edilmedi | test edilmedi |
| [`vpos.get_customer_by_safe_key`](vpos.md#get_customer_by_safe_key) | `POST /v1/vpos/getCustomerBySafeKey` | test edilmedi | test edilmedi |
| [`vpos.get_seller_order_details`](vpos.md#get_seller_order_details) | `POST /v1/vpos/getMerchantOrderDetail` | kısmen test edildi | test edilmedi |
| [`vpos.non_3_d_payment`](vpos.md#non_3_d_payment) | `POST /v1/vpos/non3DPayment` | test edilmedi | test edilmedi |
| [`vpos.non_three_d_payment_by_merchant_safe`](vpos.md#non_three_d_payment_by_merchant_safe) | `POST /v1/vpos/nonThreeDPaymentByMerchantSafe` | test edilmedi | test edilmedi |
| [`vpos.order_detail_with_payment_id`](vpos.md#order_detail_with_payment_id) | `POST /v1/vpos/orderDetailWithPaymentId` | kısmen test edildi | test edilmedi |
| [`vpos.payment_order_reversal`](vpos.md#payment_order_reversal) | `POST /v1/vpos/paymentOrderReversal` | test edilmedi | test edilmedi |
| [`vpos.pre_authorization`](vpos.md#pre_authorization) | `POST /v1/vpos/preAuthorization` | test edilmedi | test edilmedi |
| [`vpos.recurring_non_three_d_payment`](vpos.md#recurring_non_three_d_payment) | `POST /v1/vpos/recurringNonThreeDPayment` | test edilmedi | test edilmedi |
| [`vpos.sale_order_reversal`](vpos.md#sale_order_reversal) | `POST /v1/vpos/saleOrderReversal` | test edilmedi | test edilmedi |
| [`vpos.secure_partner_payment`](vpos.md#secure_partner_payment) | `POST /v1/vpos/secureCommonPaymentToken` | test edilmedi | test edilmedi |
| [`vpos.threee_d_payment`](vpos.md#threee_d_payment) | `POST /v1/vpos/threeDPayment` | test edilmedi | test edilmedi |
| [`vpos.virtual_pos_non_three_d_payment`](vpos.md#virtual_pos_non_three_d_payment) | `POST /v1/vpos/nonThreeDPayment` | test edilmedi | test edilmedi |
| [`vpos.virtual_pos_sale_reversal`](vpos.md#virtual_pos_sale_reversal) | `POST /v1/vpos/saleReversal` | test edilmedi | test edilmedi |
| [`your_banking.your_banking_account_application`](your_banking.md#your_banking_account_application) | `POST /v1/yourbank/accountApplications` | test edilmedi | test edilmedi |
| [`your_banking.your_banking_account_application_documents`](your_banking.md#your_banking_account_application_documents) | `POST /v1/yourbank/accountApplicationDocuments` | test edilmedi | test edilmedi |
| [`your_banking.your_banking_account_application_sms_validation`](your_banking.md#your_banking_account_application_sms_validation) | `POST /v1/yourbank/accountSmsOtp` | test edilmedi | test edilmedi |
| [`your_banking.your_banking_account_application_status_query`](your_banking.md#your_banking_account_application_status_query) | `POST /v1/yourbank/accountApplicationStatus` | test edildi | test edilmedi |
