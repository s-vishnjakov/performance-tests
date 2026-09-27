from grpc import Channel, insecure_channel, intercept_channel
from clients.grpc.interceptors.locust_interceptor import LocustInterceptor
from locust.env import Environment

def build_gateway_grpc_client() -> Channel:
    """
    Builder for creating a gRPC channel to the grpc-gateway service.

    :return: gRPC channel (Channel) configured at localhost:9003.
    """
    return insecure_channel("localhost:9003")


def build_gateway_locust_grpc_client(environment: Environment) -> Channel:
    locust_interceptor = LocustInterceptor(environment=environment)
    channel = insecure_channel("localhost:9003")

    return intercept_channel(channel, locust_interceptor)
