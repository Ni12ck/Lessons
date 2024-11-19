class Human:
    # Инструкция, что будет создаваться при инициализации класса
    # Метод __init__
    def __init__(self, nickname: str, dnd_class: str, lvl: int):
        # Характеристики, атрибуты
        self.nickname = nickname
        self.dnd_class = dnd_class
        self.lvl = lvl
        # Вызов функции в init
        print('Вызов функции say_info в init:')
        self.say_info()

    # Добавлю новую функцию (способность), в данной ситуации персонаж будеть говорить о себе
    def say_info(self):
        print(f'Привет! Меня зовут {self.nickname}, мой класс {self.dnd_class}, и я достиг {self.lvl} уровня)')

    # Функция повышения уровня
    def lvl_up(self):
        self.lvl += 1
        print(f'Вы получили новый уровень! {self.nickname}, теперь Ваш уровень {self.lvl}!')

    # Возврат уровня персонажа - получение размера объекта
    def __len__(self):
        return self.lvl

    # метод сравнения (оператор "меньше" - less than)
    def __lt__(self, other):
        # возвращает True, если lvl первого объекта меньше второго
        return self.lvl < other.lvl

    # метод сравнения (оператор "больше" - greter than)
    def __gt__(self, other):
        # возвращает True, если lvl первого объекта больше второго
        return self.lvl > other.lvl

    # метод сравнения (оператор равенства - equal)
    def __eq__(self, other):
        # возвращает True, если lvl первого равен второму
        return self.lvl == other.lvl and self.nickname == other.nickname

    # булевое значение
    def __bool__(self):
        return bool(self.lvl)

    # описание
    def __str__(self):
        return f'{self.nickname}'

    # Создание деструктора
    def __del__(self):
        print(f'{self.nickname}, Ваше путешествие подошло к концу')


Vladimir = Human('Ni12ck', 'Bard', 11)
Andrey = Human('Sevenmi007', 'Wizard', 7)

print(f'Уровень Владимира меньше уровня Андрея? -', Vladimir < Andrey)
print(f'Никнейм владимира: {Vladimir}')
