# Декораторы - это обёртка вокруг функций или классов, которая меняет способ работы этой функции. Разработчик может
# писать свой код так, как ему хочется и использовать декораторы только для расширения функциональности. Это функция,
# которая принимает другую функцию в качестве аргумента и возвращает третью.

# Создание декоратора
# 1. function = decorator(function)
# 2. @decorator
#    def function(...):
#         ...

# Первый пример
print('Первый пример:')


# Этот декоратор ничего не меняет
def null_decorator(func):
    return func


def greet():
    return 'Hello'


greet = null_decorator(greet)

print(f'Вывод первой функции в декораторе: {greet()}')
print()

# Второй пример
# Можно использовать синтаксис Python @ для декорирования функции за один шаг
print('Второй пример:')


@null_decorator
def greet_2():
    return 'Hello!'


print(f'Вывод второй функции в декораторе: {greet_2()}')
print()

# Третий пример
# Почему внутри декоратора нужно определить ещё одну функцию
print('Третий пример:')


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper


@uppercase
def greet_3():
    return 'Привет'


print(f'Вывод третьей функции в декораторе: {greet_3()}')
print()

# Четвёртый пример
print('Четвёртый пример:')

import time
import sys


def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result_func = func(*args, **kwargs)

        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция {func.__name__} работала: {elapsed} секунд(ы)')
        return f'Результат функции {func.__name__}:\n{result_func}'

    return surrogate


@time_track
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


# Увеличивает максимум длины строчки
sys.set_int_max_str_digits(100000)

result = digits(3141, 5926, 2718, 2818)
print(result)
