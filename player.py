import arcade
from arcade import Sprite
import math


FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4

SPEED = 9
JUMP_SPEED = 12

STATE_IDLE = 0
STATE_WALKING = 1
STATE_JUMPING = 2
STATE_CROUCHING = 4

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
        self.jump_right_textures = None
        self.jump_left_textures = None
        self.jumping = False
        self.before_jump_pos = None
        self.jump_texture_index = 0
        self.state_ = STATE_IDLE
        self.key = None
        self.previous_state_ = None

    def input_handler(self, key, type):
        self.input_type = type
        self.key = key
        if self.state_ == STATE_IDLE:
            if type == "PRESSED":
                if key == arcade.key.UP:
                    self.state_ = STATE_JUMPING
                    self.before_jump_pos = self.center_y
                    self.change_y = JUMP_SPEED
                elif key == arcade.key.DOWN:
                    self.state_ = STATE_CROUCHING
                elif key == arcade.key.LEFT:
                    self.state_ = STATE_WALKING
                    self.change_x = -SPEED
                elif key == arcade.key.RIGHT:
                    self.state_ = STATE_WALKING
                    self.change_x = SPEED
        elif self.state_ == STATE_WALKING:
            if type == "PRESSED":
                if key == arcade.key.UP:
                    self.state_ = STATE_JUMPING
                    self.before_jump_pos = self.center_y
                    self.change_y = JUMP_SPEED
                    self.previous_state_ = STATE_WALKING
            if type == "RELEASED":
                if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                    self.state_ = STATE_IDLE
                    self.change_x = 0
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
        self.center_y += self.change_y
        self.time += delta_time
        seconds = self.time % 60
        if self.state_ == STATE_CROUCHING:
            self.crouch_animation(self.input_type, self.key)
        elif self.state_ == STATE_IDLE:
            self.idle_animation(seconds)
        elif self.state_ == STATE_WALKING:
            self.walk_animation()
        elif self.state_ == STATE_JUMPING:
            self.jump_animation(seconds)
        if seconds > 0.05:
            self.time = 0.0
    
    def jump_animation(self, time):
        if self.center_y >= (self.before_jump_pos+200):
            self.change_y = -SPEED

        if self.change_y != 0 and time >= 0.05:
            self.last_texture_change_center_x = self.center_x
            self.last_texture_change_center_y = self.center_y

            if self.state == FACE_LEFT:
                texture_list = self.jump_left_textures

            elif self.state == FACE_RIGHT:
                texture_list = self.jump_right_textures

            self.jump_texture_index += 1
            if self.jump_texture_index >= len(texture_list):
                self.jump_texture_index = 0
                self.state_ = STATE_IDLE
                self.change_y = 0
                self.change_x = 0
                if self.state == FACE_LEFT:
                    self.texture = self.stand_left_textures[-1]
                if self.state == FACE_RIGHT:
                    self.texture = self.stand_right_textures[-1]
                if self.center_y != self.before_jump_pos:
                    self.center_y = self.before_jump_pos
                return

            self.texture = texture_list[self.jump_texture_index]

    def crouch_animation(self, type, key):
        if type == "PRESSED" and self.crouch_index <= 5 and self.change_x == 0 and self.change_y == 0:
            if self.crouch_index == 0:
                self.center_y -= 76
            if self.state == FACE_LEFT:
                texture_list = self.crouch_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.crouch_right_textures
            self.crouch_index += 1
            if self.crouch_index >= 5:
                self.crouch_index = 5

            self.texture = texture_list[self.crouch_index]
        
        if type == "RELEASED" and key == arcade.key.DOWN and self.crouch_index >= 5 and self.change_x == 0 and self.change_y == 0:
            if self.state == FACE_LEFT:
                texture_list = self.crouch_left_textures
            elif self.state == FACE_RIGHT:
                texture_list = self.crouch_right_textures
            self.crouch_index += 1
            if self.crouch_index >= len(texture_list):
                self.center_y += 76
                self.crouch_index = 0
                self.state_ = STATE_IDLE
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
    