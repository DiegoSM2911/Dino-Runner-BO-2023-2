from dino_runner.utils.constants import ( RUNNING, RUNNING_SHIELD, RUNNING_HAMMER,
                                          JUMPING, JUMPING_SHIELD, JUMPING_HAMMER,
                                          DUCKING, DUCKING_SHIELD, DUCKING_HAMMER,   
                                          DEFAULT_TYPE, SHIELD_TYPE, HAMMER_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH)
from dino_runner.utils.constants import HAMMER, SHIELD, HEART, HEART_TYPE
from dino_runner.components import text_utils
import pygame
import time

class Dinosaur:
  X_POS = 80
  Y_POS = 310
  Y_POS_DUCK = 340
  JUMP_VEL = 8.5 

  def __init__(self):
    self.run_img = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}
    self.jump_img = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
    self.duck_img = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
    self.type = DEFAULT_TYPE
    self.image = self.run_img[self.type][0]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index = 0
    self.dino_run = True
    self.dino_jump = False
    self.dino_duck = False
    self.jump_vel = self.JUMP_VEL
    self.dino_dead = False
    self.lives = 3
    self.shield = {"is_activated": False, "active_time": 0, "time_up_power_up": 0}
    self.hammer = {"is_activated": False, 
                   "active_time": 0, 
                   "time_up_power_up": 0, 
                   "used": False,
                   "vel": 30,
                   "pos": HAMMER.get_rect()}
    
  def update(self, user_input):
    if self.dino_jump:
      self.jump()

    elif self.dino_duck:
      self.duck()

    elif self.dino_run:
      self.run()

    if user_input[pygame.K_DOWN] and not self.dino_jump:
      self.dino_run = False
      self.dino_duck = True
      self.dino_jump = False

    elif user_input[pygame.K_UP] and not self.dino_jump:
      self.dino_run = False
      self.dino_duck = False
      self.dino_jump = True

    elif user_input[pygame.K_q] and not self.dino_jump and self.hammer["is_activated"]:
      self.hammer["pos"] = self.dino_rect 
      self.hammer["used"] = True
      self.reset_hammer()

    elif not self.dino_jump:
      self.run()

    if self.step_index >= 9:
      self.step_index = 0

    if self.shield["is_activated"]:
      time_to_show = round((self.shield["time_up_power_up"] - pygame.time.get_ticks()) / 1000, 2)
      self.shield["active_time"] = round(time_to_show)
      if time_to_show < 0:
        self.reset_shield()

    if self.hammer["is_activated"]:
      time_to_show = round((self.time_up_power_up - pygame.time.get_ticks()) / 1000, 2)
      self.hammer["active_time"] = round(time_to_show)
      if time_to_show < 0:
        self.reset_hammer()

    if self.hammer["used"]:
      self.hammer["pos"][0] += self.hammer["vel"]

    if self.hammer["pos"].x > SCREEN_WIDTH:
      self.hammer["used"] = False

  def draw(self, screen, score_color):
    screen.blit(self.image, self.dino_rect)
    screen.blit(HEART, (SCREEN_WIDTH - 120, 0))
    text, text_rect = text_utils.get_message_power_up(str(self.lives), 20, score_color)
    screen.blit(text, (SCREEN_WIDTH - 70, 0))
    if self.shield["is_activated"]:
      screen.blit(SHIELD, (SCREEN_WIDTH - 120, 30))
      text, text_rect = text_utils.get_message_power_up(str(self.shield["active_time"]), 20, score_color)
      screen.blit(text, (SCREEN_WIDTH - 70, 40))

    if self.hammer["is_activated"]:
      screen.blit(HAMMER, (SCREEN_WIDTH - 120, 70))
      text, text_rect = text_utils.get_message_power_up(str(self.hammer["active_time"]), 20, score_color)
      screen.blit(text, (SCREEN_WIDTH - 70, 80))

    if self.hammer["used"]:
      screen.blit(HAMMER, self.hammer["pos"])

    
  def run(self):
    self.image = self.run_img[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS
    self.step_index += 1

  def duck(self):
    self.image = self.duck_img[self.type][self.step_index // 5]
    self.dino_rect = self.image.get_rect()
    self.dino_rect.x = self.X_POS
    self.dino_rect.y = self.Y_POS_DUCK
    self.step_index += 1

  def jump(self):
    self.image = self.jump_img[self.type]
    if self.dino_jump:
      self.dino_rect.y -= self.jump_vel * 4 
      self.jump_vel -= 0.8
    
    if self.jump_vel < -self.JUMP_VEL:
      self.dino_rect.y = self.Y_POS
      self.dino_jump = False
      self.jump_vel = self.JUMP_VEL

  def set_power_up(self, power_up):
    if power_up.type == SHIELD_TYPE:
      self.type = SHIELD_TYPE
      self.shield["is_activated"] = True
      self.shield["time_up_power_up"] = power_up.time_up

    elif power_up.type == HAMMER_TYPE:
      self.type = HAMMER_TYPE
      self.hammer["is_activated"] = True
      self.time_up_power_up = power_up.time_up

    elif power_up.type == HEART_TYPE:
      self.lives += 1 

  def reset_shield(self):
    self.type = DEFAULT_TYPE
    self.shield["is_activated"] = False
    self.shield["time_up_power_up"] = 0

  def reset_hammer(self):
    self.type = DEFAULT_TYPE
    self.hammer["is_activated"] = False
    self.hammer["time_up_power_up"] = 0