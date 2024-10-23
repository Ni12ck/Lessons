# Задание "Слишком древний шифр":

# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку
# местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками
# для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.

# К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны
# правила для решения этого "ребуса".

# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно
# (делилось без остатка) сумме их значений.

# Пример кратности(деления без остатка):
# 1 + 2 = 3 (сумма пары)
# 9 / 3 = 3 (ровно 3 без остатка)
# 9 кратно 3 (9 делится на 3 без остатка)

# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)

# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)

# К сожалению, у вас не так много времени, чтобы подбирать пароль вручную, шипы сверху уже движутся на вас
# (обожаю клише), тем более числа в первой вставке будут попадаться случайно.

# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20) программа выдавала нужный
# пароль result, для одного введённого числа.

# Все пароли для чисел от 3 до 20 (для сверки):
# 3 - 12
# 4 - 13
# 5 - 1423
# 6 - 121524
# 7 - 162534
# 8 - 13172635
# 9 - 1218273645
# 10 - 141923283746
# 11 - 11029384756
# 12 - 12131511124210394857
# 13 - 112211310495867
# 14 - 1611325212343114105968
# 15 - 1214114232133124115106978
# 16 - 1317115262143531341251161079
# 17 - 11621531441351261171089
# 18 - 12151811724272163631545414513612711810
# 19 - 118217316415514613712811910
# 20 - 13141911923282183731746416515614713812911

# Добавляю randint из функции random
from random import randint

# Создам функцию result, которая будет выводить случайное значение и нужный пароль под это значение
def get_password(first_number):
    # Список second_number будет составляться пароль - значение во второй "каменной вставке"
    second_number = []
    # Создам список пар чисел, сумма которых равна делителям числа из первой вставки
    list_couples = []
    for i in range(1, first_number):
        for j in range(1, first_number):
            # Условия составления списка пар чисел, сумма которых равна делителям числа из первой вставки
            # Число должно делиться на пару без остатка, первое и второе числа в парах разные,
            # эта пара не должна повторяться
            if all([first_number % (i + j) == 0 and i != j and [j, i] not in list_couples]):
                # Заполню список пар чисел, сумма которых равна делителям числа из первой вставки
                list_couples.append([i, j])
    # Добавляю получившиеся значения в список, составляющий пароль
    for i in list_couples:
        second_number.extend(i)
    # Корректный вывод пароля - все элементы second_number записываются в строку без пробелов
    password = ''.join(str(i) for i in second_number)
    # Вывод списка пар, из которых состоят делители
    print('Список пар, из которых состоят делители:', list_couples)
    return password

# Присваиваю переменной random_number случайное число от 3 до 20
random_number = randint(3, 20)
# Вывожу число в первой "каменной вставке".
print('Случайное число из первой вставки:', random_number)
# Вызов функции get_password
result = get_password(random_number)
# Вывод результата
print(f'Результат: {random_number} - {result}')

