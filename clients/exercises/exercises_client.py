from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
    """Описание структуры упражнений."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

# Добавили описание структуры ответа на получение списка упражнений
class GetExercisesResponseDict(TypedDict):
    """Описание структуры ответа получения упражнений."""
    exercises: list[Exercise]

# Добавили описание структуры ответа на получение упражнения
class GetExerciseResponseDict(TypedDict):
    """Описание структуры ответа получения упражнения."""
    exercise: Exercise

# Добавили описание структуры ответа на создание задания
class CreateExerciseResponseDict(TypedDict):
    """Описание структуры ответа на создание задания."""
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """Описание структуры ответа на обновление задания."""
    exercise: Exercise

class GetExercisesQueryDict(TypedDict):
    """Описание структуры для параметров запроса получения упражнений."""
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """Описание структуры для параметров запроса создания задания."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """Описание структуры для параметров запроса обновления задания."""
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с API упражнений.
    """
    
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получает список упражнений с фильтрацией по курсу.
        
        :param query: Словарь с параметрами запроса для courseId
        :return: Response объект с данными упражнений
        """
        return self.get(url="/api/v1/exercises", params=query)
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает конкретное упражнение по его идентификатору.
        
        :param exercise_id: Идентификатор упражнения exercise_id        
        :return: Response объект с данными упражнения
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Создает новое задание.
        
        :param request: Словарь с title, courseId, maxScore, minScore,
            orderIndex, description, estimatedTime.
        :return: Response объект с данными задания
        """
        return self.post(url="/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Обновляет данные задания по его идентификатору.
        
        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex,
            description, estimatedTime.
        :return: Response объект с данными задания
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Удаляет задание по его идентификатору.
        
        :param exercise_id: Идентификатор задания
        :return: Response объект с данными задания
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # Добавили новый метод для получения списка упражнений
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получает список упражнений с фильтрацией по курсу.
        
        :param query: Словарь с параметрами запроса для courseId
        :return: Response объект с данными упражнений
        """
        response = self.get_exercises_api(query)
        return response.json()

    # Добавили новый метод для получения упражнения
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Получает конкретное упражнение по его идентификатору.
        
        :param exercise_id: Идентификатор упражнения exercise_id        
        :return: Response объект с данными упражнения
        """
        response = self.get_exercise_api(exercise_id)
        return response.json()

    # Добавили новый метод для создания задания
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Создает новое задание.
        
        :param request: Словарь с title, courseId, maxScore, minScore,
            orderIndex, description, estimatedTime.
        :return: Response объект с данными задания
        """
        response = self.create_exercise_api(request)
        return response.json()

    # Добавили новый метод для обновления задания
    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> UpdateExerciseResponseDict:
        """
        Обновляет данные задания по его идентификатору.
        
        :param exercise_id: Идентификатор задания
        :param request: Словарь с title, maxScore, minScore, orderIndex,
            description, estimatedTime.
        :return: Response объект с данными задания
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


# Добавляем builder для ExercisesClient
# Создает клиент с уже настроенной авторизацией пользователя
def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """
    Функция создает экземпляр ExercisesClient с аутентификацией пользователя.
    
    :param user: Объект AuthenticationUserSchema с email и паролем пользователя.
    :return: Готовый к использованию объект ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))