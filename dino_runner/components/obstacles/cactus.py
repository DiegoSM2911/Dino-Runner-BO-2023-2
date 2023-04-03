from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import SMALL_CACTUS
import random

class Cactus(Obstacle):
  Y_POS_CACTUS = 325 
  def __init__(self):
    image = SMALL_CACTUS[random.randint(0,2)]
    super().__init__(image)
    self.rect.y = self.Y_POS_CACTUS

new_cactus = Cactus()