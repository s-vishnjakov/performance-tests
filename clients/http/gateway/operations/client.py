from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения информации по операциям счета.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Структура данных для проведения операций по счету.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для проведения операции покупки по счету.
    Расширяет базовый класс MakeOperationRequestDict, добавляя информацию о категории покупки.
    """
    category: str


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка ВСЕХ операций по счету.

        :param query: Словарь с параметрами запроса, например: {'accountId': 'uuid'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': 'uuid'}.
        :return: Объект httpx.Response с данными об операциях.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response со ссылкой на документ и именем документа.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение информации об ОДНОЙ операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными об операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def make_fee_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции кэшбека.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции перевода.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        Создание операции покупки.

        :param request: Словарь с данными: status, amount, cardId, accountId, +category.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)


def build_cards_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
