from output import explorerHat
from constants.ps3Controller import EX, SQUARE, LEFT, RIGHT

def translateInputToOutput(buttons):
  if buttons[EX]:
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
