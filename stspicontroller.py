import pygame
import constants

from ioMap import translateInputToOutput
from input.controller import Ps3ControllerInput
from output.pygameDisplay import PygameWindowOutput

# deps
# - pygame
# - joystick
# - display
# - camera API

class StsPiController(object):
  def __init__(self):
    pygame.init()

    self.controllerInput = Ps3ControllerInput()

    self.visualOutput = PygameWindowOutput()


  def render(self):
    buttons = self.controllerInput.getActiveButtons(0)

    self.visualOutput.render(buttons)

    translateInputToOutput(buttons)


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
