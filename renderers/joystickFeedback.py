import pygame
import constants

def renderText(screen, string, x, y):
  font = pygame.font.Font(None, 20)
  text_bitmap = font.render(string, True, constants.BLACK)
  screen.blit(text_bitmap, [x, y])


def renderJoystickFeedback(screen, buttons):
  i = 1
  for key in buttons:
    if not buttons[key]: continue
    renderText(screen, constants.BUTTONS[key], 20, i*20)
    i=i+1
