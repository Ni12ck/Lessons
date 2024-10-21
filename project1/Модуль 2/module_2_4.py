# Задача "Всё не так уж просто":

# Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все непростые числа.
# Выведите списки primes и not_primes на экран(в консоль).

# Пункты задачи:
# 1. Создайте пустые списки primes и not_primes.
# 2. При помощи цикла for переберите список numbers.
# 3. Напишите ещё один цикл for (вложенный), где будут подбираться делители для числа из 1ого цикла.
# 4. Отметить простоту числа можно переменной is_prime, записав в неё значение True перед проверкой.
# 5. В процессе проверки на простоту записывайте числа из списка numbers в списки primes и not_primes
# в зависимости от значения переменной is_prime после проверки (True - в prime, False - в not_prime).
# 6. Выведите списки primes и not_primes на экран(в консоль).

# Пример результата выполнения программы:
# Исходный код:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Вывод на консоль:
# Primes: [2, 3, 5, 7, 11, 13]
# Not Primes: [4, 6, 8, 9, 10, 12, 14, 15]

# Примечания:
# Учтите, что число 1 не является ни простым, ни составным числом, поэтому оно отсутствует в конечных списках.
# Для проверки на простоту числа вам нужно убедиться, что выбранное число не делиться ни на,
# что в диапазоне от 2 до этого числа(не включительно).
# Попробуйте оптимизировать(ускорить) процесс выяснения простоты числа при помощи оператора break,
# когда найдёте делитель. (Не обязательно)
# Переменные меняющее своё булевое состояние на противоположное в процессе проверки, как is_prime,
# в кругах разработчиков называются переменными-флагами(flag).

# Дан список чисел:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# Создаю пустые списки primes и not_primes:
# В будущем в primes будут записываться простые числа, т.е. те, которые делятся только на 1 и сами на себя (кроме 1).
# А в not_primes остальные (кроме 1).
primes = []
not_primes = []
# Создам переменную Number, которая будет проверяемым числом
Number = 0
# Перебираю список numbers
for i in range(len(numbers)):
    # Создам переменную is_prime, которая будет указывать на простоту числа
    is_prime = True
    # Присваиваю переменной Number значения из списка
    Number = numbers[i]
    # Если число равно 1, то пропускаем его
    if Number == 1:
        continue
    # Создаю вложенный цикл, который ищет делители от 2 до проверяемого числа
    for j in range(2, Number):
        # Если делители находятся, то число является составным
        if Number % j == 0:
            is_prime = False
            # Попробовал оптимизировать(ускорить) процесс при помощи оператора break
            break
    # Если число простое, то добавляю его в список с простыми числами
    if is_prime:
        primes.append(Number)
    # Если число составное, то добавляю его в список с составными числами
    else:
        not_primes.append(Number)
# Вывод чисел
print(f'Primes: {primes} \nNot Primes: {not_primes}')

# Второй вариант без переменных is_prime и Number
# Создаю пустые списки primes и not_primes:
primes = []
not_primes = []
# Перебираю список numbers
for i in numbers:
    # Если число равно 1, то пропускаем его
    if i == 1:
        continue
    # Создаю вложенный цикл, который ищет делители
    for j in primes:
        if i % j == 0:
            # Если делители находятся, то добавляю его в список с составными числами
            not_primes.append(i)
            # Оптимизация процесса при помощи оператора break
            break
    else:
            # Если делители не находятся, то добавляю его в список с простыми числами
            primes.append(i)
# Вывод чисел
print(f'Primes: {primes} \nNot Primes: {not_primes}')