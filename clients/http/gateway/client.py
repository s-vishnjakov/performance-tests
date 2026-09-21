import logging
from httpx import Client
from locust.env import Environment
from clients.http.event_hooks.locust_event_hook import (
    locust_request_event_hook,
    locust_response_event_hook
)


def build_gateway_http_client() -> Client:
    """
    Creates an httpx.Client instance with the base settings of the http-gateway service.

    :return: A ready-to-use httpx.Client instance.
    """
    return Client(timeout=100, base_url="http://localhost:8003")


def build_gateway_locust_http_client(environment: Environment) -> Client:
    """
    An HTTP client designed specifically for Performance testing with Locust.

    It differs from the standard client in that:
    - It adds the `locust_request_event_hook` to record the request start time,
    - It adds the `locust_response_event_hook` , which calculates metrics
    (response time, response length, etc.) and sends them to Locust via `environment.events.request`.

    Therefore, this client automatically reports statistics to the Locust for every HTTP request.

    :param environment: The Locust environment object, required for generating metric events.
    :return: An httpx.Client with hooks enabled for Performance testing.
    """
    # Suppress HTTPX INFO logs (e.g.: "HTTP Request: GET ... 200 OK")
    # This eliminates unnecessary console output during high-load tests
    logging.getLogger("httpx").setLevel(logging.WARNING)

    return Client(
        timeout=100,
        base_url="http://localhost:8003",
        event_hooks={
            "request": [locust_request_event_hook],
            "response": [locust_response_event_hook(environment)]
        }
    )
