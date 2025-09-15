import grpc

import course_service_pb2
import course_service_pb2_grpc


# Запуск клиента
def run_client() -> None:
    # Создаем соединение с сервером
    with grpc.insecure_channel('localhost:50051') as channel:
        # Создаем клиент (stub)
        stub = course_service_pb2_grpc.CourseServiceStub(channel)
        
        # Формируем запрос
        request = course_service_pb2.GetCourseRequest(course_id="api-course")
        
        # Вызываем метод GetCourse
        response = stub.GetCourse(request)
        
        # Выводим ответ в консоль
        print(response)


if __name__ == '__main__':
    run_client()