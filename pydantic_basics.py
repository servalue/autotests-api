from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel

import json
import os


# Модель для курса
class CourseSchema(BaseModel):
    # Использование alias_generator для автоматического преобразования
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimatedTime: str


# Инициализируем модель CourseSchema через конструктор класса
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)
print('Course default model:', course_default_model)
print('-' * 60)


# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)
print('Course dict model dump:', course_dict_model.model_dump(by_alias=True))
print('-' * 60)


# Инициализируем модель CourseSchema через распаковку JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course json model:', course_json_model)
print('-' * 60)


# Инициализируем модель CourseSchema через распаковку JSON из файла
with open('testdata/files/course.json', 'r') as file:
    course_json_data = file.read()

course_json_model = CourseSchema.model_validate_json(course_json_data)
print('Course json file model:', course_json_model)
print('-' * 60)

class CourseSchema(BaseModel):
    # Использование alias_generator для автоматического преобразования
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimatedTime: str


# Инициализируем модель CourseSchema через конструктор класса
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    estimatedTime="1 week"
)
print('Course default model:', course_default_model)
print('-' * 60)