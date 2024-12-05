# Задача "Записать и запомнить":
# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
# Функция должна:
# 1. Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# 2. Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением
# - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.

# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.


# Функция custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи в файл file_name
def custom_write(file_name, strings):
    strings_positions = {}  # Словарь strings_positions
    # Открытие файла file_name для записи в кодировке 'utf-8'
    with open(file_name, 'w', encoding='utf-8') as file:
        # Создаю пары, состоящие элементов списка strings и счётчика с номера 1
        for i, string in enumerate(strings, start=1):
            file_tell = file.tell()  # Позиция курсора
            file.write(f'{string}\n')  # Запись в файл file_name всех строк из списка strings, каждая на новой строке
            strings_positions[(i, file_tell)] = string  # Присвоение номера строки и позиции курсора строке из списка
        file.close() # Закрытие файла file_name
        # Возвращаю словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а
        # значением записываемая строка
        return strings_positions


# Пример выполняемого кода:
# Список строк для записи
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
# Запись строк в файл 'test.txt'
result = custom_write('test.txt', info)
# Вывод элементов
for elem in result.items():
    print(elem)
