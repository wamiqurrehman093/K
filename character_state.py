import arcade
import math
from character_action import *

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


class CharacterState:
    def __init__(self):
        pass
    
    def handle_input(self, character, key, type):
        pass
    
    def update(self, character):
        pass


class StateIdle(CharacterState):
    def handle_input(self, character, key, type):
        if type == "PRESSED":
            if key == KEY_LEFT:
                character.change_x = -character.speed
                return StateWalk()
            elif key == KEY_RIGHT:
                character.change_x = character.speed
                return StateWalk()
            elif key == KEY_UP:
                character.before_jump_pos = character.center_y
                character.change_y = character.jump_speed
                return StateJump()
            elif key == KEY_DOWN:
                return StateCrouch()
            elif key == KEY_LP:
                character.prev_state_ = StateIdle()
                return LightPunch()
            elif key == KEY_LK:
                character.prev_state_ = StateIdle()
                return LightKick()
            elif key == KEY_HP:
                character.prev_state_ = StateIdle()
                return HeavyPunch()
            elif key == KEY_HK:
                character.prev_state_ = StateIdle()
                return HeavyKick()
    
    def update(self, character, key, type, time):
        character.current_state_ = "StateIdle"
        if character.just_finished:
            character.finished_time += time

        if character.finished_time >= 3 and time >= 0.05:
            if character.state == FACE_LEFT:
                texture_list = character.stand_left_textures
            elif character.state == FACE_RIGHT:
                texture_list = character.stand_right_textures
            character.cur_texture_index += 1
            if character.cur_texture_index >= len(texture_list):
                character.finished_time = 0.0
                character.just_finished = True
                character.cur_texture_index = -1

            character.texture = texture_list[character.cur_texture_index]



class StateWalk(CharacterState):    
    def handle_input(self, character, key, type):
        if type == "PRESSED":
            if key == KEY_LP:
                character.change_x = 0
                if character.state == FACE_LEFT:
                    character.texture = character.stand_left_textures[-1]
                if character.state == FACE_RIGHT:
                    character.texture = character.stand_right_textures[-1]
                character.prev_state_ = StateIdle()
                return LightPunch()
            elif key == KEY_LK:
                character.change_x = 0
                character.prev_state_ = StateIdle()
                return LightKick()
            elif key == KEY_HP:
                character.change_x = 0
                character.prev_state_ = StateIdle()
                return HeavyPunch()
            elif key == KEY_HK:
                character.change_x = 0
                character.prev_state_ = StateIdle()
                return HeavyKick()

        elif type == "RELEASED":
            if key == KEY_LEFT or key == KEY_RIGHT:
                character.change_x = 0
                if character.state == FACE_LEFT:
                    character.texture = character.stand_left_textures[-1]
                if character.state == FACE_RIGHT:
                    character.texture = character.stand_right_textures[-1]
                return StateIdle()
    
    def update(self, character, key, type, time):
        character.current_state_ = "StateWalk"
        x1 = character.center_x
        x2 = character.last_texture_change_center_x
        y1 = character.center_y
        y2 = character.last_texture_change_center_y
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        texture_list = []

        change_direction = False
        if character.change_x > 0 \
                and character.change_y == 0 \
                and character.state != FACE_RIGHT \
                and character.walk_right_textures \
                and len(character.walk_right_textures) > 0:
            character.state = FACE_RIGHT
            change_direction = True
        elif character.change_x < 0 and character.change_y == 0 and character.state != FACE_LEFT \
                and character.walk_left_textures and len(character.walk_left_textures) > 0:
            character.state = FACE_LEFT
            change_direction = True

        if change_direction or distance >= character.texture_change_distance:
            character.last_texture_change_center_x = character.center_x
            character.last_texture_change_center_y = character.center_y

            if character.state == FACE_LEFT:
                texture_list = character.walk_left_textures

            elif character.state == FACE_RIGHT:
                texture_list = character.walk_right_textures

            character.cur_texture_index += 1
            if character.cur_texture_index >= len(texture_list):
                character.cur_texture_index = 0

            character.texture = texture_list[character.cur_texture_index]

        if character._texture is None:
            print("Error, no texture set")
        else:
            character.width = character._texture.width * character.scale
            character.height = character._texture.height * character.scale


class StateJump(CharacterState):
    def handle_input(self, character, key, type):
        if type == "PRESSED":
            if key == KEY_LP:
                character.prev_state_ = StateJump()
                character.prev_y = character.change_y
                character.change_y = 0
                return LightPunch()
            elif key == KEY_LK:
                character.prev_state_ = StateJump()
                character.prev_y = character.change_y
                character.change_y = 0
                return LightKick()
            elif key == KEY_HP:
                character.prev_state_ = StateJump()
                character.prev_y = character.change_y
                character.change_y = 0
                return HeavyPunch()
            elif key == KEY_HK:
                character.prev_state_ = StateJump()
                character.prev_y = character.change_y
                character.change_y = 0
                return HeavyKick()

    def update(self, character, key, type, time):
        character.current_state_ = "StateJump"
        if character.center_y >= (character.before_jump_pos+200):
            character.change_y = -character.speed

        if character.change_y != 0 and time >= 0.05:
            character.last_texture_change_center_x = character.center_x
            character.last_texture_change_center_y = character.center_y

            if character.state == FACE_LEFT:
                texture_list = character.jump_left_textures

            elif character.state == FACE_RIGHT:
                texture_list = character.jump_right_textures

            
            if character.jump_texture_index >= len(texture_list):
                character.jump_texture_index = 0
                character.change_y = 0
                character.change_x = 0
                if character.state == FACE_LEFT:
                    character.texture = character.stand_left_textures[-1]
                if character.state == FACE_RIGHT:
                    character.texture = character.stand_right_textures[-1]
                if character.center_y != character.before_jump_pos:
                    character.center_y = character.before_jump_pos
                return StateIdle()

            character.texture = texture_list[character.jump_texture_index]
            character.jump_texture_index += 1



class StateCrouch(CharacterState):    
    def handle_input(self, character, key, type):
        if type == "PRESSED":
            character.prev_y = character.center_y
            if key == KEY_LP:
                character.prev_state_ = self
                return LightPunch()
            elif key == KEY_LK:
                character.prev_state_ = self
                return LightKick()
            elif key == KEY_HP:
                character.prev_state_ = self
                return HeavyPunch()
            elif key == KEY_HK:
                character.prev_state_ = self
                return HeavyKick()
        else:
            self.update(character, key, type)
    
    def update(self, character, key, type, time=0):
        character.current_state_ = "StateCrouch"
        if character.crouch_index <= 5:
            if character.crouch_index == 0:
                character.center_y -= 90
            if character.state == FACE_LEFT:
                texture_list = character.crouch_left_textures
            elif character.state == FACE_RIGHT:
                texture_list = character.crouch_right_textures
            character.crouch_index += 1
            if character.crouch_index >= 5:
                character.crouch_index = 5
            character.texture = texture_list[character.crouch_index]
        
        if type == "RELEASED" and key == KEY_DOWN and character.crouch_index >= 5:
            if character.state == FACE_LEFT:
                texture_list = character.crouch_left_textures
            elif character.state == FACE_RIGHT:
                texture_list = character.crouch_right_textures
            character.crouch_index += 1
            if character.crouch_index >= len(texture_list):
                character.center_y += 90
                character.crouch_index = 0
                if character.state == FACE_LEFT:
                    character.texture = character.stand_left_textures[-1]
                if character.state == FACE_RIGHT:
                    character.texture = character.stand_right_textures[-1]
                return StateIdle()

            character.texture = texture_list[character.crouch_index]

