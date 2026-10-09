from locust import task
# Импортируем схемы ответов, чтобы типизировать shared state
from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from contracts.services.gateway.accounts.rpc_open_savings_account_pb2 import OpenSavingsAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from tools.locust.user import LocustBaseUser


class GetDocumentsSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    """
    Performance scenario that sequentially:
    1. Creates a new user.
    2. Opens a savings account.
    3. Receives account documents (tariff and contract).

    Uses the basic GatewayGRPCSequentialTaskSet and the API clients already created within it.
    """

    # Shared state — saves query results for the future use
    create_user_response: CreateUserResponse | None = None
    open_savings_account_response: OpenSavingsAccountResponse | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_savings_account(self):
        if not self.create_user_response:
            return  # If a user not created, there is no point to continue.

        self.open_savings_account_response = self.accounts_gateway_client.open_savings_account(
            user_id=self.create_user_response.user.id
        )

    @task
    def get_documents(self):
        if not self.open_savings_account_response:
            return  # If an account not created, there is no point to continue.

        self.documents_gateway_client.get_tariff_document(
            account_id=self.open_savings_account_response.account.id
        )
        self.documents_gateway_client.get_contract_document(
            account_id=self.open_savings_account_response.account.id
        )


class GetDocumentsScenarioUser(LocustBaseUser):
    """
    Locust user executing the sequential document retrieval scenario.
    """
    tasks = [GetDocumentsSequentialTaskSet]
