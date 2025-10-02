# API Автотесты - Модульная архитектура клиентов

Учебный проект с примерами реализации различных протоколов взаимодействия на Python: gRPC, TCP, WebSocket и HTTP REST API с модульной архитектурой API клиентов.

## Структура проекта

### 🏗️ Модульная архитектура API клиентов
- **Базовый клиент**: `clients/api_clients.py` - базовый HTTP клиент на основе httpx
- **Публичные клиенты**: `clients/users/public_users_client.py` - для неавторизованных операций
- **Приватные клиенты**: `clients/users/private_users_client.py` - для авторизованных операций
- **Специализированные клиенты**: 
  - `clients/courses/courses_client.py` - работа с курсами
  - `clients/files/files_client.py` - работа с файлами
  - `clients/exercises/exercises_client.py` - работа с упражнениями
  - `authentication/authentication_client.py` - аутентификация

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
- **URL**: http://localhost:8001
- **Функциональность**: 
  - Создание пользователей (публичный API)
  - Аутентификация и работа с профилем (приватный API)
  - Управление курсами и файлами
  - Загрузка и обработка файлов
- **Технологии**: httpx, JWT авторизация, модульная архитектура

## Примеры использования

### Создание пользователя и получение данных
```bash
python api_client_get_user.py
```

### Создание курса с файлом
```bash
python api_client_create_course.py
```

### Простые HTTP примеры
```bash
python httpx_get_user_me.py
python httpx_update_user.py
python httpx_create_file.py
```

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
# Требует запущенный API сервер на порту 8001
python api_client_get_user.py
python api_client_create_course.py
```

## Архитектура API клиентов

### Базовый APIClient
- Обертка над httpx.Client
- Поддержка GET, POST, PATCH, DELETE методов
- Типизация с помощью TypedDict
- Документирование через docstring

### Специализированные клиенты
- **PublicUsersClient**: Создание пользователей без авторизации
- **PrivateUsersClient**: Работа с пользователями после авторизации
- **AuthenticationClient**: Аутентификация и обновление токенов
- **CoursesClient**: Управление курсами
- **FilesClient**: Загрузка и управление файлами

### HTTP Builders
- **PublicHttpBuilder**: Создание клиентов для публичных API
- **PrivateHttpBuilder**: Создание клиентов с авторизацией

## Тестирование
```bash
# Запуск всех тестов
pytest

# Запуск конкретных тестов
pytest tests/test_files_client.py
pytest tests/test_api_client_create_course.py
```

## Зависимости
- grpcio, grpcio-tools (для gRPC)
- websockets (для WebSocket)
- httpx (для HTTP REST API клиентов)
- faker (для генерации тестовых данных)
- pytest, pytest-mock (для тестирования)
- socket (встроенный модуль для TCP)

## Структура файлов
```
├── clients/                    # API клиенты
│   ├── api_clients.py         # Базовый HTTP клиент
│   ├── public_http_builder.py # Фабрика публичных клиентов
│   ├── private_http_builder.py # Фабрика приватных клиентов
│   ├── users/                 # Клиенты пользователей
│   ├── courses/               # Клиенты курсов
│   ├── files/                 # Клиенты файлов
│   └── exercises/             # Клиенты упражнений
├── authentication/            # Аутентификация
├── tools/                     # Утилиты (faker)
├── tests/                     # Тесты
└── testdata/                  # Тестовые данные
```