"""Nakit yönetimi uç noktaları (``kt.cash_management``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Number, Resource, merge

__all__ = ["AsyncCashManagement", "CashManagement"]


class CashManagement(Resource):
    """Nakit yönetimi - ``kt.cash_management``."""

    def cheque_information_micro(
        self,
        *,
        state: str | None = None,
        status: str | None = None,
        currency: str | None = None,
        start_date: str | None = None,
        finish_date: str | None = None,
        language_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """cheque-information-micro.

        ``POST /v1/cheque-information-micro``

        Kapsam: ``public`` · Akış: client credentials

        It is an API that provides the necessary data for customers to view information about
        checks they are owed or owed.

        Args:
            state: (gövde)
            status: (gövde)
            currency: (gövde)
            start_date: (``startDate``, gövde)
            finish_date: (``finishDate``, gövde)
            language_id: (``languageId``, gövde)

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/cheque-information-micro
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "state": state,
                "status": status,
                "currency": currency,
                "startDate": start_date,
                "finishDate": finish_date,
                "languageId": language_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/cheque-information-micro",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def dijital_bankacilik_iadesi(
        self,
        *,
        transaction_id: str,
        org_transaction_id: str,
        amount: Number,
        currency: str,
        comission_amount: Number,
        description: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Bankacılık İadesi.

        ``POST /v1/vpos/digitalPaymentRefund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Önceki gün içerisinde yapılan işlemlerde iade veya kısmi iade yapılır.

        Args:
            transaction_id: (``TransactionId``, gövde, zorunlu) İade işleminin tekil işlem
                numarası
            org_transaction_id: (``OrgTransactionId``, gövde, zorunlu) ComPay tarafından bankaya
                iade edilen orijinal işlemin benzersiz işlem numarası
            amount: (``Amount``, gövde, zorunlu) İade edilecek bilgi miktarı
            currency: (``Currency``, gövde, zorunlu) İşlem para birimi
            comission_amount: (``ComissionAmount``, gövde, zorunlu) İade işlemi için işyerinden
                alınacak komisyon tutarı.
            description: (``Description``, gövde, zorunlu) İşlem açıklaması

        Gövde alanları istekte ``DigitalPaymentRefundTransactionContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: ReturnCode, ReturnMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-iadesi
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionId": transaction_id,
                "OrgTransactionId": org_transaction_id,
                "Amount": amount,
                "Currency": currency,
                "ComissionAmount": comission_amount,
                "Description": description,
            },
            extra_body,
        )
        _body = {"DigitalPaymentRefundTransactionContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentRefund",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def dijital_bankacilik_islem_durumu(
        self,
        *,
        transaction_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Bankacılık İşlem Durumu.

        ``POST /v1/vpos/digitalPaymentStatus``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Parametrelerde belirtilen işlemin durumunu döndürür.

        Args:
            transaction_id: (``TransactionId``, gövde, zorunlu) İşlemin tekil işlem numarası

        Gövde alanları istekte ``DigitalPaymentStatContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ReturnCode, ReturnMessage, DiscountedAmount, ProductType, CostAmount,
        ComissionAmount, Amount, TransactionType, TransactionId, OrgTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-islem-durumu
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionId": transaction_id,
            },
            extra_body,
        )
        _body = {"DigitalPaymentStatContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentStatus",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def dijital_bankacilik_odeme(
        self,
        *,
        transaction_id: str,
        merchant_id: str,
        soft_descriptor: str,
        product_type: str,
        comission_amount: Number,
        amount: Number,
        transaction_currency: int,
        token_interval: int,
        payment_method: str,
        cost_amount: Number | None = None,
        success_redirect_url: str | None = None,
        fail_redirect_url: str | None = None,
        os: str | None = None,
        product_type_condition: str | None = None,
        pan: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Bankacılık Ödeme.

        ``POST /v1/vpos/digitalPayment``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Parametrelerde sağlanan müşteri profilinden ödeme bilgilerini toplar.

        Args:
            transaction_id: (``TransactionId``, gövde, zorunlu) Tekil bir sayının işlenmesi.
            merchant_id: (``MerchantId``, gövde, zorunlu) Banka tarafından belirlenen şirket
                kodu
            soft_descriptor: (``SoftDescriptor``, gövde, zorunlu) Tüccar işlem belirteci.
            product_type: (``ProductType``, gövde, zorunlu) Hesaplanan maliyetler ve komisyon
                ödeme türleri
            cost_amount: (``CostAmount``, gövde)
            comission_amount: (``ComissionAmount``, gövde, zorunlu) A commission fee will be
                taken from the workplace.
            amount: (``Amount``, gövde, zorunlu) İşlem tutarı
            transaction_currency: (``TransactionCurrency``, gövde, zorunlu) İşlem para birimi
            token_interval: (``TokenInterval``, gövde, zorunlu) Dakikalar içinde talep edilen
                token geçerlilik süresi
            success_redirect_url: (``SuccessRedirectUrl``, gövde) Müşteri, bankacılığın başarısı
                için adresi yönlendiriyor
            fail_redirect_url: (``FailRedirectUrl``, gövde) Müşteri yönlendirme adresi
                bankacılık tarafından başarısız oldu
            payment_method: (``PaymentMethod``, gövde, zorunlu) Ödeme yöntemi bilgisi
            os: (``OS``, gövde) Mobil uygulamanın işletim sistemi bilgisi.
            product_type_condition: (``ProductTypeCondition``, gövde) Farklı ürün tipleri için
                hesaplanan maliyet ve komisyon bilgileri
            pan: (``Pan``, gövde) Müşteri bilgilerinin doğruluğunu gösteren işlem

        Gövde alanları istekte ``DigitalPaymentTransactionContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: AccessToken, TokenExpireDate, ReturnCode, ReturnMessage,
        ApplicationName, ApplicationParameter

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionId": transaction_id,
                "MerchantId": merchant_id,
                "SoftDescriptor": soft_descriptor,
                "ProductType": product_type,
                "CostAmount": cost_amount,
                "ComissionAmount": comission_amount,
                "Amount": amount,
                "TransactionCurrency": transaction_currency,
                "TokenInterval": token_interval,
                "SuccessRedirectUrl": success_redirect_url,
                "FailRedirectUrl": fail_redirect_url,
                "PaymentMethod": payment_method,
                "OS": os,
                "ProductTypeCondition": product_type_condition,
                "Pan": pan,
            },
            extra_body,
        )
        _body = {"DigitalPaymentTransactionContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/digitalPayment",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def school_installment_payment_system_active_registration_inquiry_api(
        self,
        *,
        identity_number: str,
        client_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """School Installment Payment System Active Registration Inquiry API.

        ``POST /v1/school-installment/registration-inquiry``

        Kapsam: ``loans`` · Akış: client credentials

        Institutions could check through this API using the Turkish National Identity Number
        (TCKN) to determine if a student currently has an OTS registration. OTS registration is
        considered "Yes" or "No" as follows: - Canceled registration = "No" - All installments
        collected without credit = "No" - All installments collected, including some with credit
        = "Yes" - If there are installments pending payment = "Yes" * As long as any payment
        (credit or cash) is pending, OTS is considered to exist.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Öğrenci TCKN bilgisi
            client_id: (``ClientId``, gövde, zorunlu) Kurum token bilgisi

        Gövde alanları istekte ``payment`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-payment-system-active-registration-inquiry-api
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ClientId": client_id,
            },
            extra_body,
        )
        _body = {"payment": _body}
        return self._client.request(
            "POST",
            "/v1/school-installment/registration-inquiry",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def school_installment_system_registration_and_installment_cancellation_api(
        self,
        *,
        client_id: str,
        identity_number: str | None = None,
        invoice_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """School Installment System Registration and Installment Cancellation API.

        ``POST /v1/school-installment/cancelation``

        Kapsam: ``loans`` · Akış: client credentials

        Schools/Institutions can perform cancellations based on installments or Turkish National
        Identity Number (TCKN) via this API. - When only the TCKN is entered, all records and
        installments associated with that TCKN are not cancelled. - When both the TCKN and
        Invoice Number are sent, only the relevant installment is cancelled.

        Args:
            identity_number: (``IdentityNumber``, gövde) Öğrenci TCKN bilgisi
            client_id: (``ClientId``, gövde, zorunlu) Kurum token bilgisi
            invoice_number: (``InvoiceNumber``, gövde) Fatura/Taksit Numarası

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-registration-and-installment-cancellation-api
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ClientId": client_id,
                "InvoiceNumber": invoice_number,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/school-installment/cancelation",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def school_installment_system_school_guaranteed_registration_payment(
        self,
        *,
        client_id: str,
        identity_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """School Installment System School Guaranteed Registration Payment.

        ``POST /v1/school-installment/transaction-information``

        Kapsam: ``loans`` · Akış: client credentials

        School-Guaranteed schools can use this API to track parent payments based on payment
        documentation or date range. --PaymentType description: --0 --&gt; account or card, --1
        --&gt; not converted to credit but unpaid, --2 --&gt; converted to credit, parent paid,
        --3 --&gt; converted to credit, school paid

        Args:
            identity_number: (``IdentityNumber``, gövde) Öğrenci TCKN bilgisi
            client_id: (``ClientId``, gövde, zorunlu) Kurum token bilgisi

        Gövde alanları istekte ``payment`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-school-guaranteed-registration-payment
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ClientId": client_id,
            },
            extra_body,
        )
        _body = {"payment": _body}
        return self._client.request(
            "POST",
            "/v1/school-installment/transaction-information",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_buyer_order_confirmation(
        self,
        *,
        purchaser_tax_number: str,
        supplier_order_gu_id_id: str,
        supplier_order_id: str,
        list_approve_from_purchaser_contract: Sequence[Any],
        tax_exclusive_amount: Number,
        contract: Sequence[Any] | None = None,
        used_invoice_amount: Number | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Buyer Order Confirmation.

        ``POST /v1/supplierfinance/approvefrompurchaserer``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API where invoices are uploaded to the system by the receiving company.

        Args:
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Identify Purchaser
                Tax Number.
            supplier_order_gu_id_id: (``SupplierOrderGuIdId``, gövde, zorunlu) Order Number
                (GUID).
            contract: (gövde)
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Order Number.
            list_approve_from_purchaser_contract: (``ListApproveFromPurchaserContract``, gövde,
                zorunlu) Contains invoice info.
            used_invoice_amount: (``UsedInvoiceAmount``, gövde) How much of the bill will be
                used.
            tax_exclusive_amount: (``TaxExclusiveAmount``, gövde, zorunlu) Tax exclusive amount.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage,
        executionReferenceId, SupplierOrderInvoiceList, InvoiceNumber, InvoiceStatus,
        InvoiceStatusName, InvoiceAmount, PaymentAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-confirmation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "PurchaserTaxNumber": purchaser_tax_number,
                "SupplierOrderGuIdId": supplier_order_gu_id_id,
                "contract": contract,
                "SupplierOrderId": supplier_order_id,
                "ListApproveFromPurchaserContract": list_approve_from_purchaser_contract,
                "UsedInvoiceAmount": used_invoice_amount,
                "TaxExclusiveAmount": tax_exclusive_amount,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplierfinance/approvefrompurchaserer",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_buyer_order_listing(
        self,
        *,
        client_id: str,
        purchaser_tax_number: str,
        first_transaction_date: DateLike | None = None,
        end_transaction_date: DateLike | None = None,
        supplier_order_id: int | None = None,
        is_transaction_date_invoice_date: int | None = None,
        supplier_tax_number: str | None = None,
        order_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Buyer Order Listing.

        ``POST /v1/supplierfinance/getorderbypurchaser``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves supplier financing buyer order records according to the provided purchaser,
        supplier, order, date range, and transaction date filter criteria. The response includes
        supplier order, invoice, payment, status, amount, currency, profit rate, commission
        rate, and description details.

        Args:
            client_id: (``ClientId``, gövde, zorunlu) Client identifier used for the supplier
                financing order listing request.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Tax number of the
                purchaser used to filter supplier financing orders.
            first_transaction_date: (``FirstTransactionDate``, gövde) Start date of the
                transaction date range.
            end_transaction_date: (``EndTransactionDate``, gövde) End date of the transaction
                date range.
            supplier_order_id: (``supplierOrderId``, gövde) Supplier order identifier used to
                filter a specific order.
            is_transaction_date_invoice_date: (``isTransactionDateInvoiceDate``, gövde)
                Indicates whether the transaction date filter should be evaluated as invoice date.
            supplier_tax_number: (``supplierTaxNumber``, gövde) Tax number of the supplier used
                to filter supplier financing orders.
            order_number: (``orderNumber``, gövde) Order number used to filter supplier
                financing orders.

        Gövde alanları istekte ``listOrderContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderId, SupplierOrderGuidId, OrderNumber, InvoiceNumber,
        Status, StatusName, InvoiceStatus, InvoiceStatusName, OrderDate, OrderAmount,
        InvoiceAmount, PaymentAmount, LoanProfitRate, LoanCommissionRate, FecCode, Description,
        SupplierTaxNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-listing
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "ClientId": client_id,
                "PurchaserTaxNumber": purchaser_tax_number,
                "FirstTransactionDate": first_transaction_date,
                "EndTransactionDate": end_transaction_date,
                "supplierOrderId": supplier_order_id,
                "isTransactionDateInvoiceDate": is_transaction_date_invoice_date,
                "supplierTaxNumber": supplier_tax_number,
                "orderNumber": order_number,
            },
            extra_body,
        )
        _body = {"listOrderContract": _body}
        return self._client.request(
            "POST",
            "/v1/supplierfinance/getorderbypurchaser",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_invoice_cancellation(
        self,
        *,
        client_id: str,
        purchaser_invoice_upload_guid: str,
        api_client_invoice_upload_guid: str,
        purchaser_tax_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Invoice Cancellation.

        ``POST /v1/supplychainfinance/cancelinvoice``

        Kapsam: ``loans`` · Akış: client credentials

        This API cancels a supply chain finance invoice. The cancellation operation is processed
        using the client identifier, purchaser invoice upload GUID, API client invoice upload
        GUID and purchaser tax number. The response includes the invoice cancellation status and
        result message.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the invoice cancellation
                request.
            purchaser_invoice_upload_guid: (``PurchaserInvoiceUploadGUID``, gövde, zorunlu) GUID
                identifier of the purchaser invoice upload record to be cancelled.
            api_client_invoice_upload_guid: (``APIClientInvoiceUploadGUID``, gövde, zorunlu)
                GUID identifier of the invoice upload record on the API client side.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Tax number of the
                purchaser related to the invoice cancellation request.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: PurchaserInvoiceUploadGUID, APIClientInvoiceUploadGUID, Status,
        StatusName, ResultMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-invoice-cancellation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "PurchaserInvoiceUploadGUID": purchaser_invoice_upload_guid,
                "APIClientInvoiceUploadGUID": api_client_invoice_upload_guid,
                "PurchaserTaxNumber": purchaser_tax_number,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplychainfinance/cancelinvoice",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_order_last_approval_by_supplier(
        self,
        *,
        client_id: str,
        supplier_tax_number: str,
        supplier_order_id: int,
        supplier_order_guid_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Order Last Approval by Supplier.

        ``POST /v1/supplierfinance/lastapprovefromsupplier``

        Kapsam: ``loans`` · Akış: client credentials

        This API performs the final approval of a supplier financing order by the supplier. The
        approval operation is processed using the client identifier, supplier tax number,
        supplier order identifier and supplier order GUID.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the supplier financing final
                approval request.
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tax number of the
                supplier approving the supplier financing order.
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Unique identifier of the
                supplier financing order to be approved.
            supplier_order_guid_id: (``SupplierOrderGuidId``, gövde, zorunlu) GUID identifier of
                the supplier financing order to be approved.

        Gövde alanları istekte ``Contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-order-last-approval-by-supplier
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderId": supplier_order_id,
                "SupplierOrderGuidId": supplier_order_guid_id,
            },
            extra_body,
        )
        _body = {"Contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplierfinance/lastapprovefromsupplier",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_vendor_company_invoice_approval(
        self,
        *,
        client_id: str,
        purchaser_invoice_upload_guid: str,
        api_client_invoice_upload_guid: str,
        supplier_tax_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Company Invoice Approval.

        ``POST /v1/supplychainfinance/supplierapproveinvoice``

        Kapsam: ``loans`` · Akış: client credentials

        This API approves a supply chain finance invoice by the supplier. The approval operation
        is processed using the client identifier, purchaser invoice upload GUID, API client
        invoice upload GUID and supplier tax number. The response includes invoice approval
        status, result message and invoice list details.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the supplier invoice approval
                request.
            purchaser_invoice_upload_guid: (``PurchaserInvoiceUploadGUID``, gövde, zorunlu) GUID
                identifier of the purchaser invoice upload record to be approved by the supplier.
            api_client_invoice_upload_guid: (``APIClientInvoiceUploadGUID``, gövde, zorunlu)
                GUID identifier of the invoice upload record on the API client side.
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tax number of the
                supplier approving the invoice.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: PurchaserInvoiceUploadGUID, APIClientInvoiceUploadGUID, Status,
        StatusName, ResultMessage, InvoiceList, InvoiceNumber, InvoiceStatus, InvoiceStatusName,
        InvoiceAmount, PaymentAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-company-invoice-approval
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "PurchaserInvoiceUploadGUID": purchaser_invoice_upload_guid,
                "APIClientInvoiceUploadGUID": api_client_invoice_upload_guid,
                "SupplierTaxNumber": supplier_tax_number,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplychainfinance/supplierapproveinvoice",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_vendor_invoice_listing(
        self,
        *,
        client_id: str,
        supplier_tax_number: str,
        purchaser_invoice_upload_guid: str | None = None,
        purchaser_tax_number: str | None = None,
        first_transaction_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Invoice Listing.

        ``POST /v1/supplychainfinance/supplierinvoicelist``

        Kapsam: ``loans`` · Akış: client credentials

        This API retrieves supply chain finance invoice records for a supplier based on the
        provided purchaser invoice upload GUID, purchaser tax number, supplier tax number and
        transaction date criteria. The response includes invoice identifiers, invoice status,
        invoice amount, payment amount, loan profit rate, currency code and tax number details.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the supplier invoice list
                request.
            purchaser_invoice_upload_guid: (``PurchaserInvoiceUploadGUID``, gövde) GUID
                identifier of the purchaser invoice upload record used to filter invoices.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde) Tax number of the purchaser
                used to filter supplier invoices.
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tax number of the
                supplier used to filter supplier invoices.
            first_transaction_date: (``FirstTransactionDate``, gövde) Start date of the
                transaction date range.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: PurchaserInvoiceUploadGUID, APIClientInvoiceUploadGUID, InvoiceList,
        InvoiceNumber, InvoiceStatus, InvoiceStatusName, InvoiceAmount, PaymentAmount,
        LoanProfitRate, InvoiceFecCode, SupplierTaxNumber, PurchaserTaxNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-invoice-listing
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "PurchaserInvoiceUploadGUID": purchaser_invoice_upload_guid,
                "PurchaserTaxNumber": purchaser_tax_number,
                "SupplierTaxNumber": supplier_tax_number,
                "FirstTransactionDate": first_transaction_date,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplychainfinance/supplierinvoicelist",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_vendor_order_cancellation(
        self,
        *,
        supplier_tax_number: str,
        supplier_order_id: str,
        order_number: str,
        supplier_order_guid_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Order Cancellation.

        ``POST /v1/supplierfinance/cancelFromSupplier``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API where the order is canceled by the vendor.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Identify Supplier Tax
                Number.
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Order Number.
            order_number: (``OrderNumber``, gövde, zorunlu) Order number.
            supplier_order_guid_id: (``SupplierOrderGuidId``, gövde, zorunlu) Order Number
                (GUID).

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, OrderNumber, Status, StatusName, ResultMessage,
        executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-cancellation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderId": supplier_order_id,
                "OrderNumber": order_number,
                "SupplierOrderGuidId": supplier_order_guid_id,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplierfinance/cancelFromSupplier",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_vendor_order_confirmation(
        self,
        *,
        supplier_tax_number: str,
        supplier_order_gu_id_id: str,
        supplier_order_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Order Confirmation.

        ``POST /v1/supplierfinance/lastapprovefromsupplierer``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API through which the order is approved by the vendor.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Identify Supplier Tax
                Number.
            supplier_order_gu_id_id: (``SupplierOrderGuIdId``, gövde, zorunlu) Order Number
                (GUID).
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Order Number.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage,
        executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-confirmation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderGuIdId": supplier_order_gu_id_id,
                "SupplierOrderId": supplier_order_id,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplierfinance/lastapprovefromsupplierer",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def supplier_financing_vendor_order_initiation(
        self,
        *,
        supplier_tax_number: str,
        purchaser_tax_number: str,
        order_number: str,
        amount: Number,
        fec: int,
        maturity_day_count: int,
        early_payment_day_count: int,
        description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Order Initiation.

        ``POST /supplierfinance/saveordersupplier``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API used to initiate orders.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Identify Supplier Tax
                Number.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Identify Purchaser
                Tax Number.
            order_number: (``OrderNumber``, gövde, zorunlu) Supplier specific order number.
            amount: (``Amount``, gövde, zorunlu) Order Amount.
            fec: (``Fec``, gövde, zorunlu) Order Fec (Always 0).
            maturity_day_count: (``MaturityDayCount``, gövde, zorunlu) Maturity day count.
            early_payment_day_count: (``EarlyPaymentDayCount``, gövde, zorunlu) How soon will
                the payment be made .
            description: (``Description``, gövde) description

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage,
        executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-initiation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "PurchaserTaxNumber": purchaser_tax_number,
                "OrderNumber": order_number,
                "Amount": amount,
                "Fec": fec,
                "MaturityDayCount": maturity_day_count,
                "EarlyPaymentDayCount": early_payment_day_count,
                "Description": description,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/supplierfinance/saveordersupplier",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def tedarikci_finansman_geri_odeme_plani_hesaplamasi(
        self,
        *,
        supplier_tax_number: str,
        supplier_order_id: str,
        maturity_day_count: int | None = None,
        early_payment_day_count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Tedarikçi Finansman Geri Ödeme Planı Hesaplaması.

        ``POST /v1/supplierfinance/getpaybackplan``

        Kapsam: ``loans`` · Akış: client credentials

        Siparişin satıcı tarafından iptal edildiği API'dir.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tedarikçi vergi
                numarasını tanımlayın.
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Sipariş numarası.
            maturity_day_count: (``MaturityDayCount``, gövde) Vade günü sayımı.
            early_payment_day_count: (``EarlyPaymentDayCount``, gövde) Erken ödeme günü sayımı.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/tedarikci-finansman-geri-odeme-plani-hesaplamasi
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderId": supplier_order_id,
                "MaturityDayCount": maturity_day_count,
                "EarlyPaymentDayCount": early_payment_day_count,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return self._client.request(
            "POST",
            "/v1/supplierfinance/getpaybackplan",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncCashManagement(AsyncResource):
    """Nakit yönetimi (asenkron) - ``kt.cash_management``."""

    async def cheque_information_micro(
        self,
        *,
        state: str | None = None,
        status: str | None = None,
        currency: str | None = None,
        start_date: str | None = None,
        finish_date: str | None = None,
        language_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """cheque-information-micro.

        ``POST /v1/cheque-information-micro``

        Kapsam: ``public`` · Akış: client credentials

        It is an API that provides the necessary data for customers to view information about
        checks they are owed or owed.

        Args:
            state: (gövde)
            status: (gövde)
            currency: (gövde)
            start_date: (``startDate``, gövde)
            finish_date: (``finishDate``, gövde)
            language_id: (``languageId``, gövde)

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/cheque-information-micro
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "state": state,
                "status": status,
                "currency": currency,
                "startDate": start_date,
                "finishDate": finish_date,
                "languageId": language_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/cheque-information-micro",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def dijital_bankacilik_iadesi(
        self,
        *,
        transaction_id: str,
        org_transaction_id: str,
        amount: Number,
        currency: str,
        comission_amount: Number,
        description: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Bankacılık İadesi.

        ``POST /v1/vpos/digitalPaymentRefund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Önceki gün içerisinde yapılan işlemlerde iade veya kısmi iade yapılır.

        Args:
            transaction_id: (``TransactionId``, gövde, zorunlu) İade işleminin tekil işlem
                numarası
            org_transaction_id: (``OrgTransactionId``, gövde, zorunlu) ComPay tarafından bankaya
                iade edilen orijinal işlemin benzersiz işlem numarası
            amount: (``Amount``, gövde, zorunlu) İade edilecek bilgi miktarı
            currency: (``Currency``, gövde, zorunlu) İşlem para birimi
            comission_amount: (``ComissionAmount``, gövde, zorunlu) İade işlemi için işyerinden
                alınacak komisyon tutarı.
            description: (``Description``, gövde, zorunlu) İşlem açıklaması

        Gövde alanları istekte ``DigitalPaymentRefundTransactionContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: ReturnCode, ReturnMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-iadesi
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionId": transaction_id,
                "OrgTransactionId": org_transaction_id,
                "Amount": amount,
                "Currency": currency,
                "ComissionAmount": comission_amount,
                "Description": description,
            },
            extra_body,
        )
        _body = {"DigitalPaymentRefundTransactionContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentRefund",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def dijital_bankacilik_islem_durumu(
        self,
        *,
        transaction_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Bankacılık İşlem Durumu.

        ``POST /v1/vpos/digitalPaymentStatus``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Parametrelerde belirtilen işlemin durumunu döndürür.

        Args:
            transaction_id: (``TransactionId``, gövde, zorunlu) İşlemin tekil işlem numarası

        Gövde alanları istekte ``DigitalPaymentStatContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ReturnCode, ReturnMessage, DiscountedAmount, ProductType, CostAmount,
        ComissionAmount, Amount, TransactionType, TransactionId, OrgTransactionId

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-islem-durumu
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionId": transaction_id,
            },
            extra_body,
        )
        _body = {"DigitalPaymentStatContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentStatus",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def dijital_bankacilik_odeme(
        self,
        *,
        transaction_id: str,
        merchant_id: str,
        soft_descriptor: str,
        product_type: str,
        comission_amount: Number,
        amount: Number,
        transaction_currency: int,
        token_interval: int,
        payment_method: str,
        cost_amount: Number | None = None,
        success_redirect_url: str | None = None,
        fail_redirect_url: str | None = None,
        os: str | None = None,
        product_type_condition: str | None = None,
        pan: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Bankacılık Ödeme.

        ``POST /v1/vpos/digitalPayment``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Parametrelerde sağlanan müşteri profilinden ödeme bilgilerini toplar.

        Args:
            transaction_id: (``TransactionId``, gövde, zorunlu) Tekil bir sayının işlenmesi.
            merchant_id: (``MerchantId``, gövde, zorunlu) Banka tarafından belirlenen şirket
                kodu
            soft_descriptor: (``SoftDescriptor``, gövde, zorunlu) Tüccar işlem belirteci.
            product_type: (``ProductType``, gövde, zorunlu) Hesaplanan maliyetler ve komisyon
                ödeme türleri
            cost_amount: (``CostAmount``, gövde)
            comission_amount: (``ComissionAmount``, gövde, zorunlu) A commission fee will be
                taken from the workplace.
            amount: (``Amount``, gövde, zorunlu) İşlem tutarı
            transaction_currency: (``TransactionCurrency``, gövde, zorunlu) İşlem para birimi
            token_interval: (``TokenInterval``, gövde, zorunlu) Dakikalar içinde talep edilen
                token geçerlilik süresi
            success_redirect_url: (``SuccessRedirectUrl``, gövde) Müşteri, bankacılığın başarısı
                için adresi yönlendiriyor
            fail_redirect_url: (``FailRedirectUrl``, gövde) Müşteri yönlendirme adresi
                bankacılık tarafından başarısız oldu
            payment_method: (``PaymentMethod``, gövde, zorunlu) Ödeme yöntemi bilgisi
            os: (``OS``, gövde) Mobil uygulamanın işletim sistemi bilgisi.
            product_type_condition: (``ProductTypeCondition``, gövde) Farklı ürün tipleri için
                hesaplanan maliyet ve komisyon bilgileri
            pan: (``Pan``, gövde) Müşteri bilgilerinin doğruluğunu gösteren işlem

        Gövde alanları istekte ``DigitalPaymentTransactionContract`` nesnesinin içine
        yerleştirilir.

        Yanıt alanları: AccessToken, TokenExpireDate, ReturnCode, ReturnMessage,
        ApplicationName, ApplicationParameter

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/dijital-bankacilik-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "TransactionId": transaction_id,
                "MerchantId": merchant_id,
                "SoftDescriptor": soft_descriptor,
                "ProductType": product_type,
                "CostAmount": cost_amount,
                "ComissionAmount": comission_amount,
                "Amount": amount,
                "TransactionCurrency": transaction_currency,
                "TokenInterval": token_interval,
                "SuccessRedirectUrl": success_redirect_url,
                "FailRedirectUrl": fail_redirect_url,
                "PaymentMethod": payment_method,
                "OS": os,
                "ProductTypeCondition": product_type_condition,
                "Pan": pan,
            },
            extra_body,
        )
        _body = {"DigitalPaymentTransactionContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/digitalPayment",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def school_installment_payment_system_active_registration_inquiry_api(
        self,
        *,
        identity_number: str,
        client_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """School Installment Payment System Active Registration Inquiry API.

        ``POST /v1/school-installment/registration-inquiry``

        Kapsam: ``loans`` · Akış: client credentials

        Institutions could check through this API using the Turkish National Identity Number
        (TCKN) to determine if a student currently has an OTS registration. OTS registration is
        considered "Yes" or "No" as follows: - Canceled registration = "No" - All installments
        collected without credit = "No" - All installments collected, including some with credit
        = "Yes" - If there are installments pending payment = "Yes" * As long as any payment
        (credit or cash) is pending, OTS is considered to exist.

        Args:
            identity_number: (``IdentityNumber``, gövde, zorunlu) Öğrenci TCKN bilgisi
            client_id: (``ClientId``, gövde, zorunlu) Kurum token bilgisi

        Gövde alanları istekte ``payment`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-payment-system-active-registration-inquiry-api
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ClientId": client_id,
            },
            extra_body,
        )
        _body = {"payment": _body}
        return await self._client.request(
            "POST",
            "/v1/school-installment/registration-inquiry",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def school_installment_system_registration_and_installment_cancellation_api(
        self,
        *,
        client_id: str,
        identity_number: str | None = None,
        invoice_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """School Installment System Registration and Installment Cancellation API.

        ``POST /v1/school-installment/cancelation``

        Kapsam: ``loans`` · Akış: client credentials

        Schools/Institutions can perform cancellations based on installments or Turkish National
        Identity Number (TCKN) via this API. - When only the TCKN is entered, all records and
        installments associated with that TCKN are not cancelled. - When both the TCKN and
        Invoice Number are sent, only the relevant installment is cancelled.

        Args:
            identity_number: (``IdentityNumber``, gövde) Öğrenci TCKN bilgisi
            client_id: (``ClientId``, gövde, zorunlu) Kurum token bilgisi
            invoice_number: (``InvoiceNumber``, gövde) Fatura/Taksit Numarası

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-registration-and-installment-cancellation-api
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ClientId": client_id,
                "InvoiceNumber": invoice_number,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/school-installment/cancelation",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def school_installment_system_school_guaranteed_registration_payment(
        self,
        *,
        client_id: str,
        identity_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """School Installment System School Guaranteed Registration Payment.

        ``POST /v1/school-installment/transaction-information``

        Kapsam: ``loans`` · Akış: client credentials

        School-Guaranteed schools can use this API to track parent payments based on payment
        documentation or date range. --PaymentType description: --0 --&gt; account or card, --1
        --&gt; not converted to credit but unpaid, --2 --&gt; converted to credit, parent paid,
        --3 --&gt; converted to credit, school paid

        Args:
            identity_number: (``IdentityNumber``, gövde) Öğrenci TCKN bilgisi
            client_id: (``ClientId``, gövde, zorunlu) Kurum token bilgisi

        Gövde alanları istekte ``payment`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/school-installment-system-school-guaranteed-registration-payment
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "IdentityNumber": identity_number,
                "ClientId": client_id,
            },
            extra_body,
        )
        _body = {"payment": _body}
        return await self._client.request(
            "POST",
            "/v1/school-installment/transaction-information",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_buyer_order_confirmation(
        self,
        *,
        purchaser_tax_number: str,
        supplier_order_gu_id_id: str,
        supplier_order_id: str,
        list_approve_from_purchaser_contract: Sequence[Any],
        tax_exclusive_amount: Number,
        contract: Sequence[Any] | None = None,
        used_invoice_amount: Number | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Buyer Order Confirmation.

        ``POST /v1/supplierfinance/approvefrompurchaserer``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API where invoices are uploaded to the system by the receiving company.

        Args:
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Identify Purchaser
                Tax Number.
            supplier_order_gu_id_id: (``SupplierOrderGuIdId``, gövde, zorunlu) Order Number
                (GUID).
            contract: (gövde)
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Order Number.
            list_approve_from_purchaser_contract: (``ListApproveFromPurchaserContract``, gövde,
                zorunlu) Contains invoice info.
            used_invoice_amount: (``UsedInvoiceAmount``, gövde) How much of the bill will be
                used.
            tax_exclusive_amount: (``TaxExclusiveAmount``, gövde, zorunlu) Tax exclusive amount.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage,
        executionReferenceId, SupplierOrderInvoiceList, InvoiceNumber, InvoiceStatus,
        InvoiceStatusName, InvoiceAmount, PaymentAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-confirmation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "PurchaserTaxNumber": purchaser_tax_number,
                "SupplierOrderGuIdId": supplier_order_gu_id_id,
                "contract": contract,
                "SupplierOrderId": supplier_order_id,
                "ListApproveFromPurchaserContract": list_approve_from_purchaser_contract,
                "UsedInvoiceAmount": used_invoice_amount,
                "TaxExclusiveAmount": tax_exclusive_amount,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplierfinance/approvefrompurchaserer",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_buyer_order_listing(
        self,
        *,
        client_id: str,
        purchaser_tax_number: str,
        first_transaction_date: DateLike | None = None,
        end_transaction_date: DateLike | None = None,
        supplier_order_id: int | None = None,
        is_transaction_date_invoice_date: int | None = None,
        supplier_tax_number: str | None = None,
        order_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Buyer Order Listing.

        ``POST /v1/supplierfinance/getorderbypurchaser``

        Kapsam: ``loans`` · Akış: client credentials

        Retrieves supplier financing buyer order records according to the provided purchaser,
        supplier, order, date range, and transaction date filter criteria. The response includes
        supplier order, invoice, payment, status, amount, currency, profit rate, commission
        rate, and description details.

        Args:
            client_id: (``ClientId``, gövde, zorunlu) Client identifier used for the supplier
                financing order listing request.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Tax number of the
                purchaser used to filter supplier financing orders.
            first_transaction_date: (``FirstTransactionDate``, gövde) Start date of the
                transaction date range.
            end_transaction_date: (``EndTransactionDate``, gövde) End date of the transaction
                date range.
            supplier_order_id: (``supplierOrderId``, gövde) Supplier order identifier used to
                filter a specific order.
            is_transaction_date_invoice_date: (``isTransactionDateInvoiceDate``, gövde)
                Indicates whether the transaction date filter should be evaluated as invoice date.
            supplier_tax_number: (``supplierTaxNumber``, gövde) Tax number of the supplier used
                to filter supplier financing orders.
            order_number: (``orderNumber``, gövde) Order number used to filter supplier
                financing orders.

        Gövde alanları istekte ``listOrderContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderId, SupplierOrderGuidId, OrderNumber, InvoiceNumber,
        Status, StatusName, InvoiceStatus, InvoiceStatusName, OrderDate, OrderAmount,
        InvoiceAmount, PaymentAmount, LoanProfitRate, LoanCommissionRate, FecCode, Description,
        SupplierTaxNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-buyer-order-listing
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "ClientId": client_id,
                "PurchaserTaxNumber": purchaser_tax_number,
                "FirstTransactionDate": first_transaction_date,
                "EndTransactionDate": end_transaction_date,
                "supplierOrderId": supplier_order_id,
                "isTransactionDateInvoiceDate": is_transaction_date_invoice_date,
                "supplierTaxNumber": supplier_tax_number,
                "orderNumber": order_number,
            },
            extra_body,
        )
        _body = {"listOrderContract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplierfinance/getorderbypurchaser",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_invoice_cancellation(
        self,
        *,
        client_id: str,
        purchaser_invoice_upload_guid: str,
        api_client_invoice_upload_guid: str,
        purchaser_tax_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Invoice Cancellation.

        ``POST /v1/supplychainfinance/cancelinvoice``

        Kapsam: ``loans`` · Akış: client credentials

        This API cancels a supply chain finance invoice. The cancellation operation is processed
        using the client identifier, purchaser invoice upload GUID, API client invoice upload
        GUID and purchaser tax number. The response includes the invoice cancellation status and
        result message.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the invoice cancellation
                request.
            purchaser_invoice_upload_guid: (``PurchaserInvoiceUploadGUID``, gövde, zorunlu) GUID
                identifier of the purchaser invoice upload record to be cancelled.
            api_client_invoice_upload_guid: (``APIClientInvoiceUploadGUID``, gövde, zorunlu)
                GUID identifier of the invoice upload record on the API client side.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Tax number of the
                purchaser related to the invoice cancellation request.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: PurchaserInvoiceUploadGUID, APIClientInvoiceUploadGUID, Status,
        StatusName, ResultMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-invoice-cancellation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "PurchaserInvoiceUploadGUID": purchaser_invoice_upload_guid,
                "APIClientInvoiceUploadGUID": api_client_invoice_upload_guid,
                "PurchaserTaxNumber": purchaser_tax_number,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplychainfinance/cancelinvoice",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_order_last_approval_by_supplier(
        self,
        *,
        client_id: str,
        supplier_tax_number: str,
        supplier_order_id: int,
        supplier_order_guid_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Order Last Approval by Supplier.

        ``POST /v1/supplierfinance/lastapprovefromsupplier``

        Kapsam: ``loans`` · Akış: client credentials

        This API performs the final approval of a supplier financing order by the supplier. The
        approval operation is processed using the client identifier, supplier tax number,
        supplier order identifier and supplier order GUID.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the supplier financing final
                approval request.
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tax number of the
                supplier approving the supplier financing order.
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Unique identifier of the
                supplier financing order to be approved.
            supplier_order_guid_id: (``SupplierOrderGuidId``, gövde, zorunlu) GUID identifier of
                the supplier financing order to be approved.

        Gövde alanları istekte ``Contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-order-last-approval-by-supplier
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderId": supplier_order_id,
                "SupplierOrderGuidId": supplier_order_guid_id,
            },
            extra_body,
        )
        _body = {"Contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplierfinance/lastapprovefromsupplier",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_vendor_company_invoice_approval(
        self,
        *,
        client_id: str,
        purchaser_invoice_upload_guid: str,
        api_client_invoice_upload_guid: str,
        supplier_tax_number: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Company Invoice Approval.

        ``POST /v1/supplychainfinance/supplierapproveinvoice``

        Kapsam: ``loans`` · Akış: client credentials

        This API approves a supply chain finance invoice by the supplier. The approval operation
        is processed using the client identifier, purchaser invoice upload GUID, API client
        invoice upload GUID and supplier tax number. The response includes invoice approval
        status, result message and invoice list details.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the supplier invoice approval
                request.
            purchaser_invoice_upload_guid: (``PurchaserInvoiceUploadGUID``, gövde, zorunlu) GUID
                identifier of the purchaser invoice upload record to be approved by the supplier.
            api_client_invoice_upload_guid: (``APIClientInvoiceUploadGUID``, gövde, zorunlu)
                GUID identifier of the invoice upload record on the API client side.
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tax number of the
                supplier approving the invoice.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: PurchaserInvoiceUploadGUID, APIClientInvoiceUploadGUID, Status,
        StatusName, ResultMessage, InvoiceList, InvoiceNumber, InvoiceStatus, InvoiceStatusName,
        InvoiceAmount, PaymentAmount

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-company-invoice-approval
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "PurchaserInvoiceUploadGUID": purchaser_invoice_upload_guid,
                "APIClientInvoiceUploadGUID": api_client_invoice_upload_guid,
                "SupplierTaxNumber": supplier_tax_number,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplychainfinance/supplierapproveinvoice",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_vendor_invoice_listing(
        self,
        *,
        client_id: str,
        supplier_tax_number: str,
        purchaser_invoice_upload_guid: str | None = None,
        purchaser_tax_number: str | None = None,
        first_transaction_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Invoice Listing.

        ``POST /v1/supplychainfinance/supplierinvoicelist``

        Kapsam: ``loans`` · Akış: client credentials

        This API retrieves supply chain finance invoice records for a supplier based on the
        provided purchaser invoice upload GUID, purchaser tax number, supplier tax number and
        transaction date criteria. The response includes invoice identifiers, invoice status,
        invoice amount, payment amount, loan profit rate, currency code and tax number details.

        Args:
            client_id: (gövde, zorunlu) Client identifier used for the supplier invoice list
                request.
            purchaser_invoice_upload_guid: (``PurchaserInvoiceUploadGUID``, gövde) GUID
                identifier of the purchaser invoice upload record used to filter invoices.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde) Tax number of the purchaser
                used to filter supplier invoices.
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tax number of the
                supplier used to filter supplier invoices.
            first_transaction_date: (``FirstTransactionDate``, gövde) Start date of the
                transaction date range.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: PurchaserInvoiceUploadGUID, APIClientInvoiceUploadGUID, InvoiceList,
        InvoiceNumber, InvoiceStatus, InvoiceStatusName, InvoiceAmount, PaymentAmount,
        LoanProfitRate, InvoiceFecCode, SupplierTaxNumber, PurchaserTaxNumber

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-invoice-listing
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "client_id": client_id,
                "PurchaserInvoiceUploadGUID": purchaser_invoice_upload_guid,
                "PurchaserTaxNumber": purchaser_tax_number,
                "SupplierTaxNumber": supplier_tax_number,
                "FirstTransactionDate": first_transaction_date,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplychainfinance/supplierinvoicelist",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_vendor_order_cancellation(
        self,
        *,
        supplier_tax_number: str,
        supplier_order_id: str,
        order_number: str,
        supplier_order_guid_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Order Cancellation.

        ``POST /v1/supplierfinance/cancelFromSupplier``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API where the order is canceled by the vendor.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Identify Supplier Tax
                Number.
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Order Number.
            order_number: (``OrderNumber``, gövde, zorunlu) Order number.
            supplier_order_guid_id: (``SupplierOrderGuidId``, gövde, zorunlu) Order Number
                (GUID).

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, OrderNumber, Status, StatusName, ResultMessage,
        executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-cancellation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderId": supplier_order_id,
                "OrderNumber": order_number,
                "SupplierOrderGuidId": supplier_order_guid_id,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplierfinance/cancelFromSupplier",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_vendor_order_confirmation(
        self,
        *,
        supplier_tax_number: str,
        supplier_order_gu_id_id: str,
        supplier_order_id: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Order Confirmation.

        ``POST /v1/supplierfinance/lastapprovefromsupplierer``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API through which the order is approved by the vendor.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Identify Supplier Tax
                Number.
            supplier_order_gu_id_id: (``SupplierOrderGuIdId``, gövde, zorunlu) Order Number
                (GUID).
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Order Number.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage,
        executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-confirmation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderGuIdId": supplier_order_gu_id_id,
                "SupplierOrderId": supplier_order_id,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplierfinance/lastapprovefromsupplierer",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def supplier_financing_vendor_order_initiation(
        self,
        *,
        supplier_tax_number: str,
        purchaser_tax_number: str,
        order_number: str,
        amount: Number,
        fec: int,
        maturity_day_count: int,
        early_payment_day_count: int,
        description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Supplier Financing Vendor Order Initiation.

        ``POST /supplierfinance/saveordersupplier``

        Kapsam: ``loans`` · Akış: client credentials

        It is the API used to initiate orders.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Identify Supplier Tax
                Number.
            purchaser_tax_number: (``PurchaserTaxNumber``, gövde, zorunlu) Identify Purchaser
                Tax Number.
            order_number: (``OrderNumber``, gövde, zorunlu) Supplier specific order number.
            amount: (``Amount``, gövde, zorunlu) Order Amount.
            fec: (``Fec``, gövde, zorunlu) Order Fec (Always 0).
            maturity_day_count: (``MaturityDayCount``, gövde, zorunlu) Maturity day count.
            early_payment_day_count: (``EarlyPaymentDayCount``, gövde, zorunlu) How soon will
                the payment be made .
            description: (``Description``, gövde) description

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: SupplierOrderGuidId, Status, StatusName, ResultMessage,
        executionReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/cash-management/supplier-financing-vendor-order-initiation
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "PurchaserTaxNumber": purchaser_tax_number,
                "OrderNumber": order_number,
                "Amount": amount,
                "Fec": fec,
                "MaturityDayCount": maturity_day_count,
                "EarlyPaymentDayCount": early_payment_day_count,
                "Description": description,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/supplierfinance/saveordersupplier",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def tedarikci_finansman_geri_odeme_plani_hesaplamasi(
        self,
        *,
        supplier_tax_number: str,
        supplier_order_id: str,
        maturity_day_count: int | None = None,
        early_payment_day_count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Tedarikçi Finansman Geri Ödeme Planı Hesaplaması.

        ``POST /v1/supplierfinance/getpaybackplan``

        Kapsam: ``loans`` · Akış: client credentials

        Siparişin satıcı tarafından iptal edildiği API'dir.

        Args:
            supplier_tax_number: (``SupplierTaxNumber``, gövde, zorunlu) Tedarikçi vergi
                numarasını tanımlayın.
            supplier_order_id: (``SupplierOrderId``, gövde, zorunlu) Sipariş numarası.
            maturity_day_count: (``MaturityDayCount``, gövde) Vade günü sayımı.
            early_payment_day_count: (``EarlyPaymentDayCount``, gövde) Erken ödeme günü sayımı.

        Gövde alanları istekte ``contract`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/nakit-yonetimi/tedarikci-finansman-geri-odeme-plani-hesaplamasi
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "SupplierTaxNumber": supplier_tax_number,
                "SupplierOrderId": supplier_order_id,
                "MaturityDayCount": maturity_day_count,
                "EarlyPaymentDayCount": early_payment_day_count,
            },
            extra_body,
        )
        _body = {"contract": _body}
        return await self._client.request(
            "POST",
            "/v1/supplierfinance/getpaybackplan",
            scope="loans",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
