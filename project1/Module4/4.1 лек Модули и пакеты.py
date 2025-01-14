# По сути каждый файл с расширением py является модулем, который может отвечать за какую-то часть программы, за функции
# внутри программы, их разделяют по модулям, чтобы было проще ориентироваться в коде. Чтобы было проще отладить код,
# чтобы если появится ошибка, то можно было ещё проще найти в определённом модуле. Чтобы можно было подключать нужные,
# уже готовые модули к другим проектам.


# Импорт второго модуля, названия модулей желательно писать на английском языке без пробелов
# Можно добавить "псевдоним" для модуля с помощью as, в данной ситуации модуль module_2 будет называться m2
# Импортируются все команды из модуля - print('Такого быть не должно') выполнилось, хотя я не вызывал этот print
import module_2 as m2

# Пример модуля
print('Привет, я из модуля 1')
print()

# Вывод переменной "a" из второго модуля
print('Вывод переменной "a" из второго модуля:', m2.a)

# Вызов функции say_hi() из второго модуля
m2.say_hi()

print()

# Можно ещё импортировать отдельные функции из модуля, а не все сразу. При этом не надо будет использовать префикс
# Т.е. Не надо будет писать m2.say_hi(), а сразу say_hi()
# Можно импортировать всё с помощью *, т.е from module_2 import *

from module_2 import say_hi

print('Вызов функции say_hi из module_2')
say_hi()

# Вывод нежелательного кода из второго модуля nej
print(m2.nej)
print()

# Можно присваивать название и элементам из модулей
from module_2  import say_hi as sh
print('Вызов функции sh из module_2')
sh()
