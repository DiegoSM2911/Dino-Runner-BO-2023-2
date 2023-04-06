from dino_runner.components.background.path import Path
from dino_runner.components.background.clouds import Clouds
from dino_runner.components.background.moon import Moon
from dino_runner.components.background.sun import Sun

class BackgroundManager:
    def __init__(self):
      self.components = [Path(), Sun(), Moon(), Clouds()]

    def update(self, game):
      for component in self.components:
        component.update(game)  
      

    def draw(self, screen):
      for component in self.components:
        component.draw(screen)