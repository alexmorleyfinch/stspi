import pygame
import constants

positionMap = {
  constants.EX: [300, 100],
  constants.SQUARE: [250, 50],
  constants.LEFT: [100, 50],
  constants.RIGHT: [200, 50],
}

def renderText(screen, string, isGrey, key):
  font = pygame.font.Font(None, 20)
  text_bitmap = font.render(string, True, constants.GREY if not isGrey else constants.BLACK)
  screen.blit(text_bitmap, [positionMap[key][0], positionMap[key][1]])


def renderJoystickFeedback(screen, buttons):
  i = 1
  for key in buttons:
    renderText(screen, constants.BUTTONS[key], buttons[key], key)
    i=i+1
