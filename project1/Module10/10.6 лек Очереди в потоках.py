from queue import Queue
import time
import threading


def getter(queue):
    while True:
        time.sleep(5)
        item = queue.get()
        print(threading.current_thread(), 'Взял элемент', item)
        queue.put(1)


# Объект класса Queue
q = Queue(maxsize=10)  # maxsize - максимальный размер очереди

# Чтобы программа в случае основного потока действий могла завершиться, добавим параметр «daemon» и установим его на
# «True»
thread1 = threading.Thread(target=getter, args=(q,), daemon=True)
thread1.start()

# # Положил элемент в очередь
# q.put(5)
# # Выбрать элемент из очереди
# print(q.get(timeout=2))  # _queue.Empty, так как очередь пустая
# print('Конец программы')

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(), 'положил в очередь элемент', i)