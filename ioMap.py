import constants

from output import explorerHat

def translateInputToOutput(buttons):
  if buttons[constants.EX]:
    if buttons[constants.LEFT]:
      explorerHat.leftBank()
    elif buttons[constants.RIGHT]:
      explorerHat.rightBank()
    else:
      explorerHat.go()
  elif buttons[constants.SQUARE]:
    if buttons[constants.LEFT]:
      #explorerHat.reverseLeftBank()
      explorerHat.reverse()
    elif buttons[constants.RIGHT]:
      #explorerHat.reverseRightBank()
      explorerHat.reverse()
    else:
      explorerHat.reverse()
  elif buttons[constants.LEFT]:
    explorerHat.left()
  elif buttons[constants.RIGHT]:
    explorerHat.right()
  else:
    explorerHat.stop()
