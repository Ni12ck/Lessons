from pprint import pprint

import requests
import inspect

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

# Пример 1 - функция hasattr() - проверка на существование атрибута
print('Пример 1')
attr_name = 'attribute_2'
print(f'Есть ли атрибут attr_name у объекта? - {hasattr(some_object, attr_name)}')  # False
print(f'Есть ли атрибут attribute_1 у объекта? - {hasattr(some_object, 'attribute_1')}')  # True
print(f'{dir(some_object)}\n')

# Пример 2 - функция getattr() - получение атрибута
print('Пример 2')
print(f'Получить attribute_1 у объекта: {getattr(some_object, 'attribute_1')}')
# print(help(getattr))

# Можно добавить сообщение, если атрибута нет
print(f'Получить attribute_2 у объекта: {getattr(some_object, 'attribute_2', 'такого атрибута нет')}\n')

# for attr_name in dir(requests):
#     attr = getattr(requests, attr_name)
#     print(attr_name, type(attr))

# Пример 3 - функция callable() - проверка можно ли вызвать тот или иной объект
print('Пример 3')
print(f'Можно ли вызвать some_string? - {callable(some_string)}')  # False
print(f'Можно ли вызвать some_function? - {callable(some_function)}')  # True
print(f'Можно ли вызвать some_object.attribute_1? - {callable(some_object.attribute_1)}')  # False
print(f'Можно ли вызвать some_object.some_class_method? - {callable(some_object.some_class_method)}\n')  # True

# Пример 4 - функция isinstance() - является ли объект экземпляром класса
print('Пример 4')
print(f'Является ли some_number экземпляром str? - {isinstance(some_number, str)}')  # False
print(f'Является ли some_number экземпляром int? - {isinstance(some_number, int)}')  # True
print(f'Является ли some_number экземпляром SomeClass? - {isinstance(some_number, SomeClass)}')  # False
print(f'Является ли some_object экземпляром SomeClass? - {isinstance(some_object, SomeClass)}\n')  # True

# Модуль inspect
# Этот модуль собирает удобные методы и классы для отображения интроспективной информации
# Пример 5 - самые употребимые функции
print('Пример 5')
print(f'Является ли модулем requests? - {inspect.ismodule(requests)}')
print(f'Является ли модулем some_object? - {inspect.ismodule(some_object)}')
print(f'Является ли классом requests? - {inspect.isclass(requests)}')
print(f'Является ли функцией requests? - {inspect.isfunction(requests)}')
print(f'Является ли requests встроенным в питон? - {inspect.isbuiltin(requests)}')

# Из какого модуля получили объект
some_function_module = inspect.getmodule(some_function)
print(f'Тип some_function_module: {type(some_function_module)}\n'
      f'Вызов inspect.getmodule (из какого модуля получили объект): {some_function_module}')
