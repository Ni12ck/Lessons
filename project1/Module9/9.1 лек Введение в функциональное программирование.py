# Преимущества функционального стиля программирования:
# 1. Это удобная отладка кода, так как функции очень маленькие, и мы точно знаем, где что находится. И уж тем более мы
# точно знаем, где будет наша ошибка. Мы её можем либо перехватить, либо просто вывести в консоль сообщение о том, что
# в таком-то месте произошла такая-то ошибка в отличие от объектно-ориентированного программирования, где у нас много
# классов, которые взаимодействуют друг с другом. Там очень тяжело докопаться до истины и узнать, в чем именно причина
# нашей ошибки. Из этого вытекает второе.
# 2. Удобно менять код, а функции можно использовать в разных случаях. Функции настолько маленькие, что их действительно
# можно использовать в совершенно разных программах и уж тем более даже проектах. С классами можно так же, но функция
# ещё меньше, чем наши классы, и тем удобнее менять код. Наша программа вся записана сверху вниз, все функции наши
# записаны. Их мы можем вызывать в любом месте кода, в любом случае кода. Их удобно очень менять. Например, мы поменяли
# немного функцию в начале и потом она работает у нас уже по другому.


# Первый пример
print('Первый пример:')


def get_names():
    return ['Владимир', 'Андрей', 'Антон', 'Кира', 'Сергей']


print(get_names.__name__)  # Имя функции
print(get_names())
print(type(get_names))  # Тип - функция
print()

print("Работа с переменной")
my_func = get_names
print(my_func())
print(my_func.__name__)  # Имя функции get_names
print()


def get_en_names():
    return ['Bill', 'Harry', 'Jack']


name_getters = [get_names, get_en_names]

print('Вывод объектов списка name_getters:')
for names in name_getters:
    print(f'Список имён: {names()}')
print()

# Второй пример с функцией высшего порядка
print('Второй пример с функцией высшего порядка:')


def adder(args):
    res = 0
    for number in args:
        res += number
    return res


def multiplier(args):
    res = 1
    for number in args:
        res *= number
    return res


def process_numbers(numbers, function):
    result = function(numbers)
    print(f'Результат выполнения функции {function.__name__}: {result}')


my_numbers = [2, 3, 6, 7, 8]

process_numbers(numbers=my_numbers, function=adder)
process_numbers(numbers=my_numbers, function=multiplier)
print()

# Третий пример
print('Третий пример, работа с map:')


def mul_by_2(x):
    return x * 2


# map применяет функцию к каждому элементу последовательности и формирует список из результатов
result_map = map(mul_by_2, my_numbers)
print(f'Выполнение функции {mul_by_2.__name__} для списка my_numbers:')
print(result_map)  # <map object at 0x000001F41B0F5180>
print(list(result_map))
print()

# Четвёртый пример
print('Четвёртый пример, работа с filter:')


def is_odd(x):
    return x % 2


# filter вычисляет функцию для каждого элемента и добавляет элемент в список результатов, если только функция
# вернёт True
result_filter = filter(is_odd, my_numbers)
print(result_filter)
print(f'Тут остаток больше нуля (значит результат True), поэтому выводятся все нечётные числа: {list(result_filter)}')
