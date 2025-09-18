import socket # Импортируем модуль socket для работы с сокетами


def client() -> None:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем сокет
    
    server_address = ('localhost', 12345) # Адрес и порт сервера
    client_socket.connect(server_address) # Соединяемся с сервером  
    
    message = "Привет, сервер!" # Сообщение для отправки серверу
    client_socket.send(message.encode()) # Отправляем сообщение серверу
    
    response = client_socket.recv(1024).decode() # Получаем ответ от сервера
    print(f"Ответ от сервера: {response}")
    
    client_socket.close() # Закрываем соединение с сервером


if __name__ == "__main__":
    client() # Запускаем клиента