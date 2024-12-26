# Кортеж, такая же коллекция как и список, но она неизменяемая
set_of_variable_values1 = 1, 2, 3, 4, 5
set_of_variable_values2 = (1, 2, 3, 4, 5)
print('Кортеж 1:', set_of_variable_values1)
print('Кортеж 2:', set_of_variable_values2)
set_of_variable_values3 = tuple([1, 2, 3, 4, 5])
print('Кортеж 3:', set_of_variable_values3)
print(type(set_of_variable_values1), type(set_of_variable_values2), type(set_of_variable_values3))
# Также можно вводить элементы разных типов
set_of_variable_values4 = 1, 2, 3, 'coconut', 5.1, True
print('Кортеж 4:', set_of_variable_values4)
# Можно выводить элементы кортежа
print(set_of_variable_values4[3])
# но изменить его нельзя
# set_of_variable_values4[3] = 'milk'
# выдаст ошибку:
# Traceback (most recent call last):
    #   File "D:\projects_for_university\Lessons\project1\Модуль 1\1.6 лек Изменяемые и неизменяемые объекты. Кортежи.py", line 15, in <module>
    #     set_of_variable_values4[3] = 'milk'
#     ~~~~~~~~~~~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
# Плюс кортежей в том, что они занимают меньше места, чем списки
# Например, создам список точно такой же как кортеж 4
list_set_of_variable_values4 = [1, 2, 3, 'coconut', 5.1, True]
# Сравним список и кортеж
print('Размер списка:',list_set_of_variable_values4.__sizeof__())
print('Размер кортежа:', set_of_variable_values4.__sizeof__())
print('Сравнение список больше кортежа? -', list_set_of_variable_values4.__sizeof__() > set_of_variable_values4.__sizeof__())
# Сам кортеж неизменяемый, но он может хранить изменяемые объекты
# В моём случае это список [1, 2, 3, 4, 5]
set_of_variable_values5 = ([1, 2, 3, 4, 5], 0)
print('Кортеж 5 с изменяемым объектом:', set_of_variable_values5)
# Попытаюсь изменить объект в кортеже
set_of_variable_values5[0][4] = 123
print('5-ый элемент в первом объекте должен был измениться на 123:', set_of_variable_values5[0])
# Кортежи также поддерживают сложение и умножение
set_of_variable_values6 = set_of_variable_values5 + (6,7)
print('Кортеж 6 - сложение пятого кортежа с (6,7):',set_of_variable_values6)
set_of_variable_values7 = set_of_variable_values5 * 2
print('Кортеж 7 - умножение пятого кортежа на 2:',set_of_variable_values7)