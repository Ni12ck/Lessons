# библиотека для логирования
import logging

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        a / b
        logging.info(f'Delenie {a} na {b}')
        return a / b
    except ZeroDivisionError as err:
        logging.error('Delenie na nol', exc_info=True)
        return 0

def sqrt(a):
    return a**0.5

def pow(a,b):
    return a**b

if __name__ == '__main__':
    # print(add(100, 3))
    # Запись в файл
    logging.basicConfig(level=logging.INFO, filemode='w',filename='logs.log',
                        format='%(asctime)s | %(levelname)s | %(message)s' )
    # logging.debug('Сообщения уровня') # Сообщения уровня
    # logging.info('Информационные сообщения') #  Информационные сообщения
    # logging.warning('Сообщения уровня предупреждений') # Сообщения уровня предупреждений
    # logging.error('Сообщения уровня ошибок') # Сообщения уровня ошибок
    # # Сообщения уровня критических ошибок, указывающих на серьезные проблемы
    # logging.critical('Сообщения уровня критических ошибок, указывающих на серьезные проблемы')

print(div(3,4))
print(div(3,0))