print(f'Первый пример:')
# 1. Написать функцию, которая возвращает функцию повторения двух первых символов n раз
# 2. Создать массив функций с различными параметрами n и применить все функции поочерёдно к аргументу
# 3. Применить все функции поочерёдно к массиву аргументов

animal = 'Медведь'
animals = ['Заяц', 'Медведь', 'Волк']


# 1. Функция, которая возвращает функцию повторения двух первых символов n раз
def gen_repeat(n):
    def repeat(animal):
        return (animal[0: 2] + '-') * n + animal

    return repeat


# Тестовые генераторы
test_1 = gen_repeat(1)
test_2 = gen_repeat(2)
# Вывод результатов
print(test_1(animal))
print(f'{test_2(animal)}\n')

# 2. Создал массив функций с различными параметрами n и применить все функции поочерёдно к аргументу
repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(f'{result}\n')

# 3. Применил все функции поочерёдно к массиву аргументов
# тут порядок for имеет значение для вывода аргументов списка в том или ином порядке
fin_result = [func(x) for x in animals for func in repetitions]
print(f'{fin_result}\n')

# Задача - есть функция, которая возвращает результат введения числа a в степень b
# Нужно ускорить её, чтобы она не делала повторные вычисления
print('Второй пример:')


def memoiz_func(f):
    mem = {}

    def wrapper(*args):
        print(f'Выполнение функции {f.__name__} с аргументами {args}, '
              f'внутренняя память (словарь, в котором хранятся данные): {mem}')
        if args not in mem:
            mem[args] = f(*args)
            return f'Функция {f.__name__} завершила работу, ответ: {mem[args]}\n'
        else:
            return f'Функция {f.__name__} уже завершала работу с данными аргументами, ответ: {mem[args]}\n'

    return wrapper


@memoiz_func
def func(a, b):
    print(f'Выполняем функцию с аргументами - возводим {a} в степень {b}')
    return a ** b


print(func(3, 5))
print(func(3, 4))
print(func(3, 2))
print(func(3, 5))
print(func(3, 4))
print(func(3, 5))
