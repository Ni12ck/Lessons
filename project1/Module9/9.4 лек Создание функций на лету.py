# Иногда нам нужно создать функцию, которая будет делать очень короткую математическую операцию. Для этого придумали
# лямбда-функции. Это такие очень короткие функции, которые создаются и сразу выполняются.

print('Первый пример:')
my_func = lambda x: x + 10

print(f'Выполнение lambda функции: {my_func(42)}')
print(f'Тип lambda функции: {type(my_func)}')
print(f'Имя lambda функции: {my_func.__name__}')

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
result_1 = map(lambda x: x + 10, my_numbers)
print(f'Применение lambda функции в map: {list(result_1)}')

print()

# lambda функции могут принимать несколько параметров, либо ни одного
print('Второй пример:')

my_numbers_2 = [2, 7, 1, 8, 2, 8, 1, 8]

result_2 = map(lambda x, y: x + y, my_numbers, my_numbers_2)  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Применение lambda функции с двумя списками: {list(result_2)}')
print()

# lambda форма функции имеет ограниченное применение:
# 1) Создаётся в процессе выполнения кода, а не при компиляции, может снизить производительность
# 2) У них нет имени, на них нельзя ссылаться, они являются одноразовыми функциями.
# 3) Не надо пытаться записать в подобные функции сложные выражения
# 4) У них нет имени, на них нельзя ссылаться, поэтому они являются одноразовыми

# Создание функций на лету
print('Третий пример:')


# get_mul_v1 - функция высшего порядка, она возвращает функции
def get_mul_v1(n):
    if n == 2:
        def mul(x):
            return x * 2

    elif n == 3:
        def mul(x):
            return x * 3

    else:
        raise Exception('Можно умножить только на 2 или 3')

    return mul


mul_2 = get_mul_v1(2)
mul_3 = get_mul_v1(3)
# mul_4 = get_mul_v1(4)

res_mul_2 = map(mul_2, my_numbers)  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Умножение на 2: {list(res_mul_2)}')
res_mul_3 = map(mul_3, my_numbers)  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Умножение на 3: {list(res_mul_3)}')
print()

# Создание функций на лету 2
# Замыкание в Python- это функциональный объект, который запоминает значения во внешних областях, даже если они
# отсутствуют в памяти. То есть, когда мы вызовем нашу функцию высшего порядка, мы передадим в неё какой-то параметр
# «n», но потом мы будем вызывать нашу функцию «multiplier», который мы передаём параметр «x». И «n» у нас будет
# сохранён благодаря тому, что мы сперва вызвали нашу функцию высшего порядка. Это и есть замыкание переменных в Python.
print('Четвёртый пример:')


def get_mul_v2(n):
    def multiplier(x):
        return x * n

    return multiplier


mul_5 = get_mul_v2(5)
print(f'Умножение числа 42 на 5: {mul_5(x=42)}')

mul_10 = get_mul_v2(10)
mul_100 = get_mul_v2(100)

print(f'Умножение элементов списка на 10: {list(map(mul_10, my_numbers))}')  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Умножение элементов списка на 100: {list(map(mul_100, my_numbers))}')  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print()

# Показатель того, что не стоит передавать в аргументы функции изменяемый объект или замыкать их
print('Пятый пример:')

from pprint import pprint


def matrix(some_list):
    def mul_column(x):
        res = []
        for element in some_list:
            res.append(element * x)
        return res

    return mul_column


matrix_on_my_numbers = matrix(my_numbers)  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print('первая матрица')
res_matrix = map(matrix_on_my_numbers, my_numbers_2)  # my_numbers_2 = [2, 7, 1, 8, 2, 8, 1, 8]
pprint(list(res_matrix))
print()

# Но почему же нам нельзя передавать в аргумент функции изменяемые объекты? Потому что, если мы сейчас захотим увеличить
# на несколько элементов наш изначальный список «my_numbers», то у меня не вызовется никакая ошибка. Потому что в памяти
# «matrix» у нас сохранён список «my_numbers», и он в потенциале может поменяться. Поэтому, если мы поменяем его, у нас
# поменяется и результат нашей функции. У нас создастся гораздо намного больше матрица

# Если нам это не надо, то лучше всего хранить в картежах такие вещи. Но лучше следить за тем, что мы передаём в
# аргументы наших функций высшего порядка. Потому что если это изменяемые объекты, они будут замыкаться, будут
# сохраняться в памяти, но при этом они точно также могут поменяться. И как уже подействует функция «multiply_column»,
# мы не сможем точно прогнозировать. За этим нужно внимательно следить.
print('вторая матрица')
my_numbers.extend([10, 20, 30])
res_matrix_ext = map(matrix_on_my_numbers, my_numbers_2)
pprint(list(res_matrix_ext))
print()

# Создание объекта, который можно вызвать
print('Шестой пример:')


class Multiplier:

    def __init__(self, n):
        self.n = n

    def __call__(self, x):
        # если есть такой метод у класса, то его объект можно вызвать как функцию
        return x * self.n


by_200 = Multiplier(n=200)
res_by_200 = by_200(x=42)
print(f'Умножение числа 42 на 200: {res_by_200}')
res_by_200_map = map(by_200, my_numbers)  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Умножение элементов списка на 200: {list(res_by_200_map)}')
