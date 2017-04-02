import pygame
import constants

from ioMap import translateInputToOutput
from utils.gameUtils import simpleGameLoop
from renderers.joystickInfo import renderJoystickInfo
from renderers.joystickFeedback import renderJoystickFeedback

# deps
# - pygame
# - joystick
# - display
# - camera API

class StsPiController(object):
  def __init__(self):
    pygame.init()
    pygame.joystick.init()
    pygame.display.set_caption("STS-PI controller")

    self.screen = pygame.display.set_mode(constants.SIZE)

  def getActiveButtons(self, joystickId):
    joystick = pygame.joystick.Joystick(joystickId)
    joystick.init()

    buttons = {}

    for key in constants.BUTTONS:
      buttons[key] = joystick.get_button(key)

    return buttons

  def render(self):
    self.screen.fill(constants.WHITE)

    buttons = self.getActiveButtons(0);

    #renderJoystickInfo(self.screen);
    renderJoystickFeedback(self.screen, buttons);

    translateInputToOutput(buttons);

    pygame.display.flip()

  def start(self):
    self.done = False
    clock = pygame.time.Clock()

    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True

      self.render()

      clock.tick(constants.FPS)

    pygame.quit()

  def stop(self):
    self.done = True
