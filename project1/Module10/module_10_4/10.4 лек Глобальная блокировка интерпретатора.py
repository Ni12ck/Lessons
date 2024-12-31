# GIL (Global Interpreter Lock) - глобальная блокировка интерпретатора. Эта концепция была придумана много лет назад,
# когда ещё не было ясно, будут ли процессоры многоядерными или продолжат развивать мощности одноядерных процессоров.
# GIL был введён в Python для упрощения работы с памятью и сторонними библиотеками. Однако он имеет существенный
# недостаток — он блокирует работу интерпретатора.
from threading import Thread


def count_up(name, n):
    for i in range(n):
        print(name, i, sep=': ')


t1 = Thread(target=count_up, args=('Thread1', 20))
t2 = Thread(target=count_up, args=('Thread2', 20))

t1.start()
t2.start()

t1.join()
t2.join()
