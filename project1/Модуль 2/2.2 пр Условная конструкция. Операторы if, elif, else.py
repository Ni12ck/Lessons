# Задача "Все ли равны?":
# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

# Пункты задачи:
# 1. Если все числа равны между собой, то вывести 3
# 2. Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# 3. Если равных чисел среди 3-х вообще нет, то вывести 0

# Создаю три переменные: first, second и third. Пользователь должен ввести три целых числа.
first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))
# Пишу блок выполнения условий
# Самое сложно условие, при котором все числа равны, поэтому его пишу первым.
# При выполнении этого условия надо вывести "3"
if first == second == third:
    print(3)
# Второе условие, при котором 2 из 3 введённых чисел равны между собой с тремя вариантами сравнения,
# а именно первого и второго, первого и третьего, второго и третьего. Так я сравню все варианты.
# При выполнении этого условия надо вывести "2"
elif first == second or first == third or second == third:
    print(2)
# Третье условие, при котором равных чисел среди 3-х вообще нет.
# При выполнении этого условия надо вывести "0"
elif first != second != third:
    print(0)