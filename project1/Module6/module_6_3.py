# Задача "Ошибка эволюции":
# Замечали, что некоторые животные в нашем мире обладают странными и, порой, несовместимыми друг с другом свойствами?
# Например, утконос... Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах. А ещё он откладывает
# яйца... Опустим факт о том, что они потеют молоком и попробуем не эволюционным способом создать нашего утконоса.

# Необходимо написать 5 классов:

# I Animal - класс описывающий животных.

# Класс обладает следующими атрибутами:
# 1) live = True
# 2) sound = None - звук (изначально отсутствует)
# 3) _DEGREE_OF_DANGER = 0 - степень опасности существа

# Объект этого класса обладает следующими атрибутами:
# 1) _cords = [0, 0, 0] - координаты в пространстве.
# 2) speed = ... - скорость передвижения существа (определяется при создании объекта)

# И методами:
# 1) move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке,
# где множителем будет является speed. Если при попытке изменения координаты z в _cords значение будет меньше 0, то
# выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносятся.
# 2) get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>,
# Z: <координаты по z>"
# 3) attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm
# attacking you 0_0" , если равно или больше.
# 4) speak(self), который выводит строку со звуком sound.


# II Bird - класс описывающий птиц. Наследуется от Animal.

# Должен обладать атрибутом:
# beak = True - наличие клюва

# И методом:
# lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"


# III AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.

# В этом классе атрибут _DEGREE_OF_DANGER = 3.

# Должен обладать методом:
# dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z в _cords.
# Чтобы сделать dz положительным, берите его значение по модулю (функция abs). Скорость движения при нырянии должна
# уменьшаться в 2 раза, в отличие от обычного движения. (speed / 2)


# IV PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.

# В этом классе атрибут _DEGREE_OF_DANGER = 8.


# V Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal. Порядок
# наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.

# Объект этого класса должен обладать одним дополнительным атрибутом:
# sound = "Click-click-click" - звук, который издаёт утконос


# Импорт randint для вывода случайного числа от 1 до 4 в методе lay_eggs(self) класса Bird
from random import randint


# Создал Animal - класс описывающий животных
class Animal:
    # Атрибуты класса
    live = True  # живой
    sound = None  # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        # Атрибуты объекта класса
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed  # скорость передвижения существа

    # Метод move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz в том же
    # порядке, умножая их соответственно на speed. Если при попытке изменения координаты z в _cords значение будет
    # меньше 0, то выводить сообщение "It's too deep, i can't dive :(", при этом изменения не вносятся
    def move(self, dx, dy, dz):
        if (self._cords[2] + dz * self.speed) < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = self._cords[0] + dx * self.speed
            self._cords[1] = self._cords[1] + dy * self.speed
            self._cords[2] = self._cords[2] + dz * self.speed

    # Метод get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>,
    # Z: <координаты по z>
    def get_cords(self):
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}')

    # Метод attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm
    # attacking you 0_0", если равно или больше
    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    # Метод speak(self), который выводит строку со звуком sound
    def speak(self):
        print(self.sound)


# Bird - класс описывающий птиц. Наследуется от Animal
class Bird(Animal):
    # Атрибут класса
    beak = True  # наличие клюва

    # Метод lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
    def lay_eggs(self):
        print(f'Here are(is) {randint(1, 4)} eggs for you')


# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal
class AquaticAnimal(Animal):
    # Атрибут класса
    _DEGREE_OF_DANGER = 3

    # Метод dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z
    # в _cords. Чтобы сделать dz положительным, берите его значение по модулю (функция abs). Скорость движения при
    # нырянии должна уменьшаться в 2 раза, в отличие от обычного движения. (speed / 2)
    def dive_in(self, dz):
        self._cords[2] = self._cords[2] - abs(dz) * self.speed / 2


# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal
class PoisonousAnimal(Animal):
    # Атрибут класса
    _DEGREE_OF_DANGER = 8


# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal
# В примере кода утконос является опасным.
# Класс PoisonousAnimal должен быть главнее класса AquaticAnimal, чтобы получить при вызове метода attack():
# Be careful, i'm attacking you 0_0
# Поэтому в наследовании классов PoisonousAnimal пишу левее AquaticAnimal
class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"


# Создание объекта db класса Duckbill со скоростью 10
db = Duckbill(10)
# Вызов атрибута класса Animal
print(f'Жив? - {db.live}')
# Вызов атрибута класса Bird
print(f'Есть клюв? - {db.beak}')
# Вызов метода speak() из класса Animal со значением sound = "Click-click-click" из класса Duckbill
db.speak()
# Вызов метода attack() из класса Animal
db.attack()
# Вызов метода move() из класса Animal
db.move(1, 2, 3)
# Вызов метода get_cords() из класса Animal
db.get_cords()
# Вызов метода dive_in() из класса AquaticAnimal
db.dive_in(6)
# Вызов метода get_cords() из класса Animal
db.get_cords()
# Вызов метода lay_eggs() из класса Bird
db.lay_eggs()

print()
# Вызов метода mro(), который показывает цепочку наследования в порядке приоритета обращения
print(Duckbill.mro())
