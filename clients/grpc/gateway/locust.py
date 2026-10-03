from locust import TaskSet, SequentialTaskSet

# Import types and builders for building gRPC API clients
from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from clients.grpc.gateway.cards.client import CardsGatewayGRPCClient, build_cards_gateway_locust_grpc_client
from clients.grpc.gateway.documents.client import (
    DocumentsGatewayGRPCClient,
    build_documents_gateway_locust_grpc_client
)
from clients.grpc.gateway.operations.client import (
    OperationsGatewayGRPCClient,
    build_operations_gateway_locust_grpc_client
)
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client


class GatewayGRPCTaskSet(TaskSet):
    """
    Basic TaskSet for gRPC scenarios working with grpc-gateway.

    All necessary API clients that will be available in subsequent tasks are created here.
    This is used when the order of tasks within the task set is not important.
    """

    # Annotations of fields with clients
    users_gateway_client: UsersGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        """
        This method is called before TaskSet tasks are started.
        API clients are created here using the Locust environment context.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(self.user.environment)


class GatewayGRPCSequentialTaskSet(SequentialTaskSet):
    """
    A basic SequentialTaskSet for gRPC scenarios where the order of task execution is important.

    Tasks within this task set will be executed strictly in sequence, from top to bottom.
    The same API clients as in a regular TaskSet are also initialized here.
    """
    users_gateway_client: UsersGatewayGRPCClient
    cards_gateway_client: CardsGatewayGRPCClient
    accounts_gateway_client: AccountsGatewayGRPCClient
    documents_gateway_client: DocumentsGatewayGRPCClient
    operations_gateway_client: OperationsGatewayGRPCClient

    def on_start(self) -> None:
        """
        API clients creating for a sequential scenario.
        """
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.user.environment)
        self.cards_gateway_client = build_cards_gateway_locust_grpc_client(self.user.environment)
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.user.environment)
        self.documents_gateway_client = build_documents_gateway_locust_grpc_client(self.user.environment)
        self.operations_gateway_client = build_operations_gateway_locust_grpc_client(self.user.environment)
