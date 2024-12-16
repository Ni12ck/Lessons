# Функция для работы с переменными в текстовом файле
def calc(line):
    # Три переменные в строке файле, разделённые пробелом
    variable_1, operation, variable_2 = line.split(' ')
    variable_1 = int(variable_1)
    variable_2 = int(variable_2)
    # print(variable_1, variable_2, operation)
    # Математические действия
    if operation == '+':
        print(f'Результат: {variable_1 + variable_2}')
    if operation == '-':
        print(f'Результат: {variable_1 - variable_2}')
    if operation == '*':
        print(f'Результат: {variable_1 * variable_2}')
    if operation == '%':
        print(f'Результат: {variable_1 % variable_2}')
    if operation == '/':
        print(f'Результат: {variable_1 / variable_2}')
    if operation == '//':
        print(f'Результат: {variable_1 // variable_2}')


# Счётчик строк
count = 0

# Работа функции с файлом
with open('data.txt', 'r') as file:
    for line in file:
        count += 1
        # Отлов ошибок
        try:
            calc(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Возникла ошибка в строке {count}, не хватает данных для ответа')
            else:
                print(f'Возникла ошибка в строке {count}, невозможно перевести переменную в число')
        # print(f'Возникла ошибка {exc} с параметрами {exc.args} в строке {count}')
