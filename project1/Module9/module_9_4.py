# Задача "Функциональное разнообразие":

# Lambda-функция:
# Даны 2 строки:
# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
# Здесь ? - место написания lambda-функции.

# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.

# Замыкание:
# Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
# Внутри этой функции, напишите ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
# неограниченное количество данных любого типа.
# Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
# Функция get_advanced_writer возвращает функцию write_everything.

# Данный код:
# write = get_advanced_writer('example.txt')
# write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# Метод __call__:
# Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
# В этом классе также определите метод __call__ который будет случайным образом выбирать слово из words и возвращать
# его. Для случайного выбора с одинаковой вероятностью для каждого данного в коллекции можете использовать функцию
# choice из модуля random.

# Ваш код (количество слов для случайного выбора может быть другое):
# from random import choice
# # Ваш класс здесь
# first_ball = MysticBall('Да', 'Нет', 'Наверное')
# print(first_ball())
# print(first_ball())
# print(first_ball())
# Примерный результат (может отличаться из-за случайности выбора):
# Да
# Да
# Наверное

# Примечания:
# Все задания пишутся в одном модуле.
# Передаваемые данные в функции и объекты можете использовать свои, главное, чтобы ваш код полноценно демонстрировал
# логику написанного.

print('Первый пример "Lambda-функция":')
# Даны две строки:
first = 'Мама мыла раму'
second = 'Рамена мало было'
# Составил lambda-функцию
# Результатом должен быть список совпадения букв в той же позиции:
# [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# Где True - совпало, False - не совпало.
res_1 = list(map(lambda x, y: x == y, first, second))
print(f'Список совпадения букв в той же позиции: {res_1}')
print()

print('Второй пример "Замыкание":')


# Создал функцию get_advanced_writer(file_name), которая принимает название файла для записи.
def get_advanced_writer(file_name):
    # Внутри этой функции, написал ещё одну - write_everything(*data_set), где *data_set - параметр принимающий
    # неограниченное количество данных любого типа.
    def write_everything(*data_set):
        # Логика write_everything заключается в добавлении в файл file_name всех данных из data_set в том же виде.
        with open(file_name, 'a', encoding='utf-8') as file:
            # Первый вариант:
            # for element in data_set:
            #     file.write(f'{element}\n')
            # Второй вариант:
            file.write(repr(data_set))

    # Функция get_advanced_writer возвращает функцию write_everything.
    return write_everything


# Запись в файл 'example for 9-4.txt'
write = get_advanced_writer('example for 9-4.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
print("В файле 'example for 9-4.txt' должны добавиться все данные из data_set в том же виде:\n"
      "('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])\n")

print('Третий пример "Метод __call__":')

# Импортировал random
import random


# Создал класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
class MysticBall:
    def __init__(self, *words):
        self.words = words

    # Определил метод __call__, который будет случайным образом выбирать слово из words и возвращать его.
    def __call__(self, *words):
        return random.choice(self.words)


# Присвоение переменной first_ball объекта класса MysticBall
first_ball = MysticBall(1, 2, 3)
print('Вывод случайного слова из words:')
print(first_ball())
print(first_ball())
print(first_ball())
