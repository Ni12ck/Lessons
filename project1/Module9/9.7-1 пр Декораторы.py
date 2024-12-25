# Задание:
# Напишите 2 функции:
# 1. Функция, которая складывает 3 числа (sum_three)
# 2. Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.

# Пример:
# result = sum_three(2, 3, 6)
# print(result)

# Результат консоли:
# Простое
# 11

# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three

# Создал функцию декоратор is_prime, которая показывает простое или составное число получилось во внутренней функции
def is_prime(func):
    def wrapper(*args):
        res_func = func(*args)
        # Создал переменную res_is_prime, которая будет указывать на простоту числа
        res_is_prime = True
        # Создал цикл, который проверяет на деление без остатка
        for number in range(2, res_func):
            if res_func % number == 0:
                res_is_prime = False
        # Если res_is_prime = True, то вывожу, что получившееся число простое
        if res_is_prime:
            print(f'Получившееся число в функции {func.__name__} - простое')
        # Если res_is_prime = False, то вывожу, что получившееся число составное
        else:
            print(f'Получившееся число в функции {func.__name__} - составное')
        return f'Результат функции {func.__name__}: {res_func}'

    return wrapper


# Создал функцию sum_three, которая складывает три числа, обернув её в декоратор is_prime
@is_prime
def sum_three(a, b, c):
    return a + b + c


# Примеры выполнения
print('Первый пример:')
result_1 = sum_three(2, 3, 6)
print(f'{result_1}\n')

print('Второй пример:')
result_2 = sum_three(3, 4, 5)
print(result_2)
