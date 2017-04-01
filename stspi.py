import pygame
import constants

from ioMap import translateInputToOutput
from utils.gameUtils import simpleGameLoop
from renderers.joystickInfo import renderJoystickInfo
from renderers.joystickFeedback import renderJoystickFeedback


def getActiveButtons(joystickId):
  joystick = pygame.joystick.Joystick(joystickId)
  joystick.init()

  buttons = {}

  for key in constants.BUTTONS:
    buttons[key] = joystick.get_button(key)

  return buttons


def simpleWindow(screen, **theRest):
  screen.fill(constants.WHITE)

  buttons = getActiveButtons(0);

  #renderJoystickInfo(screen);
  renderJoystickFeedback(screen, buttons);

  translateInputToOutput(buttons);

  pygame.display.flip()


# ============= START =============


pygame.init()
pygame.joystick.init()
pygame.display.set_caption("STS-PI controller")

screen = pygame.display.set_mode(constants.SIZE)

simpleGameLoop(constants.FPS, simpleWindow, screen)
