from concurrent import futures
from typing import Any

import grpc

import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):

# Метод для получения информации о курсе
    def GetCourse(
        self, 
        request: course_service_pb2.GetCourseRequest, 
        context: grpc.ServicerContext
    ) -> course_service_pb2.GetCourseResponse:

        # Создаем ответ с фиксированными данными
        response = course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )
        
        return response

# Запуск сервера
def serve() -> None:
    # Создание gRPC сервера
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Регистрация нашего сервиса
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )
    
    # Настройка порта 50051
    server.add_insecure_port('[::]:50051')
    
    # Запуск сервера
    server.start()
    print("gRPC сервер запущен на порту 50051")

     # Ожидание подключений
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        print("Сервер остановлен")
        server.stop(0)


if __name__ == '__main__':
    serve()