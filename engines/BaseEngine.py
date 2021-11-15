from infra.windowManager import WindowMgr
from machine.StateMachine import StateMachine

class BaseEngine():

    def __init__(self, sct):
        self.wm = WindowMgr()
        self.wm.find_window_wildcard("BlueStacks")
        self.wm.set_foreground()
        self.machine = StateMachine(self.wm, sct)
        

