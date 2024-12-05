import io
from pprint import pprint

name = 'Sample71-2.txt'
file = open(name, 'r', encoding='utf-8')
print(f'Можем ли записывать в файл? - {file.writable()}')
print(f'Можем ли прочитать файл? - {file.readable()}')
print(f'Можем ли перемещать курсор в файле? - {file.seekable()}')
print(f'Позиция курсора: {file.tell()}')
print(f'Имя файла: {file.name}')
print(f'Буфер файла: {file.buffer}')
print(f'Файл закрыт? - {file.closed}')
pprint(file.read())
print(f'Позиция курсора: {file.tell()}')
# задаю положение курсора
# file.seek(12)
# file.write('New text')
# print(f'Позиция курсора: {file.tell()}')
file.close()
