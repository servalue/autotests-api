import httpx

# Данные для входа
login_payload = {
    "email": "devsergei@gmail.com",
    "password": "12345"
}

# Выполняем POST запрос на логин к эндпоинту /api/v1/authentication/login
login_response = httpx.post(url="http://localhost:8001/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Status Code:", login_response.status_code) # Статус код ответа
print("Login response:", login_response_data) # Ответ от сервера

# Извлекаем access token из ответа логина
access_token = login_response_data['token']['accessToken']
# Заголовки для авторизации
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Выполняем GET-запрос к эндпоинту /api/v1/users/me
get_user_response = httpx.get(url="http://localhost:8001/api/v1/users/me", headers=headers)
get_user_response_data = get_user_response.json()   
print("Status Code:", get_user_response.status_code) # Статус код ответа
print("Get user response:", get_user_response_data) # JSON-ответ с данными пользователя
