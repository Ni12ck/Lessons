# Задача "Рассылка писем":

# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя
# (администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.

# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный
# аргумент со значением по умолчанию - отправитель.

# Внутри функции реализовать следующую логику:
# 1. Проверка на корректность e-mail отправителя и получателя.
# 2. Проверка на отправку самому себе.
# 3. Проверка на отправителя по умолчанию.

# Пункты задачи:

# 1. Создайте функцию send_email, которая принимает 2 обычных аргумента: message(сообщение), recipient(получатель) и 1
# обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
# 2. Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net", то вывести на
# экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
# 3. Если же sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
# 4. Если же отправитель по умолчанию - university.help@gmail.com, то вывести сообщение: "Письмо успешно отправлено с
# адреса <sender> на адрес <recipient>."
# 5. В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес
# <recipient>."
# 6. Здесь <sender> и <recipient> - значения хранящиеся в этих переменных.
# 7. За один вызов функции выводится только одно и перечисленных уведомлений! Проверки перечислены по мере выполнения.

# Пример результата выполнения программы:

# Пример выполняемого кода (тесты):
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!

#Создаю функцию с трема аргументами message(сообщение), recipient(получатель) и 1 обязательно именованный аргумент со
# значением по умолчанию sender = "university.help@gmail.com".
def send_email(message, recipient, sender = "university.help@gmail.com"):
    # Проверка - есть ли в троке '@'
    if not all(['@' in recipient, '@' in sender,
                # Проверки на окончание строки
                recipient.endswith('.ru') or
                recipient.endswith('.com') or
                recipient.endswith('.net'),
                sender.endswith('.ru') or
                sender.endswith('.com') or
                sender.endswith('.net')]):
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient + '.')
    # Условие, если при котором sender и recipient совпадают, то вывести "Нельзя отправить письмо самому себе!"
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    # Условие, если при котором отправитель по умолчанию - university.help@gmail.com, то вывести сообщение:
    # "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient + '.')
    # Условие, если при котором почта отправителя отличается от university.help@gmail.com
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient + '.')

# Проверочные примеры вызовов функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')