from typing import TypedDict

from httpx import Response

from clients.api_clients import APIClient


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