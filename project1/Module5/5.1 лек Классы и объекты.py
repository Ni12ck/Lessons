class Human:
    # Инструкция, что будет создаваться при инициализации класса
    # Метод __init__
    def __init__(self, nickname):
        # Характеристика .nickname
        self.nickname = nickname


Vladimir = Human('Ni12ck')
Andrey = Human('Sevenmi007')

print('Тип объекта:', type(Vladimir))
print('Сравнение объектов:', Vladimir == Andrey)
print('Сравнение объектов:', Vladimir is Andrey)
print(f'ID объектов: {id(Vladimir)}, {id(Andrey)}')
print(f'Никнеймы объекта: {Vladimir.nickname}, {Andrey.nickname}')
