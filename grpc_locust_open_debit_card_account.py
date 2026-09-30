from locust import User, between, task

from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayGRPCClient
    create_user_response: CreateUserResponse

    accounts_gateway_client: AccountsGatewayGRPCClient
    open_debit_card_account_response: OpenDebitCardAccountResponse


    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)

    @task
    def open_debit_card_account(self):
        self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)
