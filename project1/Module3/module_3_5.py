# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр
# этого числа.

# Пункты задачи:
# 1. Напишите функцию get_multiplied_digits и параметр number в ней.
# 2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# 3. Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ
# из str_number в числовом представлении(int).
# 4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру
# числа на результат работы этой же функции с числом, но уже без первой цифры.
# 5. 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять
# срез str_number[1:].
# 6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.

# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3

# Пример результата выполнения программы:
# Исходный код:
# result = get_multiplied_digits(40203)
# print(result)
# Вывод на консоль:
# 24

# Примечания:
# 1. При преобразовании строки(str) в число(int) первые нули убираются. int('00123') -> 123.
# 2. Если возникает ошибка, рекомендуется пошагово отладить программу "жучком". Чаще всего ошибка заключается в
# бесконечной рекурсии или же в неверном обращении по индексу.

# Написал функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр
# этого числа.
def get_multiplied_digits(number):
    # Создал переменную str_number и записал строковое представление(str) числа number в неё.
    str_number = str(number)
    # Cоздал переменную first и буду записывать в неё первый символ из str_number в числовом представлении(int).
    first = int(str_number[0])
    # Если число состоит более чем из одной цифры, то перемножаю first с последующей цифрой
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    # Если число состоит из одной цифры, то возвращаю эту цифру
    else:
        return first


# Вывод умножения: 1*2*3*4*5
print(get_multiplied_digits(102030405))
