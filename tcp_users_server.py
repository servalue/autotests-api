import socket # Импортируем модуль socket для работы с сокетами

# Список для хранения всех сообщений
messages_history = []


def server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем сокет
    
    server_address = ('localhost', 12345) # Адрес и порт сервера
    server_socket.bind(server_address) # Привязываем сокет к адресу и порту
    
    server_socket.listen(10) # Начинаем прослушивание
    print("Сервер запущен и ждет подключений...")
    
    while True:
        client_socket, client_address = server_socket.accept() # Принимаем соединение
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        
        data = client_socket.recv(1024).decode() # Получаем данные от клиента
        print(f"Пользователь с адресом: {client_address} отправил сообщение: {data}")
        
        # Добавляем сообщение в историю
        messages_history.append(data)
        
        # Формируем ответ - всю историю сообщений, каждое с новой строки
        response = "\n".join(messages_history)
        client_socket.send(response.encode()) # Отправляем всю историю клиенту

        # Закрываем соединение с клиентом
        client_socket.close()


if __name__ == "__main__":
    server() # Запускаем сервер