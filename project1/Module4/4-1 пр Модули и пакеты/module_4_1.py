# Импортирую функции divide из модулей fake_math и true_math, назвав их fake_divide и true_divide соответственно
from fake_math import divide as fake_divide
from true_math import divide as true_divide

# Вывод результатов
print(f'Результат деления 69 на 3 с помощью функции divide из модуля fake_math: {fake_divide(69, 3)}')
print(f'Результат деления 3 на 0 с помощью функции divide из модуля fake_math: {fake_divide(3, 0)}')
print(f'Результат деления 49 на 7 с помощью функции divide из модуля true_math: {true_divide(49, 7)}')
print(f'Результат деления 15 на 0 с помощью функции divide из модуля true_math: {true_divide(15, 0)}')
