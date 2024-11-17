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


Vladimir = Human('Ni12ck', 'Bard', 11)
Andrey = Human('Sevenmi007', 'Wizard', 7)

# Вывод атрибутов
print()
print(f'Три атрибута: никнейм {Vladimir.nickname}, класс {Vladimir.dnd_class} и уровень {Vladimir.lvl}')
print(f'Три атрибута: никнейм {Andrey.nickname}, класс {Andrey.dnd_class} и уровень {Andrey.lvl}')
print()

Vladimir.subclass = 'Swords'  # можно указать атрибут вне класса
Vladimir.lvl = 12  # можно изменять атрибуты
print(f'Все атрибуты Владимира: никнейм {Vladimir.nickname}, класс {Vladimir.dnd_class}, подкласс {Vladimir.subclass} '
      f'и уровень {Vladimir.lvl}')
print()

# Вызов функции say_info к экземпляру класса
Vladimir.say_info()
Andrey.say_info()
print()

# Вызов функции lvl_up к экземпляру класса
Andrey.lvl_up()
