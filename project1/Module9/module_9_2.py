# Задача:

# Даны несколько списков, состоящих из строк
# first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
# second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. В переменную first_result запишите список созданный при помощи сборки состоящий из длин строк списка first_strings,
# при условии, что длина строк не менее 5 символов.

# 2. В переменную second_result запишите список созданный при помощи сборки состоящий из пар слов(кортежей) одинаковой
# длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)

# 3. В переменную third_result запишите словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина
# строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings. Условие
# записи пары в словарь - чётная длина строки.

# Пример выполнения кода:
# print(first_result)
# print(second_result)
# print(third_result)

# Вывод на консоль:
# [10, 8, 8]
# [('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'),
# ('Variable', 'Computer')]
# {'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

# Примечания:
# Помните, когда вы используете 2 цикла for внутри сборки, первый цикл - внешний, второй - внутренний.

# Два списка из "дано"
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Создал переменную first_result, в которую записал список созданный при помощи сборки состоящий из длин строк списка
# first_strings, при условии, что длина строк не менее 5 символов.
first_result = [len(x) for x in first_strings if len(x) >= 5]
print(f'1) Список из длин строк больше 5 из списка first_strings: {first_result}')

# Создал переменную second_result, в которую записал список, созданный при помощи сборки состоящей из пар слов(кортежей)
# одинаковой длины. Каждое слово из списка first_strings должно сравниваться с каждым из second_strings. (два цикла)
second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(f'2) Список из пар слов одинаковой длины: {second_result}')

# Создал переменную third_result, в которую записал словарь, созданный при помощи сборки, где парой ключ-значение будет
# строка-длина строки. Значения строк будут перебираться из объединённых вместе списков first_strings и second_strings.
# Условие записи пары в словарь - чётная длина строки.
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}
print(f'3) Словарь из строк и их длин, если длина является чётной: {third_result}')
