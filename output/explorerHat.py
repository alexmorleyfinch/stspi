# we have a disabled flag for when we test the code from a device where the explorer hat does not exist

disabled = False

try:
  import explorerhat as eh
except ImportError:
  disabled = True

SPEED = 100
INNER_BANK_SPEED = 20
OUTER_BANK_SPEED = 100

# we store the last command so we do not make unnecessary calls to explorerhat.
# this also conveniently allows us to disable the functions so the `eh` calls are never run

lastCommand = None
def lastCommandWas(name):
  if disabled or lastCommand == name:
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


# LED Controls

def light1(on):
  if disabled: return
  if on:
    eh.light.blue.on()
  else:
    eh.light.blue.off()

def light2(on):
  if disabled: return
  if on:
    eh.light.yellow.on()
  else:
    eh.light.yellow.off()

def light3(on):
  if disabled: return
  if on:
    eh.light.green.on()
  else:
    eh.light.green.off()

def light4(on):
  if disabled: return
  if on:
    eh.light.red.on()
  else:
    eh.light.red.off()
