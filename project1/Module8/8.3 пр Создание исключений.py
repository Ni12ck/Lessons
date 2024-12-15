# Задача "Некорректность":
# Создайте 3 класса (2 из которых будут исключениями):

# Класс Car должен обладать следующими свойствами:
# 1. Атрибут объекта model - название автомобиля (строка).
# 2. Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
# 3. Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True, если
# корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# 4. Атрибут __numbers - номера автомобиля (строка).
# 5. Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True, если
# корректный, в других случаях выбрасывает исключение. Уровень доступа private.
# 6. Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message. Где
# message - сообщение, которое будет выводиться при выбрасывании исключения


# Работа методов __is_valid_vin и __is_valid_numbers:

# __is_valid_vin
# 1. Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое число.
# (тип данных можно проверить функцией isinstance).
# 2. Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число
# находится не в диапазоне от 1000000 до 9999999 включительно.
# 3. Возвращает True, если исключения не были выброшены.

# __is_valid_numbers
# 1. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана не
# строка. (тип данных можно проверить функцией isinstance).
# 2. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна состоять
# ровно из 6 символов.
# 3. Возвращает True, если исключения не были выброшены.

# ВАЖНО!
# Методы __is_valid_vin и __is_valid_numbers должны вызываться и при создании объекта
# (в __init__ при объявлении атрибутов __vin и __numbers).

# Создал класс Car
class Car:
    def __init__(self, model: str, __vin: int, __numbers: str):
        # Атрибуты объекта класса
        self.model = model  # Название автомобиля
        self.__vin = __vin  # Номер автомобиля
        self.__numbers = __numbers  # Номера автомобиля
        self.__is_valid_vin(self.__vin)  # Вызов метода __is_valid_vin
        self.__is_valid_numbers(self.__numbers)  # Вызов метода __is_valid_number

    # Создал метод __is_valid_vin(vin_number), который принимает vin_number и проверяет его на корректность. Возвращает
    # True, если корректный, в других случаях выбрасывает исключение.
    @staticmethod
    def __is_valid_vin(vin_number):
        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое
        # число.
        if not isinstance(vin_number, int):
            raise IncorrectCarNumbers('Некорректный тип vin номер')
        # Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное
        # число находится не в диапазоне от 1000000 до 9999999 включительно.
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        # Возвращает True
        return True

    # Создал метод __is_valid_numbers(numbers), который принимает numbers и проверяет его на корректность. Возвращает
    # True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
    @staticmethod
    def __is_valid_numbers(numbers):
        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана
        # не строка.
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        # Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна
        # состоять ровно из 6 символов.
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        # Возвращает True
        return True


# Создал классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message. Где
# message - сообщение, которое будет выводиться при выбрасывании исключения
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


# Примеры выполняемого кода:
print('Пример №1:')
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

print('Пример №2:')
try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

print('Пример №3:')
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
