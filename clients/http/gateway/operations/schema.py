from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Financial operation structure description.
    """
    model_config = ConfigDict(validate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: datetime = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationsSummarySchema(BaseModel):
    """
    Operations statistics structure description.
    """
    model_config = ConfigDict(validate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class OperationReceiptSchema(BaseModel):
    """
    Operation receipt structure description.
    """
    url: HttpUrl
    document: str


class GetOperationResponseSchema(BaseModel):
    """
    Response structure for getting a single operation.
    """
    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Query parameters for getting the list of account operations.
    """
    model_config = ConfigDict(validate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Response structure for getting the list of operations.
    """
    operations: list[OperationSchema]


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Query parameters for getting the account operations statistics.
    """
    model_config = ConfigDict(validate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Response structure for getting the operations` statistics.
    """
    summary: OperationsSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Response structure for getting the operation receipt.
    """
    receipt: OperationReceiptSchema


class MakeOperationRequestSchema(BaseModel):
    """
    Base request structure for making a financial operation.
    """
    model_config = ConfigDict(validate_by_name=True)

    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a fee operation.
    """
    pass


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Response structure for making a fee operation.
    """
    operation: OperationSchema


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a top up operation.
    """
    pass


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Response structure for making a top up operation.
    """
    operation: OperationSchema


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a cashback operation.
    """
    pass


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Response structure for making a cashback operation.
    """
    operation: OperationSchema


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a transfer operation.
    """
    pass


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Response structure for making a transfer operation.
    """
    operation: OperationSchema


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a purchase operation.
    Extends the base request with the purchase category.
    """
    category: str


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Response structure for making a purchase operation.
    """
    operation: OperationSchema


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a bill payment operation.
    """
    pass


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Response structure for making a bill payment operation.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Request structure for making a cash withdrawal operation.
    """
    pass


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Response structure for making a cash withdrawal operation.
    """
    operation: OperationSchema
