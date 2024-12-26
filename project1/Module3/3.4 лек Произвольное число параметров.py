# Создадим функцию с неопределённым количеством параметров
def test_func(*params):
    print('Тип:', type(params))
    print('Аргумент:', params)


test_func(1, 2, 3, 4)

print()


# Можно посчитать сумму чисел, не зная, сколько всего будет введено чисел
def summator(txt, *values, type_sum='sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt} {s} {type_sum}'


print(summator('Сумма чисел:', 1, 2, 3, 4))
print(summator('Сумма чисел:', 1, 2, 3, 4, type_sum='summator'))

print()


# Можно передать неограниченное количество именованных параметров, которые преобразуются в словарь
# Можно использовать позиционный параметр (value), произвольное количество позиционных параметров(*types), именованный
# параметр (name_author='Vova'), произвольное количество именованных параметров(**values)
def info(value, *types, name_author='Vova', **values):
    print('Тип:', type(values))
    print('Аргумент:', values)
    for key, value in values.items():
        print(key, value)
    print(types)


info('Пример использования параметров всех типов:', 1, 2, 3, name_author='Vova', name='Vladimir', course='python')

print()


# Создам функцию, которая будет считать суммы квадратов, кубов ...
# n - степень
def my_sum(n, *args, txt='Сумма чисел:'):
    s = 0
    for i in range(len(args)):
        s += args[i] ** n
    print(txt, s)


my_sum(2, 1, 2, 3, txt='Сумма квадратов')
my_sum(1, 1, 2, 3)
