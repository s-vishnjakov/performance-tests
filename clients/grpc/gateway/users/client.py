from grpc import Channel
from clients.grpc.client import GRPCClient

from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.rpc_get_user_pb2 import GetUserRequest, GetUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from tools.fakers import fake


class UsersGatewayGRPCClient(GRPCClient):
    """
    gRPC client for interacting with the UsersGatewayService.
    Provides high-level methods for getting and creating users.
    """
    def __init__(self, channel: Channel):
        """
        Initialize a client with the specified gRPC channel.

        :param channel: gRPC channel to connect to UsersGatewayService.
        """
        super().__init__(channel)

        self.stub = UsersGatewayServiceStub(channel)

    def get_user_api(self, request: GetUserRequest) -> GetUserResponse:
        """
        Low-level call to the GetUser method via gRPC.

        :param request: gRPC request with user ID.
        :return: Response from the service with user data.
        """
        return self.stub.GetUser(request)

    def create_user_api(self, request: CreateUserRequest) -> CreateUserResponse:
        """
        Low-level call to the CreateUser method via gRPC.

        :param request: gRPC request with the new user's details.
        :return: Response from the service with the created user's details.
        """
        return self.stub.CreateUser(request)

    def get_user(self, user_id: str) -> GetUserResponse:
        """
        Getting user data by ID.

        :param user_id: User ID.
        :return: Response with user information.
        """
        request = GetUserRequest(id=user_id)
        return self.get_user_api(request)

    def create_user(self) -> CreateUserResponse:
        """
        Creating a new user with fake credentials.

        :return: Response with information about the created user.
        """
        request = CreateUserRequest(
            email=fake.email(),
            first_name=fake.first_name(),
            middle_name=fake.middle_name(),
            last_name=fake.last_name(),
            phone_number=fake.phone_number()
        )
        return self.create_user_api(request)


def build_users_gateway_grpc_client() -> UsersGatewayGRPCClient:
    """
    Builder for creating a UsersGatewayGRPCClient instance.

    :return: Initialized client for UsersGatewayService.
    """
    return UsersGatewayGRPCClient(client=build_gateway_grpc_client())
