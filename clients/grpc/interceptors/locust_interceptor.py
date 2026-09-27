import time
from grpc import UnaryUnaryClientInterceptor, RpcError
from locust.env import Environment


class LocustInterceptor(UnaryUnaryClientInterceptor):
    """
    gRPC interceptor for collecting Locust metrics.
    Used to measure call execution time and log success/errors.
    """
    def __init__(self, environment: Environment):
        """
        :param environment: The Locust environment instance containing metric collection events.
        """
        self.environment = environment

    def intercept_unary_unary(self, continuation, client_call_details, request):
        """
        Interceptor method for unary-unary gRPC calls.

        :param continuation: Function that calls the actual gRPC method.
        :param client_call_details: Request details (method, metadata, timeout, etc.).
        :param request: Request object sent to the server.
        :return: gRPC response (future object).
        """
        response = None
        exception: RpcError | None = None
        start_time = time.perf_counter()
        response_length = 0

        try:
            response = continuation(client_call_details, request)
            response_length = response.result().ByteSize()
        except RpcError as error:
            exception = error

        # Call register in the Locust metrics system
        self.environment.events.request.fire(
            name=client_call_details.method,
            context=None,  # Context can be used for extensions (optional)
            response=response,
            exception=exception,
            request_type="gRPC",
            response_time=(time.perf_counter() - start_time) * 1000,
            response_length=response_length
        )

        return response
