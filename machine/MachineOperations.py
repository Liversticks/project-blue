from infra.inputKeys import KeyPress, TwoKeyCombo
import time
import datetime
import mss.tools
from pipeline import keras_predict, categories
import logging

class MachineOperations():
    def __init__(self):
        self.classifier = keras_predict.Classifier()
        self.logger = logging.getLogger('al_state_machine.operations')
    
    # Based on the controls - see bluestacks1.md
    def free_press(self, event):
        KeyPress('A')
        self.logger.debug('Free area pressed')

    def go_back(self, event):
        TwoKeyCombo('LCTRL', 'B')
        self.logger.debug('Back button pressed')
    
    def go_to_main_menu(self, event):
        TwoKeyCombo('LCTRL', 'H')
        self.logger.debug('Main menu button pressed')
    
    def main_to_event(self, event):
        KeyPress('V')
        self.logger.debug('Went from main menu to current event chapter')

    def main_to_battle(self, event):
        KeyPress('B')
        self.logger.debug('Went from main menu to battle menu')

    def main_to_hq(self, event):
        KeyPress('H')
        self.logger.debug('Went from main menu to HQ submenu')

    def main_to_build(self, event):
        TwoKeyCombo('LCTRL', 'C')
        self.logger.debug('Went from main menu to battle menu')

    def main_to_quick_access(self, event):
        TwoKeyCombo('LCTRL', 'Q')
        self.logger.debug('Went from main menu to quick access submenu')

    def battle_to_campaign(self, event):
        TwoKeyCombo('LCTRL', 'A')
        self.logger.debug('Went from battle menu to current campaign chapter')

    def battle_to_event(self, event):
        KeyPress('V')
        self.logger.debug('Went from battle menu to current event chapter')

    def battle_to_raids(self, event):
        TwoKeyCombo('LCTRL', 'D')
        self.logger.debug('Went from battle menu to daily raids menu')

    def battle_to_exercises(self, event):
        TwoKeyCombo('LCTRL', 'E')
        self.logger.debug('Went from battle menu to exercises menu')

    def go_chapter_1(self, event):
        currentChapters = 14
        for _ in range(currentChapters):
            self.to_previous_chapter(event)
        self.logger.debug('At chapter 1')

    def to_previous_chapter(self, event):
        KeyPress('LARROW')
        self.logger.debug('Left arrow pressed')
    
    def to_next_chapter(self, event):
        KeyPress('RARROW')
        self.logger.debug('Right arrow pressed')

    def enter_1_1(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 1-1')
    
    def enter_1_2(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 1-2')
    
    def enter_1_3(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 1-3')

    def enter_1_4(self, event):
        TwoKeyCombo('LSHIFT', '4')
        self.logger.debug('Selected stage 1-4')
    
    def enter_2_1(self, event):
        TwoKeyCombo('LSHIFT', '5')
        self.logger.debug('Selected stage 2-1')
    
    def enter_2_2(self, event):
        TwoKeyCombo('LSHIFT', '4')
        self.logger.debug('Selected stage 2-2')
    
    def enter_2_3(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 2-3')
    
    def enter_2_4(self, event):
        TwoKeyCombo('LSHIFT', '6')
        self.logger.debug('Selected stage 2-4')

    def enter_3_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 3-1')
    
    def enter_3_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 3-2')
    
    def enter_3_3(self, event):
        TwoKeyCombo('LSHIFT', '4')
        self.logger.debug('Selected stage 3-3')
    
    def enter_3_4(self, event):
        TwoKeyCombo('LSHIFT', '7')
        self.logger.debug('Selected stage 3-4')

    def enter_4_1(self, event):
        TwoKeyCombo('LSHIFT', '8')
        self.logger.debug('Selected stage 4-1')
    
    def enter_4_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 4-2')
    
    def enter_4_3(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 4-3')
    
    def enter_4_4(self, event):
        TwoKeyCombo('LSHIFT', '7')
        self.logger.debug('Selected stage 4-4')

    def enter_5_1(self, event):
        TwoKeyCombo('LSHIFT', '8')
        self.logger.debug('Selected stage 5-1')
    
    def enter_5_2(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 5-2')
    
    def enter_5_3(self, event):
        TwoKeyCombo('LSHIFT', '7')
        self.logger.debug('Selected stage 5-3')
    
    def enter_5_4(self, event):
        # Not actually assigned right now
        TwoKeyCombo('LSHIFT', '')
        self.logger.debug('Selected stage 5-4')

    def enter_6_1(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 6-1')
    
    def enter_6_2(self, event):
        TwoKeyCombo('LSHIFT', '7')
        self.logger.debug('Selected stage 6-2')
    
    def enter_6_3(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 6-3')
    
    def enter_6_4(self, event):
        TwoKeyCombo('LSHIFT', '9')
        self.logger.debug('Selected stage 6-4')

    def enter_7_1(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 7-1')
    
    def enter_7_2(self, event):
        TwoKeyCombo('LSHIFT', '4')
        self.logger.debug('Selected stage 7-2')
    
    def enter_7_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
        self.logger.debug('Selected stage 7-3')
    
    def enter_7_4(self, event):
        TwoKeyCombo('LSHIFT', '5')
        self.logger.debug('Selected stage 7-4')

    def enter_8_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 8-1')
    
    def enter_8_2(self, event):
        TwoKeyCombo('LSHIFT', '8')
        self.logger.debug('Selected stage 8-2')
    
    def enter_8_3(self, event):
        TwoKeyCombo('LSHIFT', '6')
        self.logger.debug('Selected stage 8-3')
    
    def enter_8_4(self, event):
        TwoKeyCombo('LSHIFT', '5')
        self.logger.debug('Selected stage 8-4')

    def enter_9_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 9-1')
    
    def enter_9_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 9-2')
    
    def enter_9_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
        self.logger.debug('Selected stage 9-3')
    
    def enter_9_4(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 9-4')

    def enter_10_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 10-1')
    
    def enter_10_2(self, event):
        TwoKeyCombo('LSHIFT', '9')
        self.logger.debug('Selected stage 10-2')
    
    def enter_10_3(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 10-3')
    
    def enter_10_4(self, event):
        TwoKeyCombo('LSHIFT', '0')
        self.logger.debug('Selected stage 10-4')

    def enter_11_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 11-1')
    
    def enter_11_2(self, event):
        TwoKeyCombo('LSHIFT', '6')
        self.logger.debug('Selected stage 11-2')
    
    def enter_11_3(self, event):
        TwoKeyCombo('LSHIFT', '4')
        self.logger.debug('Selected stage 11-3')
    
    def enter_11_4(self, event):
        TwoKeyCombo('LSHIFT', '5')
        self.logger.debug('Selected stage 11-4')

    def enter_12_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 12-1')

    def enter_12_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 12-2')

    def enter_12_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
        self.logger.debug('Selected stage 12-3')

    def enter_12_4(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 12-4')

    def enter_13_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
        self.logger.debug('Selected stage 13-1')

    def enter_13_2(self, event):
        TwoKeyCombo('LSHIFT', '1')
        self.logger.debug('Selected stage 13-2')


    def go_select_fleet(self, event):
        KeyPress('G')
        self.logger.debug('Moved from stage info to fleet selection')

    def set_surface_1_fleet(self, event):
        fleet1 = event.kwargs.get('fleet', 1)
        KeyPress('C')
        KeyPress(fleet1)
        self.logger.debug(f'Set first surface fleet to fleet {fleet1}')

    def set_surface_2_fleet(self, event):
        fleet2 = event.kwargs.get('fleet', 2)
        offset = int(fleet2) + 3
        TwoKeyCombo('LALT', 'C')
        KeyPress(str(offset))
        self.logger.debug(f'Set second surface fleet to fleet {fleet2}')

    def set_sub_fleet(self, event):
        subs = event.kwargs.get('fleet', 1)
        offset = int(subs) + 6
        KeyPress(str(offset))
        self.logger.debug(f'Set submarine fleet to fleet {subs}')

    def clear_2_fleet(self, event):
        TwoKeyCombo('LSHIFT', 'C')
        self.logger.debug('Cleared second surface fleet')

    def set_fleet_roles(self, event):
        KeyPress('O')
        time.sleep(1)
        self.logger.debug('Set first fleet to escorts, second fleet to bosses, and submarine fleet to always engage')

    def toggle_heclp_start(self, event):
        KeyPress('P')
        self.logger.debug('Toggled high-efficiency combat logistics plan')

    date_to_file_format = '%d-%m-%Y %H_%M_%S'
    screenshot_directory = './screenshots/'
    screenshot_threshold = 30

    def wait_interval(self):
        time.sleep(self.screenshot_threshold)
        current = time.time()
        if current - self.start_time < self.min_clear_time:
            time.sleep(self.min_clear_time - (current - self.timestamp))

    def predict_and_screenshot(self):
        current = time.time()
        if current - self.timestamp > self.screenshot_threshold:
            now = datetime.datetime.now()
            date_string = now.strftime(self.date_to_file_format)
            filename = self.screenshot_directory + date_string + '.png'
            coordinates = self.window.get_window_coordinates()
            image = self.sct.grab(coordinates)
            mss.tools.to_png(image.rgb, image.size, output=filename)
            self.logger.debug(f'Saved validation image in {self.screenshot_directory}')

            can_predict = self.classifier.to_numpy(image)
            self.status = self.classifier.predict(can_predict)
            self.timestamp = time.time()
            
        return self.status
    
    def start_stage(self, event):
        KeyPress('ENTER')
        self.min_clear_time = event.kwargs.get('min_clear_time', 60)
        self.status = 6
        self.timestamp = time.time()
        self.start_time = self.timestamp
        self.logger.debug('Started stage')

    def successful_clear(self, event):
        status = self.predict_and_screenshot()
        if categories.categories[status] == 'clear_chapter':
            self.logger.debug('Finished current stage')
            return True
        else:
            return False
    
    def defeated(self, event):
        status = self.predict_and_screenshot()
        if categories.categories[status] == 'defeat':
            self.logger.debug('Defeated in current stage')
            return True
        else:
            return False

    def not_clear_yet(self, event):
        return (not self.successful_clear(event)) and self.defeated(event) 

    def go_exit_stage(self, event):
        time.sleep(2)
        self.go_back(event)

    def go_continue_stage(self, event):
        TwoKeyCombo('LCTRL', 'ENTER')
        self.timestamp = time.time()
        self.start_time = self.timestamp
        self.status = 6
        self.logger.debug('Started same stage again in clearing mode')

    def set_another_heclp(self, event):
        TwoKeyCombo('LSHIFT', 'P')
        self.logger.debug('Set a HECLP from the stage clear dialog')

    def cleanup_def(self, event):
        KeyPress('F')
        KeyPress('I')
        KeyPress('J')
        KeyPress('K')
        self.logger.debug('Returned to the stage clear dialog after a defeat')

    # TODO: unimplemented in BlueStacks for now (11/11/21)
    def event_to_SP(self, event):
        TwoKeyCombo()
    
    def hard_mode_toggle(self, event):
        KeyPress()

    def enter_AC_1(self, event):
        TwoKeyCombo('LSHIFT', 'Z')

    def enter_AC_2(self, event):
        TwoKeyCombo('LSHIFT', 'Y')
    
    def enter_AC_3(self, event):
        TwoKeyCombo('LSHIFT', 'X')
    
    def enter_BD_1(self, event):
        TwoKeyCombo('LSHIFT', 'W')
    
    def enter_B_2(self, event):
        TwoKeyCombo('LSHIFT', 'V')
    
    def enter_D_2(self, event):
        TwoKeyCombo('LSHIFT', 'U')

    def is_event_SP(self, event):
        # TODO: DB flags based on event timing
        return True

    def enter_BD_3(self, event):
        TwoKeyCombo('LSHIFT', 'T')
    
    def enter_SP_1(self, event):
        TwoKeyCombo('LSHIFT', 'S')
    
    def enter_SP_2(self, event):
        TwoKeyCombo('LSHIFT', 'R')

    def enter_SP_3(self, event):
        TwoKeyCombo('LSHIFT', 'Q')

    def is_event_T(self, event):
        # figure out later
        return True

    def event_to_T(self, event):
        for _ in range(2):
            self.to_previous_chapter(event)
    
    def enter_T_1(self, event):
        TwoKeyCombo('LSHIFT', 'Q')

    def enter_T_2(self, event):
        TwoKeyCombo('LSHIFT', 'O')

    def enter_T_3(self, event):
        TwoKeyCombo('LSHIFT', 'N')

    def enter_T_4(self, event):
        TwoKeyCombo('LSHIFT', 'M')

    def to_daily_raids_list(self, event):
        KeyPress('D')

    def go_quick_attack(self, event):
        option = event.kwargs.get('option', '1')
        TwoKeyCombo('LCTRL', option)
        TwoKeyCombo('LALT', 'D')
        # time.sleep(1)
        self.free_press(event)

    def to_cat_lodge(self, event):
        TwoKeyCombo('LCTRL', 'T')
        TwoKeyCombo('LALT', 'H')
        self.free_press(event)

    def go_forts(self, event):
        TwoKeyCombo('LALT', 'E')

    def tend_to_cats(self, event):
        for _ in range(6):
            TwoKeyCombo('LALT', 'F')

    def go_buy_box(self, event):
        TwoKeyCombo('LALT', 'B')
        TwoKeyCombo('LALT', 'A')
        # TODO: Track whether this is the first box per day
        TwoKeyCombo('LALT', 'G')
        time.sleep(2)
        for _ in range(2):
            self.free_press(event)