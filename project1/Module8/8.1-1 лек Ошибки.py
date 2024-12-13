# Ошибки можно условно разделить на два основных типа:
# 1. синтаксические ошибки
# 2. исключения

# Синтаксическая ошибка — это довольно простая вещь. Она возникает, когда код написан неправильно. Например, если мы не
# закрыли кавычку, написали число неверно или вместо запятой поставили двоеточие. Бывает также, что мы неправильно
# указали цикл и так далее. То есть синтаксическая ошибка — это ошибка на уровне кода. Она даже еще не «спустилась» на
# уровень выполнения, и интерпретатор сразу видит, что в синтаксисе есть ошибка, подсвечивает её и не начинает
# выполнение программы.

#  При возникновении ошибки выводится не просто сообщение, а появляется так называемое окно «traceback», что в переводе
#  с английского означает «трассировка»

# «Traceback» — детальный отчет, который позволяет увидеть цепочку вызовов, приведших к ошибке. Он помогает разработчику
# понять, на каком этапе и в каком месте программы произошел сбой. Благодаря «traceback» можно быстро найти источник
# ошибки и устранить её, что особенно важно при работе с большим количеством кода.

# Главное, что необходимо усвоить при работе с «traceback», — это два ключевых момента. Во-первых, его следует читать
# снизу вверх, поскольку именно в конце отчета содержится информация о первопричине ошибки.
# Во-вторых, «traceback» предоставляет два важных элемента: название класса ошибки и её описание.
# Класс ошибки указывает на тип возникшей проблемы (например, SyntaxError или TypeError), а описание детализирует её
# причину. Для программиста наиболее ценной является информация о классе ошибки и её подробное описание, так как она
# позволяет быстро локализовать и устранить проблему

# https://docs.python.org/3/library/exceptions.html
