import time
from locust.env import Environment
from httpx import Request, Response, HTTPError, HTTPStatusError


def locust_request_event_hook(request: Request) -> None:
    """
    HTTPX event hook called before sending a request.

    Stores the current time in `request.extensions["start_time"]`
    it can be used later to calculate response time.
    """
    request.extensions["start_time"] = time.time()


def locust_response_event_hook(environment: Environment):
    """
    Returns an HTTPX event hook called upon receiving a response.

    Uses `request.extensions["start_time"]` to calculate response time.
    Extracts route from `request.extensions["route"]`, if specified.
    Sends collected metrics to `environment.events.request` so Locust can aggregate statistics.

    :param environment: The Locust environment object through which metrics are sent.
    :return: Hook function for HTTPX response event hook.
    """
    def inner(response: Response) -> None:
        # Check for error status (e.g. 500, 404, etc.)
        exception: HTTPError | HTTPStatusError | None = None
        try:
            response = response.raise_for_status()
        except (HTTPError, HTTPStatusError) as error:
            exception = error

        request = response.request

        # Getting the route if it was specified via extensions, otherwise using raw path
        route = request.extensions.get("route", request.url.path)
        start_time = request.extensions.get("start_time", time.time())
        response_time = (time.time() - start_time) * 1000
        # Determine the size of the response in bytes (can be skipped)
        response_length = len(response.read())

        environment.events.request.fire(
            name=f"{request.method} {route}",
            context=None,  # Context can be used for extensions (optional)
            response=response,
            exception=exception,
            request_type="HTTP",
            response_time=response_time,
            response_length=response_length
        )

    return inner
