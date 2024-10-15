# На вход даны следующие данные:
from itertools import count

# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# 1. Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# 2. Множество students содержит неупорядоченную последовательность имён всех учеников в классе.

# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
# а значением - его средний балл.

#Дано:
# grades - список оценок для каждого ученика в алфавитном порядке
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество students, содержащее неупорядоченную последовательность имён всех учеников в классе
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # 'Aaron','Bilbo', 'Johnny', 'Khendrik', 'Steve'

# # Количество учеников
# print('Количество учеников:', len(grades))
# # Количество оценок у учеников
# print('Количество оценок у первого ученика:', len(grades[0]))
# print('Количество оценок у второго ученика:', len(grades[1]))
# print('Количество оценок у третьего ученика:', len(grades[2]))
# print('Количество оценок у четвёртого ученика:', len(grades[3]))
# print('Количество оценок у пятого ученика:', len(grades[4]))
# # Сумма оценок у учеников
# print('Сумма оценок у первого ученика:', sum(grades[0]))
# print('Сумма оценок у второго ученика:', sum(grades[1]))
# print('Сумма оценок у третьего ученика:', sum(grades[2]))
# print('Сумма оценок у четвёртого ученика:', sum(grades[3]))
# print('Сумма оценок у пятого ученика:', sum(grades[4]))
# # Средний балл у первого ученика
# print('Средний балл у первого ученика:', sum(grades[0])/len(grades[0]))
# print('Средний балл у второго ученика:', sum(grades[1])/len(grades[1]))
# print('Средний балл у третьего ученика:', sum(grades[2])/len(grades[2]))
# print('Средний балл у четвёртого ученика:', sum(grades[3])/len(grades[3]))
# print('Средний балл у пятого ученика:', sum(grades[4])/len(grades[4]))

# Отсортированный список учеников
list_students = list(sorted(students))
# print('Отсортированный список учеников:', list_students)
# Создам пустой словарь GPA, в котором ключом будет имя ученика, а значением - его средний балл.
GPA = {}
# Добавляю в словарь имена учеников с их средними баллами
GPA.update({list_students[0]: sum(grades[0])/len(grades[0]), list_students[1]: sum(grades[1])/len(grades[1]),
            list_students[2]: sum(grades[2])/len(grades[2]), list_students[3]: sum(grades[3])/len(grades[3]),
            list_students[4]: sum(grades[4])/len(grades[4])})
print('Словарь:', GPA)