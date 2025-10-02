from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

# Инициализируем клиент PublicUsersClient для получения пользователя
public_users_client = get_public_users_client()

# Создаем данные для запроса на создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="12345",
    lastName="Doe",
    firstName="John",
    middleName="Doe"
)

# Выполняем запрос на создание пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Аутентификационный пользователь
authentication_user = AuthenticationUserDict( # Аутентификационный пользователь
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиенты
files_client = get_files_client(authentication_user) # Инициализируем клиент FilesClient
courses_client = get_courses_client(authentication_user) # Инициализируем клиент CoursesClient

# Создаем данные для запроса на загрузку файла
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/test_image.png"
)
# Выполняем запрос на загрузку файла
create_file_response = files_client.create_file(create_file_request) # Загружаем файл
print('Create file data:', create_file_response)

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python API Course",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
# Выполняем запрос на создание курса
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

