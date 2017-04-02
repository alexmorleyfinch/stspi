import pygame
import constants
import time

INACTIVITY_RECONNECT_TIME = 2
RECONNECT_TIMEOUT = 1

class Ps3ControllerInput():
  def __init__(self):
    pygame.joystick.init()

    self.lastActive = 0
    self.lastReconnect = 0

  def getButtons(self, joystickId):
    joystick = pygame.joystick.Joystick(joystickId)
    joystick.init()

    buttons = {}
    for code in range(joystick.get_numbuttons()):
      buttons[code] = joystick.get_button(code)
      if buttons[code]:
        self.lastActive = time.time()

    return buttons

  def hasController(self):
    now = time.time()
    if now - self.lastActive > INACTIVITY_RECONNECT_TIME and now - self.lastReconnect > RECONNECT_TIMEOUT:
      self.lastReconnect = now
      pygame.joystick.quit()
      pygame.joystick.init()

    return pygame.joystick.get_count() > 0
