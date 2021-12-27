from infra.windowManager import WindowMgr
from machine.StateMachine import StateMachine
import logging

class BaseEngine():

    def __init__(self, sct):
        self.wm = WindowMgr()
        self.wm.find_window_wildcard("BlueStacks")
        self.wm.set_foreground()
        self.machine = StateMachine(self.wm, sct)
        self.logger = logging.getLogger('al_state_machine.engine')
        self.logger.debug('Created base engine')
        

