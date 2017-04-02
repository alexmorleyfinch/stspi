import pygame

from constants.app import TEXT, TEXT_FADED
from constants.ps3Controller import EX, SQUARE, LEFT, RIGHT

positionMap = {
  EX: [300, 100],
  SQUARE: [250, 50],
  LEFT: [100, 50],
  RIGHT: [200, 50],
}

buttonLabels = {
  EX: 'EX',
  SQUARE: 'SQUARE',
  LEFT: 'LEFT',
  RIGHT: 'RIGHT',
}


def renderText(screen, string, isActive, key):
  pos = positionMap[key]
  font = pygame.font.Font(None, 20)
  text_bitmap = font.render(string, True, TEXT if isActive else TEXT_FADED)

  screen.blit(text_bitmap, [pos[0], pos[1]])


def renderJoystickFeedback(screen, buttons):
  i = 1
  for key in buttonLabels:
    renderText(screen, buttonLabels[key], buttons[key], key)
    i=i+1
