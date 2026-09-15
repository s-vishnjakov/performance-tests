from grpc import Channel
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import (
    GetOperationRequest,
    GetOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import (
    GetOperationsRequest,
    GetOperationsResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest,
    GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest,
    MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest,
    MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest,
    MakeTransferOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest,
    MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest,
    MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest,
    MakeCashWithdrawalOperationResponse
)
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC client for interacting with the OperationsGatewayService.
    Provides high-level methods for conducting financial transactions and obtaining its data.
    """

    def __init__(self, channel: Channel):
        """
        Initialize a client with the specified gRPC channel.

        :param channel: gRPC channel to connect to the OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Low-level call to the GetOperation method via gRPC.

        :param request: gRPC request with the operation ID.
        :return: Response from the service with the operation data.
        """
        return self.stub.GetOperation(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Low-level call to the GetOperations method via gRPC.

        :param request: gRPC request with the account ID.
        :return: Response from the service with the list of operations.
        """
        return self.stub.GetOperations(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Low-level call to the GetOperationReceipt method via gRPC.

        :param request: gRPC request with the operation ID.
        :return: Response from the service with the operation receipt.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Low-level call to the GetOperationsSummary method via gRPC.

        :param request: gRPC request with the account ID.
        :return: Response from the service with the operations summary.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Low-level call to the MakeFeeOperation method via gRPC.

        :param request: gRPC request with the fee operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Low-level call to the MakeTopUpOperation method via gRPC.

        :param request: gRPC request with the top-up operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Low-level call to the MakeCashbackOperation method via gRPC.

        :param request: gRPC request with the cashback operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Low-level call to the MakeTransferOperation method via gRPC.

        :param request: gRPC request with the transfer operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Low-level call to the MakePurchaseOperation method via gRPC.

        :param request: gRPC request with the purchase operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequest
    ) -> MakeBillPaymentOperationResponse:
        """
        Low-level call to the MakeBillPaymentOperation method via gRPC.

        :param request: gRPC request with the bill payment operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequest
    ) -> MakeCashWithdrawalOperationResponse:
        """
        Low-level call to the MakeCashWithdrawalOperation method via gRPC.

        :param request: gRPC request with the cash withdrawal operation data.
        :return: Response from the service with the created operation.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Getting data for a single operation by its ID.

        :param operation_id: Operation ID.
        :return: Response with the operation data.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Getting the list of ALL operations for the specified account.

        :param account_id: Account ID.
        :return: Response with the list of operations.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Getting the receipt for the specified operation.

        :param operation_id: Operation ID.
        :return: Response with the operation receipt.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Getting operations statistics for the specified account.

        :param account_id: Account ID.
        :return: Response with the operations summary.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, account_id: str, card_id: str) -> MakeFeeOperationResponse:
        """
        Makes a fee operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakeFeeOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )

        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, account_id: str, card_id: str) -> MakeTopUpOperationResponse:
        """
        Makes a top-up operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakeTopUpOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, account_id: str, card_id: str) -> MakeCashbackOperationResponse:
        """
        Makes a cashback operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakeCashbackOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, account_id: str, card_id: str) -> MakeTransferOperationResponse:
        """
        Makes a transfer operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakeTransferOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, account_id: str, card_id: str) -> MakePurchaseOperationResponse:
        """
        Makes a purchase operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakePurchaseOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
            category=fake.category()
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, account_id: str, card_id: str) -> MakeBillPaymentOperationResponse:
        """
        Makes a bill payment operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakeBillPaymentOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus),
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, account_id: str, card_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Makes a cash withdrawal operation and returns its data.

        :param account_id: Account ID.
        :param card_id: Card ID.
        :return: Response with the created operation.
        """
        request = MakeCashWithdrawalOperationRequest(
            account_id=account_id,
            card_id=card_id,
            amount=fake.amount(),
            status=fake.proto_enum(OperationStatus)
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Builder for creating a OperationsGatewayGRPCClient instance.

    :return: Initialized client for OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())
