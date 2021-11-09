from inputKeys import KeyPress, TwoKeyCombo
import time
import datetime
import mss.tools

class MachineOperations():
    # Based on the controls - see bluestacks.md
    def go_to_main_menu(self, event):
        TwoKeyCombo('LCTRL', 'H')
    
    def main_to_event(self, event):
        KeyPress('V')

    def main_to_battle(self, event):
        KeyPress('B')

    def main_to_hq(self, event):
        KeyPress('H')

    def main_to_build(self, event):
        TwoKeyCombo('LCTRL', 'C')

    def main_to_quick_access(self, event):
        TwoKeyCombo('LCTRL', 'Q')

    def battle_to_campaign(self, event):
        TwoKeyCombo('LCTRL', 'A')

    def battle_to_event(self, event):
        KeyPress('V')

    def battle_to_raids(self, event):
        TwoKeyCombo('LCTRL', 'D')
    
    def battle_to_exercises(self, event):
        TwoKeyCombo('LCTRL', 'E')

    def go_chapter_1(self, event):
        currentChapters = 14
        for _ in range(currentChapters):
            KeyPress('LARROW')

    def to_next_chapter(self, event):
        KeyPress('RARROW')

    def enter_1_1(self, event):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_1_2(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_1_3(self, event):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_1_4(self, event):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_2_1(self, event):
        TwoKeyCombo('LSHIFT', '5')
    
    def enter_2_2(self, event):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_2_3(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_2_4(self, event):
        TwoKeyCombo('LSHIFT', '6')

    def enter_3_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_3_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_3_3(self, event):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_3_4(self, event):
        TwoKeyCombo('LSHIFT', '7')

    def enter_4_1(self, event):
        TwoKeyCombo('LSHIFT', '8')
    
    def enter_4_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_4_3(self, event):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_4_4(self, event):
        TwoKeyCombo('LSHIFT', '7')

    def enter_5_1(self, event):
        TwoKeyCombo('LSHIFT', '8')
    
    def enter_5_2(self, event):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_5_3(self, event):
        TwoKeyCombo('LSHIFT', '7')
    
    def enter_5_4(self, event):
        # Not actually assigned right now
        TwoKeyCombo('LSHIFT', '')

    def enter_6_1(self, event):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_6_2(self, event):
        TwoKeyCombo('LSHIFT', '7')
    
    def enter_6_3(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_6_4(self, event):
        TwoKeyCombo('LSHIFT', '9')

    def enter_7_1(self, event):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_7_2(self, event):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_7_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
    
    def enter_7_4(self, event):
        TwoKeyCombo('LSHIFT', '5')

    def enter_8_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_8_2(self, event):
        TwoKeyCombo('LSHIFT', '8')
    
    def enter_8_3(self, event):
        TwoKeyCombo('LSHIFT', '6')
    
    def enter_8_4(self, event):
        TwoKeyCombo('LSHIFT', '5')

    def enter_9_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_9_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_9_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
    
    def enter_9_4(self, event):
        TwoKeyCombo('LSHIFT', '3')

    def enter_10_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_10_2(self, event):
        TwoKeyCombo('LSHIFT', '9')
    
    def enter_10_3(self, event):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_10_4(self, event):
        TwoKeyCombo('LSHIFT', '0')

    def enter_11_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_11_2(self, event):
        TwoKeyCombo('LSHIFT', '6')
    
    def enter_11_3(self, event):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_11_4(self, event):
        TwoKeyCombo('LSHIFT', '5')

    def go_select_fleet(self, event):
        KeyPress('G')

    def set_surface_1_fleet(self, event):
        fleet1 = event.kwargs.get('fleet', 1)
        KeyPress('C')
        KeyPress(fleet1)

    def set_surface_2_fleet(self, event):
        fleet2 = event.kwargs.get('fleet', 2)
        offset = int(fleet2) + 3
        TwoKeyCombo('LALT', 'C')
        KeyPress(str(offset))

    def set_sub_fleet(self, event):
        subs = event.kwargs.get('fleet', 1)
        offset = int(subs) + 6
        KeyPress(str(offset))

    def clear_2_fleet(self, event):
        TwoKeyCombo('LSHIFT', 'C')

    def set_fleet_roles(self, event):
        KeyPress('O')
        time.sleep(1)

    def toggle_heclp_start(self, event):
        KeyPress('P')

    date_to_file_format = '%d-%m-%Y %H_%M_%S'
    screenshot_directory = './screenshots/'

    def set_timer(self, event):
        KeyPress('ENTER')
        stage = event.kwargs.get('stage', '1-1')
        print(stage)
        # Lookup the timing
        time.sleep(60 * 6)
        now = datetime.datetime.now()
        date_string = now.strftime(self.date_to_file_format)
        filename = self.screenshot_directory + date_string + '.png'
        coordinates = self.window.get_window_coordinates()
        image = self.sct.grab(coordinates)
        mss.tools.to_png(image.rgb, image.size, output=filename)

    def successful_clear(self, event):
        # TODO: check if the clearing rewards are displayed
        return True
    
    def defeated(self, event):
        # TODO: check if the defeated screen is displayed
        return False

    def not_clear_yet(self, event):
        return (not self.successful_clear()) and self.defeated() 

    def go_exit_stage(self, event):
        TwoKeyCombo('LCTRL', 'B')

    def go_continue_stage(self, event):
        TwoKeyCombo('LCTRL', 'ENTER')

    def set_another_heclp(self, event):
        TwoKeyCombo('LSHIFT', 'P')