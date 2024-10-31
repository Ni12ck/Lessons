# int()  --> int(input()) - просим ввод данных от человека
# bool()
# str()
# list()
# tuple() - кортеж
# dict() -  словарь
# set() - множество

# Если передадим любую строку кроме пустой, например: bool('a') - получим True
# Если передадим пустую строку bool('') - получим False
# Если передадим любое число, кроме 0, например bool(2) - получим True
# Если передадим число 0: bool(0) - получим False
# Если передадим пустой тип bool(None) - получим False

# # Пример неявного преобразования типа переменной
# type_1 = 1
# type_2 = 0
# if type_1:
#     print('type_1: ok')
# if type_2:
#     print('type_2: ok')
# # Переменные type_1 и type_2 приняли тип bool. 1 - True, 0 - False

# Можно передать в консоль список list('abcde'), в результате получим список - ['a', 'b', 'c', 'd', 'e']
# Можно передать в консоль кортеж tuple('abcde'), в результате получим кортеж - ('a', 'b', 'c', 'd', 'e')

# Перейдём к практическому примеру
# Создам список salary с зарплатами
salary = [2300, 1800.801234, 5000, 1234.583434, 7500.122323]
# Необходимо найти количество зарплат, среднюю зарплату, максимальную, минимальную и создать словарь
print('Количество зарплат:', len(salary))
print('Сумма зарплат (округлённая до двух знаков после запятой):', round(sum(salary), 2))
print('Средняя зарплата (округлённая до трёх знаков после запятой):', round(sum(salary) / len(salary), 3))
print('Максимальная зарплата:', max(salary))
print('Минимальная зарплата:', min(salary))

# Создам словарик с именами и зарплатами, объединив два списка с помощью zip
names = ['Андрей', 'Антон', 'Наташа', 'Вася', 'Вова']
zipped = dict(zip(names, salary))  # также можно создать список list(zip(names, salary))
print('Словарь из имён и зарплат:', dict(zipped))
# Можно вытаскивать значения по ключу
print('Зарплата Вовы:', zipped['Вова'])
