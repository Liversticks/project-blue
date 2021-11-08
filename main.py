from StateMachine import StateMachine
from windowManager import WindowMgr
import sys
import mss

def main():
    with mss.mss() as sct:
        wm = WindowMgr()
        wm.find_window_wildcard("BlueStacks")
        wm.set_foreground()
        m = StateMachine(wm, sct)

        m.to_battle()
        m.to_campaign()
        m.to_chapter_1()
        for _ in range(5):
            m.next_chapter()
        m.enter_4()
        m.to_select_fleet()
        m.set_surface_1(fleet='3')
        m.set_surface_2(fleet='4')
        m.set_roles()
        m.enter_combat()
        m.finish_combat()
        m.exit_stage()
        m.to_main_menu()

if __name__ == '__main__':
    main()