from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client, AccountsGatewayGRPCClient
from clients.grpc.gateway.cards.client import build_cards_gateway_grpc_client, CardsGatewayGRPCClient
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client, OperationsGatewayGRPCClient
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client, UsersGatewayGRPCClient
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client, AccountsGatewayHTTPClient
from clients.http.gateway.cards.client import build_cards_gateway_http_client, CardsGatewayHTTPClient
from clients.http.gateway.operations.client import build_operations_gateway_http_client, OperationsGatewayHTTPClient
from clients.http.gateway.users.client import build_users_gateway_http_client, UsersGatewayHTTPClient
from seeds.schema.plan import (
    SeedsPlan,
    SeedUsersPlan,
    SeedAccountsPlan,
)
from seeds.schema.result import (
    SeedsResult,
    SeedUserResult,
    SeedCardResult,
    SeedAccountResult,
    SeedOperationResult
)

class SeedsBuilder:
    """
    SeedsBuilder — a generator (seeder) that creates the required test or demo data
    based on the input plan. Works the same way with both HTTP and gRPC clients.

    Attributes:
        users_gateway_client: Client for working with users (HTTP or gRPC)
        cards_gateway_client: Client for issuing cards
        accounts_gateway_client: Client for opening accounts
        operations_gateway_client: Client for operations (top-ups, purchases, etc.)
    """

    def __init__(
            self,
            users_gateway_client: UsersGatewayGRPCClient | UsersGatewayHTTPClient,
            cards_gateway_client: CardsGatewayGRPCClient | CardsGatewayHTTPClient,
            accounts_gateway_client: AccountsGatewayGRPCClient | AccountsGatewayHTTPClient,
            operations_gateway_client: OperationsGatewayGRPCClient | OperationsGatewayHTTPClient
    ):
        self.users_gateway_client = users_gateway_client
        self.cards_gateway_client = cards_gateway_client
        self.accounts_gateway_client = accounts_gateway_client
        self.operations_gateway_client = operations_gateway_client

    def build_physical_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        """
        Issues a physical card for the given user and account.

        Args:
            user_id: User identifier
            account_id: Account identifier

        Returns:
            SeedCardResult: Result with the issued card ID
        """
        response = self.cards_gateway_client.issue_physical_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_top_up_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Makes a top-up operation on the card.

        Args:
            card_id: Card identifier
            account_id: Account identifier

        Returns:
            SeedOperationResult: Result with the completed operation ID
        """
        response = self.operations_gateway_client.make_top_up_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_purchase_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        """
        Makes a purchase operation with the card.

        Args:
            card_id: Card identifier
            account_id: Account identifier

        Returns:
            SeedOperationResult: Result with the completed operation ID
        """
        response = self.operations_gateway_client.make_purchase_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_savings_account_result(self, user_id: str) -> SeedAccountResult:
        """
        Opens a savings account for the user.

        Args:
            user_id: User identifier

        Returns:
            SeedAccountResult: Result with the created account ID
        """
        response = self.accounts_gateway_client.open_savings_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_deposit_account_result(self, user_id: str) -> SeedAccountResult:
        """
        Opens a deposit account for the user.

        Args:
            user_id: User identifier

        Returns:
            SeedAccountResult: Result with the created account ID
        """
        response = self.accounts_gateway_client.open_deposit_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_debit_card_account_result(self, plan: SeedAccountsPlan, user_id: str) -> SeedAccountResult:
        """
        Opens a debit card account for the user and, if needed:
        - issues physical cards
        - makes top-up operations
        - makes purchase operations

        Args:
            plan: Debit card account creation plan (number of cards, operations, etc.)
            user_id: User identifier

        Returns:
            SeedAccountResult: Result with the account ID and related entities (cards, operations)
        """
        response = self.accounts_gateway_client.open_debit_card_account(user_id=user_id)
        card_id = response.account.cards[0].id
        account_id = response.account.id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ]
        )

    def build_credit_card_account_result(self, plan: SeedAccountsPlan, user_id: str) -> SeedAccountResult:
        """
        Opens a credit card account and performs actions according to the plan:
        - issues physical cards
        - makes top-up operations
        - makes purchase operations

        Args:
            plan: Credit card account creation plan
            user_id: User identifier

        Returns:
            SeedAccountResult: Result with the account ID and operation details
        """
        response = self.accounts_gateway_client.open_credit_card_account(user_id=user_id)
        card_id = response.account.cards[0].id
        account_id = response.account.id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ]
        )

    def build_user(self, plan: SeedUsersPlan) -> SeedUserResult:
        """
        Creates a user and, according to the given plan:
        - opens savings and deposit accounts
        - creates debit and credit card accounts with cards and operations

        Args:
            plan: User generation plan

        Returns:
            SeedUserResult: Result with the user ID and all created entities
        """
        response = self.users_gateway_client.create_user()

        return SeedUserResult(
            user_id=response.user.id,
            deposit_accounts=[
                self.build_deposit_account_result(user_id=response.user.id)
                for _ in range(plan.deposit_accounts.count)
            ],
            savings_accounts=[
                self.build_savings_account_result(user_id=response.user.id)
                for _ in range(plan.savings_accounts.count)
            ],
            debit_card_accounts=[
                self.build_debit_card_account_result(plan=plan.debit_card_accounts, user_id=response.user.id)
                for _ in range(plan.debit_card_accounts.count)
            ],
            credit_card_accounts=[
                self.build_credit_card_account_result(plan=plan.credit_card_accounts, user_id=response.user.id)
                for _ in range(plan.credit_card_accounts.count)
            ]
        )

    def build(self, plan: SeedsPlan) -> SeedsResult:
        """
        Generates the full data structure based on the plan:
        - creates the specified number of users
        - assigns accounts, cards and operations to each user

        Args:
            plan: Full data generation plan

        Returns:
            SeedsResult: Result with the data of all created users
        """
        return SeedsResult(users=[self.build_user(plan=plan.users) for _ in range(plan.users.count)])

def build_grpc_seeds_builder() -> SeedsBuilder:
    """
    Factory for creating a seeder that uses gRPC clients.

    Returns:
        SeedsBuilder: Initialized seeder with gRPC clients
    """
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_grpc_client(),
        cards_gateway_client=build_cards_gateway_grpc_client(),
        accounts_gateway_client=build_accounts_gateway_grpc_client(),
        operations_gateway_client=build_operations_gateway_grpc_client()
    )

def build_http_seeds_builder():
    """
    Factory for creating a seeder that uses HTTP clients.

    Returns:
        SeedsBuilder: Initialized seeder with HTTP clients
    """
    return SeedsBuilder(
        users_gateway_client=build_users_gateway_http_client(),
        cards_gateway_client=build_cards_gateway_http_client(),
        accounts_gateway_client=build_accounts_gateway_http_client(),
        operations_gateway_client=build_operations_gateway_http_client()
    )
