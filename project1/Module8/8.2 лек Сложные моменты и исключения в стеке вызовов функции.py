# Пример 1
# def f1(number):
#     return 10 / number
#
#
# def f2():
#     print('Какой хороший день')
#     result_f1 = f1(0)
#     return result_f1
#
#
# try:
#     total = f2()
#     print(total)
# except ZeroDivisionError as exc:
#     print(f'Вот, что пошло не так - {exc}')


# Пример 2
# def f1(number):
#     return 10 / number
#
#
# def f2():
#     print('Какой хороший день')
#     summ = 0
#     for i in range(-2, 2):
#         summ += f1(i)
#         print(summ)
#     # в return ничего не сохранилось
#     return summ
#
#
# try:
#     total = f2()
# except ZeroDivisionError as exc:
#     print(f'Вот, что пошло не так - {exc}')


# Пример 3
# def f1(number):
#     return 10 / number
#
#
# def f2():
#     print('Какой хороший день')
#     summ = 0
#     for i in range(-2, 2, 1):
#         try:
#             summ += f1(i)
#             print(summ)
#         except ZeroDivisionError as exc:
#             print(f'Внутри функции f1 что-то пошло не так - {exc}')
#     return summ / 1
#
#
# try:
#     total = f2()
#     print(f'Вот результат функции: {total}')
# except ZeroDivisionError as exc:
#     print(f'Внутри функции f2 что-то пошло не так - {exc}')


# Пример 4
def f1(number):
    return total / number


def f2():
    try:
        result_f1 = f1(0)
        print(result_f1)
    except ZeroDivisionError as exc:
        print(f'Внутри функции f1 что-то пошло не так - {exc}')
    return result_f1 / 0


try:
    f2()
except NameError as exc:
    print(f'Внутри функции f2 что-то пошло не так - {exc}')
