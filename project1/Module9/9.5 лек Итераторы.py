# Итератор-это объект, который может перемещаться по элементам какого-либо другого объекта или последовательности.

# Как создать свой собственный итератор? А именно тот объект, который может перемещаться по элементам другого объекта
# и там производить разные алгоритмы.

# Во-первых, у этого объекта должен быть магический метод «__iter__», который принимает на вход сам объект, то есть
# «self». Этот метод создаёт итератор для перебора объекта. Это такая инициализация итератора. В этом методе мы
# сбрасываем наш счётчик. У итератора должен быть обязательно счётчик, мы его сбрасываем до нуля. И делаем, естественно,
# все те операции, которые нам необходимы

# Во-вторых, должен быть обязательно магический метод «__next__», который точно также принимает на вход самого себя
# «self». И как раз метод «__next__» переходит к следующему значению и считывает. То есть он берет и считывает первый
# элемент, как только там закончился весь алгоритм именно с этим элементом, магический метод «__next__» берет следующий
# элемент и так далее до конца пока мы сами его не остановим

# Так же есть специальное исключение, которое называется «StopIteration», которое вызывается тогда, когда нам необходимо
# закончить перебор наших элементов.


print('Первый пример:')
# библиотека itertools

import sys
from itertools import repeat

ex_itertator = repeat('4', 100_000)
print(f'Список не получим, т.к. вычисления не производились: {ex_itertator}')
print(f'Размер итератора - {sys.getsizeof(ex_itertator)}')

ex_str = '4' * 100_000
print(f'Размер списка - {sys.getsizeof(ex_str)}')
print(f'Разность размеров - {sys.getsizeof(ex_str) - sys.getsizeof(ex_itertator)}')

# Документация библиотеки itertools https://docs.python.org/3/library/itertools.html
print('Документация библиотеки itertools: https://docs.python.org/3/library/itertools.html')
print()

print('Второй пример:')


class Iter:

    def __init__(self):
        self.first = 'Первый элемент'
        self.second = 'Второй элемент'
        self.third = 'Третий элемент'
        self.i = 0

    # Описание работы для цикла for
    def __iter__(self):
        # Обнуляет счётчик перед циклом
        self.i = 0
        # Возвращает ссылку на себя, так как сам объект должен быть итератором
        return self

    def __next__(self):
        # Этот метод возвращает значения по требованию python (ленивые вычисления)
        self.i += 1
        if self.i == 1:
            return self.first
        if self.i == 2:
            return self.second
        if self.i == 3:
            return self.third
        if self.i == 4:
            return "Подсчёт окончен"
        raise StopIteration()  # Признак того, что возвращать больше нечего


obj_1 = Iter()

# Цикл for
# print(obj_1)
# for value in obj_1:
#     print(value)

# То есть интерпретатор вызывает метод __next__ при каждом проходе цикла
# Если в __next__ возникает исключение StopIteration, то значит в объекте больше нет элементов, цикл прекращается

# По сути вот так выглядит цикл for
try:
    while True:
        value = obj_1.__next__()
        print(value)
except StopIteration:
    print('Цикл for окончен')

print()

print('Третий пример функция Фибоначчи:')


def fibonacci(n):
    result = []
    a, b = 0, 1
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci(10))
for value in fibonacci(n=10):
    print(value)

print()

print('Четвёртый пример, итератор Фибоначчи:')


class Fibonacci:
    """Итератор последовательности Фибоначчи до N элементов"""

    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n
        # self.i = 0
        # self.a = 0
        # self.b = 1
        # self.n = n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a


fib_iterator = Fibonacci(20)
print(fib_iterator)
for value in fib_iterator:
    print(value)

# Каждое значение вычисляется "по месту" - тогда, когда оно понадобилось
