import pygame
import constants

def renderJoystickInfo(screen):
  # Get ready to print
  textPrint = TextPrint()

  textPrint.reset()

  # Get count of joysticks
  joystick_count = pygame.joystick.get_count()

  textPrint.print(screen, "Number of joysticks: {}".format(joystick_count))
  textPrint.indent()

  # For each joystick:
  for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()

    textPrint.print(screen, "Joystick {}".format(i))
    textPrint.indent()

    # Get the name from the OS for the controller/joystick
    name = joystick.get_name()
    textPrint.print(screen, "Joystick name: {}".format(name))

    # Usually axis run in pairs, up/down for one, and left/right for
    # the other.
    axes = joystick.get_numaxes()
    textPrint.print(screen, "Number of axes: {}".format(axes))
    textPrint.indent()

    for i in range(axes):
      axis = joystick.get_axis(i)
      textPrint.print(screen, "Axis {} value: {:>6.3f}".format(i, axis))
    textPrint.unindent()

    buttons = joystick.get_numbuttons()
    textPrint.print(screen, "Number of buttons: {}".format(buttons))
    textPrint.indent()

    for i in range(buttons):
      button = joystick.get_button(i)
      textPrint.print(screen, "Button {:>2} value: {}".format(i, button))
    textPrint.unindent()

    # Hat switch. All or nothing for direction, not like joysticks.
    # Value comes back in an array.
    hats = joystick.get_numhats()
    textPrint.print(screen, "Number of hats: {}".format(hats))
    textPrint.indent()

    for i in range(hats):
        hat = joystick.get_hat(i)
        textPrint.print(screen, "Hat {} value: {}".format(i, str(hat)))
    textPrint.unindent()

    textPrint.unindent()


class TextPrint(object):
  def __init__(self):
    self.reset()
    self.x_pos = 10
    self.y_pos = 10
    self.font = pygame.font.Font(None, 20)

  def print(self, my_screen, text_string):
    text_bitmap = self.font.render(text_string, True, constants.BLACK)
    my_screen.blit(text_bitmap, [self.x_pos, self.y_pos])
    self.y_pos += self.line_height

  def reset(self):
    self.x_pos = 10
    self.y_pos = 10
    self.line_height = 15

  def indent(self):
    self.x_pos += 10

  def unindent(self):
    self.x_pos -= 10
