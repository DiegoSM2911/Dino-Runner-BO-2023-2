from dino_runner.utils.constants import SUN, SCREEN_WIDTH
import pygame

class Sun:
  X_POS = SCREEN_WIDTH  
  Y_POS = 40

  def __init__(self):
    self.image = pygame.transform.scale(SUN, [70, 40])
    self.sun_rect = self.image.get_rect() 
    self.sun_rect.x = self.X_POS
    self.sun_rect.y = self.Y_POS

  def draw(self, screen):
    screen.blit(self.image, self.sun_rect)

  def update(self, speed_game, game):
    self.sun_rect.x -= speed_game // 2
    if self.sun_rect.x < -(self.X_POS + self.image.get_size()[0]):
      self.sun_rect.x = self.X_POS + self.image.get_size()[0]
      

    if self.sun_rect.x < -self.image.get_size()[0]:
      game.screen_color = [0, 0, 0]
