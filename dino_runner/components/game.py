import pygame
import time
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, SCREEN_COLOR
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.background.clouds import Clouds
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpsManager
from dino_runner.components.background.path import Path
from dino_runner.components.background.sun import Sun
from dino_runner.components.background.moon import Moon
from dino_runner.components import text_utils 



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen_color = SCREEN_COLOR
        self.clock = pygame.time.Clock()
        self.running  = False
        self.playing = False
        self.game_speed = 15
        self.background = Path()
        self.player = Dinosaur()
        self.clouds = Clouds()
        self.sun = Sun()
        self.moon = Moon()
        self.obstacle_manager = ObstacleManager()
        self.power_manager = PowerUpsManager()
        self.points = 0
        self.death_count = 0
        


    def run(self):
        # Game loop: events - update - draw
        start = time.time()
        self.running = True
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and not self.playing:
                self.playing == True
                self.reset()

    def update(self):
        if self.playing:
            user_inputs = pygame.key.get_pressed()
            self.player.update(user_inputs)
            self.points += 1
            self.obstacle_manager.update(self.game_speed, self.player, self)
            self.background.update(self.game_speed)
            self.clouds.update(self.game_speed)
            self.sun.update(self.game_speed, self)
            self.moon.update(self.game_speed, self)
            self.power_manager.update(self.game_speed, self.points, self.player)
            if self.points % 200 == 0:
                self.game_speed += 1
            if self.player.dino_dead:
                self.playing = False
                self.death_count += 1

    def draw(self):
        if self.playing:
            self.clock.tick(FPS)
            self.screen.fill(self.screen_color)
            self.background.draw(self.screen)
            self.player.draw(self.screen)
            self.clouds.draw(self.screen)
            self.sun.draw(self.screen)
            self.moon.draw(self.screen)
            self.obstacle_manager.draw(self.screen)
            self.power_manager.draw(self.screen)
            self.draw_score()
        else:
            self.draw_menu()
        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
        score, score_rect = text_utils.get_message("Points: " + str(self.points), 20, 1000, 40)
        self.screen.blit(score, score_rect)

    def draw_menu(self):
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_element()

    def print_menu_element(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_message("Press any key to start: ", 30)
            self.screen.blit(text, text_rect)
        else:
            text, text_rect = text_utils.get_message("Press a key to restart: ", 30)
            score, score_rect = text_utils.get_message("Press a key to restart: " + str(self.points), 30, height = SCREEN_HEIGHT )
            self.screen.blit(text, text_rect)
            self.screen.blit(score, score_rect)

    def reset (self):
        # self.running  = True
        self.playing = True
        self.game_speed = 15
        self.background = Path()
        self.player = Dinosaur()
        self.clouds = Clouds()
        self.sun = Sun()
        self.moon = Moon()
        self.obstacle_manager = ObstacleManager()
        self.power_manager = PowerUpsManager()
        self.points = 0