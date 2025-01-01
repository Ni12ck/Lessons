import threading
import time
import sys

print('Первый пример')


def some_func():
    time.sleep(0.5)
    raise Exception


def thread_func():
    try:
        some_func()
    except Exception as exc:
        print('Wow! Exception!')


t1 = threading.Thread(target=thread_func())
t2 = threading.Thread(target=thread_func())

t1.start()
t2.start()

t1.join()
t2.join()
print()

print('Второй пример')


# Еxcepthook — это функция, которая вызывается при любой ошибке в модуле «threading»

def excepthook_exmpl(arg):
    print(arg.thread.is_alive())
    print(arg.thread.name)


threading.excepthook = excepthook_exmpl

t3 = threading.Thread(target=some_func)
t4 = threading.Thread(target=some_func)

t3.start()
t4.start()

t3.join()
t4.join()
print()

print('Третий пример с hook из sys')


def excepthook_exmpl_2(arg, a, b):  # системный hook принимает три аргумента и ловит ошибки только основного потока
    print('hook из третьего примера')


sys.excepthook = excepthook_exmpl_2

raise Exception
