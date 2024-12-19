# Первый пример - как выглядит объединение функций map и filter
print('Первый пример:')


def mul_by_3(x):
    return x * 3


def is_odd(x):
    return x % 2


my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

result = map(mul_by_3, filter(is_odd, my_numbers))
print(list(result))
print()

# list comprehension - словарные и списковые сборки
print('Второй пример, списковая сборка, аналог map:')
# list_comp_1 = [x * 2 for x in range(1, 6)]
# list_comp_1 = [x * 2 for x in collection]
list_comp_1 = [x * 2 for x in my_numbers]  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(list_comp_1)
print()

# Генерация списков с фильтрацией
print('Третий пример, списковая сборка с if, аналог filter:')
# list_comp_2 = [x * 2 for x in collection if x > 5], if всего один
list_comp_2 = [x * 3 for x in my_numbers if x % 2]  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(list_comp_2)
print()

# Изменение операции над элементом
print('Четвёртый пример, условия перед циклом для того, чтобы не фильтровать данные, а поменять операцию над ними:')
# list_comp_3 = [x * 2 if x > 2 else x * 10 for x in collection], тут происходит изменение списка
my_numbers_2 = ['A', 1, 4, 'B', 5, 'C', 2, 6]
list_comp_3 = [x if type(x) == str else x * 5 for x in my_numbers_2]
print(list_comp_3)
print()

# Генерация для двух элементов
print('Пятый пример')
# list_comp_4 = [x * y for x in collection for y in collection_2]
list_numbers_1 = [3, 1, 4, 1, 5, 9, 2, 6]
list_numbers_2 = [2, 7, 1, 8, 2, 8, 1, 8]

list_comp_4 = [x * y for x in list_numbers_1 for y in list_numbers_2]
print(f'Перемножение элементов в списках: {list_comp_4}')

list_comp_4 = [x * y for x in list_numbers_1 for y in list_numbers_2 if x % 2]
print(f'Перемножение элементов в списках, если x нечётное: {list_comp_4}')

list_comp_4 = [x * y for x in list_numbers_1 for y in list_numbers_2 if x % 2 and y // 2]
print(f'Перемножение элементов в списках, если x нечётное и вместо y тут целые части от деления y на 2: {list_comp_4}')
print()

# Генераторы
print('Шестой пример')
result_6_1 = {x for x in my_numbers}  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Получается отфильтрованное множество: {result_6_1}')

result_6_2 = {x: x ** 2 for x in my_numbers}  # my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f'Получается словарь: {result_6_2}')
