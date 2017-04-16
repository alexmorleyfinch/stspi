import os
import pygame

from output import explorerHat
from constants.ps3Controller import EX, SQUARE, LEFT, RIGHT, SELECT

def translateInputToOutput(buttons):
  if buttons[SELECT]:
    safeShutdown()
  elif buttons[EX]:
    if buttons[LEFT]:
      explorerHat.leftBank()
    elif buttons[RIGHT]:
      explorerHat.rightBank()
    else:
      explorerHat.go()
  elif buttons[SQUARE]:
    if buttons[LEFT]:
      explorerHat.reverseLeftBank()
    elif buttons[RIGHT]:
      explorerHat.reverseRightBank()
    else:
      explorerHat.reverse()
  elif buttons[LEFT]:
    explorerHat.left()
  elif buttons[RIGHT]:
    explorerHat.right()
  else:
    explorerHat.stop()

def safeShutdown():
  pygame.quit()
  os.system('shutdown now -h')
