from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class IssueCardRequestDict(TypedDict):
    """
    Структура данных для создания виртуальной/физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """
    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск новой виртуальной карты.

        :param request: Словарь с данными ID пользователя и ID счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Выпуск новой физической карты.

        :param request: Словарь с данными ID пользователя и ID счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient.
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())
