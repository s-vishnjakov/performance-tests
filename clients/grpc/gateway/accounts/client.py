from grpc import Channel
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_get_accounts_pb2 import (
    GetAccountsRequest,
    GetAccountsResponse
)
from contracts.services.gateway.accounts.rpc_open_deposit_account_pb2 import (
    OpenDepositAccountRequest,
    OpenDepositAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import (
    OpenSavingsAccountRequest,
    OpenSavingsAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse
)
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse
)


class AccountsGatewayGRPCClient(GRPCClient):
    """
    gRPC client for interacting with the AccountsGatewayService.
    Provides high-level methods for retrieving and opening accounts.
    """

    def __init__(self, channel: Channel):
        """
        Initialize a client with the specified gRPC channel.

        :param channel: gRPC-channel to connect to the AccountsGatewayService.
        """
        super().__init__(channel)

        self.stub = AccountsGatewayServiceStub(channel)

    def get_accounts_api(self, request: GetAccountsRequest) -> GetAccountsResponse:
        """
        Low-level call to the GetAccounts method via gRPC.

        :param request: gRPC request with the user ID.
        :return: Response from the service with the list of accounts.
        """
        return self.stub.GetAccounts(request)

    def open_deposit_account_api(self, request: OpenDepositAccountRequest) -> OpenDepositAccountResponse:
        """
        Low-level call to the OpenDepositAccount method via gRPC.

        :param request: gRPC request with the user ID.
        :return: Response from the service with the opened deposit account details.
        """
        return self.stub.OpenDepositAccount(request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequest) -> OpenSavingsAccountResponse:
        """
        Low-level call to the OpenSavingsAccount method via gRPC.

        :param request: gRPC request with the user ID.
        :return: Response from the service with the opened savings account details.
        """
        return self.stub.OpenSavingsAccount(request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequest) -> OpenDebitCardAccountResponse:
        """
        Low-level call to the OpenDebitCardAccount method via gRPC.

        :param request: gRPC request with the user ID.
        :return: Response from the service with the opened debit card account details.
        """
        return self.stub.OpenDepositAccount(request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequest) -> OpenCreditCardAccountResponse:
        """
        Low-level call to the OpenCreditCardAccount method via gRPC.

        :param request: gRPC request with the user ID.
        :return: Response from the service with the opened credit card account details.
        """
        return self.stub.OpenCreditCardAccount(request)

    def get_accounts(self, user_id: str) -> GetAccountsResponse:
        request = GetAccountsRequest(user_id=user_id)
        return self.get_accounts_api(request)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponse:
        request = OpenDepositAccountRequest(user_id=user_id)
        return self.open_deposit_account_api(request)

    def open_savings_account(self, user_id: str) -> OpenSavingsAccountResponse:
        request = OpenSavingsAccountRequest(user_id=user_id)
        return self.open_savings_account_api(request)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponse:
        request = OpenDebitCardAccountRequest(user_id=user_id)
        return self.open_debit_card_account_api(request)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponse:
        request = OpenCreditCardAccountRequest(user_id=user_id)
        return self.open_credit_card_account_api(request)


def build_accounts_gateway_grpc_client() -> AccountsGatewayGRPCClient:
    """
    Builder for creating an AccountsGatewayGRPCClient instance.

    :return: Initialized client for AccountsGatewayService.
    """
    return AccountsGatewayGRPCClient(channel=build_gateway_grpc_client())
