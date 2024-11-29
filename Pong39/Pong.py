import arcade


class Game(arcade.Window):
    def on_draw(self):
        self.clear((49, 0, 98))


if __name__ == '__main__':
    window = Game()
    arcade.run()
