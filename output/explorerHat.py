import explorerhat as eh

def go():
  eh.motor.one.backwards(100)
  eh.motor.two.forwards(100)

def reverse():
  eh.motor.one.forwards(100)
  eh.motor.two.backwards(100)

def stop():
  eh.motor.one.stop()
  eh.motor.two.stop()

def left():
  eh.motor.one.forwards(100)
  eh.motor.two.forwards(100)

def right():
  eh.motor.one.backwards(100)
  eh.motor.two.backwards(100)

def leftBank():
  eh.motor.one.backward(70)
  eh.motor.two.forwards(100)

def rightBank():
  eh.motor.two.forwards(70)
  eh.motor.one.backward(100)
