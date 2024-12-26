# Задача "Счётчик вызовов":

# Вам необходимо написать 3 функции:

# 1. Функция count_calls подсчитывающая вызовы остальных функций.
# 2. Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем
# регистре, строку в нижнем регистре.
# 3. Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом
# списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

# Пункты задачи:

# 1. Создать переменную calls = 0 вне функций.
# 2. Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных
# двух функциях.
# 3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# 4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# 6. Вывести значение переменной calls на экран(в консоль).


# Пример результата выполнения программы:

# Пример выполняемого кода:
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)

# Вывод на консоль:
# (8, 'CAPYBARA', 'capybara')
# (10, 'ARMAGEDDON', 'armageddon')
# True
# False
# 4

# Примечания:
# Для использования глобальной переменной внутри функции используйте оператор global.
# Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.

# Создал переменную calls - количество вызовов функций
calls = 0

# Создам функцию count_calls, которая будет считать количество вызовов остальных функций.
def count_calls():
    global calls
    # При использовании функции count_calls переменная calls увеличивается на 1
    calls += 1
    # Функция возвращает значение переменной calls
    return calls

# Создам функцию string_info, которая принимает аргумент - строку и возвращает кортеж из: длины этой строки, этой строки
# в верхнем и нижнем регистрах.
def string_info(string):
    # Параметр string будет принимать строку
    string = str(string)
    # result - кортеж из длины введённой строки, этой строки в верхнем и нижнем регистрах
    result = len(string), string.upper(), string.lower()
    # Вызов функции count_calls для подсчёта количества вызовов функции string_info
    count_calls()
    # Функция возвращает result
    return result

# Создам функцию is_contains, которая принимает два аргумента: строку и список. И возвращает True, если строка находится
# в этом списке, False - если отсутствует.
def is_contains(string, list_to_search):
    # Для упрощения поиска все строки переведу в нижний регистр
    string = str(string).lower()
    list_to_search = list(list_to_search)
    # Вызов функции count_calls для подсчёта количества вызовов функции is_contains
    count_calls()
    # Объявил переменную result, которая будет показывать есть ли строка в списке или нет, по умолчанию "нет"
    result = False
    # Создам цикл для поиска строки в списке
    for i in range(len(list_to_search)):
        # Для упрощения поиска список переведу в нижний регистр
        if string == str(list_to_search[i]).lower():
            # Если строка найдена, то прерываю цикл
            result = True
            break
    # Функция возвращает result
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)