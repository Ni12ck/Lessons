# Импортируем модуль sys, чтобы узнать путь

import sys

for path in sys.path:
    print(path)

# И вижу свои директории по которым ходит интерпретатор, чтобы найти модули:
# D:\projects_for_university\Lessons\project1\.venv\Scripts\python.exe "D:\projects_for_university\Lessons\project1\Модуль 4\4.2 лек Модули. Способы импортирования кода.py"
# D:\projects_for_university\Lessons\project1\Модуль 4
# D:\projects_for_university\Lessons\project1
# D:\projects_for_university\Lessons\project1\.venv\Scripts\python313.zip
# C:\Users\*\AppData\Local\Programs\Python\Python313\DLLs
# C:\Users\*\AppData\Local\Programs\Python\Python313\Lib
# C:\Users\*AppData\Local\Programs\Python\Python313
# D:\projects_for_university\Lessons\project1\.venv

# Можно посмотреть все библиотеки в External Libraries - Lib, site-packages

# Нельзя импортировать модули друг из друга, т.е. импортировав что-то из 1 модуля во 2, нельзя уже будет импортировать
# из 2 модуля в 1, т.е. для этого желательно создать третий модуль, в который будут импортироваться сразу 1 и 2

# Импортировать желательно в начале модуля, можно конечно и позднее, всё зависит от логики самого кода