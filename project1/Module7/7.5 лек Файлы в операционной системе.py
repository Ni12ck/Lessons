# Модуль os
import os

# Можно получить абсолютный путь:
print(f'Текущая директория: {os.getcwd()}')

# exists - существует
if os.path.exists('test7-5'):
    # change dir
    os.chdir('test7-5')
else:
    # Создание папки
    os.mkdir('test7-5')
    os.chdir('test7-5')

print(f'Текущая директория: {os.getcwd()}')
# создание директорий
# os.makedirs(r'test7-51\'test7-52')

# Просмотр вложенности
# for i in os.walk('.'):
#     print(i)

os.chdir(r'D:\projects_for_university\Lessons\project1\Module7')
print(f'Текущая директория: {os.getcwd()}')

# Списки файлов и папок
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)

# Запуск файла
# os.startfile(file[14])

# Информация о файле
print(os.stat(file[14]))
# Например, размер
print(f'Размер файла: {os.stat(file[14]).st_size} байт(а)')

# Можно запускать даже команды системы
# os.system('pip install random2')
