from pydantic import BaseModel, Field, ConfigDict, EmailStr
from pydantic.alias_generators import to_camel
import uuid

class UserSchema(BaseModel):
    """
    Модель данных пользователя.
    Используется для представления пользователя в API ответах.
    """
    # Использование default_factory для генерации уникального идентификатора пользователя
    id: str = Field(default_factory=lambda: str(uuid.uuid4()),description="Уникальный идентификатор пользователя") 
    email: EmailStr = Field(description="Email адрес пользователя")
    last_name: str = Field(alias="lastName", description="Фамилия пользователя")
    first_name: str = Field(alias="firstName", description="Имя пользователя")
    middle_name: str = Field(alias="middleName", description="Отчество пользователя")
    

class CreateUserRequestSchema(BaseModel):
    """
    Модель данных для создания пользователя.
    Используется для валидации данных при создании нового пользователя.
    """
    email: EmailStr = Field(description="Email адрес пользователя")
    password: str = Field(description="Пароль пользователя")
    last_name: str = Field(alias="lastName", description="Фамилия пользователя")
    first_name: str = Field(alias="firstName", description="Имя пользователя")
    middle_name: str = Field(alias="middleName", description="Отчество пользователя")
    
class CreateUserResponseSchema(BaseModel):
    """
    Модель данных для создания пользователя.
    Содержит данные созданного пользователя.
    """
    user: CreateUserRequestSchema


# Пример создания пользователя
create_user_request = CreateUserRequestSchema(
    email="test@example.com",
    password="12345",
    lastName="Test",
    firstName="QA",
    middleName="Test"
)
create_user_response = CreateUserResponseSchema(user=create_user_request)
# Выводим ответ в формате JSON с отступами и использованием alias_generator для преобразования snake_case в camelCase
print(f"Create user response:\n {create_user_response.model_dump_json(indent=2,by_alias=True)}")

    