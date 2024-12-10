# Реализация собственного проводника

import tkinter

# Импорт модуля os
import os

# Импорт работы с диалоговыми окнами
from tkinter import filedialog


# Функция вызова диалогового окна
def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл',
                                          filetypes=(('Текстовый файл', '.txt'), ('Все файлы', '*')))
    # к тексту добавляем название файла
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)


# Создаю главное окно
window = tkinter.Tk()

# Заголовок окна
window.title('Проводник')

# Размер окна
window.geometry('350x150')

# Задний фон
window.configure(bg='purple')

# Запрет изменять размер
window.resizable(False, False)

# Текст
text = tkinter.Label(window, text='Файл:', height=3, width=50, background='white', foreground='black')

# Расположение текста по сетке
text.grid(column=1, row=1)

# Создание кнопки
button_select = tkinter.Button(window, height=3, width=15, text='Выбрать файл', background='silver',
                               command=file_select)

# Расположение кнопки по сетке
button_select.grid(column=1, row=2, pady=5)

# Постоянное обновление окна
window.mainloop()
