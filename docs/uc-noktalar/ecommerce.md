<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.ecommerce

E-ticaret · 10 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`ecommerce_application_refund_v1`](#ecommerce_application_refund_v1) | `POST /v1/lendings/{applicationId}/refund` | CC | test edilmedi | test edilmedi |
| [`ecommerce_application_refund_v1_2`](#ecommerce_application_refund_v1_2) | `POST /v1/lendings/{applicationId}/refund` | CC | test edilmedi | test edilmedi |
| [`ecommerce_get_lending_information_v1`](#ecommerce_get_lending_information_v1) | `GET /v1/lendings/{applicationId}` | CC | test edilmedi | test edilmedi |
| [`ecommerce_get_lending_information_v1_2`](#ecommerce_get_lending_information_v1_2) | `GET /v1/lendings/{applicationId}` | CC | test edilmedi | test edilmedi |
| [`ecommerce_lendings_v1`](#ecommerce_lendings_v1) | `POST /v1/lendings` | CC | test edilmedi | test edilmedi |
| [`ecommerce_lendings_v1_2`](#ecommerce_lendings_v1_2) | `POST /v1/lendings` | CC | test edilmedi | test edilmedi |
| [`ecommerce_monthly_payments_v1`](#ecommerce_monthly_payments_v1) | `POST /v1/query/monthly-payments` | CC | test edildi | test edilmedi |
| [`ecommerce_monthly_payments_v1_2`](#ecommerce_monthly_payments_v1_2) | `POST /v1/query/monthly-payments` | CC | test edildi | test edilmedi |
| [`ecommerce_pre_approved_monthly_payments_v1`](#ecommerce_pre_approved_monthly_payments_v1) | `POST /v1/query/pre-approved-monthly-payments` | CC | test edildi | test edilmedi |
| [`ecommerce_pre_approved_monthly_payments_v1_2`](#ecommerce_pre_approved_monthly_payments_v1_2) | `POST /v1/query/pre-approved-monthly-payments` | CC | test edildi | test edilmedi |

## `ecommerce_application_refund_v1` { #ecommerce_application_refund_v1 }

**Ecommerce Application Refund** · `POST /v1/lendings/{applicationId}/refund` · kapsam `digital_payments` · client credentials

Allows partial or full refund of funding.

```python
yanit = kt.ecommerce.ecommerce_application_refund_v1(application_id=..., reference_id=..., refund_type=..., refund_amount=..., order_date=..., order_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `application_id` | `applicationId` | yol | metin | evet |  |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique ID number of the request |
| `refund_type` | `refundType` | gövde | metin | evet | Full or partial refund. Enum: [ FULL, PARTIAL ]. |
| `refund_amount` | `refundAmount` | gövde | sayı | evet | Refund amount. |
| `order_date` | `orderDate` | gövde | tam sayı | evet | Date of the returned order |
| `order_id` | `orderId` | gövde | metin | evet | Id of the returned order. |
| `promotion_id` | `promotionId` | gövde | tam sayı |  | Preset id for applied promotion |

Yanıt alanları (dokümana göre): `isSuccess`, `responseCode`, `responseMessage`, `bankReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund)

## `ecommerce_application_refund_v1_2` { #ecommerce_application_refund_v1_2 }

**Ecommerce Application Refund** · `POST /v1/lendings/{applicationId}/refund` · kapsam `digital_payments` · client credentials

This API performs a refund transaction for a lending application. The refund is processed using the specified application id, company information, reference information and refund details.

```python
yanit = kt.ecommerce.ecommerce_application_refund_v1_2(application_id=..., x_company_id=..., x_sub_company_id=..., reference_id=..., refund_type=..., refund_amount=..., order_date=..., order_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `application_id` | `applicationId` | yol | metin | evet | Unique lending application identifier for which the refund will be processed. |
| `x_company_id` | `x-company-id` | gövde | metin | evet | Company identifier used to determine the company initiating the refund request. |
| `x_sub_company_id` | `x-sub-company-id` | gövde | tam sayı | evet | Sub-company identifier used to determine the related sub-company for the refund request. |
| `application_id_` | `applicationId` | gövde | metin |  |  |
| `reference_id` | `referenceId` | gövde | metin | evet | Reference identifier of the refund transaction. |
| `refund_type` | `refundType` | gövde | metin | evet | Type of the refund transaction. |
| `refund_amount` | `refundAmount` | gövde | sayı | evet | Amount to be refunded. |
| `order_date` | `orderDate` | gövde | tam sayı | evet | Order date related to the refund transaction. |
| `order_id` | `orderId` | gövde | metin | evet | Order identifier related to the refund transaction. |
| `promotion_id` | `promotionId` | gövde | metin |  | Promotion identifier related to the refund transaction. |
| `invoice_number` | `invoiceNumber` | gövde | metin |  | Invoice number related to the refund transaction. |

Yanıt alanları (dokümana göre): `isSuccess`, `responseCode`, `responseMessage`, `bankReferenceId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-application-refund)

## `ecommerce_get_lending_information_v1` { #ecommerce_get_lending_information_v1 }

**Ecommerce Get Lending Information** · `GET /v1/lendings/{applicationId}` · kapsam `digital_payments` · client credentials

Its purpose is to question the details of the loan applied for.

```python
yanit = kt.ecommerce.ecommerce_get_lending_information_v1(application_id=..., applicaction_id=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | parametre değeri bilinmiyor — yol parametresi: applicationId | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `application_id` | `applicationId` | yol | metin | evet |  |
| `applicaction_id` | `applicactionId` | sorgu | metin | evet | Application Number |

Yanıt alanları (dokümana göre): `applicationId`, `isApproved`, `applicationDate`, `responseCode`, `responseMessage`, `type`, `allocationInformation`, `isSuccess`, `allocationDate`, `totalRefundAmount`, `refundHistory`, `referenceId`, `bankReferenceId`, `refundDate`, `refundType`, `refundAmount`, `paymentPlan`, `lendingAmount`, `interestRate`, `term`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `monthlyPayments`, `amount`, `dueDate`, `isPaid`, `paymentDate`, `details`, `name`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information)

## `ecommerce_get_lending_information_v1_2` { #ecommerce_get_lending_information_v1_2 }

**Ecommerce Get Lending Information** · `GET /v1/lendings/{applicationId}` · kapsam `digital_payments` · client credentials

This API retrieves the details of a lending application by application id. The response includes application status, invoice information, allocation information, refund history, payment plan and digital onboarding information.

```python
yanit = kt.ecommerce.ecommerce_get_lending_information_v1_2(application_id=..., client_id=..., x_sub_company_id=..., date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | parametre değeri bilinmiyor — yol parametresi: applicationId | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `application_id` | `applicationId` | yol | metin | evet | Unique lending application identifier to be queried. |
| `client_id` | `client_id` | sorgu | metin | evet | Client identifier used to determine the company initiating the request. |
| `x_sub_company_id` | `x-sub-company-id` | sorgu | tam sayı | evet | Sub-company identifier used to determine the related sub-company for the request. |
| `date` | `date` | sorgu | metin | evet | Date parameter used to query the lending application details. |

Yanıt alanları (dokümana göre): `applicationId`, `isApproved`, `isInvoiceApproved`, `applicationDate`, `responseCode`, `responseMessage`, `type`, `isActiveCustomer`, `isDigitalChannelCustomer`, `allocationInformation`, `isSuccess`, `allocationDate`, `refundInformation`, `totalRefundAmount`, `refundHistory`, `referenceId`, `bankReferenceId`, `refundDate`, `refundType`, `refundAmount`, `invoiceInformation`, `invoiceStatus`, `invoiceDescription`, `paymentPlan`, `lendingAmount`, `interestRate`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `monthlyEffectiveInterestRate`, `term`, `monthlyPayments`, `amount`, `dueDate`, `isPaid`, `paymentDate`, `details`, `name`, `digitalOnboardingInformation`, `completedDate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-get-lending-information)

## `ecommerce_lendings_v1` { #ecommerce_lendings_v1 }

**Ecommerce Lendings** · `POST /v1/lendings` · kapsam `digital_payments` · client credentials

Allows you to apply for funding.

```python
yanit = kt.ecommerce.ecommerce_lendings_v1(reference_id=..., pre_approved_application_id=..., national_identity_number=..., gsm_number=..., total_term=..., type=..., time_to_live=..., order_id=..., cart=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique ID number of the request |
| `pre_approved_application_id` | `preApprovedApplicationId` | gövde | metin | evet | Pre-approved funding application number. |
| `callback_url` | `callbackUrl` | gövde | metin |  | URL to return after financing disbursement |
| `national_identity_number` | `nationalIdentityNumber` | gövde | metin | evet | National identification number. |
| `birthdate` | `birthdate` | gövde | metin |  |  |
| `gsm_number` | `gsmNumber` | gövde | metin | evet | Customer's confirmed mobile phone number. |
| `total_term` | `totalTerm` | gövde | tam sayı | evet | Total term. |
| `type` | `type` | gövde | metin | evet | Selected financing type. |
| `time_to_live` | `timeToLive` | gövde | tam sayı | evet | The lifetime of the basket. It should be used and returned within this period. |
| `order_id` | `orderId` | gövde | metin | evet | Order number. |
| `promotion_id` | `promotionId` | gövde | tam sayı |  | Predetermined id for the promotion to be applied |
| `cart` | `cart` | gövde | nesne | evet | Contains price and cart product information. |

Yanıt alanları (dokümana göre): `applicationId`, `isApproved`, `applicationDate`, `responseCode`, `responseMessage`, `bankRedirectionUrl`, `timeToLive`, `paymentPlan`, `lendingAmount`, `interestRate`, `term`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `monthlyPayments`, `amount`, `dueDate`, `details`, `name`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings)

## `ecommerce_lendings_v1_2` { #ecommerce_lendings_v1_2 }

**Ecommerce Lendings** · `POST /v1/lendings` · kapsam `digital_payments` · client credentials

This API creates a lending application using the customer's pre-approved application information, selected term, order details, callback URLs and cart content. The response includes the application result, bank redirection URL and payment plan details.

```python
yanit = kt.ecommerce.ecommerce_lendings_v1_2(x_company_id=..., x_sub_company_id=..., reference_id=..., pre_approved_application_id=..., callback_url=..., failcallback_url=..., national_identity_number=..., birth_date=..., gsm_number=..., total_term=..., type=..., time_to_live=..., order_id=..., company_code=..., cart=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `x_company_id` | `x-company-id` | gövde | metin | evet | Company identifier used to determine the company initiating the lending application. |
| `x_sub_company_id` | `x-sub-company-id` | gövde | tam sayı | evet | Sub-company identifier used to determine the related sub-company for the lending application. |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique reference identifier of the lending application request. |
| `pre_approved_application_id` | `preApprovedApplicationId` | gövde | metin | evet | Pre-approved application identifier obtained from the pre-approved monthly payments query. |
| `callback_url` | `callbackUrl` | gövde | metin | evet | URL to which the customer will be redirected after a successful lending application flow. |
| `failcallback_url` | `failcallbackUrl` | gövde | metin | evet | URL to which the customer will be redirected if the lending application flow fails. |
| `national_identity_number` | `nationalIdentityNumber` | gövde | metin | evet | Customer's national identity number. |
| `birth_date` | `birthDate` | gövde | metin | evet | Customer's birth date. |
| `gsm_number` | `gsmNumber` | gövde | metin | evet | Customer's mobile phone number. |
| `total_term` | `totalTerm` | gövde | tam sayı | evet | Total term selected for the lending application. |
| `type` | `type` | gövde | metin | evet | Type of the selected lending/payment option. |
| `time_to_live` | `timeToLive` | gövde | tam sayı | evet | Validity duration of the lending application flow. |
| `order_id` | `orderId` | gövde | metin | evet | Order identifier related to the lending application. |
| `promotion_id` | `promotionId` | gövde | metin |  | Promotion identifier related to the lending application. |
| `company_code` | `companyCode` | gövde | metin | evet | Company code associated with the lending application. |
| `cart` | `cart` | gövde | nesne | evet | Cart information containing price and item details. |

Yanıt alanları (dokümana göre): `applicationId`, `isApproved`, `applicationDate`, `responseCode`, `responseMessage`, `bankRedirectionUrl`, `timeToLive`, `paymentPlan`, `lendingAmount`, `interestRate`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `monthlyEffectiveInterestRate`, `term`, `monthlyPayments`, `amount`, `type`, `dueDate`, `details`, `name`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-lendings)

## `ecommerce_monthly_payments_v1` { #ecommerce_monthly_payments_v1 }

**Ecommerce Monthly Payments** · `POST /v1/query/monthly-payments` · kapsam `digital_payments` · client credentials

Estimated monthly return service based on the customer's cart.

```python
yanit = kt.ecommerce.ecommerce_monthly_payments_v1(reference_id=..., max_term=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | sunucu hatası — İşleminiz gerçekleştirilemedi. Daha sonra tekrar deneyiniz. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique ID number of the request |
| `max_term` | `maxTerm` | gövde | tam sayı | evet | The maxterm information sent in the request is optional and additional information. |
| `promotion_id` | `promotionId` | gövde | tam sayı |  | Predetermined ID for the promotion to be applied. |
| `cart` | `cart` | gövde | nesne |  | Contains price and cart product information. |

Yanıt alanları (dokümana göre): `interestRate`, `amount`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `type`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments)

## `ecommerce_monthly_payments_v1_2` { #ecommerce_monthly_payments_v1_2 }

**Ecommerce Monthly Payments** · `POST /v1/query/monthly-payments` · kapsam `digital_payments` · client credentials

This API queries available monthly payment options based on company information, reference information, maximum term, promotion information and cart content. The response includes available payment terms, interest rates and payment amounts.

```python
yanit = kt.ecommerce.ecommerce_monthly_payments_v1_2(x_company_id=..., x_sub_company_id=..., reference_id=..., max_term=..., cart=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | sunucu hatası — İşleminiz gerçekleştirilemedi. Daha sonra tekrar deneyiniz. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `x_company_id` | `x-company-id` | gövde | metin | evet | Company identifier used to determine the company initiating the monthly payment query. |
| `x_sub_company_id` | `x-sub-company-id` | gövde | tam sayı | evet | Sub-company identifier used to determine the related sub-company for the monthly payment query. |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique reference identifier of the monthly payment query request. |
| `max_term` | `maxTerm` | gövde | tam sayı | evet | Maximum term to be considered for monthly payment options. |
| `promotion_id` | `promotionId` | gövde | metin |  | Promotion identifier related to the monthly payment query. |
| `cart` | `cart` | gövde | nesne | evet | Cart information containing price and item details. |

Yanıt alanları (dokümana göre): `monthlyPayments`, `term`, `interestRate`, `amount`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `monthlyEffectiveInterestRate`, `type`, `responseCode`, `responseMessage`, `errors`, `message`, `code`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-monthly-payments)

## `ecommerce_pre_approved_monthly_payments_v1` { #ecommerce_pre_approved_monthly_payments_v1 }

**Ecommerce Pre Approved Monthly Payments** · `POST /v1/query/pre-approved-monthly-payments` · kapsam `digital_payments` · client credentials

Returns the pre-approved monthly payment table according to the customer's cart and personal information.

```python
yanit = kt.ecommerce.ecommerce_pre_approved_monthly_payments_v1(reference_id=..., national_identity_number=..., gsm_number=..., max_term=..., order_id=..., cart=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | sunucu hatası — İşleminiz gerçekleştirilemedi. Daha sonra tekrar deneyiniz. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique ID number of the request |
| `national_identity_number` | `nationalIdentityNumber` | gövde | metin | evet | National identification number. |
| `birthdate` | `birthdate` | gövde | metin |  | Customer's date of birth |
| `gsm_number` | `gsmNumber` | gövde | metin | evet | Customer's confirmed mobile phone number. |
| `max_term` | `maxTerm` | gövde | tam sayı | evet | The maxterm information sent in the request is optional and additional information. |
| `order_id` | `orderId` | gövde | metin | evet | Order number |
| `promotion_id` | `promotionId` | gövde | tam sayı |  | Predetermined id for the promotion to be applied |
| `cart` | `cart` | gövde | nesne | evet | Contains price and cart product information |
| `is_mixed_cart` | `IsMixedCart` | gövde | bool |  | Type of products in the basket as a whole |

Yanıt alanları (dokümana göre): `isSuccess`, `isActiveCustomer`, `isDigitalChannelCustomer`, `responseCode`, `responseMessage`, `preApprovedApplicationId`, `monthlyPayments`, `term`, `interestRate`, `amount`, `totalPaymentAmount`, `annualEffectiveInterestRate`, `type`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments)

## `ecommerce_pre_approved_monthly_payments_v1_2` { #ecommerce_pre_approved_monthly_payments_v1_2 }

**Ecommerce Pre Approved Monthly Payments** · `POST /v1/query/pre-approved-monthly-payments` · kapsam `digital_payments` · client credentials

This API queries pre-approved monthly payment options for a customer based on company information, customer identity information, order details and cart content.

```python
yanit = kt.ecommerce.ecommerce_pre_approved_monthly_payments_v1_2(x_company_id=..., x_sub_company_id=..., agent_code=..., reference_id=..., national_identity_number=..., birth_date=..., gsm_number=..., max_term=..., order_id=..., company_code=..., cart=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | sunucu hatası — İşleminiz gerçekleştirilemedi. Daha sonra tekrar deneyiniz. | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `x_company_id` | `x-company-id` | gövde | metin | evet | Company identifier used to determine the company initiating the request. |
| `x_sub_company_id` | `x-sub-company-id` | gövde | tam sayı | evet | Sub-company identifier used to determine the related sub-company for the request. |
| `agent_code` | `agentCode` | gövde | metin | evet | Agent code associated with the request. |
| `reference_id` | `referenceId` | gövde | metin | evet | Unique reference identifier of the request. |
| `national_identity_number` | `nationalIdentityNumber` | gövde | metin | evet | Customer's national identity number. |
| `birth_date` | `birthDate` | gövde | metin | evet | Customer's birth date. |
| `gsm_number` | `gsmNumber` | gövde | metin | evet | Customer's mobile phone number. |
| `max_term` | `maxTerm` | gövde | tam sayı | evet | Maximum term to be considered for monthly payment options. |
| `order_id` | `orderId` | gövde | metin | evet | Order identifier related to the payment query. |
| `promotion_id` | `promotionId` | gövde | metin |  | Promotion identifier related to the payment query. |
| `company_code` | `companyCode` | gövde | metin | evet | Company code associated with the payment query. |
| `cart` | `cart` | gövde | nesne | evet | Cart information containing price and item details. |

Yanıt alanları (dokümana göre): `isSuccess`, `isActiveCustomer`, `isDigitalChannelCustomer`, `responseCode`, `responseMessage`, `preApprovedApplicationId`, `monthlyPayments`, `term`, `interestRate`, `totalPaymentAmount`, `amount`, `annualEffectiveInterestRate`, `monthlyEffectiveInterestRate`, `type`, `contributionAmount`, `contributionRate`, `commissionBsmvAmount`, `commissionKkdfAmount`, `shopIncome`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/e-commerce/ecommerce-pre-approved-monthly-payments)
