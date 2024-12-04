# Функция «pprint» позволяет выводить информацию в терминал в более удобочитаемом формате
from pprint import pprint

name = 'Sample71.txt'
file = open(name, 'r')  # «r», «w» и «a». «r» — это чтение (от слова «read»), «w» — запись (от слова «write»),
# а «a» — добавление (от слова «append»)
# print(file)  # <_io.TextIOWrapper name='Sample71.txt' mode='r' - режим открытия encoding='cp1252'> - кодировка
print(file.tell())  # tell() показывает положение курсора
pprint(file.read())
print(file.seek(22)) # seek() передвигает курсор
pprint(file.read())
file.close()

name2 = 'Sample71-2.txt'
# file2 = open(name2, 'w')
file2 = open(name2, 'a')
# file2.write('\nHello Sample-2')
file2.close()
