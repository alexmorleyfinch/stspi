import pygame
from constants.app import FPS

class PygameLoop(object):
  def __init__(self, game):
    pygame.init()
    self.game = game

  def start(self):
    clock = pygame.time.Clock()
    done = False

    self.game.start()

    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

      self.game.render()

      clock.tick(FPS)

    self.game.stop()
