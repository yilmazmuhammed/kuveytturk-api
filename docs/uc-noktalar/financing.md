<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.financing

Finansman çözümleri · 16 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`corporate_app_agreement_v2`](#corporate_app_agreement_v2) | `GET /v2/corporateAppAgreementData` | CC |
| [`corporate_credit_card_application`](#corporate_credit_card_application) | `POST /v2/corporateCreditCardApplication` | CC |
| [`credit_limit_request`](#credit_limit_request) | `GET /v1/loans/allotmentLimit` | AC |
| [`customer_current_credit_allocation_flow_information`](#customer_current_credit_allocation_flow_information) | `POST /v1/Loans/GetLatestRouteHistoryByAccountNumber` | CC |
| [`customer_suited_card_list`](#customer_suited_card_list) | `GET /v2/customerSuitedCardList` | CC |
| [`get_digital_channel_card_application_list_v2`](#get_digital_channel_card_application_list_v2) | `GET /v2/cardApplicationList` | CC |
| [`individual_app_agreement_v2`](#individual_app_agreement_v2) | `GET /v2/individualAppAgreement` | CC |
| [`individual_credit_card_application_v2`](#individual_credit_card_application_v2) | `POST /v2/individualCreditCardApplication` | CC |
| [`loan_finance_calculation`](#loan_finance_calculation) | `GET /v1/calculations/loan` | CC |
| [`loan_finance_info`](#loan_finance_info) | `GET /v1/loans/{projectNumber}/info` | AC |
| [`loan_finance_installments`](#loan_finance_installments) | `GET /v1/loans/{projectNumber}/installments` | AC |
| [`loan_finance_list`](#loan_finance_list) | `GET /v1/loans` | AC |
| [`loans_price_list`](#loans_price_list) | `GET /v1/loans/pricelist` | CC |
| [`send_leasing_confirmation_form`](#send_leasing_confirmation_form) | `POST /v1/leasing/confirmation-form` | CC |
| [`send_leasing_current_account_file`](#send_leasing_current_account_file) | `POST /v1/leasing/current-documents` | CC |
| [`send_leasing_release_documents`](#send_leasing_release_documents) | `POST /v1/leasing/exit-documents` | CC |

## `corporate_app_agreement_v2` { #corporate_app_agreement_v2 }

**Corporate App Agreement V2** · `GET /v2/corporateAppAgreementData` · kapsam `cards` · client credentials

!!! note "Dokümandaki durum: COMING_SOON"

This API is used to retrieve credit card agreement documents before submitting a corporate credit card application. The service fetches the related corporate agreement data using the customer number, product code, language information, and application date, and returns the agreement contents in Base64 format.

```python
yanit = kt.financing.corporate_app_agreement_v2(customer_number=..., language_id=..., product_code=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | sorgu | tam sayı | evet | Customer number for which corporate credit card agreements will be retrieved. |
| `language_id` | `languageId` | sorgu | tam sayı | evet | Language information used to return agreement documents. |
| `application_date_time` | `applicationDateTime` | sorgu | metin |  | Application date information. Format: yyyy-MM-dd. |
| `product_code` | `productCode` | sorgu | metin | evet | Credit card product code for which agreement documents will be retrieved. |

Yanıt alanları (dokümana göre): `agreementListContract`, `agreementData`, `agreementDataName`, `interestFreeContractID`, `apiExecutionContract`, `errors`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-app-agreement-v2)

## `corporate_credit_card_application` { #corporate_credit_card_application }

**Corporate Credit Card Application** · `POST /v2/corporateCreditCardApplication` · kapsam `cards` · client credentials

!!! note "Dokümandaki durum: COMING_SOON"

This API is used to submit and save a corporate credit card application in BOA. The service receives information such as the selected card product, statement day, card delivery address, installment information, digital slip preference, and related customer details to initiate the corporate credit card application process.

```python
yanit = kt.financing.corporate_credit_card_application(customer_number=..., digital_slip_choice=..., statement_day=..., product_code=..., statement_delivery_type=..., card_sending_address_id=..., product_number=..., installment_count=..., suffix_customer_id=..., required_rate=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | gövde | tam sayı | evet | Main customer number for which the corporate credit card application will be submitted. |
| `digital_slip_choice` | `digitalSlipChoice` | gövde | metin | evet | Digital slip preference. |
| `statement_day` | `statementDay` | gövde | metin | evet | Selected statement day. |
| `product_code` | `productCode` | gövde | metin | evet | Credit card product code selected for the application. |
| `statement_delivery_type` | `statementDeliveryType` | gövde | metin | evet | Statement delivery type. |
| `card_sending_address_id` | `cardSendingAddressId` | gövde | tam sayı | evet | BOA address ID where the card will be delivered. |
| `product_number` | `productNumber` | gövde | metin | evet | Credit card product number selected for the application. |
| `installment_count` | `installmentCount` | gövde | tam sayı | evet | Installment count for the corporate card application. |
| `suffix_customer_id` | `suffixCustomerId` | gövde | tam sayı | evet | Related individual/additional customer number associated with the corporate customer. |
| `required_rate` | `requiredRate` | gövde | tam sayı | evet | Requested rate information for the corporate application. |

Yanıt alanları (dokümana göre): `insertedMainAppRecordId`, `insertedSuppAppRecordId`, `errors`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/corporate-credit-card-application)

## `credit_limit_request` { #credit_limit_request }

**Credit Limit Request** · `GET /v1/loans/allotmentLimit` · kapsam `loans` · authorization code (müşteri girişi gerekir)

You can request the customer''s (sent via token) credit limits in the bank. You can learn about top limits, product limits, and product collateral limits.

```python
yanit = kt.financing.credit_limit_request()
```

Yanıt alanları (dokümana göre): `accountNumber`, `status`, `AllotmentStatusName`, `maturityDate`, `tranDate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/credit-limit-request)

## `customer_current_credit_allocation_flow_information` { #customer_current_credit_allocation_flow_information }

**Customer Current Credit Allocation Flow Information** · `POST /v1/Loans/GetLatestRouteHistoryByAccountNumber` · kapsam `loans` · client credentials

Retrieves the latest route history records for the specified account number. The response includes allotment, authority, status, workflow, action, and user information related to the latest credit allocation route history.

```python
yanit = kt.financing.customer_current_credit_allocation_flow_information(account_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `account_number` | `accountNumber` | gövde | tam sayı | evet | Account number used to retrieve the latest route history records. |

Yanıt alanları (dokümana göre): `accountNumber`, `authorityType`, `status`, `allotmentId`, `allotmentMainId`, `credereArtReportNumber`, `wFInstanceId`, `name`, `actionName`, `userCode`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-current-credit-allocation-flow-information)

## `customer_suited_card_list` { #customer_suited_card_list }

**Customer Suited Card List** · `GET /v2/customerSuitedCardList` · kapsam `cards` · client credentials

!!! note "Dokümandaki durum: COMING_SOON"

This API is used to list eligible individual and/or corporate credit card products that the customer can apply for. The service returns suitable card products, statement options, card delivery types, and the customer’s address and email information that can be used during the application process.

```python
yanit = kt.financing.customer_suited_card_list(customer_number=..., language_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | sorgu | tam sayı | evet | Customer number for which eligible credit card products will be queried. |
| `language_id` | `languageId` | sorgu | tam sayı | evet | Language information used to return product and parameter descriptions. |

Yanıt alanları (dokümana göre): `addressList`, `addressText`, `addressId`, `addressTypeName`, `apartmentNumber`, `emailAddressList`, `emailAddress`, `emailId`, `eligibleCCApplicationContract`, `isIndividualCard`, `immediateProductCode`, `productName`, `productCode`, `productNumber`, `minimumInstallment`, `maximumInstallment`, `statementContractList`, `statementDay`, `statementDayDescription`, `digitalSlipChoiceList`, `paramCode`, `paramDescription`, `paramValue`, `statementDeliveryTypeList`, `statementType`, `statementDescription`, `ecomChoiceList`, `cardSendingTypeList`, `errors`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/customer-suited-card-list)

## `get_digital_channel_card_application_list_v2` { #get_digital_channel_card_application_list_v2 }

**Get Digital Channel Card Application List V2** · `GET /v2/cardApplicationList` · kapsam `cards` · client credentials

!!! note "Dokümandaki durum: COMING_SOON"

This API is used to list the customer’s individual or corporate credit card application history. The service retrieves credit card applications submitted through digital channels based on the customer number, language information, and date range, and returns the application tracking details.

```python
yanit = kt.financing.get_digital_channel_card_application_list_v2(customer_number=..., language_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | sorgu | tam sayı | evet | Customer number for which credit card application history will be queried. |
| `language_id` | `languageId` | sorgu | tam sayı | evet | Language information used to return application details. |
| `search_begin_date` | `searchBeginDate` | sorgu | metin |  | Application search start date. Format: yyyy-MM-dd. |
| `search_end_date` | `searchEndDate` | sorgu | metin |  | Application search end date. Format: yyyy-MM-dd. |

Yanıt alanları (dokümana göre): `embossBranch`, `embossCompanytransferDate`, `courierGivenDate`, `printDate`, `virtualCardDemandedFlag`, `hasSupplementaryCard`, `deliveryInquiryFlag`, `shadowCardNumber`, `isDebit`, `productCode`, `isIndividual`, `applicationDate`, `productName`, `statusCode`, `statusDescription`, `sendingAddress`, `preferredLimit`, `confirmedLimit`, `supplementaryCardFlag`, `errors`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/get-digital-channel-card-application-list-v2)

## `individual_app_agreement_v2` { #individual_app_agreement_v2 }

**Individual App Agreement V2** · `GET /v2/individualAppAgreement` · kapsam `cards` · client credentials

!!! note "Dokümandaki durum: COMING_SOON"

This API is used to retrieve credit card agreement documents before submitting an individual credit card application. The service fetches the related agreement data using the customer number and product code, and returns the agreement contents in Base64 format.

```python
yanit = kt.financing.individual_app_agreement_v2(customer_number=..., product_code=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | sorgu | tam sayı | evet | Customer number for which individual credit card agreements will be retrieved. |
| `product_code` | `productCode` | sorgu | metin | evet | Credit card product code for which agreement documents will be retrieved. |

Yanıt alanları (dokümana göre): `agreementListContract`, `agreementData`, `agreementDataName`, `interestFreeContractID`, `apiExecutionContract`, `errors`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-app-agreement-v2)

## `individual_credit_card_application_v2` { #individual_credit_card_application_v2 }

**Individual Credit Card Application V2** · `POST /v2/individualCreditCardApplication` · kapsam `cards` · client credentials

!!! note "Dokümandaki durum: COMING_SOON"

This API is used to submit and save an individual credit card application in BOA. The service receives information such as customer number, selected card product, statement day, card delivery address, email information, digital slip preference, monthly income, and job start year to initiate the individual credit card application process.

```python
yanit = kt.financing.individual_credit_card_application_v2(customer_number=..., card_sending_address_id=..., product_code=..., product_number=..., statement_day=..., monthly_net_income=..., statement_delivery_type=..., digital_slip_choice=..., email_id=..., email=..., job_starting_year=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_number` | `customerNumber` | gövde | tam sayı | evet | Customer number for which the individual credit card application will be submitted. |
| `card_sending_address_id` | `cardSendingAddressId` | gövde | tam sayı | evet | BOA address ID where the card will be delivered. |
| `product_code` | `productCode` | gövde | metin | evet | Credit card product code selected for the application. |
| `product_number` | `productNumber` | gövde | metin | evet | Credit card product number selected for the application. |
| `statement_day` | `statementDay` | gövde | metin | evet | Selected statement day. |
| `monthly_net_income` | `monthlyNetIncome` | gövde | tam sayı | evet | Customer’s monthly net income information. |
| `statement_delivery_type` | `statementDeliveryType` | gövde | metin | evet | Statement delivery type. |
| `digital_slip_choice` | `digitalSlipChoice` | gövde | metin | evet | Digital slip preference. |
| `email_id` | `emailId` | gövde | tam sayı | evet | BOA email record ID to be used in the application. |
| `email` | `email` | gövde | metin | evet | Email address to be used in the application. |
| `job_starting_year` | `jobStartingYear` | gövde | tam sayı | evet | Customer’s job starting year information. |

Yanıt alanları (dokümana göre): `insertedRecordId`, `errors`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/individual-credit-card-application-v2)

## `loan_finance_calculation` { #loan_finance_calculation }

**Loan/Finance Calculation** · `GET /v1/calculations/loan` · kapsam `public` · client credentials

Calculates the loan repayment plan according to the provided product type, installment count, funding amount, and calculation preference. The response includes monthly profit rate, total installment amount, total profit amount, tax amounts, and installment details.

```python
yanit = kt.financing.loan_finance_calculation(product_code=..., installment_count=..., funding_amount=..., is_total_amount_by_installment_amount=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `product_code` | `ProductCode` | sorgu | metin | evet | Product type code used for the loan calculation. |
| `installment_count` | `InstallmentCount` | sorgu | tam sayı | evet | Number of installments to be used in the repayment plan. |
| `funding_amount` | `FundingAmount` | sorgu | sayı | evet | Loan funding amount to be calculated. |
| `is_total_amount_by_installment_amount` | `IsTotalAmountByInstallmentAmount` | sorgu | bool | evet | Indicates whether the calculation will be performed based on installment amount. |

Yanıt alanları (dokümana göre): `monthlyProfitRate`, `fundingAmount`, `installmentCount`, `totalInstallmentAmount`, `totalProfitAmount`, `totalRUSFAmount`, `totalBITTAmount`, `installments`, `order`, `amount`, `principalAmount`, `profitAmount`, `bittAmount`, `rusfAmount`, `remainingPrincipalAmount`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-calculation)

## `loan_finance_info` { #loan_finance_info }

**Loan/Finance Info** · `GET /v1/loans/{projectNumber}/info` · kapsam `loans` · authorization code (müşteri girişi gerekir)

Returns a loan belong to given account and project number.

```python
yanit = kt.financing.loan_finance_info(project_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `project_number` | `projectNumber` | yol | tam sayı | evet | Represents the procy identifier number. |

Yanıt alanları (dokümana göre): `productName`, `projectNumber`, `type`, `fxCode`, `projectStartDate`, `projectFinishDate`, `totalLoanAmount`, `loanAmount`, `remainDebt`, `paymentStatus`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-info)

## `loan_finance_installments` { #loan_finance_installments }

**Loan/Finance Installments** · `GET /v1/loans/{projectNumber}/installments` · kapsam `loans` · authorization code (müşteri girişi gerekir)

Returns list of installments belonging to the given project (each loan is considered as a project) number.

```python
yanit = kt.financing.loan_finance_installments(project_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `project_number` | `projectNumber` | yol | tam sayı | evet | Indicates the project number (Project number is the ID-code given to each loan). |

Yanıt alanları (dokümana göre): `installmentNumber`, `fxCode`, `paymentStatus`, `maturityDate`, `installmentAmount`, `paymentAmount`, `collectedBITTAmount`, `collectedPrincipalAmount`, `collectedProfitAmount`, `collectedRUSFAmount`, `collectedVATAmount`, `installmentRemaining`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-installments)

## `loan_finance_list` { #loan_finance_list }

**Loan/Finance List** · `GET /v1/loans` · kapsam `loans` · authorization code (müşteri girişi gerekir)

Returns a list of loans belonging to the given account number.

```python
yanit = kt.financing.loan_finance_list()
```

Yanıt alanları (dokümana göre): `productName`, `projectNumber`, `type`, `fxCode`, `projectStartDate`, `projectFinishDate`, `totalLoanAmount`, `loanAmount`, `remainDebt`, `paymentStatus`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loan-finance-list)

## `loans_price_list` { #loans_price_list }

**Loans Price List** · `GET /v1/loans/pricelist` · kapsam `loans` · client credentials

Provides information about the prices of loan product information.

```python
yanit = kt.financing.loans_price_list(product_type=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `product_type` | `productType` | sorgu | tam sayı | evet | Refers to the loan product type. The expected values are from 1 to 3. |

Yanıt alanları (dokümana göre): `productName`, `nonPaymentPeriod`, `bITTRate`, `commissionRate`, `expertiseAmount`, `vehiclePledgeAmount`, `hypothecAmount`, `customerTypeDescription`, `pricingInfoList`, `MinMaturity`, `Maturity`, `ListPriceRate`, `VarianceNo`, `UpdateDate`, `bankName`, `productTypeName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/loans-price-list)

## `send_leasing_confirmation_form` { #send_leasing_confirmation_form }

**Send Leasing Confirmation Form** · `POST /v1/leasing/confirmation-form` · kapsam `loans` · client credentials

Receives the leasing confirmation form together with the related reference, transaction amount, customs tax amount, and customs firm information. The response returns the operation result for the confirmation form submission.

```python
yanit = kt.financing.send_leasing_confirmation_form(reference_number=..., transaction_amount=..., customs_tax_amount=..., confirmation_form=..., customs_firm_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_number` | `referenceNumber` | gövde | tam sayı | evet | Reference number associated with the leasing transaction. |
| `transaction_amount` | `transactionAmount` | gövde | sayı | evet | Transaction amount of the leasing operation. |
| `customs_tax_amount` | `customsTaxAmount` | gövde | sayı | evet | Customs tax amount related to the leasing transaction. |
| `confirmation_form` | `confirmationForm` | gövde | metin | evet | Confirmation form content or reference information submitted for the leasing transaction. |
| `customs_firm_id` | `customsFirmId` | gövde | tam sayı | evet | Identifier of the customs firm related to the leasing transaction. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-confirmation-form)

## `send_leasing_current_account_file` { #send_leasing_current_account_file }

**Send Leasing Current Account File** · `POST /v1/leasing/current-documents` · kapsam `loans` · client credentials

Receives the leasing current account document and import file closing document for the specified reference number. The response returns the operation result for the document submission.

```python
yanit = kt.financing.send_leasing_current_account_file(reference_number=..., current_excel=..., import_file_closing=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_number` | `referenceNumber` | gövde | tam sayı | evet | Reference number associated with the leasing transaction. |
| `current_excel` | `currentExcel` | gövde | metin | evet | Current account Excel document content or reference information submitted for the leasing transaction. |
| `import_file_closing` | `importFileClosing` | gövde | metin | evet | Import file closing document content or reference information submitted for the leasing transaction. |

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-current-account-file)

## `send_leasing_release_documents` { #send_leasing_release_documents }

**Send Leasing Release Documents** · `POST /v1/leasing/exit-documents` · kapsam `loans` · client credentials

Receives leasing release documents for the specified reference number. The request may include invoice, customs declaration, exit Excel, tax payment receipt, invoice list, customs declaration list, and exit information details. The response returns the operation result for the document submission.

```python
yanit = kt.financing.send_leasing_release_documents(reference_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_number` | `ReferenceNumber` | gövde | tam sayı | evet | Reference number associated with the leasing transaction. |
| `invoice` | `Invoice` | gövde | metin |  | Invoice document content or reference information submitted for the leasing transaction. |
| `customs_declaration` | `CustomsDeclaration` | gövde | metin |  | Customs declaration document content or reference information submitted for the leasing transaction. |
| `exit_excel` | `ExitExcel` | gövde | metin |  | Exit Excel document content or reference information submitted for the leasing transaction. |
| `tax_payment_receipt` | `TaxPaymentReceipt` | gövde | metin |  | Tax payment receipt document content or reference information submitted for the leasing transaction. |
| `invoice_list` | `InvoiceList` | gövde | liste |  | List of invoice records related to the leasing release documents. |
| `customs_declaration_list` | `CustomsDeclarationList` | gövde | liste |  | List of customs declaration records related to the leasing release documents. |
| `exit_information_list` | `ExitInformationList` | gövde | liste |  | List of exit information records related to the leasing release documents. |

Gövde alanları istekte `document` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/financing-solutions/send-leasing-release-documents)
