import pygame
import constants

class Ps3ControllerInput():
  def __init__(self):
    pygame.joystick.init()

  def getActiveButtons(self, joystickId):
    joystick = pygame.joystick.Joystick(joystickId)
    joystick.init()

    buttons = {}

    for key in constants.BUTTONS:
      buttons[key] = joystick.get_button(key)

    return buttons
