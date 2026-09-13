from grpc import Channel, insecure_channel


def build_gateway_grpc_client() -> Channel:
    """
    Builder for creating a gRPC channel to the grpc-gateway service.

    :return: gRPC channel (Channel) configured at localhost:9003.
    """
    return insecure_channel("localhost:9003")
