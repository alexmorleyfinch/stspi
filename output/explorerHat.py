#import explorerhat as eh

def go():
  output('go')
  # eh.motor.one.backwards(100)
  # eh.motor.two.forwards(100)

def reverse():
  output('reverse')
  # eh.motor.one.forwards(100)
  # eh.motor.two.backwards(100)

def stop():
  output('stop')
  # eh.motor.one.stop()
  # eh.motor.two.stop()

def left():
  output('left')
  # eh.motor.one.backwards(100)
  # eh.motor.two.backwards(100)

def right():
  output('right')
  # eh.motor.one.forwards(100)
  # eh.motor.two.forwards(100)

def leftBank():
  output('leftBank')
  # eh.motor.one.backward(70)
  # eh.motor.two.forwards(100)

def rightBank():
  output('rightBank')
  # eh.motor.two.forwards(70)
  # eh.motor.one.backward(100)





def output(s):
  # used to mask long words
  s += '                '
  print(s, end='')
  backspace(len(s))

def backspace(n):
  print('\r' * n, end='')

