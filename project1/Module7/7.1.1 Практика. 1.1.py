# Реализация собственного проводника

import tkinter

# Создаю главное окно
window = tkinter.Tk()

# Заголовок окна
window.title('Проводник')

# Размер окна
window.geometry('350x350')

# Задний фон
window.configure(bg='purple')

# Запрет изменять размер
window.resizable(False, False)

# Текст
text = tkinter.Label(window, text='Файл:', height=3, width=15, background='silver')

# Расположение текста по сетке
text.grid(column=1, row=1)

# Создание кнопки
button_select = tkinter.Button(window, height=3, width=15, text='Выбрать файл', background='silver')

# Расположение кнопки по сетке
button_select.grid(column=1, row=2)

# Постоянное обновление окна
window.mainloop()
