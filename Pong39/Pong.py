import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong_39'


# отвечает за ракетку
class Bar(arcade.Sprite):
    def __init__(self):
        super().__init__('bar.png', 1.0)


# отвечает за мяч
class Ball(arcade.Sprite):
    def __init__(self):
        super().__init__('ball.png', 1.0)
        self.change_x = 5

    # движение мячика
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


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
        self.ball.update()


if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
