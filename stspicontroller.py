import os
import pygame
import explorerhat as eh
from constants.app import FPS
from constants.ps3Controller import SELECT

from ioMap import translateInputToOutput
from input.controller import Ps3ControllerInput
from output.pygameDisplay import PygameWindowOutput

def safeShutdown():
  pygame.quit()
  os.system('shutdown now -h')

class StsPiController(object):
  def __init__(self):
    pygame.init()

    self.visualOutput = PygameWindowOutput()
    self.controllerInput = Ps3ControllerInput()

  def render(self):
    hasController = self.controllerInput.hasController()
    buttons = [] if not hasController else self.controllerInput.getButtons(0)

    if hasController and buttons[SELECT]:
      self.stop()
      return safeShutdown()

    if hasController:
      translateInputToOutput(buttons)

    self.visualOutput.render(hasController, buttons)

  def start(self):
    self.done = False
    clock = pygame.time.Clock()

    eh.light.yellow.on()

    while not self.done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.stop()

      self.render()

      clock.tick(FPS)

    eh.light.yellow.off()

  def stop(self):
    self.done = True
