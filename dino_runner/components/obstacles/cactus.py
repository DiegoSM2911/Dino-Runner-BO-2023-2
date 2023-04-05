from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS
import random

class Cactus(Obstacle):
  Y_POS_SMALL_CACTUS = 330 
  Y_POS_LARGE_CACTUS = 300
  def __init__(self):
    self.images = [*SMALL_CACTUS, *LARGE_CACTUS]
    self.image = self.images[random.randint(0,5)]
    super().__init__(self.image)
    self.rect.y = self.Y_POS_SMALL_CACTUS if self.image in SMALL_CACTUS else self.Y_POS_LARGE_CACTUS