# В true_math создайте функцию divide, которая принимает два параметра first и second. Функция должна возвращать
# результат деления first на second, но когда в second записан 0 - возвращать бесконечность

# Импорт из модуля math элемента inf
from math import inf


# Функция деления двух чисел
def divide(first, second):
    # Если второе число равно 0, то вывожу inf
    if second == 0:
        return inf
    # Иначе вывожу результат деления
    else:
        res = first / second
        return res
