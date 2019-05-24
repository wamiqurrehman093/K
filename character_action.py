import arcade
import math
from character_state import *

FACE_RIGHT = 1
FACE_LEFT = 2
FACE_UP = 3
FACE_DOWN = 4

KEY_UP = arcade.key.UP
KEY_DOWN = arcade.key.DOWN
KEY_LEFT = arcade.key.LEFT
KEY_RIGHT = arcade.key.RIGHT
KEY_LP = arcade.key.A
KEY_LK = arcade.key.S
KEY_HP = arcade.key.D
KEY_HK = arcade.key.F


class CharacterAction:
    def __init__(self):
        pass
    
    def handle_input(self, character, key, type):
        pass
    
    def update(self, character, key, type, time):
        pass


class LightPunch(CharacterAction):
    def update(self, character, key, type, time):
        if time >= 0.05:
            if character.state == FACE_RIGHT:
                if character.state_ == StateIdle() or character.state_ == StateWalk():
                    texture_list = character.stand_right_lp_textures
                elif character.state_ == StateJump():
                    texture_list = character.jump_right_lp_textures
                elif character.state_ == StateCrouch():
                    texture_list = character.crouch_right_lp_textures
            if character.state == FACE_LEFT:
                if character.state_ == StateIdle() or character.state_ == StateWalk():
                    texture_list = character.stand_left_lp_textures
                elif character.state_ == StateJump():
                    texture_list = character.jump_left_lp_textures
                elif character.state_ == StateCrouch():
                    texture_list = character.crouch_left_lp_textures
