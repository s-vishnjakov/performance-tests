import time

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserResponseSchema,
    CreateUserRequestSchema
)


class UsersGatewayHTTPClient(HTTPClient):
    """
    Client to interact with the /api/v1/users endpoint of the http-gateway service.
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Retrieves user data by the specified user ID.

        :param user_id: The unique identifier of the user.
        :return: An HTTP response containing the user data.
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Creates a new user.

        :param request: The request schema containing the new user data.
        :return: An HTTP response from the server.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Retrieves user data by the specified user ID and returns it as a validated schema object.

        :param user_id: The unique identifier of the user.
        :return: A validated GetUserResponseSchema object containing the user data.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)


    def create_user(self) -> CreateUserResponseSchema:
        """
        Creates a new user and returns the response as a validated schema object.

        :return: A validated CreateUserResponseSchema object containing the created user data.
        """
        request = CreateUserRequestSchema(
            email=f"user.{time.time()}@example.com",
            last_name="string",
            first_name="string",
            middle_name="string",
            phone_number="string"
        )
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Builds and returns an instance of UsersGatewayHTTPClient with a pre-configured HTTP client.

    :return: A ready-to-use UsersGatewayHTTPClient instance.
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
