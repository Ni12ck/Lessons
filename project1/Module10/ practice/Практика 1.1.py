# Иллюзия, что на выполнение тратиться разное время
import random
import threading
import time
from threading import Thread
import queue


class Bulka(Thread):

    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count

    # Реализация run для того, чтобы работал start
    def run(self):
        while self.count:
            time.sleep(random.randint(1, 2))
            if random.random() > 0.9:  # шанс 10%
                self.queue.put('Подгорелая булка')
            else:
                self.queue.put('Нормальная булка')


class Kotleta(Thread):

    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count  # контроль количества бургеров

    def run(self):
        while self.count:
            print('Готовых булок:', self.queue.qsize())
            bulka = self.queue.get()
            if bulka == 'Нормальная булка':
                time.sleep(random.randint(1, 2))
                self.count -= 1
            print(f'Осталось булок для приготовления: {self.count}')



# Создание очереди
queue = queue.Queue(maxsize=10)  # на подносе может быть 10 булок

thread1 = Bulka(queue, 25)
thread2 = Kotleta(queue, 20)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
