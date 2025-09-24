from httpx import Response
from typing import TypedDict

import clients.api_clients as api_clients

class PublicUsersRequestDict(TypedDict): # TypedDict - тип данных для запроса на получение пользователей
    """
    Описание структуры запроса на получение пользователей.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(api_clients.APIClient):
    """
    Клиент для работы с публичными методами пользователей /api/v1/users
    """

    def create_user_api(self, request: PublicUsersRequestDict) -> Response:
        """
        Метод создает нового пользователя в системе.

        :param request: Словарь с данными пользователя (email, password, firstName, lastName, middleName).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)