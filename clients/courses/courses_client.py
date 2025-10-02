from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.files.files_client import File
from clients.users.private_users_client import User


# Добавили описание структуры курса
class Course(TypedDict):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File  # Вложенная структура файла
    estimatedTime: str
    createdByUser: User  # Вложенная структура пользователя

class GetCoursesQueryDict(TypedDict):
    """Описание структуры для параметров запроса получения курсов."""
    userId: str

class CreateCourseRequestDict(TypedDict):
    """Описание структуры для параметров запроса создания курса."""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str

# Добавили описание структуры запроса на создание курса
class CreateCourseResponseDict(TypedDict):
    """Описание структуры для параметров запроса создания курса."""
    course: Course

class UpdateCourseRequestDict(TypedDict):
    """Описание структуры для параметров запроса обновления курса."""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


class CoursesClient(APIClient):
    """Клиент для работы с API курсов."""
    
    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """
        Получает список курсов с фильтрацией по пользователю.
        
        :param query: Словарь с параметрами запроса для userId
        :return: Response объект с данными курсов
        """
        return self.get(url="/api/v1/courses", params=query)
    
    def get_course_api(self, course_id: str) -> Response:
        """
        Получает конкретный курс по его идентификатору.
        
        :param course_id: Идентификатор курса course_id
        :return: Response объект с данными курса
        """
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """
        Создает новый курс.
        
        :param request: Словарь с title, maxScore, minScore, description,
            estimatedTime, previewFileId, createdByUserId для создания курса
        :return: Response объект с данными курса
        """
        return self.post(url="/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """
        Обновляет курс по его идентификатору.
        
        :param course_id: Идентификатор курса course_id
        :param request: Словарь с title, maxScore, minScore, description,
            estimatedTime для обновления курса
        :return: Response объект с данными курса
        """
        return self.put(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """
        Удаляет курс по его идентификатору.
        
        :param course_id: Идентификатор курса course_id
        :return: Response виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/courses/{course_id}")

     # Добавили новый метод
    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        """
        Создает новый курс.
        
        :param request: Словарь с title, maxScore, minScore, description,
            estimatedTime, previewFileId, createdByUserId для создания курса
        """
        response = self.create_course_api(request)
        return response.json()

# Добавляем builder для CoursesClient
def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """
    Функция создаёт экземпляр CoursesClient с аутентификацией пользователя.

    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект CoursesClient.
    """
    return CoursesClient(client=get_private_http_client(user)) # Передаем экземпляр httpx.Client с аутентификацией пользователя