import arcade
from player import Player


PLAYER_SCALE = 3.5


class Game(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "K'")
        self.player = None
        self.player_list = None
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
    
    def setup(self):
        self.setup_player()
    
    def setup_player(self):
        self.player_list = arcade.SpriteList()
        self.player = Player()
        self.player.stand_right_textures = []
        self.player.stand_left_textures = []
        self.player.walk_left_textures = []
        self.player.walk_right_textures = []
        self.player.crouch_right_textures = []
        self.player.crouch_left_textures = []
        self.player.jump_right_textures = []
        self.player.jump_left_textures = []

        for i in range(14):
            self.player.stand_right_textures.append(
                arcade.load_texture("images/player/stand/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(14):
            self.player.stand_left_textures.append(
                arcade.load_texture("images/player/stand/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(12):
            self.player.walk_right_textures.append(
                arcade.load_texture("images/player/walking/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(12):
            self.player.walk_left_textures.append(
                arcade.load_texture("images/player/walking/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )
        
        
        for i in range(12):
            self.player.crouch_right_textures.append(
                arcade.load_texture("images/player/crouch/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(12):
            self.player.crouch_left_textures.append(
                arcade.load_texture("images/player/crouch/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )
        
        for i in range(14):
            self.player.jump_right_textures.append(
                arcade.load_texture("images/player/jumping/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(14):
            self.player.jump_left_textures.append(
                arcade.load_texture("images/player/jumping/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        self.player.center_x = 640
        self.player.center_y = 180
        self.player.scale = PLAYER_SCALE
        self.player.texture_change_distance = 40
        self.player_list.append(self.player)

    def on_key_press(self, key, mods):
        self.player.input_handler(key, "PRESSED")

    def on_key_release(self, key, mods):
        self.player.input_handler(key, "RELEASED")

    def update(self, delta_time):
        self.player.update(delta_time)

def main():
    game = Game()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
