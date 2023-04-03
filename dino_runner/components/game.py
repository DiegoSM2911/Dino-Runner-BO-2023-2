import pygame
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, COLOR_BAKCGROUND
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.clouds import Clouds
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
import time

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.clouds = Clouds()
        self.obstacle_manager = ObstacleManager()


    def run(self):
        # Game loop: events - update - draw
        start = time.time()
        self.playing = True
        while self.playing:
            # end = time.time()
            # my_time = int(end - start)
            # if my_time < 5:
            #     global COLOR_BAKCGROUND
            #     COLOR_BAKCGROUND = [255, 255, 255]
            # else:
            #     COLOR_BAKCGROUND = [0, 0, 0]
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_inputs = pygame.key.get_pressed()
        self.player.update(user_inputs)
        self.obstacle_manager.update(self.game_speed, self.player)
        if self.player.dino_dead:
            self.playing = False

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill(COLOR_BAKCGROUND)
        self.draw_background()
        self.player.draw(self.screen)
        self.clouds.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

#tarea agregar cactus grande al juego
#intentar agregar el pajaro crear clase ave
#mostrar dinosaurio muerto