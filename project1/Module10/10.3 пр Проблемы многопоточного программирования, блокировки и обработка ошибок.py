# Задача "Банковские операции"

# Необходимо создать класс Bank со следующими свойствами:

# Атрибуты объекта:
# balance - баланс банка (int)
# lock - объект класса Lock для блокировки потоков.

# Методы объекта:
# Метод deposit:
# 1. Будет совершать 100 транзакций пополнения средств.
# 2. Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
# 3. Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
# 4. После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# 5. Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.

# Метод take:
# 1. Будет совершать 100 транзакций снятия.
# 2. Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
# 3. В начале должно выводится сообщение "Запрос на <случайное число>".
# 4. Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив
# balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
# 5. Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и
# заблокировать поток методом acquiere.

# Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
# После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".

# Импортировал threading
import threading
# Импорт randint из random
from random import randint
# Импорт time
import time


# Создал класс Bank
class Bank:
    # Атрибуты объекта класса
    def __init__(self, balance: int):
        self.balance = balance  # баланс банка (int)
        self.lock = threading.Lock()  # объект класса Lock для блокировки потоков

    # Создал метод deposit
    def deposit(self):
        # Будет совершать 100 транзакций пополнения средств
        for i in range(100):
            # Случайное целое число от 50 до 500
            random_num = randint(50, 500)
            # Если баланс больше или равен 500 и замок lock заблокирован lock.locked(), то разблокировать его методом
            # release
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            # Увеличение баланса на случайное целое число от 50 до 500
            self.balance += random_num
            # Вывод строки "Пополнение: <случайное число>. Баланс: <текущий баланс>"
            print(f'Пополнение: {random_num}. Баланс: {self.balance}')
            # Поставил ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения
            time.sleep(0.001)

    # Создал метод take
    def take(self):
        # Будет совершать 100 транзакций снятия
        for i in range(100):
            # Случайное целое число от 50 до 500
            random_num = randint(50, 500)
            # Вывод сообщения "Запрос на <случайное число>"
            print(f'Запрос на {random_num}')
            # Если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на
            # соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>"
            if random_num <= self.balance:
                self.balance -= random_num
                print(f'Снятие: {random_num}. Баланс: {self.balance}')
            # Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и
            # заблокировать поток методом acquiere.
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            # Поставил ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения
            time.sleep(0.001)


# Пример результата выполнения программы
bk = Bank(100)

# Создание потоков
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Приостановил основной поток
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')
