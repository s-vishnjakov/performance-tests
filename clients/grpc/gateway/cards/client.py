from grpc import Channel
from clients.grpc.client import GRPCClient

from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub
from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse
)
from contracts.services.gateway.cards.rpc_issue_virtual_card_pb2 import (
    IssueVirtualCardRequest,
    IssueVirtualCardResponse
)


class CardsGatewayGRPCClient(GRPCClient):
    """
    gRPC client for interacting with the CardsGatewayService.
    Provides high-level methods for issuing virtual and physical cards.
    """

    def __init__(self, channel: Channel):
        """
        Initialize a client with the specified gRPC channel.

        :param channel: gRPC channel to connect to CardsGatewayService.
        """
        super().__init__(channel)

        self.stub = CardsGatewayServiceStub(channel)

    def issue_virtual_card_api(self, request: IssueVirtualCardRequest) -> IssueVirtualCardResponse:
        """
        Low-level call to the IssueVirtualCard method via gRPC.

        :param request: gRPC request with user and account IDs.
        :return: Response from the service with the issued virtual card details.
        """
        return self.stub.IssueVirtualCard(request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequest) -> IssuePhysicalCardResponse:
        """
        Low-level call to the IssuePhysicalCard method via gRPC.

        :param request: gRPC request with user and account IDs.
        :return: Response from the service with the issued physical card details.
        """
        return self.stub.IssuePhysicalCard(request)

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponse:
        """
        Issuing a new virtual card for the specified user and account.

        :param user_id: User ID.
        :param account_id: Account ID.
        :return: Response with information about the issued virtual card.
        """
        request = IssueVirtualCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_virtual_card_api(request)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponse:
        """
        Issuing a new physical card for the specified user and account.

        :param user_id: User ID.
        :param account_id: Account ID.
        :return: Response with information about the issued physical card.
        """
        request = IssuePhysicalCardRequest(user_id=user_id, account_id=account_id)
        return self.issue_physical_card_api(request)


def build_cards_gateway_grpc_client() -> CardsGatewayGRPCClient:
    """
    Builder for creating a CardsGatewayGRPCClient instance.

    :return: Initialized client for CardsGatewayService.
    """
    return CardsGatewayGRPCClient(channel=build_gateway_grpc_client())
