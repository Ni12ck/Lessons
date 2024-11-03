# Познакомимся с графической библиотекой tkinter
# Можно изменить название библиотеки для удобства с помощью as "имя"
import tkinter as tk

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
