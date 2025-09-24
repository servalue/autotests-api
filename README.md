# API Автотесты - Примеры протоколов взаимодействия

Учебный проект с примерами реализации различных протоколов взаимодействия на Python: gRPC, TCP, WebSocket и HTTP REST API.

## Структура проекта

### 🔌 gRPC Сервис курсов
- **Файлы**: `grpc_course_server.py`, `grpc_course_client.py`, `course_service.proto`
- **Порт**: 50051
- **Функциональность**: Сервис для получения информации о курсе по ID
- **Технологии**: gRPC, Protocol Buffers

### 🔗 TCP Сервер пользователей  
- **Файлы**: `tcp_users_server.py`, `tcp_users_client.py`
- **Порт**: 12345
- **Функциональность**: Сервер ведет историю сообщений и возвращает полную историю каждому клиенту
- **Технологии**: TCP sockets

### 🌐 WebSocket Сервер пользователей
- **Файлы**: `websocket_users_server.py`, `websocket_users_client.py` 
- **Порт**: 8765
- **Функциональность**: Эхо-сервер, отправляющий 5 нумерованных ответов на каждое сообщение
- **Технологии**: WebSockets, asyncio


### 🌍 HTTP REST API Клиенты
- **Файлы**: `httpx_get_user_me.py`, `httpx_update_user.py`
- **URL**: http://localhost:8001
- **Функциональность**: Аутентификация пользователя и получение/обновление данных профиля через REST API
- **Технологии**: httpx, JWT авторизация

### 📦 API Клиенты (Новая архитектура)
- **Директория**: `clients/`
- **Базовый клиент**: `clients/api_clients.py` - универсальный HTTP клиент
- **Клиент аутентификации**: `authentication/authentication_client.py` - методы для логина и обновления токена
- **Клиент пользователей**: `clients/users/public_users_client.py` - методы для работы с пользователями
- **Вспомогательные инструменты**: `tools/fakers.py` - генерация тестовых данных

## Запуск

### gRPC
```bash
# Сервер
python grpc_course_server.py

# Клиент (в другом терминале)
python grpc_course_client.py
```

### TCP
```bash
# Сервер
python tcp_users_server.py

# Клиент (в другом терминале)
python tcp_users_client.py
```

### WebSocket
```bash
# Сервер
python websocket_users_server.py

# Клиент (в другом терминале)  
python websocket_users_client.py
```

### HTTP REST API
```bash
# Клиент (требует запущенный API сервер на порту 8001)
python httpx_get_user_me.py
```

## Зависимости
- grpcio, grpcio-tools (для gRPC)
- websockets (для WebSocket)
- httpx (для HTTP REST API клиента)
- socket (встроенный модуль для TCP)