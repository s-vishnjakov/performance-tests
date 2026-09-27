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
    """
    Builder for creating a gRPC channel adapted for the Locust.
    The channel automatically includes a LocustInterceptor,
    which logs calls in the Locust metrics system.

    :param environment: Locust runtime environment (required for sending events).
    :return: A gRPC channel with an interceptor, suitable for performance testing.
    """

    # Create an interceptor instance, pass the Locust environment to it
    locust_interceptor = LocustInterceptor(environment=environment)
    # Create a regular channel
    channel = insecure_channel("localhost:9003")
    # Wrap the channel with an interceptor so that all requests pass through it
    return intercept_channel(channel, locust_interceptor)
