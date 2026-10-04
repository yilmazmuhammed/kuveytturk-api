<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.architecht

Architecht · 3 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış | Sandbox | Canlı |
| - | - | - | - | - |
| [`architecht_career_change`](#architecht_career_change) | `POST /v1/architechtintegration/career/insertAssignment` | CC | test edilmedi | test edilmedi |
| [`customer_consent_cancellation`](#customer_consent_cancellation) | `POST /v1/airapi/revoke-consent` | CC | test edilmedi | test edilmedi |
| [`customer_consent_list`](#customer_consent_list) | `GET /v1/airapi/consent-list` | CC | test edildi | test edilmedi |

## `architecht_career_change` { #architecht_career_change }

**Architecht Career Change** · `POST /v1/architechtintegration/career/insertAssignment` · kapsam `public` · client credentials

This API is used to create an assignment record for career integration. The request includes person, organization, job, position, assignment grade, identity number and effective date information. The response returns the execution reference and assignment creation result.

```python
yanit = kt.architecht.architecht_career_change(person_id=..., organization_id=..., job_id=..., position_id=..., assignment_grade=..., identity_number=..., effective_start_date=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `person_id` | `personId` | gövde | tam sayı | evet | Person ID for whom the assignment will be created. |
| `organization_id` | `organizationId` | gövde | tam sayı | evet | Organization ID associated with the assignment. |
| `job_id` | `jobId` | gövde | tam sayı | evet | Job ID associated with the assignment. |
| `position_id` | `positionId` | gövde | tam sayı | evet | Position ID associated with the assignment. |
| `assignment_grade` | `assignmentGrade` | gövde | tam sayı | evet | Assignment grade information. |
| `identity_number` | `identityNumber` | gövde | metin | evet | Identity number of the person. |
| `effective_start_date` | `effectiveStartDate` | gövde | tarih | evet | Effective start date of the assignment. Format: dd.MM.yyyy. |
| `effective_end_date` | `effectiveEndDate` | gövde | tarih |  | Effective end date of the assignment. Format: dd.MM.yyyy. |

Gövde alanları istekte `assignmentContract` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `executionReferenceId`, `insertResult`, `processStatus`, `assignmentId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/architecht/architecht-career-change)

## `customer_consent_cancellation` { #customer_consent_cancellation }

**Customer Consent Cancellation** · `POST /v1/airapi/revoke-consent` · kapsam `accounts` · client credentials

This API is used to revoke customer consent records. The request includes the customer ID and token data list for the consents to be cancelled. The response returns the operation status with HTTP code and message information.

```python
yanit = kt.architecht.customer_consent_cancellation(customer_id=..., token_data=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edilmedi | işlem yapan uç nokta; otomatik test edilmez | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_id` | `customerId` | gövde | metin | evet | Customer ID for which consent records will be revoked. |
| `token_data` | `tokenData` | gövde | liste | evet | List of token data values identifying the consent records to be revoked. |

Yanıt alanları (dokümana göre): `httpcode`, `message`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-cancellation)

## `customer_consent_list` { #customer_consent_list }

**Customer Consent List** · `GET /v1/airapi/consent-list` · kapsam `accounts` · client credentials

This API is used to retrieve the customer consent list. The service returns consent records filtered by customer ID and token type. The response includes token information, consent status, creation date, TPP name and TPP ID.

```python
yanit = kt.architecht.customer_consent_list(customerid=..., tokentype=...)
```

| Ortam | Durum | Sonuç | Tarih |
| - | - | - | - |
| Sandbox | test edildi | çalışıyor — results: 1 kayıt (parametresiz) | 2026-10-04 |
| Canlı | test edilmedi | henüz denenmedi |  |

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customerid` | `customerid` | sorgu | tam sayı | evet | Customer ID for which the consent list will be retrieved. |
| `tokentype` | `tokentype` | sorgu | tam sayı | evet | Token type used to filter consent records. |

Yanıt alanları (dokümana göre): `token`, `status`, `created`, `tpp`, `tppId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/architecht/customer-consent-list)
