from output import explorerHat
from ioMap import translateInputToOutput
from input.controller import Ps3ControllerInput
from output.pygameDisplay import PygameWindowOutput

class StsPiController(object):
  def __init__(self):
    self.visualOutput = PygameWindowOutput()
    self.controllerInput = Ps3ControllerInput()

  def start(self):
    explorerHat.light1(True)

  def stop(self):
    explorerHat.light1(False)

  def render(self):
    hasController = self.controllerInput.hasController()
    buttons = None if not hasController else self.controllerInput.getButtons(0)

    if hasController:
      translateInputToOutput(buttons)

    self.visualOutput.render(hasController, buttons)
