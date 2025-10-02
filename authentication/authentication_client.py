from clients.api_clients import APIClient

from httpx import Response
from typing import TypedDict

from clients.public_http_builder import get_public_http_client

class Token(TypedDict):
    """
    Описание структуры токена.
    """
    accessToken: str
    refreshToken: str

class LoginRequestDict(TypedDict): # TypedDict - тип данных для запроса на аутентификацию
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class LoginResponseDict(TypedDict): # TypedDict - тип данных для ответа на аутентификацию
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str

class RefreshRequestDict(TypedDict): # TypedDict - тип данных для запроса на обновление токена
    """
    Описание структуры запроса на обновление токена.
    """
    refreshToken: str  # Название ключа совпадает с API

class AuthenticationClient(APIClient):
    """
    Клиент для работы с /api/v1/authentication
    """

    def login_api(self, request: LoginRequestDict) -> Response:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/login", json=request)

    def refresh_api(self, request: RefreshRequestDict) -> Response:
        """
        Метод обновляет токен авторизации.

        :param request: Словарь с refreshToken.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/authentication/refresh", json=request)

    # Метод login_api для аутентификации пользователя
    def login(self, request: LoginRequestDict) -> LoginResponseDict:
        """
        Метод выполняет аутентификацию пользователя.

        :param request: Словарь с email и password.
        :return: Ответ от сервера в виде словаря
        """
        response = self.login_api(request) # Выполняем аутентификацию пользователя
        return response.json()

# Добавляем builder для AuthenticationClient
def get_authentication_client() -> AuthenticationClient:
    """
    Функция создаёт экземпляр AuthenticationClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию объект AuthenticationClient.
    """
    return AuthenticationClient(client=get_public_http_client())