<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.your_banking

Senin Bankan · 4 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`your_banking_account_application`](#your_banking_account_application) | `POST /v1/yourbank/accountApplications` | CC |
| [`your_banking_account_application_documents`](#your_banking_account_application_documents) | `POST /v1/yourbank/accountApplicationDocuments` | CC |
| [`your_banking_account_application_sms_validation`](#your_banking_account_application_sms_validation) | `POST /v1/yourbank/accountSmsOtp` | CC |
| [`your_banking_account_application_status_query`](#your_banking_account_application_status_query) | `POST /v1/yourbank/accountApplicationStatus` | CC |

## `your_banking_account_application` { #your_banking_account_application }

**Your Banking Account Application** · `POST /v1/yourbank/accountApplications` · kapsam `accounts` · client credentials

This endpoint is used to create or validate a YourBank account application by checking the applicant’s identity information. The request includes identity details, application information, mobile phone information, SMS validation code, education, profession, and contact information. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.your_banking.your_banking_account_application(identity_number=..., application_code=..., birth_day=..., name_and_surname=..., gsm_country_code=..., gsm_area_code=..., gsm_number=..., sms_validation_code=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number of the applicant. |
| `application_code` | `ApplicationCode` | gövde | metin | evet | Code of the application type. |
| `birth_day` | `BirthDay` | gövde | tarih | evet | Birth date of the applicant. |
| `name_and_surname` | `NameAndSurname` | gövde | metin | evet | Full name of the applicant. |
| `identity_card_serial` | `IdentityCardSerial` | gövde | metin |  | Identity card serial information of the applicant. |
| `identity_card_number` | `IdentityCardNumber` | gövde | metin |  | Identity card number of the applicant. |
| `identity_card_serial_number` | `IdentityCardSerialNumber` | gövde | metin |  | Identity card serial number of the applicant. |
| `occupation_city_id` | `OccupationCityId` | gövde | tam sayı |  | City identifier of the applicant’s occupation location. |
| `occupation_county_id` | `OccupationCountyId` | gövde | tam sayı |  | County identifier of the applicant’s occupation location. |
| `gsm_country_code` | `GsmCountryCode` | gövde | tam sayı | evet | GSM country code of the applicant’s mobile phone number. |
| `gsm_area_code` | `GsmAreaCode` | gövde | tam sayı | evet | GSM area code of the applicant’s mobile phone number. |
| `gsm_number` | `GsmNumber` | gövde | metin | evet | GSM number of the applicant. |
| `sms_validation_code` | `SMSValidationCode` | gövde | metin | evet | SMS validation code sent to the applicant. |
| `maidenhood_surname` | `MaidenhoodSurname` | gövde | metin |  | Maidenhood surname of the applicant. |
| `education_level_id` | `EducationLevelId` | gövde | tam sayı |  | Education level identifier of the applicant. |
| `profession_id` | `ProfessionId` | gövde | tam sayı |  | Profession identifier of the applicant. |
| `email_address` | `EmailAddress` | gövde | metin |  | Email address of the applicant. |

Gövde alanları istekte `request` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application)

## `your_banking_account_application_documents` { #your_banking_account_application_documents }

**Your Banking Account Application Documents** · `POST /v1/yourbank/accountApplicationDocuments` · kapsam `accounts` · client credentials

Retrieves Your Banking account application documents according to the provided identity number, application code, and GSM information. The response includes document name, document code, document identifier, application code, document content, and document extension details.

```python
yanit = kt.your_banking.your_banking_account_application_documents(identity_number=..., application_code=..., gsm_country_code=..., gsm_area_code=..., gsm_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number used to retrieve account application documents. |
| `application_code` | `ApplicationCode` | gövde | metin | evet | Application code used to retrieve documents related to the account application. |
| `gsm_country_code` | `GsmCountryCode` | gövde | tam sayı | evet | GSM country code of the applicant. |
| `gsm_area_code` | `GsmAreaCode` | gövde | tam sayı | evet | GSM area code of the applicant. |
| `gsm_number` | `GsmNumber` | gövde | metin | evet | GSM number of the applicant. |

Gövde alanları istekte `request` nesnesinin içine yerleştirilir.

Yanıt alanları (dokümana göre): `DocumentName`, `DocumentCode`, `DocumentId`, `ApplicationCode`, `DocumentContent`, `DocumentExtension`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-documents)

## `your_banking_account_application_sms_validation` { #your_banking_account_application_sms_validation }

**Your Banking Account Application SMS Validation** · `POST /v1/yourbank/accountSmsOtp` · kapsam `accounts` · client credentials

This endpoint is used to validate the SMS OTP code and create or update person information for a YourBank account application. The request includes the application identifier, applicant identity number, mobile phone information, SMS validation code, and address details. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.your_banking.your_banking_account_application_sms_validation(application_id=..., identity_number=..., gsm_country_code=..., gsm_area_code=..., gsm_number=..., sms_validation_code=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `application_id` | `ApplicationId` | gövde | tam sayı | evet | Unique identifier of the account application. |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number of the applicant. |
| `gsm_country_code` | `GsmCountryCode` | gövde | tam sayı | evet | GSM country code of the applicant’s mobile phone number. |
| `gsm_area_code` | `GsmAreaCode` | gövde | tam sayı | evet | GSM area code of the applicant’s mobile phone number. |
| `gsm_number` | `GsmNumber` | gövde | metin | evet | GSM number of the applicant. |
| `sms_validation_code` | `SMSValidationCode` | gövde | metin | evet | SMS OTP validation code sent to the applicant. |
| `block` | `Block` | gövde | metin |  | Block information of the applicant’s address. |
| `district_name` | `DistrictName` | gövde | metin |  | District name of the applicant’s address. |
| `flat_number` | `FlatNumber` | gövde | metin |  | Flat number of the applicant’s address. |
| `street_name` | `StreetName` | gövde | metin |  | Street name of the applicant’s address. |
| `site_name` | `SiteName` | gövde | metin |  | Site name of the applicant’s address. |

Gövde alanları istekte `request` nesnesinin içine yerleştirilir.

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-sms-validation)

## `your_banking_account_application_status_query` { #your_banking_account_application_status_query }

**Your Banking Account Application Status Query** · `POST /v1/yourbank/accountApplicationStatus` · kapsam `accounts` · client credentials

This endpoint is used to retrieve account application status information for YourBank applications. The request includes the applicant identity number and mobile phone information. The response returns the matching application status records, including customer, application number, status, application code, and application type information. &gt;This API is in beta stage. Request and response models may change over time.

```python
yanit = kt.your_banking.your_banking_account_application_status_query(identity_number=..., gsm_area_code=..., gsm_number=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `identity_number` | `IdentityNumber` | gövde | metin | evet | Identity number of the applicant whose account application status will be queried. |
| `gsm_area_code` | `GsmAreaCode` | gövde | tam sayı | evet | GSM area code of the applicant’s mobile phone number. |
| `gsm_number` | `GsmNumber` | gövde | metin | evet | GSM number of the applicant. |

Yanıt alanları (dokümana göre): `PersonId`, `CustomerName`, `ApplicationNumber`, `ApplicationStatus`, `StatusName`, `ApplicationCode`, `ApplicationTypeName`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/your-banking/your-banking-account-application-status-query)
