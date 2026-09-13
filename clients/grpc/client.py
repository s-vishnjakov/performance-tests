import grpc.experimental.gevent as grpc_gevent  # Import support for gRPC threads (greenlets)

from grpc import Channel

# Initialize gevent support in gRPC.
# This is required if you're using a gevent-based framework (e.g., Locust).
# Without this initialization, gRPC will use the threading model,
# which will block greenlets and disrupt concurrency.
# Initialization allows gRPC to use a gevent-compatible implementation
# for working with sockets, timers, and I/O, even if the code is written in a synchronous style.
grpc_gevent.init_gevent()


class GRPCClient:
    """
    The gRPC Client base class.

    This class stores a common channel (Channel) for communication with the gRPC server.
    All other specific clients will inherit from it.
    """
    def __init__(self, channel: Channel):
        """
        Basic client constructor.

        :param channel: gRPC channel used to connect to the server.
                        Typically, created once and reused.
        """
        self.channel = channel
