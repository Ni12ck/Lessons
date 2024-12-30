# Состояние гонки и взаимная блокировка
# При общем значении несколько потоков могут пытаться работать с одной переменной

import threading
from logging import exception

counter = 0
lock = threading.Lock()
print(lock.locked())


def increment(name):  # функция увеличения принимает имя потока
    global counter
    # Можно ещё добавить отлов ошибок
    try:
        lock.acquire()  # Метод acquire ставит блокировку
        for i in range(10):
            counter += 1
            print(name, counter, lock.locked())  # lock.locked() - статус блокировки
    except Exception:
        pass
    finally:
        lock.release()  # Метод release снимает блокировку


# def decrement(name):  # функция уменьшения принимает имя потока
#     global counter
#     lock.acquire()  # Метод acquire ставит блокировку
#     for i in range(10):
#         counter -= 1
#         print(name, counter, lock.locked())  # lock.locked() - статус блокировки
#     lock.release()  # Метод release снимает блокировку

# Второй вариант написания блокировки
def decrement(name):  # функция уменьшения принимает имя потока
    global counter
    with lock:  # ставит и снимает блокировку (более компактный способ работы с локом)
        for i in range(10):
            counter -= 1
            print(name, counter, lock.locked())  # lock.locked() - статус блокировки


# Создание потоков для демонстрации
thread_1 = threading.Thread(target=increment, args=('thread_1',))
thread_2 = threading.Thread(target=decrement, args=('thread_2',))
thread_3 = threading.Thread(target=increment, args=('thread_3',))
thread_4 = threading.Thread(target=decrement, args=('thread_4',))

# Запуск потоков
thread_1.start()
thread_3.start()
thread_2.start()
thread_4.start()
