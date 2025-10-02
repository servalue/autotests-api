"""
Этот модуль предоставляет функции для создания предварительно настроенных
httpx.Client объектов для различных сценариев использования в тестах.
"""

from httpx import Client


def get_public_http_client() -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    return Client(timeout=100, base_url="http://localhost:8001")

