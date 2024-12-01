import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong_39'


# отвечает за ракетку
class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 1.0)

    # движение ракетки
    def update(self):
        # значение центра x будет меняться на значение change_x
        self.center_x += self.change_x
        # ограничения движений ракетки
        if self.right >= SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0


# отвечает за мяч
class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 1.0)
        # меняет координату x
        self.change_x = 5
        self.change_y = 4.5

    # движение мячика
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        # если правая сторона спрайта переехала границу окна
        if self.right >= SCREEN_WIDTH:
            # меняем движение на противоположное
            self.change_x = - self.change_x
        # и наоборот
        if self.left <= 0:
            self.change_x = - self.change_x
        # так прописываю условия для высоты и координаты y
        if self.top >= SCREEN_HEIGHT:
            self.change_y = - self.change_y
        if self.bottom <= 0:
            self.change_y = - self.change_y


# отвечает за создание окна
class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        # Создание объектов
        self.bar = Bar()
        self.ball = Ball()
        # Выставление координат
        self.setup()

    # отвечает за положение элементов в игре
    def setup(self):
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 25
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    # отвечает за отрисовку объектов
    def on_draw(self):
        self.clear((49, 0, 98))
        # отрисовка объектов
        self.bar.draw()
        self.ball.draw()

    # движение объектов
    def update(self, delta_time: float):
        # проверка на столкновение
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = - self.ball.change_y
        self.ball.update()
        self.bar.update()

    # настройка управления по зажатию кнопки
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT:
            self.bar.change_x = 4
        if symbol == arcade.key.LEFT:
            self.bar.change_x = -4

    # настройка управления после того, как кнопки будут отпускаться
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT or symbol == arcade.key.LEFT:
            # скорость движения по x меняю на 0
            self.bar.change_x = 0


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
