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
    print('Game Starting')

    try:
      while not done:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            done = True

        try:
          self.game.render()
        except pygame.error as err:
          print('Pygame Error:', err)
          done = True

        clock.tick(FPS)
    except KeyboardInterrupt:
      print(" Interrupt")

    self.game.stop()
    print('Game Stopped')
