from httpx import Response
from typing import TypedDict
from clients.http.client import HTTPClient


class IssueCardDict(TypedDict):
    """
    Структура данных для создания виртуальной/физической карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """
    def issue_virtual_card_api(self, request: IssueCardDict) -> Response:
        """
        Выпуск новой виртуальной карты.

        :param request: Словарь с данными ID пользователя и ID счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardDict) -> Response:
        """
        Выпуск новой физической карты.

        :param request: Словарь с данными ID пользователя и ID счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
