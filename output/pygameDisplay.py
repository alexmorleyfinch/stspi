import pygame

from constants.ps3Controller import EX, SQUARE, LEFT, RIGHT
from constants.app import SIZE, BACKGROUND, TEXT, TEXT_FADED

positionMap = {
  EX: [300, 100],
  SQUARE: [250, 50],
  LEFT: [100, 50],
  RIGHT: [200, 50],
}

buttonLabels = {
  EX: 'EX',
  SQUARE: 'SQUARE',
  LEFT: 'LEFT',
  RIGHT: 'RIGHT',
}


class PygameWindowOutput():
  def __init__(self):
    pygame.display.set_caption("STS-PI controller")

    self.screen = pygame.display.set_mode(SIZE)

  def renderText(self, string, x, y, colour):
    font = pygame.font.Font(None, 20)
    text_bitmap = font.render(string, True, colour)

    self.screen.blit(text_bitmap, [x, y])

  def renderJoystickFeedback(self, buttons):
    i = 1
    for key in buttonLabels:
      i=i+1
      pos = positionMap[key]
      isActive = buttons[key]
      self.renderText(buttonLabels[key], pos[0], pos[1], TEXT if isActive else TEXT_FADED)

  def render(self, buttons):
    self.screen.fill(BACKGROUND)

    self.renderJoystickFeedback(buttons)

    pygame.display.flip()

  def renderNoController(self):
    self.screen.fill(BACKGROUND)

    font = pygame.font.Font(None, 20)
    text_bitmap = font.render('No Controller', True, TEXT)

    self.screen.blit(text_bitmap, [10, 10])

    pygame.display.flip()

