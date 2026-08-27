from clients.http.client import HTTPClient
from httpx import Response, QueryParams
from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Структура финансовой операции.
    """
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения списка операций по счёту.
    """
    accountId: str



class GetOperationsResponseDict(TypedDict):
    """Структура списка операций."""
    operations: list[OperationDict]


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура query параметров запроса для получения статистики по операциям счёта.
    """
    accountId: str


class OperationsSummaryDict(TypedDict):
    """
    Описание структуры статистики по операции.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа по статистике операции.
    """
    summary: OperationsSummaryDict


class OperationReceiptDict(TypedDict):
    """
    Структура получения квитанции по операции.
    """
    url: str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    """Структура ответа по запросу квитанции."""
    receipt: OperationReceiptDict


class GetOperationResponseDict(TypedDict):
    """Описание структуры данных по операции."""
    operation: OperationDict


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура тела запроса для создания финансовой операции.
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """Структура запроса для создания операции комиссии."""
    pass


class MakeFeeOperationResponseDict(TypedDict):
    """Структура ответа по операции комиссии"""
    operation: OperationDict


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """Структура запроса для создания операции пополнения."""
    pass


class MakeTopUpOperationResponseDict(TypedDict):
    """Структура ответа по операции пополнения счёта"""
    operation: OperationDict

class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """Структура запроса для создания операции кэшбэка."""
    pass


class MakeCashbackOperationResponseDict(TypedDict):
    """Структура ответа по операции кэшбека"""
    operation: OperationDict


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """Структура запроса для создания операции перевода."""
    pass


class MakeTransferOperationResponseDict(TypedDict):
    """Структура ответа по операции перевода"""
    operation: OperationDict


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура запроса для проведения операции покупки.
    Расширяет базовый класс MakeOperationRequestDict, добавляя информацию о категории покупки.
    """
    category: str


class MakePurchaseOperationResponseDict(TypedDict):
    """Структура ответа по операции покупки"""
    operation: OperationDict


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """Структура запроса для создания операции оплаты по счёту."""
    pass


class MakeBillPaymentOperationResponseDict(TypedDict):
    """Структура ответа по операции оплаты по счёту"""
    operation: OperationDict


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """Структура запроса для создания операции снятия наличных."""
    pass


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Структура ответа по операции снятия наличных"""
    operation: OperationDict


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

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        Создание операции комиссии.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        Создание операции пополнения.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        Создание операции кэшбека.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
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

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Создание операции снятия наличных.

        :param request: Словарь с данными: status, amount, cardId, accountId.
        :return: Объект httpx.Response с данными о проведенной операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получение списка ВСЕХ операций
        :param account_id: ID счёта
        :return: Объект httpx.Response со списком ВСЕХ операций
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получение статистики по операциям
        :param account_id: ID счёта
        :return: Объект httpx.Response со статистикой операций по счёту
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получение квитанции по операции
        :param operation_id: ID операции
        :return: Объект httpx.Response с данными квитанции
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получение данных по операции
        :param operation_id: ID операции
        :return: Объект httpx.Response с данными по операции
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Проведение операции комиссии

        :param card_id: ID карты
        :param account_id: ID счёта
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Проведение операции пополнения счёта

        :param card_id: ID карты
        :param account_id: ID счёта
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1500.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Проведение операции кэшбека

        :param card_id: ID карты
        :param account_id: ID счёта
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=28.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Проведение операции перевода

        :param card_id: ID карты
        :param account_id: ID счёта
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=350.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str, category: str) -> MakePurchaseOperationResponseDict:
        """
        Проведение операции покупки

        :param card_id: ID карты
        :param account_id: ID счёта
        :param category: категория операции покупки
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=99.98,
            cardId=card_id,
            accountId=account_id,
            category=category
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment__operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Проведение операции оплаты счёта

        :param card_id: ID карты
        :param account_id: ID счёта
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=128.50,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Проведение операции снятия наличных

        :param card_id: ID карты
        :param account_id: ID счёта
        :return: JSON объект с данными о проведенной операции.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=1000.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
