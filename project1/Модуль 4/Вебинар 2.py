z = 5
y = 8


def func(t=5, *numbers):
    f = t + 5
    for i in numbers:
        f = f + i

    return f


# через ctrl + лкм можно перейти модуль с функцией
print(func(5, 8, 9, 1, 10))

print(z)
print()


def func2():
    global z, y
    z = 12
    y = 10
    a = z + y
    print(a)


func2()
print(z, y)
print()


# nonlocal

def func3():
    a = 5
    print(a)

    def func4():
        nonlocal a
        a = a + 8

    func4()
    print('Значение локальной переменной изменено:', a)


func3()
