from typing import TypedDict

from httpx import Client

from authentication.authentication_client import get_authentication_client, LoginRequestDict

class AuthenticationUserDict(TypedDict):
    """
    Описание структуры пользователя для аутентификации.
    """
    email: str
    password: str


# Создаем private builder
def get_private_http_client(user: AuthenticationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект httpx.Client с установленным заголовком Authorization.
    """
    # Инициализируем AuthenticationClient для аутентификации
    authentication_client = get_authentication_client()

    # Инициализируем запрос на аутентификацию
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    # Выполняем POST запрос и аутентифицируемся
    login_response = authentication_client.login(login_request)

    return Client(
        timeout=100,
        base_url="http://localhost:8001",
        # Добавляем заголовок авторизации
        headers={"Authorization": f"Bearer {login_response['token']['accessToken']}"}
    )