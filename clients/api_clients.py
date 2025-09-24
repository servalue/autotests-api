from httpx import Client, URL, QueryParams, Response, RequestData, RequestFiles
from typing import Any


class APIClient:
    # конструктор класса
    def __init__(
        self,  # self - экземпляр класса
        client: Client # экземпляр httpx клиента
        ) -> None:
        """
        Базовый API клиент, принимающий объект httpx.Client.
        
        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """
        self.client = client  # Сохраняем экземпляр httpx клиента

    # GET запрос с опциональными параметрами
    def get(
        self, 
        url: URL | str,  # URL запроса
        params: QueryParams | None = None # параметры запроса
        ) -> Response:
        """
        Выполняет GET-запрос.
        
        :param url: URL-адрес эндпоинта.
        :param params: GET-параметры запроса (например, ?key=value).
        :return: Объект Response с данными ответа.
        """
        return self.client.get(url, params=params) 

    # POST запрос с опциональными параметрами
    def post(
        self,
        url: URL | str,  # URL запроса
        json: Any | None = None,  # JSON данные для тела запроса
        data: RequestData | None = None,  # Form данные для тела запроса
        files: RequestFiles | None = None,  # Файлы для загрузки
    ) -> Response:
        """
        Выполняет POST-запрос.
        
        :param url: URL-адрес эндпоинта.
        :param json: Данные в формате JSON.
        :param data: Форматированные данные формы (например, application/x-www-form-urlencoded).
        :param files: Файлы для загрузки на сервер.
        :return: Объект Response с данными ответа.
        """
        return self.client.post(url, json=json, data=data, files=files) 

    # PATCH запрос с опциональными параметрами
    def patch(
        self,
        url: URL | str, # URL запроса
        json: Any | None = None,  # JSON данные для обновления
    ) -> Response:
        """
        Выполняет PATCH-запрос (частичное обновление данных).

        :param url: URL-адрес эндпоинта.
        :param json: Данные для обновления в формате JSON.
        :return: Объект Response с данными ответа.
        """
        return self.client.patch(url, json=json)

    # DELETE запрос для удаления ресурса
    def delete(
        self, 
        url: URL | str # URL запроса
        ) -> Response:
        """
        Выполняет DELETE-запрос (удаление данных).

        :param url: URL-адрес эндпоинта.
        :return: Объект Response с данными ответа.
        """
        return self.client.delete(url) 