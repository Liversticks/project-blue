from machine.StateMachine import StateMachine
import logging

class BaseEngine():

    def __init__(self, debug, wm, sct):
        self.debug = debug
        self.wm = wm
        if self.wm is not None:
            self.wm.find_window_wildcard("BlueStacks")
            self.wm.set_foreground()
        self.machine = StateMachine(debug, self.wm, sct)
        self.logger = logging.getLogger('al_state_machine.engine')
        self.logger.debug('Created base engine')
        

