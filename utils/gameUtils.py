import pygame

def simpleGameLoop(fps, fn, *args):
  done = False
  clock = pygame.time.Clock()

  while not done:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True

    fn(*args)

    clock.tick(fps)

  pygame.quit()
