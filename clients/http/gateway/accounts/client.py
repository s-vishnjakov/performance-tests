from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.accounts.schema import (
    GetAccountsQuerySchema,
    GetAccountsResponseSchema,
    OpenCreditCardAccountRequestSchema,
    OpenCreditCardAccountResponseSchema,
    OpenDebitCardAccountRequestSchema,
    OpenDebitCardAccountResponseSchema,
    OpenDepositAccountRequestSchema,
    OpenDepositAccountResponseSchema,
    OpenSavingsAccountRequestSchema,
    OpenSavingsAccountResponseSchema
)


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with the /api/v1/accounts endpoint of the http-gateway service.
    """

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """
        Retrieves the list of user accounts.

        :param query: The query schema containing the user identifier.
        :return: An HTTP response containing the accounts data.
        """
        return self.get(
            "/api/v1/accounts",
            params=QueryParams(**query.model_dump(by_alias=True))
        )

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """
        Opens a deposit account.

        :param request: The request schema containing the user identifier.
        :return: An HTTP response containing the result of the operation.
        """
        return self.post(
            "/api/v1/accounts/open-deposit-account",
            json=request.model_dump(by_alias=True)
        )

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        """
        Opens a savings account.

        :param request: The request schema containing the user identifier.
        :return: An HTTP response containing the result of the operation.
        """
        return self.post(
            "/api/v1/accounts/open-savings-account",
            json=request.model_dump(by_alias=True)
        )

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """
        Opens a debit card account.

        :param request: The request schema containing the user identifier.
        :return: An HTTP response containing the result of the operation.
        """
        return self.post(
            "/api/v1/accounts/open-debit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """
        Opens a credit card account.

        :param request: The request schema containing the user identifier.
        :return: An HTTP response containing the result of the operation.
        """
        return self.post(
            "/api/v1/accounts/open-credit-card-account",
            json=request.model_dump(by_alias=True)
        )

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_saving_account(self, user_id: str) -> OpenSavingsAccountResponseSchema:
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Creates an instance of AccountsGatewayHTTPClient with a pre-configured HTTP client.

    :return: A ready-to-use AccountsGatewayHTTPClient instance.
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())
