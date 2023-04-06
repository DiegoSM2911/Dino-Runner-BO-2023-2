from pygame.font import Font
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_COLOR

FONT_STYLE = "freesansbold.ttf"
black_color = [0, 0 ,0]

def get_message(message, size, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2, text_color = [0, 0, 0]):
  font = Font(FONT_STYLE, size)
  text = font.render(message, True, text_color)
  text_rect = text.get_rect()
  text_rect.center = (width, height)
  return text, text_rect

def get_message_power_up(message, size,text_color = [0, 0, 0]):
  font = Font(FONT_STYLE, size)
  text = font.render(message, True, text_color)
  text_rect = text.get_rect()
  return text, text_rect
    