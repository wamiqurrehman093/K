import arcade
from arcade import Sprite
import math


FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4

SPEED = 9


class Player(arcade.Sprite):
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
        self.walk_up_textures = None
        self.walk_down_textures = None
        self.cur_texture_index = 0
        self.texture_change_distance = 20
        self.last_texture_change_center_x = 0
        self.last_texture_change_center_y = 0
        self.finished_time = 4
        self.just_finished = False
        self.time = 0.0
        self.down_key = False
        self.input_type = None
        self.crouch_left_textures = None
        self.crouch_right_textures = None
        self.crouch_index = 0
        self.other_keys = False

    def input_handler(self, key, type):
        self.input_type = type
        if type == "PRESSED":
            if key == arcade.key.DOWN and not self.other_keys:
                self.down_key = True
            elif key == arcade.key.LEFT:
                self.change_x = -SPEED
                self.other_keys = True
            elif key == arcade.key.RIGHT:
                self.change_x = SPEED
                self.other_keys = True
        elif type == "RELEASED":
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.change_x = 0
                self.other_keys = False
                if self.state == FACE_LEFT:
                    self.texture = self.stand_left_textures[-1]
                if self.state == FACE_RIGHT:
                    self.texture = self.stand_right_textures[-1]

    def idle_animation(self, time):
        if self.just_finished:
            self.finished_time += time

        if self.finished_time >= 3 and self.change_x == 0 and self.change_y == 0 and time >= 0.05:
            if self.state == FACE_LEFT:
                texture_list = self.stand_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.stand_right_textures
            self.cur_texture_index += 1
            if self.cur_texture_index >= len(texture_list):
                self.finished_time = 0.0
                self.just_finished = True
                self.cur_texture_index = -1

            self.texture = texture_list[self.cur_texture_index]

    def update(self, delta_time):
        self.center_x += self.change_x
        if self.down_key:
            self.crouch_animation(self.input_type)
        else:
            self.time += delta_time
            seconds = self.time % 60
            self.idle_animation(seconds)
            self.walk_animation()
            if seconds > 0.05:
                self.time = 0.0

    def crouch_animation(self, type):
        if type == "PRESSED" and self.crouch_index <= 5 and self.change_x == 0 and self.change_y == 0:
            if self.crouch_index == 0:
                self.center_y -= 64
            if self.state == FACE_LEFT:
                texture_list = self.crouch_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.crouch_right_textures
            self.crouch_index += 1
            if self.crouch_index >= 5:
                self.crouch_index = 5

            self.texture = texture_list[self.crouch_index]
        
        if type == "RELEASED" and self.crouch_index >= 5 and self.change_x == 0 and self.change_y == 0:
            if self.state == FACE_LEFT:
                texture_list = self.crouch_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.crouch_right_textures
            self.crouch_index += 1
            if self.crouch_index >= len(texture_list):
                self.center_y += 64
                self.crouch_index = 0
                self.down_key = False
                if self.state == FACE_LEFT:
                    self.texture = self.stand_left_textures[-1]
                if self.state == FACE_RIGHT:
                    self.texture = self.stand_right_textures[-1]
                return

            self.texture = texture_list[self.crouch_index]

    def walk_animation(self):
        x1 = self.center_x
        x2 = self.last_texture_change_center_x
        y1 = self.center_y
        y2 = self.last_texture_change_center_y
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        texture_list = []

        change_direction = False
        if self.change_x > 0 \
                and self.change_y == 0 \
                and self.state != FACE_RIGHT \
                and self.walk_right_textures \
                and len(self.walk_right_textures) > 0:
            self.state = FACE_RIGHT
            change_direction = True
        elif self.change_x < 0 and self.change_y == 0 and self.state != FACE_LEFT \
                and self.walk_left_textures and len(self.walk_left_textures) > 0:
            self.state = FACE_LEFT
            change_direction = True

        if change_direction or distance >= self.texture_change_distance:
            self.last_texture_change_center_x = self.center_x
            self.last_texture_change_center_y = self.center_y

            if self.state == FACE_LEFT:
                texture_list = self.walk_left_textures

            elif self.state == FACE_RIGHT:
                texture_list = self.walk_right_textures

            self.cur_texture_index += 1
            if self.cur_texture_index >= len(texture_list):
                self.cur_texture_index = 0

            self.texture = texture_list[self.cur_texture_index]

        if self._texture is None:
            print("Error, no texture set")
        else:
            self.width = self._texture.width * self.scale
            self.height = self._texture.height * self.scale
        

def get_distance_between_sprites(sprite1: Sprite, sprite2: Sprite) -> float:
    distance = math.sqrt((sprite1.center_x - sprite2.center_x) ** 2 + (sprite1.center_y - sprite2.center_y) ** 2)
    return distance
    