class Human:  # Родительский класс
    head = True
    _legs = True  # Символ "_" делает имя доступным только для локального использования
    __arms = True  # Символ "__" защищает имя от переопределения в дочерних классах

    def say_hello(self):
        print('Привет')

    def about(self):
        print(self.head)
        print(self._legs)
        print(self.__arms)


class Student(Human):  # Наследование класса Human (родительского) классом Student (дочерним)
    arms = False

    def about_st(self):
        print('Я студент')


class Teacher(Human):
    pass


human = Human()
human.about()

print()

student = Student()
student.about()

print()

# print(dir(human))
# print(dir(student))
print(student._Human__arms)

# символ _ сохраняет результат предыдущего действия
# 5 + 5
# 10
# 10 + _
# 20
# _ + _
# 40
