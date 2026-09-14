from grpc import Channel
from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (
    GetTariffDocumentRequest,
    GetTariffDocumentResponse
)
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (
    GetContractDocumentRequest,
    GetContractDocumentResponse
)

class DocumentsGatewayGRPCClient(GRPCClient):
    """
    gRPC client for interacting with the DocumentsGatewayService.
    Provides high-level methods to interact with documents.
    """

    def __init__(self, channel: Channel):
        """
        Initialize a client with the specified gRPC channel.

        :param channel: gRPC-channel to connect to the DocumentsGatewayService.
        """
        super().__init__(channel)

        self.stub = DocumentsGatewayServiceStub(channel)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> GetTariffDocumentResponse:
        """
        Low-level call to the GetTariffDocument method via gRPC.

        :param request: gRPC request with account ID.
        :return: Response from the service with tariff documents` data.
        """
        return self.stub.GetTariffDocument(request)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        """
        Low-level call to the GetContractDocument method via gRPC.

        :param request: gRPC request with account ID.
        :return: Response from the service with contract documents` data.
        """
        return self.stub.GetContractDocument(request)

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponse:
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponse:
        request = GetContractDocumentRequest(account_id=account_id)
        return self.get_contract_document_api(request)


def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    """
    Builder for creating a DocumentsGatewayGRPCClient instance.

    :return: Initialized client for DocumentsGatewayService.
    """
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())
