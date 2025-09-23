from faker import Faker # библиотека для генерации случайных данных

faker = Faker() # создаем экземпляр класса Faker

def get_random_email(): # функция для генерации случайной электронной почты
    return faker.email()
