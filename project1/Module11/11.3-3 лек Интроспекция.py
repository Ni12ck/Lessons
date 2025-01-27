# Полезный системный пакет - sys
import sys
from pprint import pprint
print(dir(sys))

# Путь к интерпретатору python
print(f'Путь к интерпретатору python: {sys.executable}')

# В какой операционной системе мы работаем
print(f'В какой операционной системе мы работаем: {sys.platform}')

# Текущая версия Python
print(f'Текущая версия Python: {sys.version}')
print(sys.version_info)

# Список, содержащий параметры командной строки, если она была задана
print(f'Список, содержащий параметры командной строки, если она была задана: {sys.argv}')

# Путь поиска модуля, список каталогов, в которых Python будет искать модуля во время импорта
print(f'Путь поиска модуля, список каталогов, в которых Python будет искать модуля во время импорта: '
      f'\n{sys.path}')

# Словарь, который отображает имена модулей в объекты модулей для всех загруженных в данный момент модулей
print(f'Словарь, который отображает имена модулей в объекты модулей для всех загруженных в данный момент модулей: '
      f'\n{sys.modules}')

# Стоит упомянуть __builtins__ - псевдо-модуль, содержащий в интерпретатор объекты (константы, исключения, функции)
print(f'Псевдо-модуль __builtins__: {__builtins__}')
print(dir(__builtins__))
print()

print('Первый пример')
def func(x):
    if sys.version.split(' ')[0] == '3.13.0':
        return x + 10
    else:
        raise Exception('Недопустимая версия')

print(f'Если версия питона 3.13.0, то получу результат: {func(10)}\n')

# sys используется не только для того, чтобы узнавать новую информацию
print('Второй пример')
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
# Увеличение максимального значения рекурсии
sys.setrecursionlimit(5000)
# Увеличение символов в строке
sys.set_int_max_str_digits(10000)
print(f'Факториал 2000!: {factorial(2000)}')
print(f'Размер в байтах функции factorial: {sys.getsizeof(factorial)} байт')
