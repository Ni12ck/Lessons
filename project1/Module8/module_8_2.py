# Задача "План перехват":

# Напишите 2 функции:

# Функция personal_sum(numbers):
# 1. Должна принимать коллекцию numbers.
# 2. Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
# 3. Если же при переборе встречается данное типа отличного от числового, то обработать исключение TypeError, увеличив
# счётчик incorrect_data на 1.
# 4. В конечном итоге функция возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - кол-во
# некорректных данных.

# Функция calculate_average(numbers)
# Среднее арифметическое - сумма всех данных делённая на их количество.
# 1. Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
# 2. Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
# 3. Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError при делении на 0 и
# верните 0.
# 4. Также в numbers может быть записана не коллекция, а другие типы данных, например числа. Обработайте исключение
# TypeError выводя строку 'В numbers записан некорректный тип данных'. В таком случае функция просто вернёт None.


# Создал функцию personal_sum(numbers), которая должна принимать коллекцию numbers
def personal_sum(numbers):
    # Счётчик result, в который будет записываться сумма чисел из коллекции numbers
    result = 0
    # Счётчик incorrect_data, в который будет записываться количество ошибок TypeError
    incorrect_data = 0
    # Цикл прибавления чисел к счётчику result
    for number in numbers:
        try:
            result += number
        # Блок except, в котором описаны действия при возникновении ошибки TypeError в блоке try
        except TypeError:
            incorrect_data += 1
            # Раскомментировать для вывода как в примере
            # print(f'Некорректный тип данных для подсчёта суммы - {number}')
    # Возвращает кортеж из двух значений: result - сумма чисел, incorrect_data - количество некорректных данных.
    return result, incorrect_data


# Создал функцию calculate_average(numbers), которая должна принимать коллекцию numbers и возвращать: среднее
# арифметическое всех чисел
def calculate_average(numbers):
    try:
        # result - сумма чисел, incorrect_data - количество некорректных данных
        result, incorrect_data = personal_sum(numbers)
        # avg - среднее арифметическое
        # Тут количество чисел - разность длины numbers и количества некорректных данных
        avg = result / (len(numbers) - incorrect_data)
        return avg
    # Блок except, в котором описаны действия при возникновении ошибки ZeroDivisionError в блоке try
    except ZeroDivisionError:
        return 0
    # Блок except, в котором описаны действия при возникновении ошибки TypeError в блоке try
    except TypeError:
        return print(f'В numbers записан некорректный тип данных')


# Пример выполнения программы:
print(f'1) Строка перебирается, но каждый символ - строковый тип: {calculate_average("1, 2, 3")}')
print(f'2) Учитываются только 1 и 3: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'3) Передана не коллекция: {calculate_average(567)}')
print(f'4) Всё должно работать: {calculate_average([42, 15, 36, 13])}')
print(f'5) Пустая коллекция numbers: {calculate_average([])}')
