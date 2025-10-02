# скрипт получения пользователя из API

from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient
public_users_client = get_public_users_client() # Экземпляр клиента PublicUsersClient

# Инициализируем запрос на создание пользователя
create_user_request = CreateUserRequestDict( 
    email=get_random_email(),
    password="12345",
    firstName="John",
    lastName="Doe",
    middleName="Doe"
)

# Выполняем запрос на создание пользователя
# Используем метод create_user
create_user_response = public_users_client.create_user(create_user_request) # Отправляем запрос на создание пользователя
print('Create user data:', create_user_response)

# Инициализируем пользовательские данные для аутентификации
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'], # Получаем email из запроса на создание пользователя
    password=create_user_request['password'] # Получаем пароль из запроса на создание пользователя
)

# Инициализируем клиент PrivateUsersClient
private_users_client = get_private_users_client(authentication_user) # Экземпляр клиента PrivateUsersClient


# Выполняем GET запрос на получение данных пользователя
get_user_response = private_users_client.get_user(create_user_response['user']['id']) # Отправляем запрос на получение данных пользователя
print('Get user data:', get_user_response)