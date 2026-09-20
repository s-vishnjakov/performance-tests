from typing import Any, TypedDict
from httpx import Client, URL, QueryParams, Response


# Type of extensions, that can be transmitted into request
# In ours case we only use "route" parameter, but other can be added.
class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    """
    Base HTTP API client that wraps an httpx.Client instance.

    :param client: The httpx.Client instance used to perform HTTP requests.
    """

    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            extensions: HTTPClientExtensions | None = None  # Extensions support
    ) -> Response:
        """
        Performs a GET request.

        :param url: The endpoint URL.
        :param params: The query parameters of the request (for example, ?key=value).
        :param extensions: Additional data, transmitted via HTTPX extensions.
        :return: A Response object containing the response data.
        """
        return self.client.get(url=url, params=params, extensions=extensions)  # Transmit extension into httpx.Client

    def post(self,
             url: URL | str,
             json: Any | None = None,
             extensions: HTTPClientExtensions | None = None  # Extensions support for the POST-request
    ) -> Response:
        """
        Performs a POST request.

        :param url: The endpoint URL.
        :param json: The request payload in JSON format.
        :param extensions: Additional data, transmitted via HTTPX extensions.
        :return: A Response object containing the response data.
        """
        return self.client.post(url=url, json=json, extensions=extensions)  # Transmit extension into httpx.Client


client = HTTPClient()

client.get()
