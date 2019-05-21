import arcade


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "K'")
        self.player = None
        self.player_list = None
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
    
    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player = arcade.Sprite('images/player/standing/0.png', 3)
        self.player.center_x = 640
        self.player.center_y = 180
        self.player_list.append(self.player)
    
    def on_key_press(self, key, mods):
        if key == arcade.key.LEFT:
            self.player.change_x = -5
        if key == arcade.key.RIGHT:
            self.player.change_x = 5

    def on_key_release(self, key, mods):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0
    
    def update(self, delta_time):
        self.player.center_x += self.player.change_x

def main():
    game = Game()
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
