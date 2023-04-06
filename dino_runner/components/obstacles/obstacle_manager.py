from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
import random 

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            current_obstacle = Bird() if random.randint(0,1) == 1 else Cactus() 
            self.obstacles.append(current_obstacle)
            game.game_speed += 0.3

        for obstacle in self.obstacles:
            if obstacle.rect.x < -obstacle.rect.width:
                 self.obstacles.pop()
            if type(obstacle).__name__ == "Bird":
                obstacle.update_image()
            obstacle.update(game)
            
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)