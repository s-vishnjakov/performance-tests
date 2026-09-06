from typing import Any
from httpx import Client, URL, QueryParams, Response


class HTTPClient:
    """
    Base HTTP API client that wraps an httpx.Client instance.

    :param client: The httpx.Client instance used to perform HTTP requests.
    """
    def __init__(self, client: Client):
        self.client = client

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Performs a GET request.

        :param url: The endpoint URL.
        :param params: The query parameters of the request (for example, ?key=value).
        :return: A Response object containing the response data.
        """
        return self.client.get(url, params=params)

    def post(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Performs a POST request.

        :param url: The endpoint URL.
        :param json: The request payload in JSON format.
        :return: A Response object containing the response data.
        """
        return self.client.post(url, json=json)
