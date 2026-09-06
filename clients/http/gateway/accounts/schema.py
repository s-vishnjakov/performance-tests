from pydantic import BaseModel, Field, ConfigDict
from clients.http.gateway.cards.schema import CardSchema
from enum import StrEnum


class AccountType(StrEnum):
    SAVINGS = "SAVINGS"
    DEPOSIT ="DEPOSIT"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"


class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


class AccountSchema(BaseModel):
    """
    Account structure description.
    """
    id: str
    type: AccountType
    cards: list[CardSchema]   # Nested structure: CardSchema
    status: AccountStatus
    balance: float


class GetAccountsQuerySchema(BaseModel):
    """
    Query parameters for getting the list of user accounts.
    """
    model_config = ConfigDict(validate_by_name=True)

    user_id: str = Field(alias="userId")


class GetAccountsResponseSchema(BaseModel):
    """
    Response structure for getting the list of accounts.
    """
    accounts: list[AccountSchema]


class OpenDepositAccountRequestSchema(BaseModel):
    """
    Request structure for opening a deposit account.
    """
    model_config = ConfigDict(validate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Response structure for opening a deposit account.
    """
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    Request structure for opening a savings account.
    """
    model_config = ConfigDict(validate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenSavingsAccountResponseSchema(BaseModel):
    """
    Response structure for opening a savings account.
    """
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    Request structure for opening a debit card account.
    """
    model_config = ConfigDict(validate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Response structure for opening a debit card account.
    """
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    Request structure for opening a credit card account.
    """
    model_config = ConfigDict(validate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Response structure for opening a credit card account.
    """
    account: AccountSchema