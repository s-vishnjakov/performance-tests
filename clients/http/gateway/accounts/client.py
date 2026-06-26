from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict


class GetAccountsQueryDict(TypedDict):
    """
    Структура данных для получения списка счетов пользователя.
    """
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    """
    Структура данных для открытия депозитного счета.
    """
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    """
    Структура данных для открытия сберегательного счета.
    """
    userId: str


class OpenDebitAccountRequestDict(TypedDict):
    """
    Структура данных для открытия дебетового счета.
    """
    userId: str


class OpenCreditAccountRequestDict(TypedDict):
    """
    Структура данных для открытия кредитного счета.
    """
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts сервиса http-gateway.
    """

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка счетов пользователя.

        :param query: Словарь с параметрами запроса, например: {'userId': '123'}.
        :return: Объект httpx.Response с данными о счетах.
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия депозитного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия сберегательного счёта.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    def open_debit_account_api(self, request: OpenDebitAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия дебетовой карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-debit-account", json=request)

    def open_credit_account_api(self, request: OpenCreditAccountRequestDict) -> Response:
        """
        Выполняет POST-запрос для открытия кредитной карты.

        :param request: Словарь с userId.
        :return: Объект httpx.Response.
        """
        return self.post("/api/v1/accounts/open-credit-account", json=request)
