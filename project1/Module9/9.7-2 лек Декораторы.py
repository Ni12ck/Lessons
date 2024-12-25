# Функция, которая генерирует декоратор, который генерирует функцию заместитель

# Первый пример - функция, которая возвращает декоратор

print('Первый пример:')

import time
import sys


def func_gen_dec(precision):
    def dec(func):
        # Трекер времени, как в прошлой лекции
        def wrapper(*args, **kwargs):
            started_at = time.time()

            result_func = func(*args, **kwargs)

            ended_at = time.time()
            # Тут указываем precision - степень округления (количество цифр после запятой)
            elapsed = round(ended_at - started_at, precision)
            print(f'Функция {func.__name__} работала: {elapsed} секунд(ы)')
            return f'Результат функции {func.__name__}: {result_func}'

        return wrapper

    return dec


# Можно сразу записать так:
# @func_gen_dec(precision=2)
def digits(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


# Увеличивает максимум длины строчки
sys.set_int_max_str_digits(100000)

# Теперь можно менять декоратор в зависимости от нужной степени округления
# Тут создаём декоратор степенью округления - 2
time_track_precision_2 = func_gen_dec(precision=2)
# Оборачиваем нашу функцию в декоратор
digits = time_track_precision_2(digits)
result = digits(3141, 5926, 2718, 2818)
print(result)
print()

# Второй пример
print('Второй пример:')


def func_gen_dec_2(precision):
    print('Этапы выполнения:')
    print(f'1. Получили точность {precision}, с которой надо выводить результат')
    print('2. Начинаем создавать декоратор')

    def dec(func):
        print(f'4. Декоратор принял на вход функцию {func.__name__}, которую надо будет декорировать')
        print('5. Начинает создавать функцию wrapper (обёртку)')

        # Трекер времени, как в прошлой лекции
        def wrapper(*args, **kwargs):
            started_at = time.time()
            print(f'7. Запускаем функцию {func.__name__} с переданными в обёртку параметрами и запоминаем результат')
            result_func = func(*args, **kwargs)
            print('8. Определяем затраченное время')
            ended_at = time.time()
            print(f'9. Вот тут используется (precision = {precision}) - он запомнился в замыкании surrogate')
            # Тут указываем precision - степень округления (количество цифр после запятой)
            elapsed = round(ended_at - started_at, precision)
            print(f'10. Функция {func.__name__} работала: {elapsed} секунд(ы)')
            print('11. Возвращаем результат, который вернула функция')
            return f'12. Результат функции {func.__name__}: {result_func}'

        print('6. Декоратор создал функцию обёртку и возвращает её')
        return wrapper

    print('3. Декоратор создан и пора его вернуть')
    return dec


@func_gen_dec_2(precision=5)
def digits_2(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))


result_2 = digits_2(3141, 5926, 2718, 2818)
print(result_2)
