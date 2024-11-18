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

    # Создание деструктора
    def __del__(self):
        print(f'{self.nickname}, Ваше путешествие подошло к концу')


# В контексте предыдущего занятия рассмотрены два объекта. Стоит отметить, что конструктор '__init__' работает не совсем
# так, как может показаться. Сначала выполняется метод '__new__', который также является специальным методом, но его
# редко используют при переопределении. Обычно ограничиваются стандартным использованием метода '__init__'

Vladimir = Human('Ni12ck', 'Bard', 11)
Andrey = Human('Sevenmi007', 'Wizard', 7)
# del Vladimir
# Деструктор сработает после выполнения всего кода, в данном случае после input'а
# input()
print(f'Уровень Владимира: {len(Vladimir)}')

# 1) Наследование — этот принцип позволяет создавать новые классы на основе существующих, что даёт возможность расширять
# и изменять поведение базового класса, делая производные классы более уникальными.
# 2) Инкапсуляция — позволяет скрывать внутренние детали реализации класса от пользователей, предоставляя доступ только
# к необходимым элементам. Это способствует более безопасной работе и предотвращает случайные ошибки.
# 3) Полиморфизм — позволяет использовать объекты разных классов через единый интерфейс, что упрощает взаимодействие с
# ними и делает код более гибким.
