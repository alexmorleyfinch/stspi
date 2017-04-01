import constants
import motorControl

def translateInputToOutput(buttons):
  if buttons[constants.EX]:
    if buttons[constants.LEFT]:
      motorControl.leftBank()
    elif buttons[constants.RIGHT]:
      motorControl.rightBank()
    else:
      motorControl.go()
  elif buttons[constants.SQUARE]:
    if buttons[constants.LEFT]:
      #motorControl.reverseLeftBank()
      motorControl.reverse()
    elif buttons[constants.RIGHT]:
      #motorControl.reverseRightBank()
      motorControl.reverse()
    else:
      motorControl.reverse()
  elif buttons[constants.LEFT]:
    motorControl.left()
  elif buttons[constants.RIGHT]:
    motorControl.right()
  else:
    motorControl.stop()
