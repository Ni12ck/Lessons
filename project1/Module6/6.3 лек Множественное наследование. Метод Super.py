class Human:
    def __init__(self, name, group):
        self.name = name  # 1)!!!!!!!!
        super().__init__(group)  # 1)!!!!!!!!
        super().about()  # 1)!!!!!!!!

    def info(self):
        print(f'2) Привет, меня зовут {self.name}')  # 2)!!!!!!!!


class StudentGroup:
    def __init__(self, group: int):
        self.group = group  # 3) !!!!!!!!

    def about(self):
        print(f'1) {self.name} учится в группе {self.group}')  # 1)!!!!!!!!


class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        # Human.__init__(self, name) - равносильно super().__init__(name), метод super позволяет обращаться к классу
        # родителя
        super().__init__(name, group)
        self.place = place
        super().info()  # 2)!!!!!!!!


# human1 = Human('Владимир')
# print(human1.name)
student1 = Student('Андрей', "ИГХТУ", '42')

print()

print(f'3) Группа первого студента: {student1.group}')  # 3) !!!!!!!!
# print(Student.mro())  # mro() - метод вывода цепочки наследования в порядке приоритета обращения
# [<class '__main__.Student'>, <class '__main__.Human'>, <class '__main__.StudentGroup'>, <class 'object'>]
