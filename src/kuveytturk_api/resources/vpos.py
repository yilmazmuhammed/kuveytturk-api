"""Sanal POS uç noktaları (``kt.vpos``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, Resource, merge

__all__ = ["AsyncVpos", "Vpos"]


class Vpos(Resource):
    """Sanal POS - ``kt.vpos``."""

    def _3_d_secure_odeme(
        self,
        *,
        card_expire_date_month: str | None = None,
        amount: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        success_url: str | None = None,
        fail_url: str | None = None,
        description: str | None = None,
        merchant_order_id: str | None = None,
        user_name: str | None = None,
        card_expire_date_year: str | None = None,
        merchant_id: str | None = None,
        hash_data: str | None = None,
        installment_count: str | None = None,
        deferring_count: str | None = None,
        currency: str | None = None,
        card_number: str | None = None,
        currency_code: Any | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """3D Secure Ödeme.

        ``POST /v1/vpos/threeDPayment``

        Kapsam: ``public`` · Akış: client credentials

        Virtual POS 3D Secure (threeDPayment), kart sahibi, banka ve satıcı arasındaki veri
        akışını özel şifreleme anahtarları kullanarak doğrulayarak e-ticaret işlemlerinde
        güvenliği artıran bir çevrimiçi ödeme işleme altyapısıdır.

        Args:
            card_expire_date_month: (``cardExpireDateMonth``, gövde) Sanal POS mağaza numarası.
                Başvuru onayıyla birlikte işletmeye e-posta yoluyla gönderilir.
            amount: (gövde) Tutar. Örneğin, İşlem Tutarı: 1 TL için 100, 1.234,50 TL için 123450
                gönderilmelidir.
            card_cvv2: (``cardCVV2``, gövde) ​​Kart CVV değeri
            card_holder_name: (``cardHolderName``, gövde) Kart sahibinin adı
            success_url: (``successUrl``, gövde) Güvenli Ödeme işlemlerinde, kart doğrulama
                aşamasında kullanıcı SMS yoluyla doğrulama sayfasına yönlendirilir.
            fail_url: (``failUrl``, gövde) Kart doğrulama hatası veya parametrelere bağlı olarak
                oluşabilecek hatalar durumunda sonucun gönderileceği adres.
            description: (gövde) açıklama
            merchant_order_id: (``merchantOrderId``, gövde) Bu, müşteri sipariş numarasını
                temsil eder.
            user_name: (``userName``, gövde) API kullanıcı adı.
            card_expire_date_year: (``cardExpireDateYear``, gövde) Kartın son kullanma yılı
            merchant_id: (``merchantId``, gövde) Sanal POS mağaza numarası. Başvuru
                onaylandıktan sonra işletmeye e-posta yoluyla gönderilecektir.
            hash_data: (``hashData``, gövde) İşletmenin oluşturduğu ve işlem bilgileriyle
                birlikte gönderdiği ve banka tarafından kontrol edilen alan.
            installment_count: (``installmentCount``, gövde) Bu, satıcı tarafından güvenli iş
                ortağı ödeme sayfasına gönderilecek taksit tutarını temsil eder.
            deferring_count: (``deferringCount``, gövde) Harcama erteleme bilgileri
            currency: (gövde)
            card_number: (``cardNumber``, gövde) “Sale” Güvenli İş Ortağı Ödeme sisteminden
                yapılacak işlemin bir satış işlemi olduğunu gösterir.
            currency_code: (``currencyCode``, gövde) Para birimi. TL için “0949” olarak
                gönderilmelidir.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Yanıt alanları: htmlContent, responseCode, responseMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/3d-secure-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cardExpireDateMonth": card_expire_date_month,
                "amount": amount,
                "cardCVV2": card_cvv2,
                "cardHolderName": card_holder_name,
                "successUrl": success_url,
                "failUrl": fail_url,
                "description": description,
                "merchantOrderId": merchant_order_id,
                "userName": user_name,
                "cardExpireDateYear": card_expire_date_year,
                "merchantId": merchant_id,
                "hashData": hash_data,
                "installmentCount": installment_count,
                "deferringCount": deferring_count,
                "currency": currency,
                "cardNumber": card_number,
                "currencyCode": currency_code,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/threeDPayment",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def dijital_odeme_komisyon_mutabakati(
        self,
        *,
        transaction_list: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Ödeme Komisyon Mutabakatı.

        ``POST /v1/vpos/commissionReconciliation``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Gönderilen transaction list bilgilerine göre digital payment transactions için
        commission reconciliation işlemi yapar. Cevapta her transaction için transaction
        identifier, status code, status message ve commission type bilgileriyle birlikte
        reconciliation status bilgisi döner.

        Args:
            transaction_list: (``transactionList``, gövde, zorunlu) Commission reconciliation
                işlemine dahil edilecek digital payment transaction listesidir.

        Yanıt alanları: transactionId, statusCode, statusMessage, commissionType

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/dijital-odeme-komisyon-mutabakati
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionList": transaction_list,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/vpos/commissionReconciliation",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def duzenli_non_three_d_odeme(
        self,
        *,
        merchant_order_id: str | None = None,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        user_name: str | None = None,
        hash_data: str | None = None,
        amount: str | None = None,
        currency: str | None = None,
        installment_count: int | None = None,
        deferring_count: int | None = None,
        card_number: str | None = None,
        card_expire_date_year: str | None = None,
        card_expire_date_month: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        description: str | None = None,
        customer_name: str | None = None,
        payment_start_date: str | None = None,
        iteration_counter: int | None = None,
        period_number: int | None = None,
        period_type: int | None = None,
        card_holder_customer_id: int | None = None,
        merchant_customer_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Düzenli NonThreeD Ödeme.

        ``POST /v1/vpos/recurringNonThreeDPayment``

        Kapsam: ``public`` · Akış: client credentials

        Düzenli / tekrarlı ödeme almak için kullanılan API’dır.

        Args:
            merchant_order_id: (``merchantOrderId``, gövde)
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            hash_data: (``hashData``, gövde)
            amount: (gövde)
            currency: (gövde)
            installment_count: (``installmentCount``, gövde)
            deferring_count: (``deferringCount``, gövde)
            card_number: (``cardNumber``, gövde)
            card_expire_date_year: (``cardExpireDateYear``, gövde)
            card_expire_date_month: (``cardExpireDateMonth``, gövde)
            card_cvv2: (``cardCvv2``, gövde)
            card_holder_name: (``cardHolderName``, gövde)
            description: (gövde)
            customer_name: (``customerName``, gövde)
            payment_start_date: (``paymentStartDate``, gövde)
            iteration_counter: (``iterationCounter``, gövde)
            period_number: (``periodNumber``, gövde)
            period_type: (``periodType``, gövde)
            card_holder_customer_id: (``cardHolderCustomerId``, gövde)
            merchant_customer_id: (``merchantCustomerId``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/duzenli-nonthreed-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantOrderId": merchant_order_id,
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "hashData": hash_data,
                "amount": amount,
                "currency": currency,
                "installmentCount": installment_count,
                "deferringCount": deferring_count,
                "cardNumber": card_number,
                "cardExpireDateYear": card_expire_date_year,
                "cardExpireDateMonth": card_expire_date_month,
                "cardCvv2": card_cvv2,
                "cardHolderName": card_holder_name,
                "description": description,
                "customerName": customer_name,
                "paymentStartDate": payment_start_date,
                "iterationCounter": iteration_counter,
                "periodNumber": period_number,
                "periodType": period_type,
                "cardHolderCustomerId": card_holder_customer_id,
                "merchantCustomerId": merchant_customer_id,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/recurringNonThreeDPayment",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def gelen_odeme_iptali(
        self,
        *,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        user_name: str | None = None,
        merchant_order_id: str | None = None,
        amount: int | None = None,
        ok_url: str | None = None,
        fail_url: str | None = None,
        entry_gate_method: str | None = None,
        hash_data: str | None = None,
        parent_payment_id: int | None = None,
        payment_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Gelen Ödeme İptali.

        ``POST /v1/vpos/paymentOrderReversal``

        Kapsam: ``public`` · Akış: client credentials

        Henüz kesinleşmemiş / tahsilata dönüşmemiş bir “tahsilat işlemini”nin iptal edilmesi
        için kullanılır.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            amount: (gövde)
            ok_url: (``okUrl``, gövde)
            fail_url: (``failUrl``, gövde)
            entry_gate_method: (``entryGateMethod``, gövde)
            hash_data: (``hashData``, gövde)
            parent_payment_id: (``parentPaymentId``, gövde)
            payment_id: (``paymentId``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/gelen-odeme-iptali
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "merchantOrderId": merchant_order_id,
                "amount": amount,
                "okUrl": ok_url,
                "failUrl": fail_url,
                "entryGateMethod": entry_gate_method,
                "hashData": hash_data,
                "parentPaymentId": parent_payment_id,
                "paymentId": payment_id,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/paymentOrderReversal",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def isyeri_onayli_non_three_d_odeme(
        self,
        *,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        payment_customer_id: int | None = None,
        merchant_order_id: str | None = None,
        user_name: str | None = None,
        hash_data: str | None = None,
        amount: str | None = None,
        currency: str | None = None,
        installment_count: int | None = None,
        deferring_count: int | None = None,
        safe_key: str | None = None,
        description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """İşyeri Onaylı NonThreeD Ödeme.

        ``POST /v1/vpos/nonThreeDPaymentByMerchantSafe``

        Kapsam: ``public`` · Akış: client credentials

        İşyeri onaylı olan NonThreeD Ödeme işlemi yapılan API’dır.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            payment_customer_id: (``paymentCustomerId``, gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            user_name: (``userName``, gövde)
            hash_data: (``hashData``, gövde)
            amount: (gövde)
            currency: (gövde)
            installment_count: (``installmentCount``, gövde)
            deferring_count: (``deferringCount``, gövde)
            safe_key: (``safeKey``, gövde)
            description: (gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/isyeri-onayli-nonthreed-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "paymentCustomerId": payment_customer_id,
                "merchantOrderId": merchant_order_id,
                "userName": user_name,
                "hashData": hash_data,
                "amount": amount,
                "currency": currency,
                "installmentCount": installment_count,
                "deferringCount": deferring_count,
                "safeKey": safe_key,
                "description": description,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/nonThreeDPaymentByMerchantSafe",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def merchant_safe_icin_kart_ekleme(
        self,
        *,
        business_key: int | None = None,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        user_name: str | None = None,
        hash_data: str | None = None,
        merchant_order_id: str | None = None,
        payment_customer_id: int | None = None,
        card_number: str | None = None,
        card_expire_date_month: str | None = None,
        card_expire_date_year: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Merchant‑Safe için Kart Ekleme.

        ``POST /v1/vpos/addCardToMerchantSafe``

        Kapsam: ``public`` · Akış: client credentials

        Merchant‑safe (işyeri sorumluluğunda) Non‑3D Secure ödeme akışlarında kullanılmak üzere,
        müşterinin kart bilgisini ödeme sistemine güvenli şekilde kaydetmek için kullanılan
        API’dir.

        Args:
            business_key: (``businessKey``, gövde)
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            hash_data: (``hashData``, gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            payment_customer_id: (``paymentCustomerId``, gövde)
            card_number: (``cardNumber``, gövde)
            card_expire_date_month: (``cardExpireDateMonth``, gövde)
            card_expire_date_year: (``cardExpireDateYear``, gövde)
            card_cvv2: (``cardCvv2``, gövde)
            card_holder_name: (``cardHolderName``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/merchant-safe-icin-kart-ekleme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "businessKey": business_key,
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "hashData": hash_data,
                "merchantOrderId": merchant_order_id,
                "paymentCustomerId": payment_customer_id,
                "cardNumber": card_number,
                "cardExpireDateMonth": card_expire_date_month,
                "cardExpireDateYear": card_expire_date_year,
                "cardCvv2": card_cvv2,
                "cardHolderName": card_holder_name,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/addCardToMerchantSafe",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def on_provizyon(
        self,
        *,
        merchant_id: str | None = None,
        customer_id: str | None = None,
        user_name: str | None = None,
        amount: str | None = None,
        merchant_order_id: str | None = None,
        card_number: str | None = None,
        card_expire_date_year: str | None = None,
        card_expire_date_month: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        currency: str | None = None,
        hash_data: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ön Provizyon.

        ``POST /v1/vpos/preAuthorization``

        Kapsam: ``public`` · Akış: client credentials

        Müşteri kartından tutar tahsil edilmeden, belirtilen tutar için ön provizyon (limit
        blokajı) almak amacıyla kullanılan sanal POS servisidir.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            amount: (gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            card_number: (``cardNumber``, gövde)
            card_expire_date_year: (``cardExpireDateYear``, gövde)
            card_expire_date_month: (``cardExpireDateMonth``, gövde)
            card_cvv2: (``cardCVV2``, gövde)
            card_holder_name: (``cardHolderName``, gövde)
            currency: (gövde)
            hash_data: (``hashData``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/on-provizyon
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "amount": amount,
                "merchantOrderId": merchant_order_id,
                "cardNumber": card_number,
                "cardExpireDateYear": card_expire_date_year,
                "cardExpireDateMonth": card_expire_date_month,
                "cardCVV2": card_cvv2,
                "cardHolderName": card_holder_name,
                "currency": currency,
                "hashData": hash_data,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/preAuthorization",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def satis_islemi_iptal(
        self,
        *,
        merchant_id: str | None = None,
        customer_id: str | None = None,
        user_name: str | None = None,
        amount: int | None = None,
        merchant_order_id: str | None = None,
        order_id: int | None = None,
        hash_data: str | None = None,
        sale_reversal_type: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Satış İşlemi İptal.

        ``POST /v1/vpos/saleOrderReversal``

        Kapsam: ``public`` · Akış: client credentials

        Başarılı bir satış işlemini gün sonu öncesinde iptal ederek tahsilatın tamamen geri
        alınmasını sağlar.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            amount: (gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            order_id: (``orderId``, gövde)
            hash_data: (``hashData``, gövde)
            sale_reversal_type: (``saleReversalType``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/satis-islemi-iptal
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "amount": amount,
                "merchantOrderId": merchant_order_id,
                "orderId": order_id,
                "hashData": hash_data,
                "saleReversalType": sale_reversal_type,
            },
            extra_body,
        )
        _body = {"request": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/saleOrderReversal",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncVpos(AsyncResource):
    """Sanal POS (asenkron) - ``kt.vpos``."""

    async def _3_d_secure_odeme(
        self,
        *,
        card_expire_date_month: str | None = None,
        amount: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        success_url: str | None = None,
        fail_url: str | None = None,
        description: str | None = None,
        merchant_order_id: str | None = None,
        user_name: str | None = None,
        card_expire_date_year: str | None = None,
        merchant_id: str | None = None,
        hash_data: str | None = None,
        installment_count: str | None = None,
        deferring_count: str | None = None,
        currency: str | None = None,
        card_number: str | None = None,
        currency_code: Any | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """3D Secure Ödeme.

        ``POST /v1/vpos/threeDPayment``

        Kapsam: ``public`` · Akış: client credentials

        Virtual POS 3D Secure (threeDPayment), kart sahibi, banka ve satıcı arasındaki veri
        akışını özel şifreleme anahtarları kullanarak doğrulayarak e-ticaret işlemlerinde
        güvenliği artıran bir çevrimiçi ödeme işleme altyapısıdır.

        Args:
            card_expire_date_month: (``cardExpireDateMonth``, gövde) Sanal POS mağaza numarası.
                Başvuru onayıyla birlikte işletmeye e-posta yoluyla gönderilir.
            amount: (gövde) Tutar. Örneğin, İşlem Tutarı: 1 TL için 100, 1.234,50 TL için 123450
                gönderilmelidir.
            card_cvv2: (``cardCVV2``, gövde) ​​Kart CVV değeri
            card_holder_name: (``cardHolderName``, gövde) Kart sahibinin adı
            success_url: (``successUrl``, gövde) Güvenli Ödeme işlemlerinde, kart doğrulama
                aşamasında kullanıcı SMS yoluyla doğrulama sayfasına yönlendirilir.
            fail_url: (``failUrl``, gövde) Kart doğrulama hatası veya parametrelere bağlı olarak
                oluşabilecek hatalar durumunda sonucun gönderileceği adres.
            description: (gövde) açıklama
            merchant_order_id: (``merchantOrderId``, gövde) Bu, müşteri sipariş numarasını
                temsil eder.
            user_name: (``userName``, gövde) API kullanıcı adı.
            card_expire_date_year: (``cardExpireDateYear``, gövde) Kartın son kullanma yılı
            merchant_id: (``merchantId``, gövde) Sanal POS mağaza numarası. Başvuru
                onaylandıktan sonra işletmeye e-posta yoluyla gönderilecektir.
            hash_data: (``hashData``, gövde) İşletmenin oluşturduğu ve işlem bilgileriyle
                birlikte gönderdiği ve banka tarafından kontrol edilen alan.
            installment_count: (``installmentCount``, gövde) Bu, satıcı tarafından güvenli iş
                ortağı ödeme sayfasına gönderilecek taksit tutarını temsil eder.
            deferring_count: (``deferringCount``, gövde) Harcama erteleme bilgileri
            currency: (gövde)
            card_number: (``cardNumber``, gövde) “Sale” Güvenli İş Ortağı Ödeme sisteminden
                yapılacak işlemin bir satış işlemi olduğunu gösterir.
            currency_code: (``currencyCode``, gövde) Para birimi. TL için “0949” olarak
                gönderilmelidir.

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Yanıt alanları: htmlContent, responseCode, responseMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/3d-secure-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "cardExpireDateMonth": card_expire_date_month,
                "amount": amount,
                "cardCVV2": card_cvv2,
                "cardHolderName": card_holder_name,
                "successUrl": success_url,
                "failUrl": fail_url,
                "description": description,
                "merchantOrderId": merchant_order_id,
                "userName": user_name,
                "cardExpireDateYear": card_expire_date_year,
                "merchantId": merchant_id,
                "hashData": hash_data,
                "installmentCount": installment_count,
                "deferringCount": deferring_count,
                "currency": currency,
                "cardNumber": card_number,
                "currencyCode": currency_code,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/threeDPayment",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def dijital_odeme_komisyon_mutabakati(
        self,
        *,
        transaction_list: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Dijital Ödeme Komisyon Mutabakatı.

        ``POST /v1/vpos/commissionReconciliation``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Gönderilen transaction list bilgilerine göre digital payment transactions için
        commission reconciliation işlemi yapar. Cevapta her transaction için transaction
        identifier, status code, status message ve commission type bilgileriyle birlikte
        reconciliation status bilgisi döner.

        Args:
            transaction_list: (``transactionList``, gövde, zorunlu) Commission reconciliation
                işlemine dahil edilecek digital payment transaction listesidir.

        Yanıt alanları: transactionId, statusCode, statusMessage, commissionType

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/dijital-odeme-komisyon-mutabakati
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionList": transaction_list,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/vpos/commissionReconciliation",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def duzenli_non_three_d_odeme(
        self,
        *,
        merchant_order_id: str | None = None,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        user_name: str | None = None,
        hash_data: str | None = None,
        amount: str | None = None,
        currency: str | None = None,
        installment_count: int | None = None,
        deferring_count: int | None = None,
        card_number: str | None = None,
        card_expire_date_year: str | None = None,
        card_expire_date_month: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        description: str | None = None,
        customer_name: str | None = None,
        payment_start_date: str | None = None,
        iteration_counter: int | None = None,
        period_number: int | None = None,
        period_type: int | None = None,
        card_holder_customer_id: int | None = None,
        merchant_customer_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Düzenli NonThreeD Ödeme.

        ``POST /v1/vpos/recurringNonThreeDPayment``

        Kapsam: ``public`` · Akış: client credentials

        Düzenli / tekrarlı ödeme almak için kullanılan API’dır.

        Args:
            merchant_order_id: (``merchantOrderId``, gövde)
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            hash_data: (``hashData``, gövde)
            amount: (gövde)
            currency: (gövde)
            installment_count: (``installmentCount``, gövde)
            deferring_count: (``deferringCount``, gövde)
            card_number: (``cardNumber``, gövde)
            card_expire_date_year: (``cardExpireDateYear``, gövde)
            card_expire_date_month: (``cardExpireDateMonth``, gövde)
            card_cvv2: (``cardCvv2``, gövde)
            card_holder_name: (``cardHolderName``, gövde)
            description: (gövde)
            customer_name: (``customerName``, gövde)
            payment_start_date: (``paymentStartDate``, gövde)
            iteration_counter: (``iterationCounter``, gövde)
            period_number: (``periodNumber``, gövde)
            period_type: (``periodType``, gövde)
            card_holder_customer_id: (``cardHolderCustomerId``, gövde)
            merchant_customer_id: (``merchantCustomerId``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/duzenli-nonthreed-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantOrderId": merchant_order_id,
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "hashData": hash_data,
                "amount": amount,
                "currency": currency,
                "installmentCount": installment_count,
                "deferringCount": deferring_count,
                "cardNumber": card_number,
                "cardExpireDateYear": card_expire_date_year,
                "cardExpireDateMonth": card_expire_date_month,
                "cardCvv2": card_cvv2,
                "cardHolderName": card_holder_name,
                "description": description,
                "customerName": customer_name,
                "paymentStartDate": payment_start_date,
                "iterationCounter": iteration_counter,
                "periodNumber": period_number,
                "periodType": period_type,
                "cardHolderCustomerId": card_holder_customer_id,
                "merchantCustomerId": merchant_customer_id,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/recurringNonThreeDPayment",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def gelen_odeme_iptali(
        self,
        *,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        user_name: str | None = None,
        merchant_order_id: str | None = None,
        amount: int | None = None,
        ok_url: str | None = None,
        fail_url: str | None = None,
        entry_gate_method: str | None = None,
        hash_data: str | None = None,
        parent_payment_id: int | None = None,
        payment_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Gelen Ödeme İptali.

        ``POST /v1/vpos/paymentOrderReversal``

        Kapsam: ``public`` · Akış: client credentials

        Henüz kesinleşmemiş / tahsilata dönüşmemiş bir “tahsilat işlemini”nin iptal edilmesi
        için kullanılır.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            amount: (gövde)
            ok_url: (``okUrl``, gövde)
            fail_url: (``failUrl``, gövde)
            entry_gate_method: (``entryGateMethod``, gövde)
            hash_data: (``hashData``, gövde)
            parent_payment_id: (``parentPaymentId``, gövde)
            payment_id: (``paymentId``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/gelen-odeme-iptali
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "merchantOrderId": merchant_order_id,
                "amount": amount,
                "okUrl": ok_url,
                "failUrl": fail_url,
                "entryGateMethod": entry_gate_method,
                "hashData": hash_data,
                "parentPaymentId": parent_payment_id,
                "paymentId": payment_id,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/paymentOrderReversal",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def isyeri_onayli_non_three_d_odeme(
        self,
        *,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        payment_customer_id: int | None = None,
        merchant_order_id: str | None = None,
        user_name: str | None = None,
        hash_data: str | None = None,
        amount: str | None = None,
        currency: str | None = None,
        installment_count: int | None = None,
        deferring_count: int | None = None,
        safe_key: str | None = None,
        description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """İşyeri Onaylı NonThreeD Ödeme.

        ``POST /v1/vpos/nonThreeDPaymentByMerchantSafe``

        Kapsam: ``public`` · Akış: client credentials

        İşyeri onaylı olan NonThreeD Ödeme işlemi yapılan API’dır.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            payment_customer_id: (``paymentCustomerId``, gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            user_name: (``userName``, gövde)
            hash_data: (``hashData``, gövde)
            amount: (gövde)
            currency: (gövde)
            installment_count: (``installmentCount``, gövde)
            deferring_count: (``deferringCount``, gövde)
            safe_key: (``safeKey``, gövde)
            description: (gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/isyeri-onayli-nonthreed-odeme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "paymentCustomerId": payment_customer_id,
                "merchantOrderId": merchant_order_id,
                "userName": user_name,
                "hashData": hash_data,
                "amount": amount,
                "currency": currency,
                "installmentCount": installment_count,
                "deferringCount": deferring_count,
                "safeKey": safe_key,
                "description": description,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/nonThreeDPaymentByMerchantSafe",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def merchant_safe_icin_kart_ekleme(
        self,
        *,
        business_key: int | None = None,
        merchant_id: int | None = None,
        customer_id: int | None = None,
        user_name: str | None = None,
        hash_data: str | None = None,
        merchant_order_id: str | None = None,
        payment_customer_id: int | None = None,
        card_number: str | None = None,
        card_expire_date_month: str | None = None,
        card_expire_date_year: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Merchant‑Safe için Kart Ekleme.

        ``POST /v1/vpos/addCardToMerchantSafe``

        Kapsam: ``public`` · Akış: client credentials

        Merchant‑safe (işyeri sorumluluğunda) Non‑3D Secure ödeme akışlarında kullanılmak üzere,
        müşterinin kart bilgisini ödeme sistemine güvenli şekilde kaydetmek için kullanılan
        API’dir.

        Args:
            business_key: (``businessKey``, gövde)
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            hash_data: (``hashData``, gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            payment_customer_id: (``paymentCustomerId``, gövde)
            card_number: (``cardNumber``, gövde)
            card_expire_date_month: (``cardExpireDateMonth``, gövde)
            card_expire_date_year: (``cardExpireDateYear``, gövde)
            card_cvv2: (``cardCvv2``, gövde)
            card_holder_name: (``cardHolderName``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/merchant-safe-icin-kart-ekleme
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "businessKey": business_key,
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "hashData": hash_data,
                "merchantOrderId": merchant_order_id,
                "paymentCustomerId": payment_customer_id,
                "cardNumber": card_number,
                "cardExpireDateMonth": card_expire_date_month,
                "cardExpireDateYear": card_expire_date_year,
                "cardCvv2": card_cvv2,
                "cardHolderName": card_holder_name,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/addCardToMerchantSafe",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def on_provizyon(
        self,
        *,
        merchant_id: str | None = None,
        customer_id: str | None = None,
        user_name: str | None = None,
        amount: str | None = None,
        merchant_order_id: str | None = None,
        card_number: str | None = None,
        card_expire_date_year: str | None = None,
        card_expire_date_month: str | None = None,
        card_cvv2: str | None = None,
        card_holder_name: str | None = None,
        currency: str | None = None,
        hash_data: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Ön Provizyon.

        ``POST /v1/vpos/preAuthorization``

        Kapsam: ``public`` · Akış: client credentials

        Müşteri kartından tutar tahsil edilmeden, belirtilen tutar için ön provizyon (limit
        blokajı) almak amacıyla kullanılan sanal POS servisidir.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            amount: (gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            card_number: (``cardNumber``, gövde)
            card_expire_date_year: (``cardExpireDateYear``, gövde)
            card_expire_date_month: (``cardExpireDateMonth``, gövde)
            card_cvv2: (``cardCVV2``, gövde)
            card_holder_name: (``cardHolderName``, gövde)
            currency: (gövde)
            hash_data: (``hashData``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/on-provizyon
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "amount": amount,
                "merchantOrderId": merchant_order_id,
                "cardNumber": card_number,
                "cardExpireDateYear": card_expire_date_year,
                "cardExpireDateMonth": card_expire_date_month,
                "cardCVV2": card_cvv2,
                "cardHolderName": card_holder_name,
                "currency": currency,
                "hashData": hash_data,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/preAuthorization",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def satis_islemi_iptal(
        self,
        *,
        merchant_id: str | None = None,
        customer_id: str | None = None,
        user_name: str | None = None,
        amount: int | None = None,
        merchant_order_id: str | None = None,
        order_id: int | None = None,
        hash_data: str | None = None,
        sale_reversal_type: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Satış İşlemi İptal.

        ``POST /v1/vpos/saleOrderReversal``

        Kapsam: ``public`` · Akış: client credentials

        Başarılı bir satış işlemini gün sonu öncesinde iptal ederek tahsilatın tamamen geri
        alınmasını sağlar.

        Args:
            merchant_id: (``merchantId``, gövde)
            customer_id: (``customerId``, gövde)
            user_name: (``userName``, gövde)
            amount: (gövde)
            merchant_order_id: (``merchantOrderId``, gövde)
            order_id: (``orderId``, gövde)
            hash_data: (``hashData``, gövde)
            sale_reversal_type: (``saleReversalType``, gövde)

        Gövde alanları istekte ``request`` nesnesinin içine yerleştirilir.

        Doküman: https://developer.kuveytturk.com.tr/documentation/sanal-pos-vpos/satis-islemi-iptal
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantId": merchant_id,
                "customerId": customer_id,
                "userName": user_name,
                "amount": amount,
                "merchantOrderId": merchant_order_id,
                "orderId": order_id,
                "hashData": hash_data,
                "saleReversalType": sale_reversal_type,
            },
            extra_body,
        )
        _body = {"request": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/saleOrderReversal",
            scope="public",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
