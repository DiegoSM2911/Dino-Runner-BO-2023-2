from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD
import random

class Bird(Obstacle):
  X_POS = 80
  Y_POS = 310
  def __init__(self):  
    self.image = BIRD[0]
    super().__init__(self.image)
    self.rect.y = random.randint(240, 290)
    self.step_index = 0
    

  def update_image(self):
    self.image = BIRD[0] if self.step_index < 5 else BIRD[1]
    self.step_index += 1
    if self.step_index >= 10:
      self.step_index = 0