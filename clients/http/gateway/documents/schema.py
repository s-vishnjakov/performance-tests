from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    """
    Document structure description.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Response structure for getting the tariff document.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Response structure for getting the contract document.
    """
    contract: DocumentSchema
