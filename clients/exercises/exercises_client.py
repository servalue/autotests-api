from typing import TypedDict
from httpx import Response
from clients.api_clients import APIClient


class GetExercisesQueryDict(TypedDict):
    """Описание структуры для параметров запроса получения упражнений."""
    courseId: str


class ExercisesClient(APIClient):
    """
    Клиент для работы с API упражнений.
    """
    
    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Получает список упражнений с фильтрацией по курсу.
        
        :param query: Словарь с параметрами запроса, включая courseId
        :return: Response объект с данными упражнений
        """
        return self.get(url="/api/v1/exercises", params=query)
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Получает конкретное упражнение по его идентификатору.
        
        :param exercise_id: Идентификатор упражнения
        :return: Response объект с данными упражнения
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")