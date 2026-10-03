from locust import TaskSet, SequentialTaskSet

# Import types and builders to initialize HTTP API clients
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.cards.client import CardsGatewayHTTPClient, build_cards_gateway_locust_http_client
from clients.http.gateway.documents.client import (
    DocumentsGatewayHTTPClient,
    build_documents_gateway_locust_http_client
)
from clients.http.gateway.operations.client import (
    OperationsGatewayHTTPClient,
    build_operations_gateway_locust_http_client
)
from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client


class GatewayHTTPTaskSet(TaskSet):
    """
    A basic TaskSet for HTTP scenarios working with http-gateway.

    All necessary API clients that will be available in subsequent tasks are created here.
    This is used when the order of tasks within the taskset is not important.
    """

    # Annotations of fields with clients
    users_gateway_client: UsersGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient

    def on_start(self) -> None:
        """
        This method is called before TaskSet tasks are started.
        API clients are created here using the Locust environment context.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)


class GatewayHTTPSequentialTaskSet(SequentialTaskSet):
    """
    A basic SequentialTaskSet for HTTP scenarios where the order of task execution is important.

    Tasks within this task set will be executed strictly in sequence, from top to bottom.
    The same API clients as in a regular TaskSet are also initialized here.
    """

    users_gateway_client: UsersGatewayHTTPClient
    cards_gateway_client: CardsGatewayHTTPClient
    accounts_gateway_client: AccountsGatewayHTTPClient
    documents_gateway_client: DocumentsGatewayHTTPClient
    operations_gateway_client: OperationsGatewayHTTPClient

    def on_start(self) -> None:
        """
        API clients creating for a sequential scenario.
        """
        self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)
