# Познакомимся с графической библиотекой tkinter
# Можно изменить название библиотеки для удобства с помощью as "имя"
import tkinter as tk


# Создам функции

# Функция, которая принимает значения
def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2


# Функция очищения и ввода результата, которая принимает value и подставляет в поле для ответа
def clean_and_insert_values(value):
    # Заранее очищаю поле с 0 до конца
    answer_entry.delete(0, 'end')
    # Вставляю результат в поле для ответа с помощью insert
    answer_entry.insert(0, value)  # Тут 0 это индекс, куда надо будет вставить результат


# Функция сложения
def add():
    # Надо получить значения, поэтому использую get, то что получу, будет переводиться в текст, поэтому надо перевести
    # в int для работы с числами
    num1, num2 = get_values()
    # результат выполнения функции
    res = num1 + num2
    # Вызов функции очищения и ввода результата, которая берёт res
    clean_and_insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    clean_and_insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    clean_and_insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    clean_and_insert_values(res)


# Создадим переменную window
window = tk.Tk()

# Название окна
window.title('Калькулятор')
# Размер окна
window.geometry("350x350")
# Окно нельзя будет изменять
window.resizable(False, False)
# Создание виджетов
button_add = tk.Button(window, text="+", width=2, height=2, command=add)
# Место виджета
button_add.place(x=100, y=200)
# Текст, размер, команда для кнопки Button
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)
# Текстовые поля с вводимыми цифрами Entry
number1_entry = tk.Entry(window, width=28)
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=150)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=300)
# Описание полей Label
number1 = tk.Label(window, text="Введите первое число:")
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=125)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=275)
# Запуск цикла обновления событий
window.mainloop()
