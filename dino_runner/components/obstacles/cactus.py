# from dino_runner.components.obstacles.obstacle import Obstacle 
from obstacle import Obstacle


class Cactus(Obstacle):
  def __init__(self):
    Obstacle.__init__(self)
    pass

new_cactus = Cactus()

print("hhi")
new_cactus.draw()
new_cactus.update()