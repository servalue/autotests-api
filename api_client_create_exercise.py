from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
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
print('Create user data:', create_user_response)

# Аутентификационный пользователь
authentication_user = AuthenticationUserDict( # Аутентификационный пользователь
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем клиенты
files_client = get_files_client(authentication_user) # Инициализируем клиент FilesClient
courses_client = get_courses_client(authentication_user) # Инициализируем клиент CoursesClient
exercises_client = get_exercises_client(authentication_user) # Инициализируем клиент ExercisesClient

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
    title="Test Course",
    maxScore=100,
    minScore=10,
    description="API Test Course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'], # Идентификатор файла, который будет использоваться как превью курса
    createdByUserId=create_user_response['user']['id'] # Идентификатор пользователя, создавшего курс
)
# Выполняем запрос на создание курса
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Создаем задание
create_exercise_request = CreateExerciseRequestDict(
    title="Test Exercise",
    courseId=create_course_response['course']['id'], # Идентификатор курса, к которому будет привязано задание
    maxScore=100,
    minScore=10,
    description="API Test Exercise",
    estimatedTime="2 weeks"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request) # Выполняем запрос на создание задания
print('Create exercise data:', create_exercise_response)
