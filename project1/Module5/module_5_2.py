# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче.
# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

# Создаю класс House
class House:
    # Определил метод __init__, в который передаю название и кол-во этажей
    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    # Создал специальный метод __len__(self), который должен возвращать кол-во этажей здания self.number_of_floors
    def __len__(self):
        return self.number_of_floors

    # Создал специальный метод __str__(self), который должен возвращать строку: "Название: <название>, кол-во этажей:
    # <этажи>"
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'


# Создал два объекта класса House
House_1 = House('ЖК Эльбрус', 10)
House_2 = House('ЖК Акация', 20)

# Вызов метода __str__(self)
print(House_1)
print(House_2)

# Вызов метода __len__(self)
print(f'Количество этажей первого дома: {len(House_1)}')
print(f'Количество этажей второго дома: {len(House_2)}')
