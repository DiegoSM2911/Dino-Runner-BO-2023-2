from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH

class Clouds():
  CLOUD_VEL = 2.5

  def __init__(self):
    self.image = CLOUD
    self.pos_img1 = [-200, 15]
    self.pos_img2 = [350, 40]
    self.pos_img3 = [850, 25]
    self.cloud_vel = self.CLOUD_VEL

  def draw(self, screen):
    pos_images = [self.pos_img1, self.pos_img2, self.pos_img3]
    for pos_image in pos_images:
      screen.blit(self.image, pos_image)
    self.advance()

  def advance(self):
    pos_images = [self.pos_img1, self.pos_img2, self.pos_img3]
    for pos_image in pos_images:
      pos_image[0] -= self.cloud_vel 
      if pos_image[0] < -300: 
        pos_image[0] = SCREEN_WIDTH