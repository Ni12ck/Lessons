# 1. Создайте новую функцию test_function
# 2. Создайте внутри test_function другую функцию - inner_function, Эта функция должна печатать значение "Я в области
# видимости функции test_function"
# 3. Вызовите функцию inner_function внутри функции test_function
# 4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

# Создал новую функцию test_function
def test_function():
    # Создал внутри новую функцию inner_function
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызовите функцию inner_function внутри функции test_function
    inner_function()


# Если вызвать test_function, то получу результат работы вложенной функции inner_function:
# Я в области видимости функции test_function
test_function()

# Вызываю функцию inner_function внутри функции test_function
inner_function()

# Получил ошибку при вызове inner_function, потому что test_function объемлющая для inner_function:
# Traceback (most recent call last):
#   File "D:\projects_for_university\Lessons\project1\Модуль 4\Пространство имен и области видимости\module_4_2.py", line 18, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
