from dino_runner.utils.constants import BG

class Path:
  def __init__(self) :
    self.image = BG
    self.x_pos_bg = 0
    self.y_pos_bg = 380

  # def draw(self, screen, game_speed):
  #   image_width = self.image.get_width()
  #   screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg))
  #   screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))
  #   if self.x_pos_bg <= -image_width:
  #     screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))
  #     self.x_pos_bg = 0
  #   self.x_pos_bg -= game_speed

  def draw(self, screen):
    image_width = self.image.get_width()
    screen.blit(self.image, (self.x_pos_bg, self.y_pos_bg))
    screen.blit(self.image, (image_width + self.x_pos_bg, self.y_pos_bg))

  def update(self, speed_game):
    image_width = self.image.get_width()
    if self.x_pos_bg <= -image_width:
      self.x_pos_bg = 0
    self.x_pos_bg -= speed_game

  def xd(self, selfw):
    print(selfw.points)