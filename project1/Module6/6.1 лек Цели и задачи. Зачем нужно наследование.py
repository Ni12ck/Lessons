class Human:  # Родительский класс
    head = True

    def say_hello(self):
        print('Привет')

    # Создадим конструктор
    # def __init__(self):
    #     self.about_st


class Student(Human):  # Наследование класса Human (родительского) классом Student (дочерним)
    head = False

    def about_st(self):
        print('Я студент')


class Teacher(Human):
    pass


# human_1 = Human()
student_1 = Student()
teacher_1 = Teacher()
# print(human_1.head)
student_1.about_st()
print(student_1.head)
# human_1.about_st - ошибка из-за отсутствия наследования
teacher_1.say_hello()
student_1.say_hello()
