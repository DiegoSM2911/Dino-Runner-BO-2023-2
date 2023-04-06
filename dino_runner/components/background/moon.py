from dino_runner.utils.constants import MOON, SCREEN_WIDTH, SUN
import pygame

class Moon:
  X_POS = SCREEN_WIDTH  
  Y_POS = 40

  def __init__(self):
    self.image = pygame.transform.scale(MOON, [70, 40])
    self.moon_rect = self.image.get_rect()
    self.moon_rect.x = -self.image.get_size()[0]
    self.moon_rect.y = self.Y_POS

  def draw(self, screen):
    screen.blit(self.image, self.moon_rect)

  def update(self, game):
    self.moon_rect.x -= game.game_speed // 3
    if self.moon_rect.x < -(self.X_POS + self.image.get_size()[0]):
      self.moon_rect.x = self.X_POS + self.image.get_size()[0]

    if self.moon_rect.x < -self.image.get_size()[0]:
      game.screen_color = [255, 255, 255]
      game.score_color = [0, 0, 0]
