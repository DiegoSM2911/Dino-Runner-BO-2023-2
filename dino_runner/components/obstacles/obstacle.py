from dino_runner.utils.constants import SCREEN_WIDTH, DEAD
import pygame

class Obstacle:
  def __init__(self, image):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH

  def update(self, game): 
    self.rect.x -= game.game_speed
    if game.player.lives == 0:
        game.player.image = DEAD
        pygame.time.delay(300)
        game.player.dino_dead = True

    if self.rect.colliderect(game.player.dino_rect) and not game.player.shield["is_activated"]:
      game.player.lives -= 1
      self.rect.x = -self.image.get_size()[0]

    if self.rect.colliderect(game.player.hammer["pos"]):
        self.rect.x = -self.image.get_size()[0]
  
  def draw(self, screen): 
    screen.blit(self.image, self.rect)