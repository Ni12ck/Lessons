# Напишите 4 переменных которые буду обозначать следующие данные:
# 1 Количество выполненных ДЗ (запишите значение 12)
Number_of_homework_completed = 12
print('Количество выполненных ДЗ:', Number_of_homework_completed)
# 2 Количество затраченных часов (запишите значение 1.5)
Number_of_hours_spent = 1.5
print('Количество затраченных часов:', Number_of_hours_spent)
# 3 Название курса (запишите значение 'Python')
Course_name = 'Python'
print('Название курса:', Course_name)
# 4 Время на одно задание (вычислить используя 1 и 2 переменные)
Time_spent_on_one_task = Number_of_hours_spent / Number_of_homework_completed
print('Время на одно задание:', Time_spent_on_one_task)
#Выведите на экран(в консоль), используя переменные, следующую строку:
#Курс: Python, всего задач:12, затрачено часов: 1.5, среднее время выполнения 0.125 часа.
print('Курс: ', Course_name,', всего задач: ', Number_of_homework_completed , ', затрачено часов: ', Number_of_hours_spent, ', среднее время выполнения ', Time_spent_on_one_task, ' часа.', sep='')

# Ещё метод вывода, так для себя
print(f'Курс: {Course_name}, всего задач: {Number_of_homework_completed}, затрачено часов: {Number_of_hours_spent}, среднее время выполнения {Time_spent_on_one_task} часа.')