from pydantic import BaseModel, Field


class SeedCardsPlan(BaseModel):
    """
    Account's card generation plan.

    Attributes:
        count (int): Number of cards (virtual or physical) to generate.
    """
    count: int = 0


class SeedOperationsPlan(BaseModel):
    """
    Account transaction generation plan.

    Attributes:
        count (int): The number of transactions (e.g., deposits or purchases) to generate.
    """
    count: int = 0


class SeedAccountsPlan(BaseModel):
    """
    A plan for generating accounts of a single type (e.g., deposit or credit).

    Attributes:
        count (int): Number of accounts of this type.
        physical_cards (SeedCardsPlan): Plan for creating physical cards in accounts.
        top_up_operations (SeedOperationsPlan): Plan for creating top-up operations.
        purchase_operations (SeedOperationsPlan): Plan for creating purchase operations.
    """
    count: int = 0
    physical_cards: SeedCardsPlan = Field(default_factory=SeedCardsPlan)
    top_up_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)
    purchase_operations: SeedOperationsPlan = Field(default_factory=SeedOperationsPlan)


class SeedUsersPlan(BaseModel):
    """
    Plan for generating users and their different account types.

    Attributes:
        count (int): Number of users.
        deposit_accounts (SeedAccountsPlan): Deposit accounts plan.
        savings_accounts (SeedAccountsPlan): Savings accounts plan.
        debit_card_accounts (SeedAccountsPlan): Debit cards plan.
        credit_card_accounts (SeedAccountsPlan): Credit cards plan.
    """
    count: int = 0
    deposit_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    savings_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    debit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)
    credit_card_accounts: SeedAccountsPlan = Field(default_factory=SeedAccountsPlan)


class SeedsPlan(BaseModel):
    """
    The main seeding plan model.

    Attributes:
        users (SeedUsersPlan): Plan for creating users and all related structures.
    """
    users: SeedUsersPlan = Field(default_factory=SeedUsersPlan)
