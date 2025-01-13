# Интроспекция — это способность объекта в процессе выполнения программы получать информацию о своём типе, доступных
# атрибутах и методах, а также другую важную информацию, необходимую для выполнения дополнительных операций с объектом

# Встроенная помощь
import requests

# help(requests)
# help(requests.get)

some_string = 'i am is string'
some_number = 42
some_list = [some_string, some_number]

def some_function(param, param_2='n/a'):
    print('my params is', param, param_2)

class SomeClass:
    def __init__(self):
        self.attribute_1 = 27

    def some_class_method(self, value):
        self.attribute_1 = value
        print(self.attribute_1)

some_object = SomeClass()

func = some_function

# Пример 1 - Атрибут класса __name__
print('Пример 1')
print(some_function.__name__)
print(SomeClass.__name__)
print(requests.__name__)
print(f'{func.__name__}\n')
# У них нет имён
# print(some_string.__name__)
# print(some_number.__name__)

# Пример 2 - узнаём тип объекта
print('Пример 2')
print(type(some_number))

print(type(some_number) is int)
print(type(some_number) is list)

print(type(requests))
print(f'{type(requests.get)}\n')

# Пример 3 - функция dir
# Функция dir возвращает отсортированный список атрибутов и методов, доступных для указанного объекта, который может
# быть объявленной переменной или функцией
print('Пример 3')
from pprint import pprint

pprint(dir(some_number))
# pprint(dir(some_list))
# pprint(dir(some_function))
# pprint(dir(SomeClass))
# pprint(dir(some_object))
# pprint(dir(requests))

# Без указания аргумента dir() выводит доступные в локальной области видимости
#pprint(dir())