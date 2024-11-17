# Задача "Developer - не только разработчик":
# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".

# Пункты задачи:
# 1. Создайте класс House.
# 2. Внутри класса House определите метод __init__, в который передадите название и кол-во этажей.
# 3. Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors, присвойте им переданные
# значения.
# 4. Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# 5. Создайте объект класса House с произвольным названием и количеством этажей.
# 6. Вызовите метод go_to у этого объекта с произвольным числом.

# Создаю класс House
class House:
    # Определил метод __init__, в который передаю название и кол-во этажей
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    # Создал метод go_to с параметром new_floor, который выводит на экран(в консоль) значения от 1 до
    # new_floor(включительно)
    def go_to(self, new_floor: int):
        i = 1
        # Если new_floor больше чем self.number_of_floors или меньше 1, то вывожу строку "Такого этажа не существует"
        if all([new_floor > self.number_of_floors or new_floor < 1]):
            print("Такого этажа не существует")
        else:
            # Вывод этажей
            for i in range(1, new_floor + 1):
                print(i)


# Создал объект класса House с произвольным названием и количеством этажей
House_1 = House('ЖК Эльбрус', 10)
# Вызвал метод go_to у этого объекта с произвольным количеством этажей House_1
print(f'Вывод этажей для первого дома от 1 до 5:')
House_1.go_to(5)
print()

# Второй вариант с ошибкой "Такого этажа не существует"
House_2 = House('Исполин', 2)
# Вызвал метод go_to у этого объекта с произвольным количеством этажей House_2
print(f'Вывод ошибки для второго дома, т.к. указан номер этажа больше количества этажей в доме:')
House_2.go_to(3)
print()

# Третий вариант с ошибкой "Такого этажа не существует"
House_3 = House('Небоскрёб', 100)
# Вызвал метод go_to у этого объекта с произвольным количеством этажей House_3
print(f'Вывод ошибки для третьего дома, т.к. указан номер этажа меньше 1:')
House_3.go_to(0)
