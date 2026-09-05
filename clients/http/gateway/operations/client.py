from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    OperationStatus
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with the /api/v1/operations endpoint of the http-gateway service.
    """

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Retrieves ALL operations of the specified account.

        :param query: The query schema containing the account identifier.
        :return: An HTTP response containing the operations` data.
        """
        return self.get(
            "/api/v1/operations",
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Retrieves the operations statistics of the specified account.

        :param query: The query schema containing the account identifier.
        :return: An HTTP response containing the operations` statistics.
        """
        return self.get(
            "/api/v1/operations/operations-summary",
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Retrieves the receipt of the specified operation.

        :param operation_id: The unique identifier of the operation.
        :return: An HTTP response containing the document link and the document itself.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Retrieves data of a SINGLE operation by the specified operation ID.

        :param operation_id: The unique identifier of the operation.
        :return: An HTTP response containing the operation data.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        Makes a fee operation.

        :param request: The request schema containing status, amount, cardId and accountId.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-fee-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        Makes a top up operation.

        :param request: The request schema containing status, amount, cardId and accountId.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-top-up-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        Makes a cashback operation.

        :param request: The request schema containing status, amount, cardId and accountId.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-cashback-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        Makes a transfer operation.

        :param request: The request schema containing status, amount, cardId and accountId.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-transfer-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        Makes a purchase operation.

        :param request: The request schema containing status, amount, cardId, accountId and category.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-purchase-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Makes a bill payment operation.

        :param request: The request schema containing status, amount, cardId and accountId.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-bill-payment-operation",
            json=request.model_dump(by_alias=True)
        )

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Makes a cash withdrawal operation.

        :param request: The request schema containing status, amount, cardId and accountId.
        :return: An HTTP response containing the completed operation data.
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation",
            json=request.model_dump(by_alias=True)
        )

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Retrieves ALL operations of the specified account as a validated schema object.

        :param account_id: The unique identifier of the account.
        :return: A validated GetOperationsResponseSchema object containing the operations` data.
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Retrieves the operations statistics of the specified account as a validated schema object.

        :param account_id: The unique identifier of the account.
        :return: A validated GetOperationsSummaryResponseSchema object containing the statistics.
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Retrieves the receipt of the specified operation as a validated schema object.

        :param operation_id: The unique identifier of the operation.
        :return: A validated GetOperationReceiptResponseSchema object containing the receipt data.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Retrieves data of a SINGLE operation as a validated schema object.

        :param operation_id: The unique identifier of the operation.
        :return: A validated GetOperationResponseSchema object containing the operation data.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Makes a fee operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :return: A validated MakeFeeOperationResponseSchema object containing the operation data.
        """
        request = MakeFeeOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        Makes a top up operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :return: A validated MakeTopUpOperationResponseSchema object containing the operation data.
        """
        request = MakeTopUpOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1500.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Makes a cashback operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :return: A validated MakeCashbackOperationResponseSchema object containing the operation data.
        """
        request = MakeCashbackOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=28.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Makes a transfer operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :return: A validated MakeTransferOperationResponseSchema object containing the operation data.
        """
        request = MakeTransferOperationRequestSchema(
            status=OperationStatus.FAILED,
            amount=350.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(
            self,
            card_id: str,
            account_id: str,
            category: str
    ) -> MakePurchaseOperationResponseSchema:
        """
        Makes a purchase operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :param category: The category of the purchase.
        :return: A validated MakePurchaseOperationResponseSchema object containing the operation data.
        """
        request = MakePurchaseOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=99.98,
            card_id=card_id,
            account_id=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Makes a bill payment operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :return: A validated MakeBillPaymentOperationResponseSchema object containing the operation data.
        """
        request = MakeBillPaymentOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=128.50,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(
            self,
            card_id: str,
            account_id: str
    ) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Makes a cash withdrawal operation and returns the response as a validated schema object.

        :param card_id: The unique identifier of the card.
        :param account_id: The unique identifier of the account.
        :return: A validated MakeCashWithdrawalOperationResponseSchema object containing the operation data.
        """
        request = MakeCashWithdrawalOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Creates an instance of OperationsGatewayHTTPClient with a pre-configured HTTP client.

    :return: A ready-to-use OperationsGatewayHTTPClient instance.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
