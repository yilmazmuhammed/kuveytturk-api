"""Ödeme çözümleri uç noktaları (``kt.payment_solutions``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Number, Resource, merge

__all__ = ["AsyncPaymentSolutions", "PaymentSolutions"]


class PaymentSolutions(Resource):
    """Ödeme çözümleri - ``kt.payment_solutions``."""

    def digital_payment_get_token(
        self,
        *,
        transaction_id: str,
        order_number: str,
        merchant_id: int,
        is_sub_merchant: int,
        soft_descriptor: str,
        payment_type: int,
        amount: Number,
        channel: str,
        order_item_count: int,
        currency: int,
        basket_product_list: Sequence[Any],
        request_date: DateLike,
        description: str | None = None,
        commission_amount: Number | None = None,
        transaction_currency: str | None = None,
        token_interval: int | None = None,
        success_redirect_url: str | None = None,
        fail_redirect_url: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Get Token.

        ``POST /v1/vpos/digitalPaymentGetToken``

        Kapsam: ``digital_payments`` · Akış: client credentials

        It is used to finance e commerce. It can work with various payment methods.
        (Funding,Money Transfer,etc)

        Args:
            transaction_id: (``transactionId``, gövde, zorunlu) End-to-end unique ID for the
                transaction
            order_number: (``orderNumber``, gövde, zorunlu) Order number in the merchant
            merchant_id: (``merchantId``, gövde, zorunlu) Merchant code defined by Kuveyt Türk
            is_sub_merchant: (``isSubMerchant``, gövde, zorunlu) 1: Yes, 0: No
            description: (gövde) Optional description
            soft_descriptor: (``softDescriptor``, gövde, zorunlu) Accounting description for
                slip
            payment_type: (``paymentType``, gövde, zorunlu) 1: Money transfer, 2: Financing
            commission_amount: (``commissionAmount``, gövde) Fee taken from the merchant
            amount: (gövde, zorunlu) Transaction amount
            transaction_currency: (``transactionCurrency``, gövde)
            token_interval: (``tokenInterval``, gövde) Validity period in msec. If it is less
                than ours, this will be considered
            success_redirect_url: (``successRedirectUrl``, gövde) Customer redirect address for
                success
            fail_redirect_url: (``failRedirectUrl``, gövde) Customer redirect address for
                failure
            channel: (gövde, zorunlu) WM, MM, WW
            order_item_count: (``orderItemCount``, gövde, zorunlu) Distinct count of items in
                the basket
            currency: (gövde, zorunlu) Transaction currency
            basket_product_list: (``basketProductList``, gövde, zorunlu) Basket Product List
            request_date: (``requestDate``, gövde, zorunlu) Date info in order to use for
                reconciliation, cancel and query

        Gövde alanları istekte ``ApiTransactionContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: accessToken, tokenExpireDate, returnCode, returnMessage,
        applicationName, applicationParameter

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-get-token
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionId": transaction_id,
                "orderNumber": order_number,
                "merchantId": merchant_id,
                "isSubMerchant": is_sub_merchant,
                "description": description,
                "softDescriptor": soft_descriptor,
                "paymentType": payment_type,
                "commissionAmount": commission_amount,
                "amount": amount,
                "transactionCurrency": transaction_currency,
                "tokenInterval": token_interval,
                "successRedirectUrl": success_redirect_url,
                "failRedirectUrl": fail_redirect_url,
                "channel": channel,
                "orderItemCount": order_item_count,
                "currency": currency,
                "basketProductList": basket_product_list,
                "requestDate": request_date,
            },
            extra_body,
        )
        _body = {"ApiTransactionContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentGetToken",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def digital_payment_query(
        self,
        *,
        merchant_id: int,
        transaction_id: str | None = None,
        start_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Query.

        ``POST /v1/vpos/digitalPaymentQuery``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Used to query the transaction result

        Args:
            transaction_id: (``transactionId``, gövde) End-to-end unique ID for the transaction.
            merchant_id: (``merchantId``, gövde, zorunlu) Merchant code defined by Kuveyt Turk.
            start_date: (``startDate``, gövde) When there is no transaction ID, start date of
                the transaction list.
            end_date: (``endDate``, gövde) When there is no Transaction ID, end date of the
                transaction list.

        Gövde alanları istekte ``QueryContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: returnCode, returnMessage, transactionId, statusCode, statusMessage,
        paymentType, commissionAmount, amount, currency

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-query
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionId": transaction_id,
                "merchantId": merchant_id,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        _body = {"QueryContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentQuery",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def digital_payment_refund(
        self,
        *,
        transaction_id: str,
        org_transaction_id: str,
        merchant_id: int,
        amount: Number,
        currency: int,
        commission_amount: Number | None = None,
        description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Refund.

        ``POST /v1/vpos/digitalPaymentDoRefund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Used for digital payment's refund transactions.

        Args:
            transaction_id: (``transactionId``, gövde, zorunlu) Unique ID for refund transaction
            org_transaction_id: (``orgTransactionId``, gövde, zorunlu) Transaction ID from
                sale/funding will be refund
            merchant_id: (``merchantId``, gövde, zorunlu) Merchant's ID given by the bank
            amount: (gövde, zorunlu) Refund amount
            currency: (gövde, zorunlu) Currency code for refund transaction
            commission_amount: (``commissionAmount``, gövde) Commission amount for refund
                transaction
            description: (gövde) Description for refund transaction

        Gövde alanları istekte ``RefundContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ReturnCode, ReturnMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-refund
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionId": transaction_id,
                "orgTransactionId": org_transaction_id,
                "merchantId": merchant_id,
                "amount": amount,
                "currency": currency,
                "commissionAmount": commission_amount,
                "description": description,
            },
            extra_body,
        )
        _body = {"RefundContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentDoRefund",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def digital_payment_send_document(
        self,
        *,
        document_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Send Document.

        ``POST /v1/vpos/sendDocument``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Used to send document after funding/sale transactions.

        Args:
            document_list: (``documentList``, gövde)

        Gövde alanları istekte ``SendDocumentContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: transactionId, returnCode, returnMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-send-document
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "documentList": document_list,
            },
            extra_body,
        )
        _body = {"SendDocumentContract": _body}
        return self._client.request(
            "POST",
            "/v1/vpos/sendDocument",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pos_merchant_number_list(
        self,
        *,
        customer_id: int,
        start_date: DateLike,
        end_date: DateLike,
        corporate_user_name: str | None = None,
        merchant_block_number: int | None = None,
        merchant_number: str | None = None,
        count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Pos Merchant Number List.

        ``GET /v1/pos/merchant-number``

        Kapsam: ``public`` · Akış: client credentials

        Retrieves POS merchant detail transactions according to the provided customer, corporate
        user, merchant, count, and date range filters. The response includes POS transaction
        details such as authorization, batch, merchant, card, branch, currency, installment,
        commission, amount, terminal, transaction, and request information.

        Args:
            customer_id: (``customerId``, sorgu, zorunlu) Customer identifier used to retrieve
                POS merchant detail transactions.
            corporate_user_name: (``corporateUserName``, sorgu) Corporate user name used to
                filter POS merchant detail transactions.
            merchant_block_number: (``merchantBlockNumber``, sorgu) Merchant block number used
                to filter POS transactions.
            merchant_number: (``merchantNumber``, sorgu) Merchant number used to filter POS
                transactions.
            count: (sorgu) Maximum number of POS transaction records to return.
            start_date: (``startDate``, sorgu, zorunlu) Start date of the POS transaction query
                period.
            end_date: (``endDate``, sorgu, zorunlu) End date of the POS transaction query
                period.

        Yanıt alanları: posDetailTransactions, authorizationNumber, batchNumber, blockDay,
        blockPeriod, blockedAccountSuffix, branchCode, branchName, cardBrand,
        cardSourceGroupCode, cardType, chainMerchantNumber, citizenshipNumber, currencyCode,
        currencyCodeDescription, currentAccountSuffix, customerNumber, deferringCount,
        deferringDate, installmentAmount, installmentCount, installmentDate, installmentNumber,
        isContactlessFlag, maskedCardNumber, mcc, merchantBlockNumber, merchantName,
        merchantNumber, merchantValueDate, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-merchant-number-list
        """
        _query = merge(
            {
                "customerId": customer_id,
                "corporateUserName": corporate_user_name,
                "merchantBlockNumber": merchant_block_number,
                "merchantNumber": merchant_number,
                "count": count,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/pos/merchant-number",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def pos_transaction_details_for_tpp_v2(
        self,
        *,
        merchant_block_number: str,
        count: str,
        start_date: DateLike,
        end_date: DateLike,
        merchant_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """POS Transaction Details For TPP(Third Party Provider) V2.

        ``POST /v2/pos/detail-transactions``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        With this API, you can behave as a TPP (Third Party Provider) / Fintech and access
        Kuveyt Turk customers POS transaction details after you get the consent of the customer.
        If you want to access POS Transaction details only for your own account, you should use
        the POS Transaction Details V3. &gt; This API is in beta stage. Request and response
        models may change over time.

        Args:
            merchant_block_number: (``merchantBlockNumber``, gövde, zorunlu) Represents the
                blocked number which belongs to customer for POS transactions. This information must
                be obtained using the POS Transactions Summary V2 service.
            merchant_number: (``merchantNumber``, gövde) Represents the merchant number which
                belongs to customer for POS transactions. If the merchant number is not given, a
                search will be made for all merchant numbers belongs to the customer.
            count: (gövde, zorunlu) Represents the number of detail records to query. Max count
                value must be a thousand (1000).
            start_date: (``startDate``, gövde, zorunlu) Represents a filter parameter indicating
                the lower date bound before which the transactions happened.
            end_date: (``endDate``, gövde, zorunlu) Represents a filter parameter indicating the
                upper date bound before which the transactions happened (Enddate is included in the
                search).

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-for-tpp-third-party-provider-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantBlockNumber": merchant_block_number,
                "merchantNumber": merchant_number,
                "count": count,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/pos/detail-transactions",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pos_transaction_details_v3(
        self,
        *,
        merchant_block_number: str,
        count: str,
        start_date: DateLike,
        end_date: DateLike,
        corporate_user_name: str,
        merchant_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """POS Transaction Details V3.

        ``POST /v3/pos/detail-transactions``

        Kapsam: ``cards`` · Akış: client credentials

        With this API, you can only access the POS transaction details of your own accounts. If
        you want to behave as a TPP (Third Party Provider) / Fintech you should use the POS
        Transaction Details V2. &gt; This API is in beta stage. Request and response models may
        change over time.

        Args:
            merchant_block_number: (``merchantBlockNumber``, gövde, zorunlu) Represents the
                blocked number which belongs to customer for POS transactions. This information must
                be obtained using the POS Transactions Summary V2 service.
            merchant_number: (``merchantNumber``, gövde) Represents the merchant number which
                belongs to customer for POS transactions. If the merchant number is not given, a
                search will be made for all merchant numbers belongs to the customer.
            count: (gövde, zorunlu) Represents the number of detail records to query. Max count
                value must be a thousand (1000).
            start_date: (``startDate``, gövde, zorunlu) Represents a filter parameter indicating
                the lower date bound before which the transactions happened.
            end_date: (``endDate``, gövde, zorunlu) Represents a filter parameter indicating the
                upper date bound before which the transactions happened (Enddate is included in the
                search).
            corporate_user_name: (``corporateUserName``, gövde, zorunlu) Represents the User
                Name information belonging to an authorized user of the customer for POS transaction
                details.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-v3
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantBlockNumber": merchant_block_number,
                "merchantNumber": merchant_number,
                "count": count,
                "startDate": start_date,
                "endDate": end_date,
                "corporateUserName": corporate_user_name,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v3/pos/detail-transactions",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def pos_transactions_summary_v3(
        self,
        *,
        corporate_user_name: str,
        start_date: DateLike,
        end_date: DateLike,
        member_number: str | None = None,
        extract_type: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """POS Transactions Summary V3.

        ``POST /v3/pos/transactions``

        Kapsam: ``cards`` · Akış: client credentials

        With this API, you can only access the POS transactions of your own accounts. If you
        want to behave as a TPP (Third Party Provider) / Fintech you should use the POS
        Transaction V2. &gt; This API is in beta stage. Request and response models may change
        over time.

        Args:
            corporate_user_name: (``corporateUserName``, gövde, zorunlu) Represents the User
                Name information belonging to an authorized user of the customer for POS
                transactions.
            member_number: (``memberNumber``, gövde) Represents the merchant number that belongs
                to the customer for POS transactions. If the merchant number is not given, a search
                will be made for all merchant numbers belonging to the customer.
            start_date: (``startDate``, gövde, zorunlu) Represents a filter parameter indicating
                the lower date bound before which the transactions happened.
            end_date: (``endDate``, gövde, zorunlu) Represents a filter parameter indicating the
                upper date bound before which the transactions happened (End date is included in the
                search).
            extract_type: (``extractType``, gövde) Represents the POS transaction status. H: All
                Transactions, B: Blocked Transactions, C: UnBlocked Transactions. If the extractType
                is not given, a search will be made according to "H" value.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transactions-summary-v3
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "corporateUserName": corporate_user_name,
                "memberNumber": member_number,
                "startDate": start_date,
                "endDate": end_date,
                "extractType": extract_type,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v3/pos/transactions",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_order_distribution_detail_v2(
        self,
        *,
        distribution_list: Sequence[Any],
        e_tender_delivery_id: int,
        attachment: str | None = None,
        document_extension: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Order Distribution Detail V2.

        ``POST /v3/purchase/orderdistribution``

        Kapsam: ``payments`` · Akış: client credentials

        Submits order distribution and delivery details to the BOA system for the purchase
        process. The request includes distribution records with delivery, cargo, waybill and
        rejection information, along with optional document attachment details. The response
        returns whether the order distribution submission was successful and includes error
        details if available.

        Args:
            distribution_list: (``DistributionList``, gövde, zorunlu) List of order distribution
                records to be submitted.
            e_tender_delivery_id: (``ETenderDeliveryId``, gövde, zorunlu) Identifier of the
                e-tender delivery record associated with the distribution item or the overall
                request.
            attachment: (``Attachment``, gövde) Content of the related document. It is typically
                sent as base64 encoded document data.
            document_extension: (``DocumentExtension``, gövde) File extension of the submitted
                document. For example: pdf, jpg, png.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/send-order-distribution-detail-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DistributionList": distribution_list,
                "ETenderDeliveryId": e_tender_delivery_id,
                "Attachment": attachment,
                "DocumentExtension": document_extension,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v3/purchase/orderdistribution",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def virtual_pos(
        self,
        *,
        ok_url: str,
        fail_url: str,
        hash_data: str,
        merchant_id: int,
        user_name: str,
        transaction_type: str,
        currency_code: int,
        transaction_security: int,
        api_version: str | None = None,
        customer_id: int | None = None,
        card_number: str | None = None,
        card_expire_date_year: int | None = None,
        card_expire_date_month: int | None = None,
        card_cvv2: int | None = None,
        card_holder_name: str | None = None,
        card_holder_ip_address: str | None = None,
        card_type: str | None = None,
        installment_count: int | None = None,
        amount: Number | None = None,
        display_amount: Number | None = None,
        description: str | None = None,
        merchant_order_id: int | None = None,
        kuveyt_turk_v_pos_additional_data: Mapping[str, Any] | None = None,
        exp_sign: str | None = None,
        customer_ip_address: str | None = None,
        three_d_secure_level: int | None = None,
        batch_id: int | None = None,
        identity_tax_number: str | None = None,
        qery_id: int | None = None,
        debt_id: int | None = None,
        debtor_name: str | None = None,
        period: str | None = None,
        surcharge_amount: Number | None = None,
        sgk_debt_amount: Number | None = None,
        hash_password: str | None = None,
        installment_maturity_commision_flag: int | None = None,
        explain: str | None = None,
        explain2: str | None = None,
        explain3: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS.

        ``POST /v1/vpos``

        Kapsam: ``cards`` · Akış: client credentials

        This endpoint is used to initiate a Virtual POS 3D Model payment transaction. The
        request includes card details, merchant information, transaction amount, redirection
        URLs, and transaction security information. The response returns the content required
        for the 3D authentication or payment flow.

        Args:
            api_version: (``APIVersion``, gövde) API version information to be used for the
                transaction.
            ok_url: (``OkUrl``, gövde, zorunlu) URL where the cardholder will be redirected if
                the transaction is successful.
            fail_url: (``FailUrl``, gövde, zorunlu) URL where the cardholder will be redirected
                if the transaction fails.
            hash_data: (``HashData``, gövde, zorunlu) Hash value generated for transaction
                verification.
            merchant_id: (``MerchantId``, gövde, zorunlu) Merchant identifier.
            customer_id: (``$CustomerId``, gövde)
            user_name: (``UserName``, gövde, zorunlu) Virtual POS user name.
            card_number: (``$CardNumber``, gövde)
            card_expire_date_year: (``$CardExpireDateYear``, gövde)
            card_expire_date_month: (``$CardExpireDateMonth``, gövde)
            card_cvv2: (``$CardCVV2``, gövde)
            card_holder_name: (``$CardHolderName``, gövde)
            card_holder_ip_address: (``CardHolderIPAddress``, gövde) IP address of the
                cardholder.
            card_type: (``CardType``, gövde) Card type information.
            transaction_type: (``TransactionType``, gövde, zorunlu) Type of transaction to be
                performed.
            installment_count: (``InstallmentCount``, gövde) Number of installments. For single
                payment transactions, 0 or 1 can be sent.
            amount: (``$Amount``, gövde)
            display_amount: (``$DisplayAmount``, gövde)
            description: (``Description``, gövde) Description of the transaction.
            currency_code: (``CurrencyCode``, gövde, zorunlu) Currency code of the transaction.
            merchant_order_id: (``$MerchantOrderId``, gövde)
            transaction_security: (``TransactionSecurity``, gövde, zorunlu) Indicates the
                transaction security level.
            kuveyt_turk_v_pos_additional_data: (``KuveytTurkVPosAdditionalData``, gövde) Object
                that contains additional data related to the transaction.
            exp_sign: (``ExpSign``, gövde) Additional signature information related to the
                transaction.
            customer_ip_address: (``CustomerIPAddress``, gövde) Customer IP address.
            three_d_secure_level: (``ThreeDSecureLevel``, gövde) Indicates the 3D Secure level.
            batch_id: (``BatchID``, gövde) Batch identifier associated with the transaction.
            identity_tax_number: (``$IdentityTaxNumber``, gövde)
            qery_id: (``QeryId``, gövde) Query identifier.
            debt_id: (``DebtId``, gövde) Debt identifier.
            debtor_name: (``DebtorName``, gövde) Name, surname, or title of the debtor.
            period: (``Period``, gövde) Debt or payment period information.
            surcharge_amount: (``$SurchargeAmount``, gövde)
            sgk_debt_amount: (``$SGKDebtAmount``, gövde)
            hash_password: (``HashPassword``, gövde) Password used for hash generation.
            installment_maturity_commision_flag: (``InstallmentMaturityCommisionFlag``, gövde)
                Indicates whether installment maturity commission will be applied.
            explain: (``Explain``, gövde) Additional explanation field for the transaction.
            explain2: (``Explain2``, gövde) Second additional explanation field for the
                transaction.
            explain3: (``Explain3``, gövde) Third additional explanation field for the
                transaction.

        Gövde alanları istekte ``KuveytTurkVPosMessage`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ClientResponse, ContentType, BusinessKey, OrderId, ReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "APIVersion": api_version,
                "OkUrl": ok_url,
                "FailUrl": fail_url,
                "HashData": hash_data,
                "MerchantId": merchant_id,
                "$CustomerId": customer_id,
                "UserName": user_name,
                "$CardNumber": card_number,
                "$CardExpireDateYear": card_expire_date_year,
                "$CardExpireDateMonth": card_expire_date_month,
                "$CardCVV2": card_cvv2,
                "$CardHolderName": card_holder_name,
                "CardHolderIPAddress": card_holder_ip_address,
                "CardType": card_type,
                "TransactionType": transaction_type,
                "InstallmentCount": installment_count,
                "$Amount": amount,
                "$DisplayAmount": display_amount,
                "Description": description,
                "CurrencyCode": currency_code,
                "$MerchantOrderId": merchant_order_id,
                "TransactionSecurity": transaction_security,
                "KuveytTurkVPosAdditionalData": kuveyt_turk_v_pos_additional_data,
                "ExpSign": exp_sign,
                "CustomerIPAddress": customer_ip_address,
                "ThreeDSecureLevel": three_d_secure_level,
                "BatchID": batch_id,
                "$IdentityTaxNumber": identity_tax_number,
                "QeryId": qery_id,
                "DebtId": debt_id,
                "DebtorName": debtor_name,
                "Period": period,
                "$SurchargeAmount": surcharge_amount,
                "$SGKDebtAmount": sgk_debt_amount,
                "HashPassword": hash_password,
                "InstallmentMaturityCommisionFlag": installment_maturity_commision_flag,
                "Explain": explain,
                "Explain2": explain2,
                "Explain3": explain3,
            },
            extra_body,
        )
        _body = {"KuveytTurkVPosMessage": _body}
        return self._client.request(
            "POST",
            "/v1/vpos",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def virtual_pos_end_day_all_list(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS EndDayAll List.

        ``POST /v1/vpos/endDayAllList``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to retrieve the end-of-day transaction list for a Virtual POS
        merchant within the specified date range. The request includes the date filter and
        Virtual POS login information required to validate the merchant. >This API is in beta
        stage. Request and response models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the end-of-day list filter criteria.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: OrderId, MerchantOrderId, MerchantId, CardHolderName, CardType,
        CardNumber, OrderDate, OrderStatus, LastOrderStatus, OrderType, TransactionStatus,
        FirstAmount, CancelAmount, DrawbackAmount, PartialDrawbackAmount, ClosedAmount, FEC,
        VPSEntryMode, InstallmentCount, DeferringCount, TransactionSecurity, ResponseCode,
        ResponseExplain, EndOfDayStatus, TransactionSide, CardHolderIPAddress,
        MerchantIPAddress, MerchantUserName, ProvNumber, BatchId, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-enddayall-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/vpos/endDayAllList",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def virtual_pos_end_of_day(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS EndOfDay.

        ``POST /v1/vpos/endOfDay``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to perform the end-of-day closing operation for Virtual POS
        transactions within the specified date range. The request includes the date filter,
        merchant information, and Virtual POS login information required to validate the
        merchant and process eligible transactions. >This API is in beta stage. Request and
        response models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the end-of-day closing filter criteria.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: VPosMessage, VPosMessageV2, VposMessageCommon, LoginResponse,
        IsEnrolled, IsVirtual, PareqHtmlFormString, ProvisionNumber, RRN, Stan, ResponseCode,
        IsSuccess, ResponseMessage, OrderId, TransactionTime, MerchantOrderId, HashData, MD,
        AuthenticationPacket, ACSURL, Password, CurrencyCode, TransactionType, SafeKey,
        ReferenceId, MerchantId, BusinessKey, PaymentOrderList, WebFlowResponse,
        StartAuthenticationResult, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-endofday
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/vpos/endOfDay",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def virtual_pos_general_transaction(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS General Transaction.

        ``POST /v1/vpos/transaction``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to perform Virtual POS transaction operations such as refund,
        partial refund, and sale reversal for an existing order. The request includes the order
        information, transaction type, optional refund amount, and Virtual POS login information
        required to validate the merchant. >This API is in beta stage. Request and response
        models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the transaction operation details.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: VPosMessage, VPosMessageV2, VposMessageCommon, LoginResponse,
        IsEnrolled, IsVirtual, PareqHtmlFormString, ProvisionNumber, RRN, Stan, ResponseCode,
        IsSuccess, ResponseMessage, OrderId, TransactionTime, MerchantOrderId, HashData, MD,
        AuthenticationPacket, ACSURL, Password, CurrencyCode, TransactionType, SafeKey,
        ReferenceId, MerchantId, BusinessKey, PaymentOrderList, WebFlowResponse,
        StartAuthenticationResult, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-general-transaction
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/vpos/transaction",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def virtual_pos_order_filter(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS Order Filter.

        ``POST /v1/vpos/orderFilter``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to retrieve Virtual POS order records based on the specified
        filter criteria. The request includes date range, cardholder name, amount limits,
        merchant information, and Virtual POS login information required to validate the
        merchant. >This API is in beta stage. Request and response models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the order filter criteria.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: OrderId, MerchantOrderId, MerchantId, CardHolderName, CardType,
        CardNumber, OrderDate, OrderStatus, LastOrderStatus, OrderType, TransactionStatus,
        FirstAmount, CancelAmount, DrawbackAmount, PartialDrawbackAmount, ClosedAmount, FEC,
        VPSEntryMode, InstallmentCount, DeferringCount, TransactionSecurity, ResponseCode,
        ResponseExplain, EndOfDayStatus, TransactionSide, CardHolderIPAddress,
        MerchantIPAddress, MerchantUserName, ProvNumber, BatchId, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-order-filter
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/vpos/orderFilter",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncPaymentSolutions(AsyncResource):
    """Ödeme çözümleri (asenkron) - ``kt.payment_solutions``."""

    async def digital_payment_get_token(
        self,
        *,
        transaction_id: str,
        order_number: str,
        merchant_id: int,
        is_sub_merchant: int,
        soft_descriptor: str,
        payment_type: int,
        amount: Number,
        channel: str,
        order_item_count: int,
        currency: int,
        basket_product_list: Sequence[Any],
        request_date: DateLike,
        description: str | None = None,
        commission_amount: Number | None = None,
        transaction_currency: str | None = None,
        token_interval: int | None = None,
        success_redirect_url: str | None = None,
        fail_redirect_url: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Get Token.

        ``POST /v1/vpos/digitalPaymentGetToken``

        Kapsam: ``digital_payments`` · Akış: client credentials

        It is used to finance e commerce. It can work with various payment methods.
        (Funding,Money Transfer,etc)

        Args:
            transaction_id: (``transactionId``, gövde, zorunlu) End-to-end unique ID for the
                transaction
            order_number: (``orderNumber``, gövde, zorunlu) Order number in the merchant
            merchant_id: (``merchantId``, gövde, zorunlu) Merchant code defined by Kuveyt Türk
            is_sub_merchant: (``isSubMerchant``, gövde, zorunlu) 1: Yes, 0: No
            description: (gövde) Optional description
            soft_descriptor: (``softDescriptor``, gövde, zorunlu) Accounting description for
                slip
            payment_type: (``paymentType``, gövde, zorunlu) 1: Money transfer, 2: Financing
            commission_amount: (``commissionAmount``, gövde) Fee taken from the merchant
            amount: (gövde, zorunlu) Transaction amount
            transaction_currency: (``transactionCurrency``, gövde)
            token_interval: (``tokenInterval``, gövde) Validity period in msec. If it is less
                than ours, this will be considered
            success_redirect_url: (``successRedirectUrl``, gövde) Customer redirect address for
                success
            fail_redirect_url: (``failRedirectUrl``, gövde) Customer redirect address for
                failure
            channel: (gövde, zorunlu) WM, MM, WW
            order_item_count: (``orderItemCount``, gövde, zorunlu) Distinct count of items in
                the basket
            currency: (gövde, zorunlu) Transaction currency
            basket_product_list: (``basketProductList``, gövde, zorunlu) Basket Product List
            request_date: (``requestDate``, gövde, zorunlu) Date info in order to use for
                reconciliation, cancel and query

        Gövde alanları istekte ``ApiTransactionContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: accessToken, tokenExpireDate, returnCode, returnMessage,
        applicationName, applicationParameter

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-get-token
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionId": transaction_id,
                "orderNumber": order_number,
                "merchantId": merchant_id,
                "isSubMerchant": is_sub_merchant,
                "description": description,
                "softDescriptor": soft_descriptor,
                "paymentType": payment_type,
                "commissionAmount": commission_amount,
                "amount": amount,
                "transactionCurrency": transaction_currency,
                "tokenInterval": token_interval,
                "successRedirectUrl": success_redirect_url,
                "failRedirectUrl": fail_redirect_url,
                "channel": channel,
                "orderItemCount": order_item_count,
                "currency": currency,
                "basketProductList": basket_product_list,
                "requestDate": request_date,
            },
            extra_body,
        )
        _body = {"ApiTransactionContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentGetToken",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def digital_payment_query(
        self,
        *,
        merchant_id: int,
        transaction_id: str | None = None,
        start_date: DateLike | None = None,
        end_date: DateLike | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Query.

        ``POST /v1/vpos/digitalPaymentQuery``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Used to query the transaction result

        Args:
            transaction_id: (``transactionId``, gövde) End-to-end unique ID for the transaction.
            merchant_id: (``merchantId``, gövde, zorunlu) Merchant code defined by Kuveyt Turk.
            start_date: (``startDate``, gövde) When there is no transaction ID, start date of
                the transaction list.
            end_date: (``endDate``, gövde) When there is no Transaction ID, end date of the
                transaction list.

        Gövde alanları istekte ``QueryContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: returnCode, returnMessage, transactionId, statusCode, statusMessage,
        paymentType, commissionAmount, amount, currency

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-query
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionId": transaction_id,
                "merchantId": merchant_id,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        _body = {"QueryContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentQuery",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def digital_payment_refund(
        self,
        *,
        transaction_id: str,
        org_transaction_id: str,
        merchant_id: int,
        amount: Number,
        currency: int,
        commission_amount: Number | None = None,
        description: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Refund.

        ``POST /v1/vpos/digitalPaymentDoRefund``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Used for digital payment's refund transactions.

        Args:
            transaction_id: (``transactionId``, gövde, zorunlu) Unique ID for refund transaction
            org_transaction_id: (``orgTransactionId``, gövde, zorunlu) Transaction ID from
                sale/funding will be refund
            merchant_id: (``merchantId``, gövde, zorunlu) Merchant's ID given by the bank
            amount: (gövde, zorunlu) Refund amount
            currency: (gövde, zorunlu) Currency code for refund transaction
            commission_amount: (``commissionAmount``, gövde) Commission amount for refund
                transaction
            description: (gövde) Description for refund transaction

        Gövde alanları istekte ``RefundContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ReturnCode, ReturnMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-refund
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "transactionId": transaction_id,
                "orgTransactionId": org_transaction_id,
                "merchantId": merchant_id,
                "amount": amount,
                "currency": currency,
                "commissionAmount": commission_amount,
                "description": description,
            },
            extra_body,
        )
        _body = {"RefundContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/digitalPaymentDoRefund",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def digital_payment_send_document(
        self,
        *,
        document_list: Sequence[Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Digital Payment Send Document.

        ``POST /v1/vpos/sendDocument``

        Kapsam: ``digital_payments`` · Akış: client credentials

        Used to send document after funding/sale transactions.

        Args:
            document_list: (``documentList``, gövde)

        Gövde alanları istekte ``SendDocumentContract`` nesnesinin içine yerleştirilir.

        Yanıt alanları: transactionId, returnCode, returnMessage

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/digital-payment-send-document
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "documentList": document_list,
            },
            extra_body,
        )
        _body = {"SendDocumentContract": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos/sendDocument",
            scope="digital_payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pos_merchant_number_list(
        self,
        *,
        customer_id: int,
        start_date: DateLike,
        end_date: DateLike,
        corporate_user_name: str | None = None,
        merchant_block_number: int | None = None,
        merchant_number: str | None = None,
        count: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Pos Merchant Number List.

        ``GET /v1/pos/merchant-number``

        Kapsam: ``public`` · Akış: client credentials

        Retrieves POS merchant detail transactions according to the provided customer, corporate
        user, merchant, count, and date range filters. The response includes POS transaction
        details such as authorization, batch, merchant, card, branch, currency, installment,
        commission, amount, terminal, transaction, and request information.

        Args:
            customer_id: (``customerId``, sorgu, zorunlu) Customer identifier used to retrieve
                POS merchant detail transactions.
            corporate_user_name: (``corporateUserName``, sorgu) Corporate user name used to
                filter POS merchant detail transactions.
            merchant_block_number: (``merchantBlockNumber``, sorgu) Merchant block number used
                to filter POS transactions.
            merchant_number: (``merchantNumber``, sorgu) Merchant number used to filter POS
                transactions.
            count: (sorgu) Maximum number of POS transaction records to return.
            start_date: (``startDate``, sorgu, zorunlu) Start date of the POS transaction query
                period.
            end_date: (``endDate``, sorgu, zorunlu) End date of the POS transaction query
                period.

        Yanıt alanları: posDetailTransactions, authorizationNumber, batchNumber, blockDay,
        blockPeriod, blockedAccountSuffix, branchCode, branchName, cardBrand,
        cardSourceGroupCode, cardType, chainMerchantNumber, citizenshipNumber, currencyCode,
        currencyCodeDescription, currentAccountSuffix, customerNumber, deferringCount,
        deferringDate, installmentAmount, installmentCount, installmentDate, installmentNumber,
        isContactlessFlag, maskedCardNumber, mcc, merchantBlockNumber, merchantName,
        merchantNumber, merchantValueDate, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-merchant-number-list
        """
        _query = merge(
            {
                "customerId": customer_id,
                "corporateUserName": corporate_user_name,
                "merchantBlockNumber": merchant_block_number,
                "merchantNumber": merchant_number,
                "count": count,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/pos/merchant-number",
            scope="public",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def pos_transaction_details_for_tpp_v2(
        self,
        *,
        merchant_block_number: str,
        count: str,
        start_date: DateLike,
        end_date: DateLike,
        merchant_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """POS Transaction Details For TPP(Third Party Provider) V2.

        ``POST /v2/pos/detail-transactions``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        With this API, you can behave as a TPP (Third Party Provider) / Fintech and access
        Kuveyt Turk customers POS transaction details after you get the consent of the customer.
        If you want to access POS Transaction details only for your own account, you should use
        the POS Transaction Details V3. &gt; This API is in beta stage. Request and response
        models may change over time.

        Args:
            merchant_block_number: (``merchantBlockNumber``, gövde, zorunlu) Represents the
                blocked number which belongs to customer for POS transactions. This information must
                be obtained using the POS Transactions Summary V2 service.
            merchant_number: (``merchantNumber``, gövde) Represents the merchant number which
                belongs to customer for POS transactions. If the merchant number is not given, a
                search will be made for all merchant numbers belongs to the customer.
            count: (gövde, zorunlu) Represents the number of detail records to query. Max count
                value must be a thousand (1000).
            start_date: (``startDate``, gövde, zorunlu) Represents a filter parameter indicating
                the lower date bound before which the transactions happened.
            end_date: (``endDate``, gövde, zorunlu) Represents a filter parameter indicating the
                upper date bound before which the transactions happened (Enddate is included in the
                search).

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-for-tpp-third-party-provider-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantBlockNumber": merchant_block_number,
                "merchantNumber": merchant_number,
                "count": count,
                "startDate": start_date,
                "endDate": end_date,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/pos/detail-transactions",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pos_transaction_details_v3(
        self,
        *,
        merchant_block_number: str,
        count: str,
        start_date: DateLike,
        end_date: DateLike,
        corporate_user_name: str,
        merchant_number: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """POS Transaction Details V3.

        ``POST /v3/pos/detail-transactions``

        Kapsam: ``cards`` · Akış: client credentials

        With this API, you can only access the POS transaction details of your own accounts. If
        you want to behave as a TPP (Third Party Provider) / Fintech you should use the POS
        Transaction Details V2. &gt; This API is in beta stage. Request and response models may
        change over time.

        Args:
            merchant_block_number: (``merchantBlockNumber``, gövde, zorunlu) Represents the
                blocked number which belongs to customer for POS transactions. This information must
                be obtained using the POS Transactions Summary V2 service.
            merchant_number: (``merchantNumber``, gövde) Represents the merchant number which
                belongs to customer for POS transactions. If the merchant number is not given, a
                search will be made for all merchant numbers belongs to the customer.
            count: (gövde, zorunlu) Represents the number of detail records to query. Max count
                value must be a thousand (1000).
            start_date: (``startDate``, gövde, zorunlu) Represents a filter parameter indicating
                the lower date bound before which the transactions happened.
            end_date: (``endDate``, gövde, zorunlu) Represents a filter parameter indicating the
                upper date bound before which the transactions happened (Enddate is included in the
                search).
            corporate_user_name: (``corporateUserName``, gövde, zorunlu) Represents the User
                Name information belonging to an authorized user of the customer for POS transaction
                details.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transaction-details-v3
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "merchantBlockNumber": merchant_block_number,
                "merchantNumber": merchant_number,
                "count": count,
                "startDate": start_date,
                "endDate": end_date,
                "corporateUserName": corporate_user_name,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v3/pos/detail-transactions",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def pos_transactions_summary_v3(
        self,
        *,
        corporate_user_name: str,
        start_date: DateLike,
        end_date: DateLike,
        member_number: str | None = None,
        extract_type: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """POS Transactions Summary V3.

        ``POST /v3/pos/transactions``

        Kapsam: ``cards`` · Akış: client credentials

        With this API, you can only access the POS transactions of your own accounts. If you
        want to behave as a TPP (Third Party Provider) / Fintech you should use the POS
        Transaction V2. &gt; This API is in beta stage. Request and response models may change
        over time.

        Args:
            corporate_user_name: (``corporateUserName``, gövde, zorunlu) Represents the User
                Name information belonging to an authorized user of the customer for POS
                transactions.
            member_number: (``memberNumber``, gövde) Represents the merchant number that belongs
                to the customer for POS transactions. If the merchant number is not given, a search
                will be made for all merchant numbers belonging to the customer.
            start_date: (``startDate``, gövde, zorunlu) Represents a filter parameter indicating
                the lower date bound before which the transactions happened.
            end_date: (``endDate``, gövde, zorunlu) Represents a filter parameter indicating the
                upper date bound before which the transactions happened (End date is included in the
                search).
            extract_type: (``extractType``, gövde) Represents the POS transaction status. H: All
                Transactions, B: Blocked Transactions, C: UnBlocked Transactions. If the extractType
                is not given, a search will be made according to "H" value.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/pos-transactions-summary-v3
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "corporateUserName": corporate_user_name,
                "memberNumber": member_number,
                "startDate": start_date,
                "endDate": end_date,
                "extractType": extract_type,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v3/pos/transactions",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_order_distribution_detail_v2(
        self,
        *,
        distribution_list: Sequence[Any],
        e_tender_delivery_id: int,
        attachment: str | None = None,
        document_extension: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Order Distribution Detail V2.

        ``POST /v3/purchase/orderdistribution``

        Kapsam: ``payments`` · Akış: client credentials

        Submits order distribution and delivery details to the BOA system for the purchase
        process. The request includes distribution records with delivery, cargo, waybill and
        rejection information, along with optional document attachment details. The response
        returns whether the order distribution submission was successful and includes error
        details if available.

        Args:
            distribution_list: (``DistributionList``, gövde, zorunlu) List of order distribution
                records to be submitted.
            e_tender_delivery_id: (``ETenderDeliveryId``, gövde, zorunlu) Identifier of the
                e-tender delivery record associated with the distribution item or the overall
                request.
            attachment: (``Attachment``, gövde) Content of the related document. It is typically
                sent as base64 encoded document data.
            document_extension: (``DocumentExtension``, gövde) File extension of the submitted
                document. For example: pdf, jpg, png.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/send-order-distribution-detail-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DistributionList": distribution_list,
                "ETenderDeliveryId": e_tender_delivery_id,
                "Attachment": attachment,
                "DocumentExtension": document_extension,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v3/purchase/orderdistribution",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def virtual_pos(
        self,
        *,
        ok_url: str,
        fail_url: str,
        hash_data: str,
        merchant_id: int,
        user_name: str,
        transaction_type: str,
        currency_code: int,
        transaction_security: int,
        api_version: str | None = None,
        customer_id: int | None = None,
        card_number: str | None = None,
        card_expire_date_year: int | None = None,
        card_expire_date_month: int | None = None,
        card_cvv2: int | None = None,
        card_holder_name: str | None = None,
        card_holder_ip_address: str | None = None,
        card_type: str | None = None,
        installment_count: int | None = None,
        amount: Number | None = None,
        display_amount: Number | None = None,
        description: str | None = None,
        merchant_order_id: int | None = None,
        kuveyt_turk_v_pos_additional_data: Mapping[str, Any] | None = None,
        exp_sign: str | None = None,
        customer_ip_address: str | None = None,
        three_d_secure_level: int | None = None,
        batch_id: int | None = None,
        identity_tax_number: str | None = None,
        qery_id: int | None = None,
        debt_id: int | None = None,
        debtor_name: str | None = None,
        period: str | None = None,
        surcharge_amount: Number | None = None,
        sgk_debt_amount: Number | None = None,
        hash_password: str | None = None,
        installment_maturity_commision_flag: int | None = None,
        explain: str | None = None,
        explain2: str | None = None,
        explain3: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS.

        ``POST /v1/vpos``

        Kapsam: ``cards`` · Akış: client credentials

        This endpoint is used to initiate a Virtual POS 3D Model payment transaction. The
        request includes card details, merchant information, transaction amount, redirection
        URLs, and transaction security information. The response returns the content required
        for the 3D authentication or payment flow.

        Args:
            api_version: (``APIVersion``, gövde) API version information to be used for the
                transaction.
            ok_url: (``OkUrl``, gövde, zorunlu) URL where the cardholder will be redirected if
                the transaction is successful.
            fail_url: (``FailUrl``, gövde, zorunlu) URL where the cardholder will be redirected
                if the transaction fails.
            hash_data: (``HashData``, gövde, zorunlu) Hash value generated for transaction
                verification.
            merchant_id: (``MerchantId``, gövde, zorunlu) Merchant identifier.
            customer_id: (``$CustomerId``, gövde)
            user_name: (``UserName``, gövde, zorunlu) Virtual POS user name.
            card_number: (``$CardNumber``, gövde)
            card_expire_date_year: (``$CardExpireDateYear``, gövde)
            card_expire_date_month: (``$CardExpireDateMonth``, gövde)
            card_cvv2: (``$CardCVV2``, gövde)
            card_holder_name: (``$CardHolderName``, gövde)
            card_holder_ip_address: (``CardHolderIPAddress``, gövde) IP address of the
                cardholder.
            card_type: (``CardType``, gövde) Card type information.
            transaction_type: (``TransactionType``, gövde, zorunlu) Type of transaction to be
                performed.
            installment_count: (``InstallmentCount``, gövde) Number of installments. For single
                payment transactions, 0 or 1 can be sent.
            amount: (``$Amount``, gövde)
            display_amount: (``$DisplayAmount``, gövde)
            description: (``Description``, gövde) Description of the transaction.
            currency_code: (``CurrencyCode``, gövde, zorunlu) Currency code of the transaction.
            merchant_order_id: (``$MerchantOrderId``, gövde)
            transaction_security: (``TransactionSecurity``, gövde, zorunlu) Indicates the
                transaction security level.
            kuveyt_turk_v_pos_additional_data: (``KuveytTurkVPosAdditionalData``, gövde) Object
                that contains additional data related to the transaction.
            exp_sign: (``ExpSign``, gövde) Additional signature information related to the
                transaction.
            customer_ip_address: (``CustomerIPAddress``, gövde) Customer IP address.
            three_d_secure_level: (``ThreeDSecureLevel``, gövde) Indicates the 3D Secure level.
            batch_id: (``BatchID``, gövde) Batch identifier associated with the transaction.
            identity_tax_number: (``$IdentityTaxNumber``, gövde)
            qery_id: (``QeryId``, gövde) Query identifier.
            debt_id: (``DebtId``, gövde) Debt identifier.
            debtor_name: (``DebtorName``, gövde) Name, surname, or title of the debtor.
            period: (``Period``, gövde) Debt or payment period information.
            surcharge_amount: (``$SurchargeAmount``, gövde)
            sgk_debt_amount: (``$SGKDebtAmount``, gövde)
            hash_password: (``HashPassword``, gövde) Password used for hash generation.
            installment_maturity_commision_flag: (``InstallmentMaturityCommisionFlag``, gövde)
                Indicates whether installment maturity commission will be applied.
            explain: (``Explain``, gövde) Additional explanation field for the transaction.
            explain2: (``Explain2``, gövde) Second additional explanation field for the
                transaction.
            explain3: (``Explain3``, gövde) Third additional explanation field for the
                transaction.

        Gövde alanları istekte ``KuveytTurkVPosMessage`` nesnesinin içine yerleştirilir.

        Yanıt alanları: ClientResponse, ContentType, BusinessKey, OrderId, ReferenceId

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "APIVersion": api_version,
                "OkUrl": ok_url,
                "FailUrl": fail_url,
                "HashData": hash_data,
                "MerchantId": merchant_id,
                "$CustomerId": customer_id,
                "UserName": user_name,
                "$CardNumber": card_number,
                "$CardExpireDateYear": card_expire_date_year,
                "$CardExpireDateMonth": card_expire_date_month,
                "$CardCVV2": card_cvv2,
                "$CardHolderName": card_holder_name,
                "CardHolderIPAddress": card_holder_ip_address,
                "CardType": card_type,
                "TransactionType": transaction_type,
                "InstallmentCount": installment_count,
                "$Amount": amount,
                "$DisplayAmount": display_amount,
                "Description": description,
                "CurrencyCode": currency_code,
                "$MerchantOrderId": merchant_order_id,
                "TransactionSecurity": transaction_security,
                "KuveytTurkVPosAdditionalData": kuveyt_turk_v_pos_additional_data,
                "ExpSign": exp_sign,
                "CustomerIPAddress": customer_ip_address,
                "ThreeDSecureLevel": three_d_secure_level,
                "BatchID": batch_id,
                "$IdentityTaxNumber": identity_tax_number,
                "QeryId": qery_id,
                "DebtId": debt_id,
                "DebtorName": debtor_name,
                "Period": period,
                "$SurchargeAmount": surcharge_amount,
                "$SGKDebtAmount": sgk_debt_amount,
                "HashPassword": hash_password,
                "InstallmentMaturityCommisionFlag": installment_maturity_commision_flag,
                "Explain": explain,
                "Explain2": explain2,
                "Explain3": explain3,
            },
            extra_body,
        )
        _body = {"KuveytTurkVPosMessage": _body}
        return await self._client.request(
            "POST",
            "/v1/vpos",
            scope="cards",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def virtual_pos_end_day_all_list(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS EndDayAll List.

        ``POST /v1/vpos/endDayAllList``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to retrieve the end-of-day transaction list for a Virtual POS
        merchant within the specified date range. The request includes the date filter and
        Virtual POS login information required to validate the merchant. >This API is in beta
        stage. Request and response models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the end-of-day list filter criteria.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: OrderId, MerchantOrderId, MerchantId, CardHolderName, CardType,
        CardNumber, OrderDate, OrderStatus, LastOrderStatus, OrderType, TransactionStatus,
        FirstAmount, CancelAmount, DrawbackAmount, PartialDrawbackAmount, ClosedAmount, FEC,
        VPSEntryMode, InstallmentCount, DeferringCount, TransactionSecurity, ResponseCode,
        ResponseExplain, EndOfDayStatus, TransactionSide, CardHolderIPAddress,
        MerchantIPAddress, MerchantUserName, ProvNumber, BatchId, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-enddayall-list
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/vpos/endDayAllList",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def virtual_pos_end_of_day(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS EndOfDay.

        ``POST /v1/vpos/endOfDay``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to perform the end-of-day closing operation for Virtual POS
        transactions within the specified date range. The request includes the date filter,
        merchant information, and Virtual POS login information required to validate the
        merchant and process eligible transactions. >This API is in beta stage. Request and
        response models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the end-of-day closing filter criteria.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: VPosMessage, VPosMessageV2, VposMessageCommon, LoginResponse,
        IsEnrolled, IsVirtual, PareqHtmlFormString, ProvisionNumber, RRN, Stan, ResponseCode,
        IsSuccess, ResponseMessage, OrderId, TransactionTime, MerchantOrderId, HashData, MD,
        AuthenticationPacket, ACSURL, Password, CurrencyCode, TransactionType, SafeKey,
        ReferenceId, MerchantId, BusinessKey, PaymentOrderList, WebFlowResponse,
        StartAuthenticationResult, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-endofday
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/vpos/endOfDay",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def virtual_pos_general_transaction(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS General Transaction.

        ``POST /v1/vpos/transaction``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to perform Virtual POS transaction operations such as refund,
        partial refund, and sale reversal for an existing order. The request includes the order
        information, transaction type, optional refund amount, and Virtual POS login information
        required to validate the merchant. >This API is in beta stage. Request and response
        models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the transaction operation details.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: VPosMessage, VPosMessageV2, VposMessageCommon, LoginResponse,
        IsEnrolled, IsVirtual, PareqHtmlFormString, ProvisionNumber, RRN, Stan, ResponseCode,
        IsSuccess, ResponseMessage, OrderId, TransactionTime, MerchantOrderId, HashData, MD,
        AuthenticationPacket, ACSURL, Password, CurrencyCode, TransactionType, SafeKey,
        ReferenceId, MerchantId, BusinessKey, PaymentOrderList, WebFlowResponse,
        StartAuthenticationResult, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-general-transaction
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/vpos/transaction",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def virtual_pos_order_filter(
        self,
        *,
        order_filter_contract: Mapping[str, Any],
        v_pos_login_contract: Mapping[str, Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Virtual POS Order Filter.

        ``POST /v1/vpos/orderFilter``

        Kapsam: ``cards`` · Akış: authorization code (müşteri girişi gerekir)

        This endpoint is used to retrieve Virtual POS order records based on the specified
        filter criteria. The request includes date range, cardholder name, amount limits,
        merchant information, and Virtual POS login information required to validate the
        merchant. >This API is in beta stage. Request and response models may change over time.

        Args:
            order_filter_contract: (``OrderFilterContract``, gövde, zorunlu) Object that
                contains the order filter criteria.
            v_pos_login_contract: (``VPosLoginContract``, gövde, zorunlu) Object that contains
                Virtual POS merchant login information.

        Yanıt alanları: OrderId, MerchantOrderId, MerchantId, CardHolderName, CardType,
        CardNumber, OrderDate, OrderStatus, LastOrderStatus, OrderType, TransactionStatus,
        FirstAmount, CancelAmount, DrawbackAmount, PartialDrawbackAmount, ClosedAmount, FEC,
        VPSEntryMode, InstallmentCount, DeferringCount, TransactionSecurity, ResponseCode,
        ResponseExplain, EndOfDayStatus, TransactionSide, CardHolderIPAddress,
        MerchantIPAddress, MerchantUserName, ProvNumber, BatchId, ...

        Doküman: https://developer.kuveytturk.com.tr/documentation/payment-solutions/virtual-pos-order-filter
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "OrderFilterContract": order_filter_contract,
                "VPosLoginContract": v_pos_login_contract,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/vpos/orderFilter",
            scope="cards",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )
