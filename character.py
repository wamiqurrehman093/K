import arcade
from arcade import Sprite
from character_state import *
import math


class Character(arcade.Sprite):
    def __init__(self, scale: float = 1,
                 image_x: float = 0, image_y: float = 0,
                 center_x: float = 0, center_y: float = 0):
        super().__init__(scale=scale, image_x=image_x, image_y=image_y,
                         center_x=center_x, center_y=center_y)
        self.state = FACE_RIGHT
        self.stand_right_textures = None
        self.stand_left_textures = None
        self.walk_left_textures = None
        self.walk_right_textures = None
        self.crouch_left_textures = None
        self.crouch_right_textures = None
        self.jump_right_textures = None
        self.jump_left_textures = None
        self.cur_texture_index = 0
        self.crouch_index = 0
        self.jump_texture_index = 0
        self.texture_change_distance = 20
        self.last_texture_change_center_x = 0
        self.last_texture_change_center_y = 0
        self.finished_time = 4
        self.just_finished = False
        self.time = 0.0
        self.input_type = None
        self.before_jump_pos = None
        self.state_ = StateIdle()
        self.key = None
        self.speed = 9
        self.jump_speed = 15

    def input_handler(self, key, type):
        state = self.state_.handle_input(self, key, type)
        if state is not None:
            self.state_ = state
        self.input_type = type
        self.key = key

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.time += delta_time
        seconds = self.time % 60
        state = self.state_.update(self, self.key, self.input_type, seconds)
        if state is not None:
            self.state_ = state
        if seconds > 0.05:
            self.time = 0.0
    
        
def get_distance_between_sprites(sprite1: Sprite, sprite2: Sprite) -> float:
    distance = math.sqrt((sprite1.center_x - sprite2.center_x) ** 2 + (sprite1.center_y - sprite2.center_y) ** 2)
    return distance
    