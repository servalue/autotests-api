from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

# Добавили описание структуры файла
class File(TypedDict):
    """
    Описание структуры файла.
    """
    id: str
    url: str
    file_name: str
    directory: str


class CreateFileRequestDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str

# Добавили описание структуры запроса на создание файла
class CreateFileResponseDict(TypedDict):
    """
    Описание структуры ответа на создание файла.
    """
    file: File


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self, file_id: str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        with open(request["upload_file"], "rb") as file:
            return self.post(
                "/api/v1/files",
                data=request,
                files={"upload_file": file}
            )


    def delete_file_api(self, file_id: str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/files/{file_id}")

    # Добавили новый метод
    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Словарь с данными созданного файла.
        """
        response = self.create_file_api(request) # Выполняем запрос на создание файла   
        return response.json()

# Добавляем builder для FilesClient
def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """
    Функция создаёт экземпляр FilesClient с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект FilesClient.
    """
    return FilesClient(client=get_private_http_client(user)) # Передаем экземпляр httpx.Client с аутентификацией пользователя