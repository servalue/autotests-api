import httpx

from tools.fakers import get_random_email



# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
# Создаем пользователя POST
create_user_response = httpx.post("http://localhost:8001/api/v1/users", json=create_user_payload)
# Получаем данные после создания пользователя
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
# Проходим аутентификацию POST  
login_response = httpx.post("http://localhost:8001/api/v1/authentication/login", json=login_payload)
# Получаем данные после аутентификации
login_response_data = login_response.json()
print('Login data:', login_response_data)

# Получаем токен
auth_token = login_response_data['token']['accessToken']

# Обновляем данные пользователя
patch_user_payload = {
    "email": get_random_email(),
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
# Устанавливаем заголовок авторизации PATCH
patch_user_headers = {
    "Authorization": f"Bearer {auth_token}"
}
# Метод PATCH, Обновляем данные пользователя
patch_user_response = httpx.patch(
    f"http://localhost:8001/api/v1/users/{create_user_response_data['user']['id']}",
    json=patch_user_payload,
    headers=patch_user_headers
    )
# Получаем данные пользователя после обновления
patch_user_response_data = patch_user_response.json()
print('Patch user data:', patch_user_response_data)