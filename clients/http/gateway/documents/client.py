from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.documents.schema import (
    GetContractDocumentResponseSchema,
    GetTariffDocumentResponseSchema
)


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with the /api/v1/documents endpoint of the http-gateway service.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Retrieves the tariff document of the specified account.

        :param account_id: The unique identifier of the account.
        :return: An HTTP response from the server.
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Retrieves the contract document of the specified account.

        :param account_id: The unique identifier of the account.
        :return: An HTTP response from the server.
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseSchema:
        response = self.get_tariff_document_api(account_id)
        return GetTariffDocumentResponseSchema.model_validate_json(response.text)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseSchema:
        response = self.get_contract_document_api(account_id)
        return GetContractDocumentResponseSchema.model_validate_json(response.text)


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Creates an instance of DocumentsGatewayHTTPClient with a pre-configured HTTP client.

    :return: A ready-to-use DocumentsGatewayHTTPClient instance.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
