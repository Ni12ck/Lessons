# Задача "Потоки гостей в кафе":
# Необходимо имитировать ситуацию с посещением гостями кафе.
# Создайте 3 класса: Table, Guest и Cafe.
import queue
# I
# Класс Table:
# 1. Объекты этого класса должны создаваться следующим способом - Table(1)
# 2. Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)

# II
# Класс Guest:
# 1. Должен наследоваться от класса Thread (быть потоком).
# 2. Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
# 3. Обладать атрибутом name - имя гостя.
# 4. Обладать методом run, где происходит ожидание случайным образом от 3 до 10 секунд.

# III
# Класс Cafe:
# 1. Объекты этого класса должны создаваться следующим способом - Cafe(Table(1), Table(2),....)
# 2. Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
# 3. Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).

# Метод guest_arrival(self, *guests):
# 1. Должен принимать неограниченное кол-во гостей (объектов класса Guest).
# 2. Далее, если есть свободный стол, то сажать гостя за стол (назначать столу guest), запускать поток гостя и выводить
# на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
# 3. Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение
# "<имя гостя> в очереди".

# Метод discuss_guests(self):
# Этот метод имитирует процесс обслуживания гостей.
# 1. Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
# 2. Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то
# вывести строки "<имя гостя за текущим столом> покушал(-а) и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же
# текущий стол освобождается (table.guest = None).
# 3. Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается
# гость взятый из очереди (queue.get()). Далее выводится строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а)
# за стол номер <номер стола>"
# 4. Далее запустить поток этого гостя (start)

# Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
# 1. Table - стол, хранит информацию о находящемся за ним гостем (Guest).
# 2. Guest - гость, поток, при запуске которого происходит задержка от 3 до 10 секунд.
# 3. Cafe - кафе, в котором есть определённое кол-во столов и происходит имитация прибытия гостей (guest_arrival) и их
# обслуживания (discuss_guests).

# Импортировал threading
import threading
# Импортировал time
import time
# Импортировал Queue
from queue import Queue
# Импортировал randint
from random import randint


# Создал класс Table
class Table:
    # Атрибуты объекта класса
    def __init__(self, number: int):
        self.number = number  # номер стола
        self.guest = None  # гость, который сидит за этим столом


# Создал класс Guest
class Guest(threading.Thread):
    # Атрибуты объекта класса
    def __init__(self, name):
        super().__init__()  # вызов конструктора родительского класса
        self.name = name  # имя гостя

    # Метод run, где происходит ожидание случайным образом от 3 до 10 секунд
    def run(self):
        time.sleep(randint(3, 10))


# Создал класс Cafe
class Cafe:
    # Атрибуты объекта класса
    def __init__(self, *table):
        self.queue = Queue()  # очередь (объект класса Queue)
        self.tables = list(table)  # столы в этом кафе

    # Создал метод guest_arrival (прибытие гостей)
    def guest_arrival(self, *guests):
        for guest in guests:
            for table in self.tables:
                # Если есть свободный стол, то сажаем гостя за стол (назначаем столу guest)
                if table.guest is None:
                    table.guest = guest
                    # Запуск потока гостя
                    guest.start()
                    # Вывод строки "<имя гостя> сел(-а) за стол номер <номер стола>"
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    break
            else:
                # Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    # Первый вариант метода discuss_guests
    # Создал метод discuss_guests (обслужить гостей)
    def discuss_guests(self):
        while not self.queue.empty() or self.search_table():
            for table in self.tables:
                # Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод
                # is_alive)
                if table.guest is not None and not table.guest.is_alive():
                    # Вывод строки "<имя гостя за текущим столом> покушал(-а)
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    # Вывод строки "Стол номер <номер стола> свободен"
                    print(f'Стол номер {table.number} свободен')
                    # Текущий стол освобождается (table.guest = None)
                    table.guest = None
                    # Если очередь ещё не пуста (метод empty) и один из столов освободился (None)
                    if not self.queue.empty():
                        # текущему столу присваивается гость взятый из очереди (queue.get())
                        table.guest = self.queue.get()
                        # Вывод строки "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер
                        # стола>"
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        # Запуск потока этого гостя (start)
                        table.guest.start()

    # Метод поиска свободного стола
    def search_table(self):
        for table in self.tables:
            if table.guest is not None:
                return True
        return False

    # Второй вариант метода discuss_guests
    # Создал метод discuss_guests (обслужить гостей)
    def discuss_guests_recursive(self):
        is_guests_active = False
        for table in self.tables:
            # Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод
            # is_alive)
            if table.guest is not None and not table.guest.is_alive():
                # Вывод строки "<имя гостя за текущим столом> покушал(-а)
                print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                # Вывод строки "Стол номер <номер стола> свободен"
                print(f'Стол номер {table.number} свободен')
                # Текущий стол освобождается (table.guest = None)
                table.guest = None
                # Если очередь ещё не пуста (метод empty) и один из столов освободился (None)
                if not self.queue.empty():
                    # текущему столу присваивается гость взятый из очереди (queue.get())
                    table.guest = self.queue.get()
                    # Вывод строки "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер
                    # стола>"
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    # Запуск потока этого гостя (start)
                    table.guest.start()
            if table.guest is not None:
                is_guests_active = True
        if is_guests_active or not self.queue.empty():
            # Ожидание, чтобы не достигнуть максимального лимита рекурсии
            time.sleep(0.3)
            self.discuss_guests_recursive()


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
                'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
# Первый вариант метода discuss_guests
# cafe.discuss_guests()
# Второй вариант метода discuss_guests
cafe.discuss_guests_recursive()
