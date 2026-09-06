from httpx import Client


def build_gateway_http_client() -> Client:
    """
    Creates an httpx.Client instance with the base settings of the http-gateway service.

    :return: A ready-to-use httpx.Client instance.
    """
    return Client(timeout=100, base_url="http://localhost:8003")
