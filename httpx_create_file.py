import httpx

from tools.fakers import get_random_email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "test",
    "firstName": "Test",
    "lastName": "Test",
    "middleName": "Test"
}

create_user_response = httpx.post("http://localhost:8001/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload["email"],
    "password": "test"
}

login_response = httpx.post("http://localhost:8001/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

token = login_response_data["token"]["accessToken"]

# Выполняем загрузку файла
create_file_headers = {
    "Authorization": f"Bearer {token}"
}

create_file_payload = {
    "upload_file": open('./testdata/files/test_image.png', 'rb')
}

create_file_response = httpx.post(
"http://localhost:8001/api/v1/files",
data={"filename": "test_image.png", "directory": "courses"},
files=create_file_payload,
headers=create_file_headers
)
create_file_response_data = create_file_response.json()
print('Create file data:', create_file_response_data)