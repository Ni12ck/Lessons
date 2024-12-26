def say_hi():
    print('Я из функции во втором модуле')
    from random import randint
    # Тут randint создаётся только внутри функции и не может работать вне функции
    print('Импортированный randint:',randint(1, 10))


a = 5
b = 10


def nej():
    print('Такого быть не должно')

if __name__ == '__nej__':
    nej()
