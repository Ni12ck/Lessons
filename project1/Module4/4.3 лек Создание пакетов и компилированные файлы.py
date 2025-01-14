# Все данные связанные с импортируемыми модулями хранятся в __pycache__

from dis import dis


def some_func():
    a = 'Я из второго модуля'
    print('Я из второго модуля')
    return a


dis(some_func)

# dis отображает байт код
#  6           RESUME                   0
#
#  7           LOAD_CONST               1 ('Я из второго модуля')
#              STORE_FAST               0 (a)
#
#  8           LOAD_GLOBAL              1 (print + NULL)
#              LOAD_CONST               1 ('Я из второго модуля')
#              CALL                     1
#              POP_TOP
#
#  9           LOAD_FAST                0 (a)
#              RETURN_VALUE

# Для группировки модулей по тем или иным свойствам существуют пакеты
# Например можно создать папку с модулями, откуда уже буду импортировать

from Modules import module_2
# или
from Modules.module_2 import say_hi

# Пакет — это директория, которая по сути такая же, как и наша "modules". Единственным отличием пакета от обычной папки
# является наличие внутри файла "__init__.py" с двойным подчеркиванием. Когда мы создали файл "__init__.py", мы
# заметили, что на изображении нашей папки "modules" появился кружочек. Этот кружочек обозначает, что наш модуль, или
# наша папка, теперь стала пакетом.

# Существует особенность: когда мы импортируем пакет или взаимодействуем с ним, код из файла "__init__.py" с двойным
# подчеркиванием начинает выполняться. Это происходит аналогично тому, как происходит выполнение кода при импорте
# какого-либо модуля, где вся информация из модуля считывается и выполняется. В случае с файлом "__init__.py" также
# считывается и выполняется код, содержащийся в этом файле.

# Создал module_3 и вижу в нём исполнение кода из файла "__init__.py"
