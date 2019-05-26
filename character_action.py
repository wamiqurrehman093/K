import arcade
import math
# from character_state import *

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
    
    def enter_state(self, character):
        pass
    
    def update(self, character, key, type, time):
        pass


class LightPunch(CharacterAction):
    def update(self, character, key, input_type, time):
        if time >= 0.05:
            texture_list = []
            if character.state == FACE_RIGHT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_right_lp_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_right_lp_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_right_lp_textures
            if character.state == FACE_LEFT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_left_lp_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_left_lp_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_left_lp_textures
            
            if character.action_texture_index >= len(texture_list):
                character.action_texture_index = 0
                if character.current_state_ == "StateJump":
                    character.change_y = character.prev_y
                    character.prev_y = 0
                return character.prev_state_

            character.texture = texture_list[character.action_texture_index]
            character.action_texture_index += 1

class LightKick(CharacterAction):
    def update(self, character, key, input_type, time):
        if time >= 0.05:
            texture_list = []
            if character.state == FACE_RIGHT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_right_lk_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_right_lk_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_right_lk_textures
            if character.state == FACE_LEFT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_left_lk_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_left_lk_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_left_lk_textures
            
            if character.action_texture_index >= len(texture_list):
                character.action_texture_index = 0
                if character.current_state_ == "StateJump":
                    character.change_y = character.prev_y
                    character.prev_y = 0
                return character.prev_state_

            character.texture = texture_list[character.action_texture_index]
            character.action_texture_index += 1

class HeavyPunch(CharacterAction):
    def update(self, character, key, input_type, time):
        if time >= 0.05:
            texture_list = []
            if character.state == FACE_RIGHT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_right_hp_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_right_hp_textures
                elif character.current_state_ == "StateCrouch":
                    character.center_y = character.prev_y
                    texture_list = character.crouch_right_hp_textures
            if character.state == FACE_LEFT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_left_hp_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_left_hp_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_left_hp_textures
            
            if character.action_texture_index >= len(texture_list):
                character.action_texture_index = 0
                if character.current_state_ == "StateCrouch":
                    character.center_y = character.prev_y
                    character.prev_y = 0
                if character.current_state_ == "StateJump":
                    character.change_y = character.prev_y
                    character.prev_y = 0
                return character.prev_state_

            character.texture = texture_list[character.action_texture_index]
            character.action_texture_index += 1

class HeavyKick(CharacterAction):
    def update(self, character, key, input_type, time):
        if time >= 0.05:
            texture_list = []
            if character.state == FACE_RIGHT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_right_hk_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_right_hk_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_right_hk_textures
            if character.state == FACE_LEFT:
                if character.current_state_ == "StateIdle" or character.current_state_ == "StateWalk":
                    texture_list = character.stand_left_hk_textures
                elif character.current_state_ == "StateJump":
                    texture_list = character.jump_left_hk_textures
                elif character.current_state_ == "StateCrouch":
                    texture_list = character.crouch_left_hk_textures
            
            if character.action_texture_index >= len(texture_list):
                character.action_texture_index = 0
                if character.current_state_ == "StateJump":
                    character.change_y = character.prev_y
                    character.prev_y = 0
                return character.prev_state_

            character.texture = texture_list[character.action_texture_index]
            character.action_texture_index += 1
