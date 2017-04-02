import pygame
import constants

positionMap = {
  constants.EX: [300, 100],
  constants.SQUARE: [250, 50],
  constants.LEFT: [100, 50],
  constants.RIGHT: [200, 50],
}

buttonLabels = {
  constants.EX: 'EX',
  constants.SQUARE: 'SQUARE',
  constants.LEFT: 'LEFT',
  constants.RIGHT: 'RIGHT',
}


def renderText(screen, string, isActive, key):
  pos = positionMap[key]
  font = pygame.font.Font(None, 20)
  text_bitmap = font.render(string, True, constants.BLACK if isActive else constants.GREY)

  screen.blit(text_bitmap, [pos[0], pos[1]])


def renderJoystickFeedback(screen, buttons):
  i = 1
  for key in buttonLabels:
    renderText(screen, buttonLabels[key], buttons[key], key)
    i=i+1
