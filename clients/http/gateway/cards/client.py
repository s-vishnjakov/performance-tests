from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.cards.schema import (
    IssuePhysicalCardRequestSchema,
    IssuePhysicalCardResponseSchema,
    IssueVirtualCardRequestSchema,
    IssueVirtualCardResponseSchema
)


class CardsGatewayHTTPClient(HTTPClient):
    """
    Client to interact with the /api/v1/cards endpoint of the http-gateway service.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """
        Issues a new virtual card.

        :param request: The request schema containing the user ID and the account ID.
        :return: An HTTP response from the server.
        """
        return self.post(
            "/api/v1/cards/issue-virtual-card",
            json=request.model_dump(by_alias=True )
        )

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """
        Issues a new physical card.

        :param request: The request schema containing the user ID and the account ID.
        :return: An HTTP response from the server.
        """
        return self.post(
            "/api/v1/cards/issue-physical-card",
            json=request.model_dump(by_alias=True)
        )

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        request = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        request = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Creates an instance of CardsGatewayHTTPClient with a pre-configured HTTP client.

    :return: A ready-to-use CardsGatewayHTTPClient instance.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
