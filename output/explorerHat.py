import explorerhat as eh

SPEED = 100
INNER_BANK_SPEED = 20
OUTER_BANK_SPEED = 100

lastCommand = None

def lastCommandWas(name):
  if lastCommand == name:
    return True

  lastCommand = name
  return False

def go():
  if lastCommandWas('go'): return
  eh.motor.one.backwards(SPEED)
  eh.motor.two.forwards(SPEED)

def reverse():
  if lastCommandWas('reverse'): return
  eh.motor.one.forwards(SPEED)
  eh.motor.two.backwards(SPEED)

def stop():
  if lastCommandWas('stop'): return
  eh.motor.one.stop()
  eh.motor.two.stop()

def left():
  if lastCommandWas('left'): return
  eh.motor.one.forwards(SPEED)
  eh.motor.two.forwards(SPEED)

def right():
  if lastCommandWas('right'): return
  eh.motor.one.backwards(SPEED)
  eh.motor.two.backwards(SPEED)

def leftBank():
  if lastCommandWas('leftBank'): return
  eh.motor.one.backward(INNER_BANK_SPEED)
  eh.motor.two.forwards(OUTER_BANK_SPEED)

def rightBank():
  if lastCommandWas('rightBank'): return
  eh.motor.two.forwards(INNER_BANK_SPEED)
  eh.motor.one.backward(OUTER_BANK_SPEED)

def reverseLeftBank():
  if lastCommandWas('reverseLeftBank'): return
  eh.motor.one.backward(OUTER_BANK_SPEED)
  eh.motor.two.forwards(INNER_BANK_SPEED)

def reverseRightBank():
  if lastCommandWas('reverseRightBank'): return
  eh.motor.two.forwards(OUTER_BANK_SPEED)
  eh.motor.one.backward(INNER_BANK_SPEED)
