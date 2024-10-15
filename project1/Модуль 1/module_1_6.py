# 2. Работа со словарями:
# 2.1 Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
my_dict = {'Владимир': 1995, 'Наташа': 1992, 'Андрей': 1994, 'Витя': 2011}
# 2.2 Выведите на экран словарь my_dict.
print('Словарь годов:', my_dict)
# 2.3 Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
print('Значение по существующему ключу "Владимир":', my_dict.get('Владимир', 'Такого года рождения нет'))
print('Значение по отсутствующему ключу "Сергей":', my_dict.get('Сергей', 'Такого года рождения нет'))
# 2.4 Добавьте ещё две произвольные пары того же формата в словарь my_dict.
my_dict.update({'Арина': 1989, 'Влад': 2002})
# 2.5 Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
Vitya_pop = my_dict.pop('Витя')
print('Год рождения Вити:', Vitya_pop)
# 2.6 Выведите на экран словарь my_dict.
print('Словарь годов:', my_dict)

print()

# 3. Работа с множествами:
# 3.1 Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
my_set = {1, 2, 3, 4, 5, 1, 3, 4, 2, 'значение', True, 1.5, (1, 2, 3, 4)}
# 3.2 Выведите на экран множество my_set (должны отобразиться только уникальные значения).
print('Множество my_set:', my_set)
# 3.2 Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
print('Добавление двух элементов "0" и "7":', my_set.update([0,7]))
# 3.3 Удалите один любой элемент из множества my_set.
print('Удаление из множества my_set элемента "1" с помощью discard:', my_set.discard(1))
# Второй вариант удаления: print('Удаление из множества my_set элемента "1" с помощью remove:', my_set.remove(1))
# 3.4 Выведите на экран измененное множество my_set.
print('Изменённое множество my_set:', my_set)
