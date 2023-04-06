from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.life import Life
import random

class PowerUpsManager():
    def __init__(self):
        self.power_ups = []

    def update(self, game):
        if len(self.power_ups) == 0: #and points % 100 == 0 :#and random.randint(0,1) == 0:
          self.power_ups.append(Shield() if random.randint(0,1) == 1 else Hammer())

        if game.points % 300 == 0: #and points % 100 == 0 :#and random.randint(0,1) == 0:
          self.power_ups.append(Life())
          game.player.lifes += 1
        for power_up in self.power_ups:
            if power_up.rect.x < -power_up.rect.width or power_up.used:
                self.power_ups.remove(power_up) 
            if power_up.used:
                game.player.set_power_up(power_up)
            power_up.update(game)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)