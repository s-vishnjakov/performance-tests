from locust import User, between, task
# Import response schemas to type the shared state
from clients.http.gateway.accounts.schema import OpenSavingsAccountResponseSchema
from clients.http.gateway.locust import GatewayHTTPSequentialTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema


class GetDocumentsSequentialTaskSet(GatewayHTTPSequentialTaskSet):
    """
    Performance scenario that sequentially:
    1. Creates a new user.
    2. Opens a savings account.
    3. Receives account documents (tariff and contract).

    Uses the basic GatewayHTTPSequentialTaskSet and the API clients already created within it.
    """

    # Shared state — saves query results for the future use
    create_user_response: CreateUserResponseSchema | None = None
    open_savings_account_response: OpenSavingsAccountResponseSchema | None = None

    @task
    def create_user(self):
        self.create_user_response = self.users_gateway_client.create_user()

    @task
    def open_savings_account(self):
        if not self.create_user_response:
            return  # If a user not created, there is no point to continue.

        self.open_savings_account_response = self.accounts_gateway_client.open_saving_account(
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


class GetDocumentsUser(User):
    """
    Locust user executing the sequential document retrieval scenario.
    """
    host = "localhost"
    tasks = [GetDocumentsSequentialTaskSet]
    wait_time = between(1, 3)
