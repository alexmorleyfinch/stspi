import pygame
from constants.app import FPS

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

    self.visualOutput = PygameWindowOutput()
    self.controllerInput = Ps3ControllerInput()

  def render(self):
    buttons = self.controllerInput.getButtons(0)

    translateInputToOutput(buttons)
    self.visualOutput.render(buttons)

  def tryReconnect(self):
    done = False
    clock = pygame.time.Clock()

    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
          done = True

      if self.controllerInput.hasController():
        done = True

      self.visualOutput.renderNoController()

      clock.tick(FPS)

  def start(self):
    self.done = False
    clock = pygame.time.Clock()

    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True

      if not self.controllerInput.hasController():
        self.tryReconnect()

      self.render()

      clock.tick(FPS)

  def stop(self):
    self.done = True
