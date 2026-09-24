from locust import User, between, task


from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.accounts.schema import OpenDebitCardAccountResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)

    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema

    accounts_gateway_client: AccountsGatewayHTTPClient
    open_debit_card_account_response: OpenDebitCardAccountResponseSchema


    def on_start(self) -> None:
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)

    @task
    def open_debit_card_account(self):
        self.open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(
            self.create_user_response.user.id
        )
