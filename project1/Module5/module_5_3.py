# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
# Необходимо дополнить класс House следующими специальными методами:
# 1. __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# 2. Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# 3. __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# 4. __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:

# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
# действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House

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

    # Создал специальный метод __eq__(self, other), который должен возвращать True, если количество этажей одинаковое
    # у self и у other
    def __eq__(self, other):
        # Проверка принадлежности other к классу House и количеству этажей other к int
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # Возвращает True, если количество этажей первого объекта равно количеству этажей второго
            return self.number_of_floors == other.number_of_floors

    # Создал специальный метод __ne__(self, other), который должен возвращать True, если количество этажей разное
    # у self и у other
    def __ne__(self, other):
        # Проверка принадлежности other к классу House и количеству этажей other к int
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # Возвращает True, если количество этажей первого объекта отличается от количества этажей второго
            return self.number_of_floors != other.number_of_floors

    # Создал специальный метод __lt__(self, other), который должен возвращать True, если количество этажей у self
    # меньше, чем у other
    def __lt__(self, other):
        # Проверка принадлежности other к классу House и количеству этажей other к int
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # Возвращает True, если количество этажей первого объекта меньше количества этажей второго
            return self.number_of_floors < other.number_of_floors

    # Создал специальный метод __le__(self, other) который должен возвращать True, если количество этажей у self
    # меньше или равно количеству этажей other
    def __le__(self, other):
        # Проверка принадлежности other к классу House и количеству этажей other к int
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # Возвращает True, если количество этажей первого объекта меньше или равно количеству этажей второго
            return self.number_of_floors <= other.number_of_floors

    # Создал специальный метод __gt__(self, other), который должен возвращать True, если количество этажей у self
    # больше, чем у other
    def __gt__(self, other):
        # Проверка принадлежности other к классу House и количеству этажей other к int
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # Возвращает True, если количество этажей первого объекта больше количества этажей второго
            return self.number_of_floors > other.number_of_floors

    # Создал специальный метод __ge__(self, other) который должен возвращать True, если количество этажей у self
    # больше или равно количеству этажей other
    def __ge__(self, other):
        # Проверка принадлежности other к классу House и количеству этажей other к int
        if isinstance(other, House) and isinstance(other.number_of_floors, int):
            # Возвращает True, если количество этажей первого объекта больше или равно количеству этажей второго
            return self.number_of_floors >= other.number_of_floors

    # Создал специальный метод __add__(self, value), который увеличивает кол-во этажей на переданное значение value,
    # возвращает сам объект self
    def __add__(self, value):
        # Проверка принадлежности value к int
        if isinstance(value, int):
            # Увеличение количества этажей на значение value
            self.number_of_floors = self.number_of_floors + value
            return self

    # Создал специальный метод __radd__(self, value), который увеличивает кол-во этажей на переданное значение value,
    # возвращает сам объект self
    def __radd__(self, value):
        # Проверка принадлежности value к int
        if isinstance(value, int):
            # Увеличение количества этажей на значение value
            self.number_of_floors = value + self.number_of_floors
            return self

    # Создал специальный метод __iadd__(self, value), который увеличивает кол-во этажей на переданное значение value,
    # возвращает сам объект self
    def __iadd__(self, value):
        # Проверка принадлежности value к int
        if isinstance(value, int):
            # Увеличение количества этажей на значение value
            self.number_of_floors += value
            return self


# Создал два объекта класса House
House_1 = House('ЖК Эльбрус', 10)
House_2 = House('ЖК Акация', 20)

# Вызов метода __str__(self)
print(House_1)
print(House_2)
print()

print('Пункт 1')
# Вызов метода __eq__(self, other)
print(f'Количество этажей в House_1 и House_2 равны? - {House_1 == House_2}')
print()

print('Пункт 2')
# Вызов метода __ne__(self, other)
print(f'Количество этажей в House_1 отличается от количества этажей в House_2? - {House_1 != House_2}')

# Вызов метода __lt__(self, other)
print(f'Количество этажей в House_1 меньше, чем в House_2? - {House_1 < House_2}')

# Вызов метода __le__(self, other)
print(f'Количество этажей в House_1 меньше или равно количеству этажей House_2? - {House_1 <= House_2}')

# Вызов метода __gt__(self, other)
print(f'Количество этажей в House_1 больше, чем в House_2? - {House_1 > House_2}')

# Вызов метода __ge__(self, other)
print(f'Количество этажей в House_1 больше или равно количеству этажей House_2? - {House_1 >= House_2}')
print()

print('Пункт 3')
# Вызов метода __add__(self, value) - увеличил количество этажей House_1 на 10 (теперь должно быть 20 этажей)
House_1 = House_1 + 10
print(House_1)
print()

print('Пункт 4')
# Вызов метода __radd__(self, value) - увеличил количество этажей House_2 на 10 (теперь должно быть 30 этажей)
House_2 = 10 + House_2
print(House_2)

# Вызов метода __iadd__(self, value) - увеличил количество этажей House_1 на 10 (теперь должно быть 30 этажей)
House_1 += 10
print(House_1)
