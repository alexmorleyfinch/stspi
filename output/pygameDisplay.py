import pygame
import constants

from renderers.joystickInfo import renderJoystickInfo
from renderers.joystickFeedback import renderJoystickFeedback

class PygameWindowOutput():
  def __init__(self):
    pygame.display.set_caption("STS-PI controller")

    self.screen = pygame.display.set_mode(constants.SIZE)

  def render(self, buttons):
    self.screen.fill(constants.WHITE)

    #renderJoystickInfo(self.screen)
    renderJoystickFeedback(self.screen, buttons)

    pygame.display.flip()

  def renderNoController(self):
    self.screen.fill(constants.WHITE)

    font = pygame.font.Font(None, 20)
    text_bitmap = font.render('No Controller', True, constants.BLACK)

    self.screen.blit(text_bitmap, [10, 10])

    pygame.display.flip()

