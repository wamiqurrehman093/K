import arcade
from character import Character


PLAYER_SCALE = 4
PLAYER_CENTER_X = 210
PLAYER_CENTER_Y = 300


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
        self.player = Character()
        # basic movements
        self.player.stand_right_textures = []
        self.player.stand_left_textures = []
        self.player.walk_left_textures = []
        self.player.walk_right_textures = []
        self.player.crouch_right_textures = []
        self.player.crouch_left_textures = []
        self.player.jump_right_textures = []
        self.player.jump_left_textures = []
        # light punch
        self.player.crouch_right_lp_textures = []
        self.player.crouch_left_lp_textures = []
        self.player.jump_right_lp_textures = []
        self.player.jump_left_lp_textures = []
        self.player.stand_right_lp_textures = []
        self.player.stand_left_lp_textures = []
        # light kick
        self.player.stand_right_lk_textures = []
        self.player.stand_left_lk_textures = []
        self.player.jump_right_lk_textures = []
        self.player.jump_left_lk_textures = []
        self.player.crouch_right_lk_textures = []
        self.player.crouch_left_lk_textures = []
        # heavy punch
        self.player.stand_right_hp_textures = []
        self.player.stand_left_hp_textures = []
        self.player.jump_right_hp_textures = []
        self.player.jump_left_hp_textures = []
        self.player.crouch_right_hp_textures = []
        self.player.crouch_left_hp_textures = []
        # heavy kick
        self.player.stand_right_hk_textures = []
        self.player.stand_left_hk_textures = []
        self.player.jump_right_hk_textures = []
        self.player.jump_left_hk_textures = []
        self.player.crouch_right_hk_textures = []
        self.player.crouch_left_hk_textures = []

        # basic movements
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
        
        # light punch
        for i in range(5):
            self.player.stand_right_lp_textures.append(
                arcade.load_texture(
                    "images/player/light_punch/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(5):
            self.player.stand_left_lp_textures.append(
                arcade.load_texture(
                    "images/player/light_punch/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(6):
            self.player.jump_right_lp_textures.append(
                arcade.load_texture(
                    "images/player/jump_lp/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(6):
            self.player.jump_left_lp_textures.append(
                arcade.load_texture(
                    "images/player/jump_lp/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(6):
            self.player.crouch_right_lp_textures.append(
                arcade.load_texture(
                    "images/player/crouch_lp/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(6):
            self.player.crouch_left_lp_textures.append(
                arcade.load_texture(
                    "images/player/crouch_lp/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )
        
        # light kick
        for i in range(8):
            self.player.stand_right_lk_textures.append(
                arcade.load_texture(
                    "images/player/light_kick/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(8):
            self.player.stand_left_lk_textures.append(
                arcade.load_texture(
                    "images/player/light_kick/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(7):
            self.player.jump_right_lk_textures.append(
                arcade.load_texture(
                    "images/player/jump_lk/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(7):
            self.player.jump_left_lk_textures.append(
                arcade.load_texture(
                    "images/player/jump_lk/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(5):
            self.player.crouch_right_lk_textures.append(
                arcade.load_texture(
                    "images/player/crouch_lk/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(5):
            self.player.crouch_left_lk_textures.append(
                arcade.load_texture(
                    "images/player/crouch_lk/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )
        
        # heavy punch
        for i in range(10):
            self.player.stand_right_hp_textures.append(
                arcade.load_texture(
                    "images/player/heavy_punch/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(10):
            self.player.stand_left_hp_textures.append(
                arcade.load_texture(
                    "images/player/heavy_punch/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(6):
            self.player.jump_right_hp_textures.append(
                arcade.load_texture(
                    "images/player/jump_hp/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(6):
            self.player.jump_left_hp_textures.append(
                arcade.load_texture(
                    "images/player/jump_hp/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(11):
            self.player.crouch_right_hp_textures.append(
                arcade.load_texture(
                    "images/player/crouch_hp/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(11):
            self.player.crouch_left_hp_textures.append(
                arcade.load_texture(
                    "images/player/crouch_hp/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )
        
        # heavy kick
        for i in range(12):
            self.player.stand_right_hk_textures.append(
                arcade.load_texture(
                    "images/player/heavy_kick/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(12):
            self.player.stand_left_hk_textures.append(
                arcade.load_texture(
                    "images/player/heavy_kick/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(8):
            self.player.jump_right_hk_textures.append(
                arcade.load_texture(
                    "images/player/jump_hk/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(8):
            self.player.jump_left_hk_textures.append(
                arcade.load_texture(
                    "images/player/jump_hk/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )

        for i in range(11):
            self.player.crouch_right_hk_textures.append(
                arcade.load_texture(
                    "images/player/crouch_hk/"+str(i)+".png", scale=PLAYER_SCALE)
            )

        for i in range(11):
            self.player.crouch_left_hk_textures.append(
                arcade.load_texture(
                    "images/player/crouch_hk/"+str(i)+".png", scale=PLAYER_SCALE, mirrored=True)
            )
        
        self.player.center_x = PLAYER_CENTER_X
        self.player.center_y = PLAYER_CENTER_Y
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
