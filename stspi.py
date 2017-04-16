from stspicontroller import StsPiController
from pygameloop import PygameLoop

game = StsPiController()
loop = PygameLoop(game)

loop.start()
