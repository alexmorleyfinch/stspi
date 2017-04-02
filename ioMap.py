from constants.ps3Controller import EX, SQUARE, LEFT, RIGHT

from output import explorerHat

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
      #explorerHat.reverseLeftBank()
      explorerHat.reverse()
    elif buttons[RIGHT]:
      #explorerHat.reverseRightBank()
      explorerHat.reverse()
    else:
      explorerHat.reverse()
  elif buttons[LEFT]:
    explorerHat.left()
  elif buttons[RIGHT]:
    explorerHat.right()
  else:
    explorerHat.stop()
