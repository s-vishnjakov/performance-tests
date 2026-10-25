import random
from pydantic import BaseModel, Field


class SeedCardResult(BaseModel):
    """
    Card generation result.

    Attributes:
        card_id (str): Unique card identifier.
    """
    card_id: str


class SeedOperationResult(BaseModel):
    """
    Operation generation result.

    Attributes:
        operation_id (str): Unique operation identifier.
    """
    operation_id: str


class SeedAccountResult(BaseModel):
    """
    Account generation result with nested entities.

    Attributes:
        account_id (str): Unique account identifier.
        physical_cards (list[SeedCardResult]): List of physical cards linked to the account.
        top_up_operations (list[SeedOperationResult]): List of top-up operations.
        purchase_operations (list[SeedOperationResult]): List of purchase operations.
    """
    account_id: str
    physical_cards: list[SeedCardResult] = Field(default_factory=list)
    top_up_operations: list[SeedOperationResult] = Field(default_factory=list)
    purchase_operations: list[SeedOperationResult] = Field(default_factory=list)


class SeedUserResult(BaseModel):
    """
    User generation result with linked accounts.

    Attributes:
        user_id (str): Unique user identifier.
        deposit_accounts (list[SeedAccountResult]): List of deposit accounts.
        savings_accounts (list[SeedAccountResult]): List of savings accounts.
        debit_card_accounts (list[SeedAccountResult]): List of debit card accounts.
        credit_card_accounts (list[SeedAccountResult]): List of credit card accounts.
    """
    user_id: str
    deposit_accounts: list[SeedAccountResult] = Field(default_factory=list)
    savings_accounts: list[SeedAccountResult] = Field(default_factory=list)
    debit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)
    credit_card_accounts: list[SeedAccountResult] = Field(default_factory=list)


class SeedsResult(BaseModel):
    """
    Main seeding result model — aggregates all created users.

    Attributes:
        users (list[SeedUserResult]): List of generated users.
    """
    users: list[SeedUserResult] = Field(default_factory=list)

    def get_next_user(self) -> SeedUserResult:
        """
        Returns and removes the first user from the list.

        Used when each virtual user needs its own new test user.
        Convenient for strictly sequential user distribution in test scenarios.

        Returns:
            SeedUserResult: The next user from the list.
        """
        return self.users.pop(0)

    def get_random_user(self) -> SeedUserResult:
        """
        Returns a random user from the list without removing it.

        Used when order does not matter and the user is picked at random.

        Returns:
            SeedUserResult: A random user.
        """
        return random.choice(self.users)
