"""Ödemeler uç noktaları (``kt.payments``).

Bu dosya scripts/generate.py tarafından üretildi; elle düzenlemeyin.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

from .._base import RequestOptions
from ..response import APIResponse
from ._resource import AsyncResource, DateLike, Number, Resource, merge

__all__ = ["AsyncPayments", "Payments"]


class Payments(Resource):
    """Ödemeler - ``kt.payments``."""

    def account_validation_by_account_number_for_group_money_transfer(
        self,
        *,
        account_list_to_validate: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Validation By Account Number For Group Money Transfer.

        ``POST /v1/groupmoneytransfer/accountvalidation``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Validates a list of recipient accounts by account number and account suffix for group
        money transfer operations. The response returns validation results for each submitted
        account, including the reference number, message code, message detail, and customer name
        information.

        Args:
            account_list_to_validate: (``accountListToValidate``, gövde, zorunlu) List of
                account records to be validated by account number and account suffix.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, CustomerName

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-account-number-for-group-money-transfer
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountListToValidate": account_list_to_validate,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/groupmoneytransfer/accountvalidation",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def account_validation_by_iban_for_group_money_transfer(
        self,
        *,
        account_list_to_validate: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Validation By Iban For Group Money Transfer.

        ``POST /v1/groupmoneytransfer/account``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Validates a list of recipient accounts by IBAN for group money transfer operations. The
        response returns validation results for each submitted account, including the reference
        number, message code, message detail, and customer name information.

        Args:
            account_list_to_validate: (``accountListToValidate``, gövde, zorunlu) List of
                account records to be validated by IBAN.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, CustomerName

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountListToValidate": account_list_to_validate,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/groupmoneytransfer/account",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def account_validation_by_iban_for_group_money_transfer_v2(
        self,
        *,
        account_list_to_validate: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Validation By Iban For Group Money Transfer V2.

        ``POST /v2/groupmoneytransfer/account``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        This endpoint is used to validate a list of receiver accounts by IBAN for group money
        transfer operations. The request includes the reference number, receiver name, IBAN, and
        currency code for each account to be validated. The response returns validation results
        for each submitted account, including message details and customer name information when
        available.

        Args:
            account_list_to_validate: (``accountListToValidate``, gövde, zorunlu) List of
                accounts to be validated by IBAN.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, CustomerName

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountListToValidate": account_list_to_validate,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/groupmoneytransfer/account",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def cancel_money_transfers_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        incoming_transfer_list_to_cancel: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Cancel Money Transfers From KTBank To Kuveyt Turk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/cancellist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Cancels a list of incoming transfer records for group money transfer operations. The
        response returns cancellation results for each submitted transfer, including the
        reference number, message code, and message detail information.

        Args:
            incoming_transfer_list_to_cancel: (``incomingTransferListToCancel``, gövde, zorunlu)
                List of incoming transfer records to be cancelled.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/cancel-money-transfers-from-ktbank-to-kuveyt-turk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incomingTransferListToCancel": incoming_transfer_list_to_cancel,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/cancellist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def check_money_transfers_status_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        reference_number_list: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Check Money Transfers Status From KTBank to KuveytTurk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist``

        Kapsam: ``intrabank_money_transfers`` · Akış: authorization code (müşteri girişi gerekir)

        Checks the status of incoming transfer records for group money transfer operations by
        using the provided reference number list. The response returns status information for
        each submitted reference number, including message code, message detail, and transaction
        status.

        Args:
            reference_number_list: (``referenceNumberList``, gövde, zorunlu) List of reference
                numbers to be checked for incoming transfer status.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, TransactionStatus

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/check-money-transfers-status-from-ktbank-to-kuveytturk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumberList": reference_number_list,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/checkstatuslist",
            scope="intrabank_money_transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    def do_stamp_duty_tax_payment_offline(
        self,
        *,
        contract: Mapping[str, Any],
        resource_code: str,
        main_debit_contract: Mapping[str, Any],
        tax_code: str,
        installment_number: int,
        tax_amount: Number,
        total_amount: Number,
        due_date: DateLike,
        amount: Number,
        do_notification: bool | None = None,
        sub_tax_amount: Number | None = None,
        debit_contract_list: Sequence[Any] | None = None,
        opsatir_o_id: str | None = None,
        opsh_o_id: str | None = None,
        table_type: int | None = None,
        serial_and_order_number: str | None = None,
        sub_tax_code: str | None = None,
        description: str | None = None,
        discount_amount: Number | None = None,
        total_discount_amount: Number | None = None,
        service_call_id: int | None = None,
        early_payment_state: bool | None = None,
        late_state: bool | None = None,
        valid_installment: bool | None = None,
        begin_installment_date: DateLike | None = None,
        end_installment_date: DateLike | None = None,
        accrual_number: str | None = None,
        name: str | None = None,
        tax_price_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Do Stamp Duty Tax Payment Offline.

        ``POST /v1/tax/do-stamp-duty-tax-payment-offline``

        Kapsam: ``payments`` · Akış: client credentials

        Performs an offline stamp duty tax payment according to the provided taxpayer, payment,
        account, tax office, debit, accrual, vehicle, ATM amount, and reference information. The
        response includes payment, tax, amount, branch, channel, business key, taxpayer,
        transaction date, payer, corporation, and transaction reference details.

        Args:
            contract: (gövde, zorunlu) Contains the offline stamp duty tax payment request
                details.
            resource_code: (``resourceCode``, gövde, zorunlu) Resource code used for the tax
                payment operation.
            do_notification: (``doNotification``, gövde) Indicates whether notification should
                be sent after the payment.
            main_debit_contract: (``MainDebitContract``, gövde, zorunlu) Contains main debit
                details of the tax payment.
            tax_code: (``TaxCode``, gövde, zorunlu) Tax code of the main debit record.
            installment_number: (``InstallmentNumber``, gövde, zorunlu) Installment number of
                the tax payment.
            tax_amount: (``TaxAmount``, gövde, zorunlu) Main tax amount.
            sub_tax_amount: (``SubTaxAmount``, gövde) Sub tax amount.
            total_amount: (``TotalAmount``, gövde, zorunlu) Total payment amount.
            due_date: (``DueDate``, gövde, zorunlu) Due date of the tax payment.
            debit_contract_list: (``DebitContractList``, gövde) List of debit details related to
                the main debit record.
            opsatir_o_id: (``OpsatirOId``, gövde) OPSATIR object identifier of the debit detail.
            opsh_o_id: (``OpshOId``, gövde) OPSH object identifier of the debit detail.
            table_type: (``TableType``, gövde) Table type of the debit detail.
            serial_and_order_number: (``SerialAndOrderNumber``, gövde) Serial and order number
                of the debit detail.
            sub_tax_code: (``SubTaxCode``, gövde) Sub tax code of the debit detail.
            amount: (``Amount``, gövde, zorunlu) Amount of the debit detail.
            description: (``Description``, gövde) Description of the debit detail.
            discount_amount: (``DiscountAmount``, gövde) Discount amount of the debit detail.
            total_discount_amount: (``TotalDiscountAmount``, gövde) Total discount amount of the
                main debit record.
            service_call_id: (``ServiceCallId``, gövde) Service call identifier related to the
                tax inquiry or payment.
            early_payment_state: (``EarlyPaymentState``, gövde) Indicates whether early payment
                status applies.
            late_state: (``LateState``, gövde) Indicates whether late payment status applies.
            valid_installment: (``ValidInstallment``, gövde) Indicates whether the installment
                is valid for payment.
            begin_installment_date: (``BeginInstallmentDate``, gövde) Begin date of the
                installment period.
            end_installment_date: (``EndInstallmentDate``, gövde) End date of the installment
                period.
            accrual_number: (``AccrualNumber``, gövde) Accrual number of the tax payment.
            name: (``Name``, gövde) Name related to the tax record.
            tax_price_id: (``TaxPriceId``, gövde) Tax price identifier.

        Yanıt alanları: installmentNumber, paymentId, taxCode, taxOfficeCode, period, year,
        serialNumber, orderNumber, paymentType, amount, branchId, channelId, businessKey,
        taxNumber, isOnlinePayment, transactionDate, firstName, lastName, corporationName,
        transactionReference, errors, message, code

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/do-stamp-duty-tax-payment-offline
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "contract": contract,
                "resourceCode": resource_code,
                "doNotification": do_notification,
                "MainDebitContract": main_debit_contract,
                "TaxCode": tax_code,
                "InstallmentNumber": installment_number,
                "TaxAmount": tax_amount,
                "SubTaxAmount": sub_tax_amount,
                "TotalAmount": total_amount,
                "DueDate": due_date,
                "DebitContractList": debit_contract_list,
                "OpsatirOId": opsatir_o_id,
                "OpshOId": opsh_o_id,
                "TableType": table_type,
                "SerialAndOrderNumber": serial_and_order_number,
                "SubTaxCode": sub_tax_code,
                "Amount": amount,
                "Description": description,
                "DiscountAmount": discount_amount,
                "TotalDiscountAmount": total_discount_amount,
                "ServiceCallId": service_call_id,
                "EarlyPaymentState": early_payment_state,
                "LateState": late_state,
                "ValidInstallment": valid_installment,
                "BeginInstallmentDate": begin_installment_date,
                "EndInstallmentDate": end_installment_date,
                "AccrualNumber": accrual_number,
                "Name": name,
                "TaxPriceId": tax_price_id,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/tax/do-stamp-duty-tax-payment-offline",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def insert_money_transfers_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        incoming_transfer_list: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Insert Money Transfers From KT Bank To Kuveyt Turk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/insertlist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Creates a list of incoming transfer records for group money transfer operations. The
        request includes sender, receiver, account, branch, transaction, amount, currency,
        reference, and description information. The response returns the processing result for
        each submitted transfer, including the reference number, message code, and message
        detail.

        Args:
            incoming_transfer_list: (``incomingTransferList``, gövde, zorunlu) List of incoming
                transfer records to be created.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/insert-money-transfers-from-kt-bank-to-kuveyt-turk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incomingTransferList": incoming_transfer_list,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/insertlist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def invoice_company_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Invoice Company List.

        ``GET /v1/invoices/companies``

        Kapsam: ``payments`` · Akış: authorization code (müşteri girişi gerekir)

        &lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and
        response models may change over time. &lt;/div&gt; Retrieves all companies where bill
        payment can be made.

        Yanıt alanları: companyList, description, name, companyId, fullName, companyDebtDetails,
        debtTypeId, installmentNumberName, installmentNumberDescription,
        installmentNumberLength, corporationType, corporationTypeInt

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/invoice-company-list
        """
        _query = merge({}, extra_query)
        return self._client.request(
            "GET",
            "/v1/invoices/companies",
            scope="payments",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    def kt_bank_error_message_list(
        self,
        *,
        message_code: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Bank Error Message List.

        ``GET /v1/groupmoneytransfer/errormessagelist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Retrieves the error message list used in group money transfer operations. The list can
        be filtered by message code. The response includes message type, message code, and
        message description information.

        Args:
            message_code: (``messageCode``, sorgu) Message code used to filter the error message
                list.

        Yanıt alanları: MessageType, MessageCode, MessageDescription

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/kt-bank-error-message-list
        """
        _query = merge(
            {
                "messageCode": message_code,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/groupmoneytransfer/errormessagelist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def kuveyt_turk_branch_list_for_group_money_transfer(
        self,
        *,
        branch_id: int | None = None,
        branch_name: str | None = None,
        city_id: int | None = None,
        city_name: str | None = None,
        county_id: int | None = None,
        county_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk Branch List For Group Money Transfer.

        ``GET /v1/groupmoneytransfer/branchlist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Retrieves the branch list for group money transfer operations according to the provided
        branch, city, and county filter criteria. The response includes branch identity,
        location, contact, transaction date, and active status information.

        Args:
            branch_id: (``branchId``, sorgu) Branch identifier used to filter the branch list.
            branch_name: (``branchName``, sorgu) Branch name used to filter the branch list.
            city_id: (``cityId``, sorgu) City identifier used to filter branches by city.
            city_name: (``cityName``, sorgu) City name used to filter branches by city.
            county_id: (``countyId``, sorgu) County identifier used to filter branches by
                county.
            county_name: (``countyName``, sorgu) County name used to filter branches by county.

        Yanıt alanları: BranchId, BranchName, CityId, CityName, CountyId, CountyName,
        BranchAddress, PhoneNumber, Email, FirstTransactionDate, IsActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/kuveyt-turk-branch-list-for-group-money-transfer
        """
        _query = merge(
            {
                "branchId": branch_id,
                "branchName": branch_name,
                "cityId": city_id,
                "cityName": city_name,
                "countyId": county_id,
                "countyName": county_name,
            },
            extra_query,
        )
        return self._client.request(
            "GET",
            "/v1/groupmoneytransfer/branchlist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    def return_money_transfers_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        incoming_transfer_list_to_return: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Return Money Transfers From KTBank To Kuveyt Turk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/returnlist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Returns a list of incoming transfer records for group money transfer operations. The
        request includes the reference number and return description for each incoming transfer.
        The response returns the processing result for each submitted transfer, including the
        reference number, message code, and message detail.

        Args:
            incoming_transfer_list_to_return: (``incomingTransferListToReturn``, gövde, zorunlu)
                List of incoming transfer records to be returned.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/return-money-transfers-from-ktbank-to-kuveyt-turk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incomingTransferListToReturn": incoming_transfer_list_to_return,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/returnlist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_multiple_invoice_v2(
        self,
        *,
        delivery_id_list: Sequence[Any],
        invoice_number_serial: str,
        invoice_date: DateLike,
        attachment: str,
        document_extension: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Multiple Invoice V2.

        ``POST /v2/purchase/multipleinvoice``

        Kapsam: ``payments`` · Akış: client credentials

        Submits invoice details to the BOA system for multiple delivery records related to the
        purchase process. The request includes the delivery ID list, invoice serial number,
        invoice date, document content and document extension. The response returns whether the
        multiple invoice submission was successful and includes error details if available.

        Args:
            delivery_id_list: (``DeliveryIdList``, gövde, zorunlu) List of delivery record IDs
                to be associated with the invoice.
            invoice_number_serial: (``InvoiceNumberSerial``, gövde, zorunlu) Invoice serial and
                number information.
            invoice_date: (``InvoiceDate``, gövde, zorunlu) Invoice date.
            attachment: (``Attachment``, gövde, zorunlu) Content of the invoice document. It is
                typically sent as base64 encoded document data.
            document_extension: (``DocumentExtension``, gövde, zorunlu) File extension of the
                submitted invoice document. For example: pdf, jpg, png.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-multiple-invoice-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DeliveryIdList": delivery_id_list,
                "InvoiceNumberSerial": invoice_number_serial,
                "InvoiceDate": invoice_date,
                "Attachment": attachment,
                "DocumentExtension": document_extension,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v2/purchase/multipleinvoice",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_offer_vendor_detail(
        self,
        *,
        contract_list: Mapping[str, Any],
        attachment: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Offer Vendor Detail.

        ``POST /v1/purchase/offervendor``

        Kapsam: ``payments`` · Akış: client credentials

        This API endpoint is called to send the vendor information, price fields used in the
        purchase offer system.

        Args:
            contract_list: (``contractList``, gövde, zorunlu) Offer detail object
            attachment: (``Attachment``, gövde) Attachment base64 string.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-offer-vendor-detail
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "contractList": contract_list,
                "Attachment": attachment,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/purchase/offervendor",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_order_distribution_detail(
        self,
        *,
        distribution_list: Mapping[str, Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Order Distribution Detail.

        ``POST /v1/purchase/orderdistribution``

        Kapsam: ``payments`` · Akış: client credentials

        This API endpoint is called to send the distribution details used in the purchase order
        system.

        Args:
            distribution_list: (``distributionList``, gövde) Order a distribution object.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "distributionList": distribution_list,
            },
            extra_body,
        )
        return self._client.request(
            "POST",
            "/v1/purchase/orderdistribution",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    def send_order_distribution_detail_v2(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Order Distribution Detail V2.

        ``POST /v3/purchase/orderdistribution``

        Kapsam: ``payments`` · Akış: client credentials

        This API endpoint is called to send the distribution details used in the purchase order
        system.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge({}, extra_body)
        return self._client.request(
            "POST",
            "/v3/purchase/orderdistribution",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )


class AsyncPayments(AsyncResource):
    """Ödemeler (asenkron) - ``kt.payments``."""

    async def account_validation_by_account_number_for_group_money_transfer(
        self,
        *,
        account_list_to_validate: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Validation By Account Number For Group Money Transfer.

        ``POST /v1/groupmoneytransfer/accountvalidation``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Validates a list of recipient accounts by account number and account suffix for group
        money transfer operations. The response returns validation results for each submitted
        account, including the reference number, message code, message detail, and customer name
        information.

        Args:
            account_list_to_validate: (``accountListToValidate``, gövde, zorunlu) List of
                account records to be validated by account number and account suffix.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, CustomerName

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-account-number-for-group-money-transfer
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountListToValidate": account_list_to_validate,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/groupmoneytransfer/accountvalidation",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def account_validation_by_iban_for_group_money_transfer(
        self,
        *,
        account_list_to_validate: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Validation By Iban For Group Money Transfer.

        ``POST /v1/groupmoneytransfer/account``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Validates a list of recipient accounts by IBAN for group money transfer operations. The
        response returns validation results for each submitted account, including the reference
        number, message code, message detail, and customer name information.

        Args:
            account_list_to_validate: (``accountListToValidate``, gövde, zorunlu) List of
                account records to be validated by IBAN.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, CustomerName

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountListToValidate": account_list_to_validate,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/groupmoneytransfer/account",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def account_validation_by_iban_for_group_money_transfer_v2(
        self,
        *,
        account_list_to_validate: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Account Validation By Iban For Group Money Transfer V2.

        ``POST /v2/groupmoneytransfer/account``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        This endpoint is used to validate a list of receiver accounts by IBAN for group money
        transfer operations. The request includes the reference number, receiver name, IBAN, and
        currency code for each account to be validated. The response returns validation results
        for each submitted account, including message details and customer name information when
        available.

        Args:
            account_list_to_validate: (``accountListToValidate``, gövde, zorunlu) List of
                accounts to be validated by IBAN.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, CustomerName

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/account-validation-by-iban-for-group-money-transfer-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "accountListToValidate": account_list_to_validate,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/groupmoneytransfer/account",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def cancel_money_transfers_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        incoming_transfer_list_to_cancel: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Cancel Money Transfers From KTBank To Kuveyt Turk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/cancellist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Cancels a list of incoming transfer records for group money transfer operations. The
        response returns cancellation results for each submitted transfer, including the
        reference number, message code, and message detail information.

        Args:
            incoming_transfer_list_to_cancel: (``incomingTransferListToCancel``, gövde, zorunlu)
                List of incoming transfer records to be cancelled.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/cancel-money-transfers-from-ktbank-to-kuveyt-turk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incomingTransferListToCancel": incoming_transfer_list_to_cancel,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/cancellist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def check_money_transfers_status_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        reference_number_list: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Check Money Transfers Status From KTBank to KuveytTurk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/checkstatuslist``

        Kapsam: ``intrabank_money_transfers`` · Akış: authorization code (müşteri girişi gerekir)

        Checks the status of incoming transfer records for group money transfer operations by
        using the provided reference number list. The response returns status information for
        each submitted reference number, including message code, message detail, and transaction
        status.

        Args:
            reference_number_list: (``referenceNumberList``, gövde, zorunlu) List of reference
                numbers to be checked for incoming transfer status.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail, TransactionStatus

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/check-money-transfers-status-from-ktbank-to-kuveytturk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "referenceNumberList": reference_number_list,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/checkstatuslist",
            scope="intrabank_money_transfers",
            flow="authorization_code",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def do_stamp_duty_tax_payment_offline(
        self,
        *,
        contract: Mapping[str, Any],
        resource_code: str,
        main_debit_contract: Mapping[str, Any],
        tax_code: str,
        installment_number: int,
        tax_amount: Number,
        total_amount: Number,
        due_date: DateLike,
        amount: Number,
        do_notification: bool | None = None,
        sub_tax_amount: Number | None = None,
        debit_contract_list: Sequence[Any] | None = None,
        opsatir_o_id: str | None = None,
        opsh_o_id: str | None = None,
        table_type: int | None = None,
        serial_and_order_number: str | None = None,
        sub_tax_code: str | None = None,
        description: str | None = None,
        discount_amount: Number | None = None,
        total_discount_amount: Number | None = None,
        service_call_id: int | None = None,
        early_payment_state: bool | None = None,
        late_state: bool | None = None,
        valid_installment: bool | None = None,
        begin_installment_date: DateLike | None = None,
        end_installment_date: DateLike | None = None,
        accrual_number: str | None = None,
        name: str | None = None,
        tax_price_id: int | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Do Stamp Duty Tax Payment Offline.

        ``POST /v1/tax/do-stamp-duty-tax-payment-offline``

        Kapsam: ``payments`` · Akış: client credentials

        Performs an offline stamp duty tax payment according to the provided taxpayer, payment,
        account, tax office, debit, accrual, vehicle, ATM amount, and reference information. The
        response includes payment, tax, amount, branch, channel, business key, taxpayer,
        transaction date, payer, corporation, and transaction reference details.

        Args:
            contract: (gövde, zorunlu) Contains the offline stamp duty tax payment request
                details.
            resource_code: (``resourceCode``, gövde, zorunlu) Resource code used for the tax
                payment operation.
            do_notification: (``doNotification``, gövde) Indicates whether notification should
                be sent after the payment.
            main_debit_contract: (``MainDebitContract``, gövde, zorunlu) Contains main debit
                details of the tax payment.
            tax_code: (``TaxCode``, gövde, zorunlu) Tax code of the main debit record.
            installment_number: (``InstallmentNumber``, gövde, zorunlu) Installment number of
                the tax payment.
            tax_amount: (``TaxAmount``, gövde, zorunlu) Main tax amount.
            sub_tax_amount: (``SubTaxAmount``, gövde) Sub tax amount.
            total_amount: (``TotalAmount``, gövde, zorunlu) Total payment amount.
            due_date: (``DueDate``, gövde, zorunlu) Due date of the tax payment.
            debit_contract_list: (``DebitContractList``, gövde) List of debit details related to
                the main debit record.
            opsatir_o_id: (``OpsatirOId``, gövde) OPSATIR object identifier of the debit detail.
            opsh_o_id: (``OpshOId``, gövde) OPSH object identifier of the debit detail.
            table_type: (``TableType``, gövde) Table type of the debit detail.
            serial_and_order_number: (``SerialAndOrderNumber``, gövde) Serial and order number
                of the debit detail.
            sub_tax_code: (``SubTaxCode``, gövde) Sub tax code of the debit detail.
            amount: (``Amount``, gövde, zorunlu) Amount of the debit detail.
            description: (``Description``, gövde) Description of the debit detail.
            discount_amount: (``DiscountAmount``, gövde) Discount amount of the debit detail.
            total_discount_amount: (``TotalDiscountAmount``, gövde) Total discount amount of the
                main debit record.
            service_call_id: (``ServiceCallId``, gövde) Service call identifier related to the
                tax inquiry or payment.
            early_payment_state: (``EarlyPaymentState``, gövde) Indicates whether early payment
                status applies.
            late_state: (``LateState``, gövde) Indicates whether late payment status applies.
            valid_installment: (``ValidInstallment``, gövde) Indicates whether the installment
                is valid for payment.
            begin_installment_date: (``BeginInstallmentDate``, gövde) Begin date of the
                installment period.
            end_installment_date: (``EndInstallmentDate``, gövde) End date of the installment
                period.
            accrual_number: (``AccrualNumber``, gövde) Accrual number of the tax payment.
            name: (``Name``, gövde) Name related to the tax record.
            tax_price_id: (``TaxPriceId``, gövde) Tax price identifier.

        Yanıt alanları: installmentNumber, paymentId, taxCode, taxOfficeCode, period, year,
        serialNumber, orderNumber, paymentType, amount, branchId, channelId, businessKey,
        taxNumber, isOnlinePayment, transactionDate, firstName, lastName, corporationName,
        transactionReference, errors, message, code

        Doküman: https://developer.kuveytturk.com.tr/documentation/other/do-stamp-duty-tax-payment-offline
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "contract": contract,
                "resourceCode": resource_code,
                "doNotification": do_notification,
                "MainDebitContract": main_debit_contract,
                "TaxCode": tax_code,
                "InstallmentNumber": installment_number,
                "TaxAmount": tax_amount,
                "SubTaxAmount": sub_tax_amount,
                "TotalAmount": total_amount,
                "DueDate": due_date,
                "DebitContractList": debit_contract_list,
                "OpsatirOId": opsatir_o_id,
                "OpshOId": opsh_o_id,
                "TableType": table_type,
                "SerialAndOrderNumber": serial_and_order_number,
                "SubTaxCode": sub_tax_code,
                "Amount": amount,
                "Description": description,
                "DiscountAmount": discount_amount,
                "TotalDiscountAmount": total_discount_amount,
                "ServiceCallId": service_call_id,
                "EarlyPaymentState": early_payment_state,
                "LateState": late_state,
                "ValidInstallment": valid_installment,
                "BeginInstallmentDate": begin_installment_date,
                "EndInstallmentDate": end_installment_date,
                "AccrualNumber": accrual_number,
                "Name": name,
                "TaxPriceId": tax_price_id,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/tax/do-stamp-duty-tax-payment-offline",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def insert_money_transfers_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        incoming_transfer_list: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Insert Money Transfers From KT Bank To Kuveyt Turk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/insertlist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Creates a list of incoming transfer records for group money transfer operations. The
        request includes sender, receiver, account, branch, transaction, amount, currency,
        reference, and description information. The response returns the processing result for
        each submitted transfer, including the reference number, message code, and message
        detail.

        Args:
            incoming_transfer_list: (``incomingTransferList``, gövde, zorunlu) List of incoming
                transfer records to be created.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/insert-money-transfers-from-kt-bank-to-kuveyt-turk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incomingTransferList": incoming_transfer_list,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/insertlist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def invoice_company_list(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Invoice Company List.

        ``GET /v1/invoices/companies``

        Kapsam: ``payments`` · Akış: authorization code (müşteri girişi gerekir)

        &lt;div class="alert alert-warning"&gt; Note: This API is in beta stage. Request and
        response models may change over time. &lt;/div&gt; Retrieves all companies where bill
        payment can be made.

        Yanıt alanları: companyList, description, name, companyId, fullName, companyDebtDetails,
        debtTypeId, installmentNumberName, installmentNumberDescription,
        installmentNumberLength, corporationType, corporationTypeInt

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/invoice-company-list
        """
        _query = merge({}, extra_query)
        return await self._client.request(
            "GET",
            "/v1/invoices/companies",
            scope="payments",
            flow="authorization_code",
            query=_query,
            options=request_options,
        )

    async def kt_bank_error_message_list(
        self,
        *,
        message_code: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """KT Bank Error Message List.

        ``GET /v1/groupmoneytransfer/errormessagelist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Retrieves the error message list used in group money transfer operations. The list can
        be filtered by message code. The response includes message type, message code, and
        message description information.

        Args:
            message_code: (``messageCode``, sorgu) Message code used to filter the error message
                list.

        Yanıt alanları: MessageType, MessageCode, MessageDescription

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/kt-bank-error-message-list
        """
        _query = merge(
            {
                "messageCode": message_code,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/groupmoneytransfer/errormessagelist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def kuveyt_turk_branch_list_for_group_money_transfer(
        self,
        *,
        branch_id: int | None = None,
        branch_name: str | None = None,
        city_id: int | None = None,
        city_name: str | None = None,
        county_id: int | None = None,
        county_name: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Kuveyt Turk Branch List For Group Money Transfer.

        ``GET /v1/groupmoneytransfer/branchlist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Retrieves the branch list for group money transfer operations according to the provided
        branch, city, and county filter criteria. The response includes branch identity,
        location, contact, transaction date, and active status information.

        Args:
            branch_id: (``branchId``, sorgu) Branch identifier used to filter the branch list.
            branch_name: (``branchName``, sorgu) Branch name used to filter the branch list.
            city_id: (``cityId``, sorgu) City identifier used to filter branches by city.
            city_name: (``cityName``, sorgu) City name used to filter branches by city.
            county_id: (``countyId``, sorgu) County identifier used to filter branches by
                county.
            county_name: (``countyName``, sorgu) County name used to filter branches by county.

        Yanıt alanları: BranchId, BranchName, CityId, CityName, CountyId, CountyName,
        BranchAddress, PhoneNumber, Email, FirstTransactionDate, IsActive

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/kuveyt-turk-branch-list-for-group-money-transfer
        """
        _query = merge(
            {
                "branchId": branch_id,
                "branchName": branch_name,
                "cityId": city_id,
                "cityName": city_name,
                "countyId": county_id,
                "countyName": county_name,
            },
            extra_query,
        )
        return await self._client.request(
            "GET",
            "/v1/groupmoneytransfer/branchlist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            options=request_options,
        )

    async def return_money_transfers_from_kt_bank_to_kuveyt_turk(
        self,
        *,
        incoming_transfer_list_to_return: Sequence[Any],
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Return Money Transfers From KTBank To Kuveyt Turk.

        ``POST /v1/groupmoneytransfer/incomingtransfer/returnlist``

        Kapsam: ``intrabank_money_transfers`` · Akış: client credentials

        Returns a list of incoming transfer records for group money transfer operations. The
        request includes the reference number and return description for each incoming transfer.
        The response returns the processing result for each submitted transfer, including the
        reference number, message code, and message detail.

        Args:
            incoming_transfer_list_to_return: (``incomingTransferListToReturn``, gövde, zorunlu)
                List of incoming transfer records to be returned.

        Yanıt alanları: ReferenceNumber, MessageCode, MessageDetail

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/return-money-transfers-from-ktbank-to-kuveyt-turk
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "incomingTransferListToReturn": incoming_transfer_list_to_return,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/groupmoneytransfer/incomingtransfer/returnlist",
            scope="intrabank_money_transfers",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_multiple_invoice_v2(
        self,
        *,
        delivery_id_list: Sequence[Any],
        invoice_number_serial: str,
        invoice_date: DateLike,
        attachment: str,
        document_extension: str,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Multiple Invoice V2.

        ``POST /v2/purchase/multipleinvoice``

        Kapsam: ``payments`` · Akış: client credentials

        Submits invoice details to the BOA system for multiple delivery records related to the
        purchase process. The request includes the delivery ID list, invoice serial number,
        invoice date, document content and document extension. The response returns whether the
        multiple invoice submission was successful and includes error details if available.

        Args:
            delivery_id_list: (``DeliveryIdList``, gövde, zorunlu) List of delivery record IDs
                to be associated with the invoice.
            invoice_number_serial: (``InvoiceNumberSerial``, gövde, zorunlu) Invoice serial and
                number information.
            invoice_date: (``InvoiceDate``, gövde, zorunlu) Invoice date.
            attachment: (``Attachment``, gövde, zorunlu) Content of the invoice document. It is
                typically sent as base64 encoded document data.
            document_extension: (``DocumentExtension``, gövde, zorunlu) File extension of the
                submitted invoice document. For example: pdf, jpg, png.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-multiple-invoice-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "DeliveryIdList": delivery_id_list,
                "InvoiceNumberSerial": invoice_number_serial,
                "InvoiceDate": invoice_date,
                "Attachment": attachment,
                "DocumentExtension": document_extension,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v2/purchase/multipleinvoice",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_offer_vendor_detail(
        self,
        *,
        contract_list: Mapping[str, Any],
        attachment: str | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Offer Vendor Detail.

        ``POST /v1/purchase/offervendor``

        Kapsam: ``payments`` · Akış: client credentials

        This API endpoint is called to send the vendor information, price fields used in the
        purchase offer system.

        Args:
            contract_list: (``contractList``, gövde, zorunlu) Offer detail object
            attachment: (``Attachment``, gövde) Attachment base64 string.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-offer-vendor-detail
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "contractList": contract_list,
                "Attachment": attachment,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/purchase/offervendor",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_order_distribution_detail(
        self,
        *,
        distribution_list: Mapping[str, Any] | None = None,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Order Distribution Detail.

        ``POST /v1/purchase/orderdistribution``

        Kapsam: ``payments`` · Akış: client credentials

        This API endpoint is called to send the distribution details used in the purchase order
        system.

        Args:
            distribution_list: (``distributionList``, gövde) Order a distribution object.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail
        """
        _query = merge({}, extra_query)
        _body: Any = merge(
            {
                "distributionList": distribution_list,
            },
            extra_body,
        )
        return await self._client.request(
            "POST",
            "/v1/purchase/orderdistribution",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )

    async def send_order_distribution_detail_v2(
        self,
        *,
        extra_query: Mapping[str, Any] | None = None,
        extra_body: Mapping[str, Any] | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Send Order Distribution Detail V2.

        ``POST /v3/purchase/orderdistribution``

        Kapsam: ``payments`` · Akış: client credentials

        This API endpoint is called to send the distribution details used in the purchase order
        system.

        Doküman: https://developer.kuveytturk.com.tr/documentation/payments/send-order-distribution-detail-v2
        """
        _query = merge({}, extra_query)
        _body: Any = merge({}, extra_body)
        return await self._client.request(
            "POST",
            "/v3/purchase/orderdistribution",
            scope="payments",
            flow="client_credentials",
            query=_query,
            body=_body,
            options=request_options,
        )
