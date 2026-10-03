<!-- Bu sayfa scripts/generate.py tarafından üretildi; elle düzenlemeyin. -->

# kt.donations

Bağışlar · 5 uç nokta

Asenkron istemcide (`AsyncKuveytTurk`) aynı metotlar `await` ile çağrılır. Her metot ayrıca `extra_query`, `extra_body` ve `request_options` kabul eder ([ayrıntı](../kilavuzlar/dogrudan-istek.md)).

| Metot | İstek | Akış |
| - | - | - |
| [`account_transactions_for_the_organization`](#account_transactions_for_the_organization) | `POST /v1/donations/transactions` | AC |
| [`campaign_list_for_organization`](#campaign_list_for_organization) | `POST /v1/donations/campaignList` | AC |
| [`donation_list_for_organization`](#donation_list_for_organization) | `POST /v1/donations/donationList` | CC |
| [`donation_list_for_organization_tdv`](#donation_list_for_organization_tdv) | `POST /v1/donations/donationListTdv` | CC |
| [`external_payments_list`](#external_payments_list) | `POST /v1/donations/externalPayments` | AC |

## `account_transactions_for_the_organization` { #account_transactions_for_the_organization }

**Account Transactions for the Organization** · `POST /v1/donations/transactions` · kapsam `donations` · authorization code (müşteri girişi gerekir)

Returns the list of all transactions between the start and end date made to the organization.

```python
yanit = kt.donations.account_transactions_for_the_organization(organization_id=..., password=..., start_date=..., end_date=..., campaign_account_suffix=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `organization_id` | `organizationId` | gövde | tam sayı | evet | Organization Code |
| `password` | `password` | gövde | metin | evet | Organization Password |
| `start_date` | `startDate` | gövde | tarih | evet | Report Start Date |
| `end_date` | `endDate` | gövde | tarih | evet | Report End Date |
| `campaign_account_suffix` | `campaignAccountSuffix` | gövde | tam sayı | evet | Customer Account Suffix |

Yanıt alanları (dokümana göre): `AccountNumber`, `AccountSuffix`, `Balance`, `FECName`, `IBAN`, `BranchId`, `BranchName`, `TransactionCount`, `TransactionList`, `Amount`, `TranDate`, `ValueDate`, `BusinessKey`, `CurrentBalance`, `Description`, `SenderIdentityNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/other/account-transactions-for-the-organization)

## `campaign_list_for_organization` { #campaign_list_for_organization }

**Campaign List for Organization** · `POST /v1/donations/campaignList` · kapsam `donations` · authorization code (müşteri girişi gerekir)

Returns the list of all transactions between the start and end date made to the organization.

```python
yanit = kt.donations.campaign_list_for_organization(organization_id=..., password=..., start_date=..., end_date=..., campaign_account_suffix=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `organization_id` | `organizationId` | gövde | tam sayı | evet | Organization Code |
| `password` | `password` | gövde | metin | evet | Organization Password |
| `start_date` | `startDate` | gövde | tarih | evet | Report Start Date |
| `end_date` | `endDate` | gövde | tarih | evet | Report End Date |
| `campaign_account_suffix` | `campaignAccountSuffix` | gövde | tam sayı | evet | Customer Account Suffix |

Yanıt alanları (dokümana göre): `AccountNumber`, `AccountSuffix`, `Balance`, `FECName`, `IBAN`, `BranchId`, `BranchName`, `TransactionCount`, `TransactionList`, `Amount`, `TranDate`, `ValueDate`, `BusinessKey`, `CurrentBalance`, `Description`, `SenderIdentityNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/donations/campaign-list-for-organization)

## `donation_list_for_organization` { #donation_list_for_organization }

**Donation List for Organization** · `POST /v1/donations/donationList` · kapsam `donations` · client credentials

Retrieves the donation payment list for an organization. The request can be filtered by campaign account number, campaign ID, last payment ID, cancellation inclusion flag and date range. The response includes donation summary information and detailed payment records.

```python
yanit = kt.donations.donation_list_for_organization(customer_id=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `customer_id` | `CustomerId` | gövde | tam sayı | evet | Campaign account number of the organization for which donation payments will be listed. |
| `campaign_id` | `campaignId` | gövde | tam sayı |  | Campaign identifier used to filter donation payments. |
| `last_payment_id` | `lastPaymentId` | gövde | tam sayı |  | Last payment identifier used for pagination or retrieving records after a specific payment. |
| `is_canceled_included` | `isCanceledIncluded` | gövde | tam sayı |  | Indicates whether canceled donation payments should be included in the response. |
| `start_date` | `startDate` | gövde | metin |  | Start date of the donation payment search range. |
| `end_date` | `endDate` | gövde | metin |  | End date of the donation payment search range. |

Yanıt alanları (dokümana göre): `DonationDetail`, `LastPaymentId`, `DonationCount`, `PaymentList`, `PaymentId`, `TranDate`, `BankCode`, `BankName`, `CampaignId`, `CampaignCode`, `CampaignName`, `UnitAmount`, `Quantity`, `TotalAmount`, `FecCode`, `CampaignAccountNumber`, `CampaignAccountSuffix`, `StatusName`, `TranTaxNumber`, `TranTitle`, `TranGsmNumber`, `TranPhoneNumber`, `TranEMail`, `TranCountry`, `TranCountryName`, `TranCity`, `TranCityName`, `TranCounty`, `TranAddress`, `Description`, `IsExplicitConsentName`, `DetailModelCount`, `DetailList`, `Title`, `PhoneNumber`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization)

## `donation_list_for_organization_tdv` { #donation_list_for_organization_tdv }

**Donation List for Organization TDV** · `POST /v1/donations/donationListTdv` · kapsam `donations` · client credentials

Retrieves the donation payment list for TDV within the specified date range. The request can be filtered by organization ID, campaign ID, last payment ID, cancellation inclusion flag and date range. The response includes donation summary information and detailed payment records.

```python
yanit = kt.donations.donation_list_for_organization_tdv(organization_id=..., password=..., campaign_id=..., last_payment_id=..., is_canceled_included=..., start_date=..., end_date=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `organization_id` | `organizationId` | gövde | tam sayı | evet | Organization identifier used to retrieve donation payments. |
| `password` | `password` | gövde | metin | evet | Organization password used for request authorization. |
| `campaign_id` | `campaignId` | gövde | tam sayı | evet | Campaign identifier used to filter donation payments. |
| `last_payment_id` | `lastPaymentId` | gövde | tam sayı | evet | Last payment identifier used for pagination or retrieving records after a specific payment. |
| `is_canceled_included` | `isCanceledIncluded` | gövde | tam sayı | evet | Indicates whether canceled donation payments should be included in the response. Use 0 for false and 1 for true. |
| `start_date` | `startDate` | gövde | metin | evet | Start date of the donation payment search range. For example: 2015-06-01. |
| `end_date` | `endDate` | gövde | metin | evet | End date of the donation payment search range. For example: 2015-06-30. |

Yanıt alanları (dokümana göre): `DonationDetail`, `LastPaymentId`, `DonationCount`, `PaymentList`, `PaymentId`, `TranDate`, `PaymentAccountNo`, `BusinessKey`, `BankCode`, `BankName`, `BranchCode`, `BranchName`, `ChannelName`, `CampaignId`, `CampaignName`, `CampaignCode`, `UnitAmount`, `Quantity`, `TotalAmount`, `FecCode`, `CampaignAccountNumber`, `CampaignAccountSuffix`, `StatusName`, `TranTaxNumber`, `TranTitle`, `TranGsmNumber`, `TranPhoneNumber`, `TranBirthDate`, `TranGenderName`, `TranEducation`, `TranProfession`, `TranEMail`, `TranCountry`, `TranCountryName`, `TranCity`, `TranCityName`, `TranCounty`, `TranAddress`, `TranZipCode`, `Attorneyship`, `TranAccountNumber`, `TranAccountSuffix`, `Privacy`, `Description`, `DetailModelCount`, `DetailList`, `Title`, `PhoneNumber`, `CancelTranDate`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/donations/donation-list-for-organization-tdv)

## `external_payments_list` { #external_payments_list }

**External Payments List** · `POST /v1/donations/externalPayments` · kapsam `donations` · authorization code (müşteri girişi gerekir)

Returns all the external payments, such as EFT, money transfers, and cash processing, made to the selected campaign within the specified date range for the authenticated organization.

```python
yanit = kt.donations.external_payments_list(organization_id=..., password=..., start_date=..., end_date=..., account_suffix=...)
```

| Parametre | API'deki adı | Yer | Tür | Zorunlu | Açıklama |
| - | - | - | - | - | - |
| `organization_id` | `organizationId` | gövde | tam sayı | evet | Organization Code |
| `password` | `password` | gövde | metin | evet | Organization Password |
| `start_date` | `startDate` | gövde | metin | evet | Report Start Date e.g., "2015-06-01" |
| `end_date` | `endDate` | gövde | metin | evet | Report End Date e.g., "2015-06-01" |
| `account_suffix` | `accountSuffix` | gövde | tam sayı | evet | Account Suffix Number |

Yanıt alanları (dokümana göre): `Amount`, `ProcessDate`, `BusinessKey`, `SenderIdentityNumber`, `ReceiverIdentityNumber`, `SenderName`, `ReceiverName`, `Description`, `BranchId`, `ProcessType`, `BranchName`, `FecName`, `SenderIbanNumber`, `SenderBankCode`, `SenderBranchId`

[Resmî doküman](https://developer.kuveytturk.com.tr/documentation/donations/external-payments-list)
