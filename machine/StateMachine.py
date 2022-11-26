from infra.inputKeys import KeyPress, TwoKeyCombo
import time
import datetime
import mss.tools
from pipeline import keras_predict, categories
import logging
from transitions import Machine

class StateMachine(Machine):
    def __init__(self, debug, window, sct, screenshot_threshold=30):
        self.classifier = keras_predict.Classifier()
        self.debug = debug
        self.logger = logging.getLogger('al_state_machine.operations')
        self.window = window
        self.sct = sct
        self.screenshot_threshold = screenshot_threshold

        states = [
            'disconnected',
            'main-menu',
            'quick-access',
            'hq',
            'dorm',
            'academy',
            'battle',
            # Chapter states
            'chapter-normal-*',
            'chapter-normal-1',
            'chapter-normal-2',
            'chapter-normal-3',
            'chapter-normal-4',
            'chapter-normal-5',
            'chapter-normal-6',
            'chapter-normal-7',
            'chapter-normal-8',
            'chapter-normal-9',
            'chapter-normal-10',
            'chapter-normal-11',
            'chapter-normal-12',
            'chapter-normal-13',
            'chapter-normal-14',
            'chapter-hard-1',
            'chapter-hard-2',
            'chapter-hard-3',
            'chapter-hard-4',
            'chapter-hard-5',
            'chapter-hard-6',
            'chapter-hard-7',
            'chapter-hard-8',
            'chapter-hard-9',
            'chapter-hard-10',
            'chapter-hard-11',
            'chapter-hard-12',
            # Event "chapters"
            'current-event-*',
            'current-event-A',
            'current-event-B',
            'current-event-C',
            'current-event-D',
            'current-event-SP',
            'current-event-EX',
            'current-event-T',
            'current-event-TH',
            # All stages (Clearing mode must be on and Auto-Search must be enabled!)
            'enter-stage',
            'enter-stage-hard',
            # Fleet selection (normal stages only)
            'select-fleet',
            'combat',
            'combat-poll',
            'combat-done',
            'stage-clear',
            'stage-defeat',
            # Exercises
            'exercises-overview',
            'exercises-opponent',
            'exercises-fleet',
            'exercises-victory',
            'exercises-defeat',
            # Daily raids
            'daily-raids-t',
            'daily-raids-e',
            'daily-raids-a',
            'daily-raids-f', 
            'daily-raids-s',
            'tactical-training-levels',
            'maritime-attack-levels',
            'escort-levels',
            'fierce-assault-levels',
            'backline-disruption-levels',
            # TODO: War Archives
            # Build, exchange, retire
            'build-*',
            'build-build',
            'build-orders',
            'build-special',
            'build-exchange',
            'build-retire',
            # Cattery
            'cattery-main',
            'cattery-comffort',
            'cattery-order',
            'cattery-train',
        ]

        # template: { 'trigger': '', 'source': '', 'dest': '', 'before': '' },
        transitions = [
            { 'trigger': 'login', 'source': 'disconnected', 'dest': 'main-menu' },
            # Main menu
            { 'trigger': 'to_battle', 'source': 'main-menu', 'dest': 'battle', 'before': 'main_to_battle' },
            { 'trigger': 'to_event', 'source': 'main-menu', 'dest': 'current-event-*', 'before': 'main_to_event' },
            { 'trigger': 'to_build', 'source': 'main-menu', 'dest': 'build-*', 'before': 'main_to_build' },
            { 'trigger': 'to_hq', 'source': 'main-menu', 'dest': 'hq', 'before': 'main_to_hq' },
            { 'trigger': 'to_quick_access', 'source': 'main-menu', 'dest': 'quick-access', 'before': 'main_to_quick_access' },
            { 'trigger': 'to_main_menu', 'source': [
                'quick-access',
                'hq',
                'battle',
                'chapter-normal-*',
                'chapter-normal-1',
                'chapter-normal-2',
                'chapter-normal-3',
                'chapter-normal-4',
                'chapter-normal-5',
                'chapter-normal-6',
                'chapter-normal-7',
                'chapter-normal-8',
                'chapter-normal-9',
                'chapter-normal-10',
                'chapter-normal-11',
                'chapter-normal-12',
                'chapter-normal-13',
                'chapter-normal-14',
                'chapter-hard-1',
                'chapter-hard-2',
                'chapter-hard-3',
                'chapter-hard-4',
                'chapter-hard-5',
                'chapter-hard-6',
                'chapter-hard-7',
                'chapter-hard-8',
                'chapter-hard-9',
                'chapter-hard-10',
                'chapter-hard-11',
                'chapter-hard-12',
                'current-event-*',
                'daily-raids-a',
                'daily-raids-t',
                'daily-raids-f',
                'daily-raids-e',
                'daily-raids-s',
                ], 'dest': 'main-menu', 'before': 'go_to_main_menu' },
            # Quick access submenu
            { 'trigger': 'collect_coins', 'source': 'quick-access', 'dest': None },
            { 'trigger': 'collect_oil', 'source': 'quick-access', 'dest': None },
            { 'trigger': 'collect_XP_packs', 'source': 'quick-access', 'dest': None },
            # HQ submenu
            { 'trigger': 'to_academy', 'source': 'hq', 'dest': 'academy' },
            { 'trigger': 'to_dorm', 'source': 'hq', 'dest': 'dorm' },
            { 'trigger': 'to_cattery', 'source': 'hq', 'dest': 'cattery-main', 'before': 'to_cat_lodge' },
            # Battle menu
            { 'trigger': 'to_campaign', 'source': 'battle', 'dest': 'chapter-normal-*', 'before': 'battle_to_campaign' },
            { 'trigger': 'to_event', 'source': 'battle', 'dest': 'current-event-*', 'before': 'battle_to_event' },
            { 'trigger': 'to_exercises', 'source': 'battle', 'dest': 'exercises-overview', 'before': 'battle_to_exercises' },
            { 'trigger': 'to_daily_raids', 'source': 'battle', 'dest': 'daily-raids-t', 'before': 'battle_to_raids' },
            # Campaign stages
            { 'trigger': 'to_chapter_1', 'source': 'chapter-normal-*', 'dest': 'chapter-normal-1', 'before': 'go_chapter_1' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-1', 'dest': 'chapter-normal-2', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-2', 'dest': 'chapter-normal-3', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-3', 'dest': 'chapter-normal-4', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-4', 'dest': 'chapter-normal-5', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-5', 'dest': 'chapter-normal-6', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-6', 'dest': 'chapter-normal-7', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-7', 'dest': 'chapter-normal-8', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-8', 'dest': 'chapter-normal-9', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-9', 'dest': 'chapter-normal-10', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-10', 'dest': 'chapter-normal-11', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-11', 'dest': 'chapter-normal-12', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-12', 'dest': 'chapter-normal-13', 'before': 'to_next_chapter' },
            { 'trigger': 'next_chapter', 'source': 'chapter-normal-13', 'dest': 'chapter-normal-14', 'before': 'to_next_chapter' },
            # prev_chapter is unnecessary because of to_chapter_1
            { 'trigger': 'to_hard', 'source': 'chapter-normal-1', 'dest': 'chapter-hard-1' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-2', 'dest': 'chapter-hard-2' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-3', 'dest': 'chapter-hard-3' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-4', 'dest': 'chapter-hard-4' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-5', 'dest': 'chapter-hard-5' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-6', 'dest': 'chapter-hard-6' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-7', 'dest': 'chapter-hard-7' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-8', 'dest': 'chapter-hard-8' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-9', 'dest': 'chapter-hard-9' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-10', 'dest': 'chapter-hard-10' },
            { 'trigger': 'to_hard', 'source': 'chapter-normal-11', 'dest': 'chapter-hard-11' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage', 'before': 'enter_1_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage', 'before': 'enter_1_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage', 'before': 'enter_1_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage', 'before': 'enter_1_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage', 'before': 'enter_2_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage', 'before': 'enter_2_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage', 'before': 'enter_2_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage', 'before': 'enter_2_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage', 'before': 'enter_3_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage', 'before': 'enter_3_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage', 'before': 'enter_3_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage', 'before': 'enter_3_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage', 'before': 'enter_4_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage', 'before': 'enter_4_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage', 'before': 'enter_4_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage', 'before': 'enter_4_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage', 'before': 'enter_5_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage', 'before': 'enter_5_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage', 'before': 'enter_5_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage', 'before': 'enter_5_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage', 'before': 'enter_6_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage', 'before': 'enter_6_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage', 'before': 'enter_6_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage', 'before': 'enter_6_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage', 'before': 'enter_7_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage', 'before': 'enter_7_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage', 'before': 'enter_7_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage', 'before': 'enter_7_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage', 'before': 'enter_8_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage', 'before': 'enter_8_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage', 'before': 'enter_8_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage', 'before': 'enter_8_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage', 'before': 'enter_9_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage', 'before': 'enter_9_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage', 'before': 'enter_9_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage', 'before': 'enter_9_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-10', 'chapter-hard-10'], 'dest': 'enter-stage', 'before': 'enter_10_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-10', 'chapter-hard-10'], 'dest': 'enter-stage', 'before': 'enter_10_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-10', 'chapter-hard-10'], 'dest': 'enter-stage', 'before': 'enter_10_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-10', 'chapter-hard-10'], 'dest': 'enter-stage', 'before': 'enter_10_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage', 'before': 'enter_11_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage', 'before': 'enter_11_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage', 'before': 'enter_11_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage', 'before': 'enter_11_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-12', 'chapter-hard-12'], 'dest': 'enter-stage', 'before': 'enter_12_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-12', 'chapter-hard-12'], 'dest': 'enter-stage', 'before': 'enter_12_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-12', 'chapter-hard-12'], 'dest': 'enter-stage', 'before': 'enter_12_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-12', 'chapter-hard-12'], 'dest': 'enter-stage', 'before': 'enter_12_4' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-13'], 'dest': 'enter-stage', 'before': 'enter_13_1' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-13'], 'dest': 'enter-stage', 'before': 'enter_13_2' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-13'], 'dest': 'enter-stage', 'before': 'enter_13_3' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-13'], 'dest': 'enter-stage', 'before': 'enter_13_4' },
            # Event stages
            { 'trigger': 'to_SP', 'source': ['current-event-*', 'current-event-T'], 'dest': 'current-event-SP', 'before': 'event_to_SP' },
            { 'trigger': 'to_D', 'source': 'current-event-SP', 'dest': 'current-event-D', 'before': 'event_to_SP' },
            { 'trigger': 'to_B', 'source': 'current-event-SP', 'dest': 'current-event-B', 'before': 'hard_mode_toggle' },
            { 'trigger': 'to_C', 'source': 'current-event-D', 'dest': 'current-event-C', 'before': 'to_previous_chapter' },
            { 'trigger': 'to_A', 'source': 'current-event-B', 'dest': 'current-event-A', 'before': 'to_previous_chapter' },
            { 'trigger': 'to_T', 'source': 'current-event-*', 'dest': 'current-event-T', 'before': 'event_to_T' },
            { 'trigger': 'to_TH', 'source': 'current-event-SP', 'dest': 'current-event-TH', 'before': 'event_to_SP' },
            { 'trigger': 'enter_1', 'source': ['current-event-A', 'current-event-C'], 'dest': 'enter-stage', 'before': 'enter_AC_1' },
            { 'trigger': 'enter_2', 'source': ['current-event-A', 'current-event-C'], 'dest': 'enter-stage', 'before': 'enter_AC_2' },
            { 'trigger': 'enter_3', 'source': ['current-event-A', 'current-event-C'], 'dest': 'enter-stage', 'before': 'enter_AC_3' },
            { 'trigger': 'enter_1', 'source': 'current-event-B', 'dest': 'enter-stage', 'before': 'enter_B_1' },
            { 'trigger': 'enter_1', 'source': 'current-event-D', 'dest': 'enter-stage', 'before': 'enter_D_1' },
            { 'trigger': 'enter_2', 'source': 'current-event-B', 'dest': 'enter-stage', 'before': 'enter_B_2' },
            { 'trigger': 'enter_2', 'source': 'current-event-D', 'dest': 'enter-stage', 'before': 'enter_D_2' },
            { 'trigger': 'enter_3', 'source': ['current-event-B', 'current-event-D'], 'dest': 'enter-stage', 'before': 'enter_BD_3' },
            { 'trigger': 'enter_1', 'source': 'current-event-*', 'dest': 'enter-stage', 'before': 'enter_SP_1', 'conditions': 'is_event_SP' },
            { 'trigger': 'enter_2', 'source': 'current-event-*', 'dest': 'enter-stage', 'before': 'enter_SP_2', 'conditions': 'is_event_SP' },
            { 'trigger': 'enter_3', 'source': 'current-event-*', 'dest': 'enter-stage', 'before': 'enter_SP_3', 'conditions': 'is_event_SP' },
            { 'trigger': 'enter_4', 'source': 'current-event-*', 'dest': 'enter-stage', 'before': 'enter_SP_4', 'conditions': 'is_event_SP' },
            { 'trigger': 'enter_1', 'source': 'current-event-T', 'dest': 'enter-stage', 'before': 'enter_T_1', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_2', 'source': 'current-event-T', 'dest': 'enter-stage', 'before': 'enter_T_2', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_3', 'source': 'current-event-T', 'dest': 'enter-stage', 'before': 'enter_T_3', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_4', 'source': 'current-event-T', 'dest': 'enter-stage', 'before': 'enter_T_4', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_5', 'source': 'current-event-T', 'dest': 'enter-stage', 'before': 'enter_T_5', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_1', 'source': 'current-event-TH', 'dest': 'enter-stage', 'before': 'enter_T_1', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_2', 'source': 'current-event-TH', 'dest': 'enter-stage', 'before': 'enter_T_2', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_3', 'source': 'current-event-TH', 'dest': 'enter-stage', 'before': 'enter_T_3', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_4', 'source': 'current-event-TH', 'dest': 'enter-stage', 'before': 'enter_T_4', 'conditions': 'is_event_T' },
            { 'trigger': 'enter_5', 'source': 'current-event-TH', 'dest': 'enter-stage', 'before': 'enter_T_5', 'conditions': 'is_event_T' },
            # TODO: War Archive stages
            
            # Normal mode fleet selection
            # Hard mode requires manually pre-selecting the fleets (which are the same for the entire chapter)
            { 'trigger': 'to_select_fleet', 'source': 'enter-stage', 'dest': 'select-fleet', 'before': 'go_select_fleet' },
            { 'trigger': 'set_surface_1', 'source': 'select-fleet', 'dest': None, 'before': 'set_surface_1_fleet' },
            { 'trigger': 'set_surface_2', 'source': 'select-fleet', 'dest': None, 'before': 'set_surface_2_fleet' },
            { 'trigger': 'set_sub', 'source': 'select-fleet', 'dest': None, 'before': 'set_sub_fleet' },
            { 'trigger': 'clear_2', 'source': 'select-fleet', 'dest': None, 'before': 'clear_2_fleet' },
            { 'trigger': 'set_roles_main', 'source': 'select-fleet', 'dest': None, 'before': 'set_fleet_roles_main' },
            { 'trigger': 'set_roles_alt', 'source': 'select-fleet', 'dest': None, 'before': 'set_fleet_roles_alt' },
            { 'trigger': 'toggle_heclp', 'source': 'select-fleet', 'dest': None, 'before': 'toggle_heclp_start' },
            { 'trigger': 'enter_combat', 'source': 'select-fleet', 'dest': 'combat', 'before': 'start_stage' },
            # TODO: some way to detect whether we finish in Normal or Hard Mode
            # For default_time_clear, avoid using the screenshot engine
            { 'trigger': 'default_time_clear', 'source': 'combat', 'dest': 'stage-clear', 'before': 'wait_default' },
            { 'trigger': 'poll_clear', 'source': 'combat', 'dest': 'combat-poll' },
            { 'trigger': 'poll_clear', 'source': 'combat-poll', 'dest': None, 'conditions': 'not_clear_yet', 'before': 'wait_interval' },
            { 'trigger': 'poll_clear', 'source': 'combat-poll', 'dest': 'combat-done', 'unless': 'not_clear_yet' },
            { 'trigger': 'finish_combat', 'source': 'combat-done', 'dest': 'stage-clear', 'conditions': 'successful_clear' },
            { 'trigger': 'finish_combat', 'source': 'combat-done', 'dest': 'stage-defeat', 'conditions': 'defeated' },
            { 'trigger': 'set_heclp', 'source': 'stage-clear', 'dest': None, 'before': 'set_another_heclp' },
            { 'trigger': 'continue_stage', 'source': 'stage-clear', 'dest': 'combat', 'before': 'go_continue_stage' },
            { 'trigger': 'exit_stage', 'source': 'stage-clear', 'dest': 'chapter-normal-*', 'before': 'go_exit_stage' },
            { 'trigger': 'cleanup_defeat', 'source': 'stage-defeat', 'dest': 'stage-clear', 'before': 'cleanup_def' },
            # Daily Raids
            { 'trigger': 'raids_left', 'source': 'daily-raids-t', 'dest': 'daily-raids-f', 'before': 'to_previous_chapter' },
            { 'trigger': 'raids_right', 'source': 'daily-raids-t', 'dest': 'daily-raids-a', 'before': 'to_next_chapter' },
            { 'trigger': 'raids_left', 'source': 'daily-raids-f', 'dest': 'daily-raids-s', 'before': 'to_previous_chapter' },
            { 'trigger': 'raids_right', 'source': 'daily-raids-f', 'dest': 'daily-raids-t', 'before': 'to_next_chapter' },
            { 'trigger': 'raids_left', 'source': 'daily-raids-s', 'dest': 'daily-raids-e', 'before': 'to_previous_chapter' },
            { 'trigger': 'raids_right', 'source': 'daily-raids-s', 'dest': 'daily-raids-f', 'before': 'to_next_chapter' },
            { 'trigger': 'raids_left', 'source': 'daily-raids-e', 'dest': 'daily-raids-a', 'before': 'to_previous_chapter' },
            { 'trigger': 'raids_right', 'source': 'daily-raids-e', 'dest': 'daily-raids-s', 'before': 'to_next_chapter' },
            { 'trigger': 'raids_left', 'source': 'daily-raids-a', 'dest': 'daily-raids-t', 'before': 'to_previous_chapter' },
            { 'trigger': 'raids_right', 'source': 'daily-raids-a', 'dest': 'daily-raids-e', 'before': 'to_next_chapter' },
            { 'trigger': 'to_levels', 'source': 'daily-raids-t', 'dest': 'tactical-training-levels', 'before': 'to_daily_raids_list' },
            { 'trigger': 'to_levels', 'source': 'daily-raids-e', 'dest': 'escort-levels', 'before': 'to_daily_raids_list' },
            { 'trigger': 'to_levels', 'source': 'daily-raids-a', 'dest': 'maritime-attack-levels', 'before': 'to_daily_raids_list' },
            { 'trigger': 'to_levels', 'source': 'daily-raids-f', 'dest': 'fierce-assault-levels', 'before': 'to_daily_raids_list' },
            { 'trigger': 'to_levels', 'source': 'daily-raids-s', 'dest': 'backline-disruption-levels', 'before': 'to_daily_raids_list' },
            { 'trigger': 'quick_attack', 'source': ['escort-levels', 'fierce-assault-levels', 'maritime-attack-levels', 'tactical-training-levels'], 'dest': None, 'before': 'go_quick_attack' },
            { 'trigger': 'to_daily_raids', 'source': 'escort-levels', 'dest': 'daily-raids-e', 'before': 'go_exit_stage' },
            { 'trigger': 'to_daily_raids', 'source': 'fierce-assault-levels', 'dest': 'daily-raids-f', 'before': 'go_exit_stage' },
            { 'trigger': 'to_daily_raids', 'source': 'maritime-attack-levels', 'dest': 'daily-raids-a', 'before': 'go_exit_stage' },
            { 'trigger': 'to_daily_raids', 'source': 'tactical-training-levels', 'dest': 'daily-raids-t', 'before': 'go_exit_stage' },
            { 'trigger': 'to_daily_raids', 'source': 'backline-disruption-levels', 'dest': 'daily-raids-s', 'before': 'go_exit_stage' },
            # Cattery
            { 'trigger': 'to_forts', 'source': 'cattery-main', 'dest': 'cattery-comffort', 'before': 'go_forts' },
            { 'trigger': 'level_forts', 'source': 'cattery-comffort', 'dest': 'cattery-main', 'before': 'tend_to_cats' },
            { 'trigger': 'buy_cat', 'source': 'cattery-main', 'dest': None, 'before': 'go_buy_box' },
            { 'trigger': 'to_main_menu', 'source': 'cattery-main', 'dest': 'main-menu', 'before': 'go_back' },
        ]

        Machine.__init__(self, states=states, transitions=transitions, initial='main-menu', auto_transitions=False, send_event=True)
    
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

    def enter_13_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
        self.logger.debug('Selected stage 13-3')

    def enter_13_4(self, event):
        TwoKeyCombo('LSHIFT', '3')
        self.logger.debug('Selected stage 13-4')

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

    def set_fleet_roles_main(self, event):
        KeyPress('O')
        time.sleep(1)
        self.logger.debug('Set first fleet to escorts, second fleet to bosses, and submarine fleet to always engage')

    def set_fleet_roles_alt(self, event):
        KeyPress('N')
        time.sleep(1)
        self.logger.debug('Set first fleet to bosses and second fleet to escorts')

    def toggle_heclp_start(self, event):
        KeyPress('P')
        self.logger.debug('Toggled high-efficiency combat logistics plan')

    date_to_file_format = '%Y-%m-%d %H_%M_%S'
    screenshot_directory = './screenshots/'

    def wait_default(self, event):
        wait = event.kwargs.get('wait', 300)
        self.logger.debug(f'Begin default wait of {wait} seconds')
        time.sleep(wait)

    def wait_interval(self, event):
        time.sleep(self.screenshot_threshold)

    def predict_and_screenshot(self):
        current = time.time()
        if current - self.timestamp > self.screenshot_threshold:
            coordinates = self.window.get_window_coordinates()
            image = self.sct.grab(coordinates)
            
            can_predict = self.classifier.to_numpy(image)
            self.status = self.classifier.predict(can_predict)
            
            if self.debug:
                now = datetime.datetime.now()
                date_string = now.strftime(self.date_to_file_format)
                filename = f'{self.screenshot_directory}{categories.categories[self.status]}/{date_string}.png'
                mss.tools.to_png(image.rgb, image.size, output=filename)
                self.logger.debug(f'Saved validation image in {self.screenshot_directory}')

            self.timestamp = time.time()
            
        return self.status
    
    def start_stage(self, event):
        KeyPress('ENTER')
        self.status = 6
        self.timestamp = time.time()
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
        return (not self.successful_clear(event)) and (not self.defeated(event)) 

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

    def event_to_SP(self, event):
        TwoKeyCombo('LSHIFT', 'Y')
    
    def hard_mode_toggle(self, event):
        TwoKeyCombo('LSHIFT', 'Z')

    def enter_AC_1(self, event):
        TwoKeyCombo('LSHIFT', '2')

    def enter_AC_2(self, event):
        TwoKeyCombo('LSHIFT', 'O')
    
    def enter_AC_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
    
    def enter_B_1(self, event):
        TwoKeyCombo('LSHIFT', '9')
    
    def enter_D_1(self, event):
        TwoKeyCombo('LSHIFT', '2')
    
    # TODO: find a more permanent mapping
    def enter_B_2(self, event):
        TwoKeyCombo('LALT', 'E')
    
    def enter_D_2(self, event):
        TwoKeyCombo('LSHIFT', '1')

    def is_event_SP(self, event):
        # TODO: DB flags based on event timing
        return True

    def enter_BD_3(self, event):
        TwoKeyCombo('LSHIFT', '0')
    
    def enter_SP_1(self, event):
        TwoKeyCombo('LSHIFT', 'S')
    
    def enter_SP_2(self, event):
        TwoKeyCombo('LSHIFT', 'R')

    def enter_SP_3(self, event):
        TwoKeyCombo('LSHIFT', 'Q')

    def enter_SP_4(self, event):
        TwoKeyCombo('LSHIFT', '0')

    def is_event_T(self, event):
        # figure out later
        return True

    def event_to_T(self, event):
        for _ in range(2):
            self.to_previous_chapter(event)
    
    def enter_T_1(self, event):
        TwoKeyCombo('LSHIFT', '7')

    def enter_T_2(self, event):
        TwoKeyCombo('LSHIFT', 'A')

    def enter_T_3(self, event):
        TwoKeyCombo('LSHIFT', 'Q')

    def enter_T_4(self, event):
        TwoKeyCombo('LSHIFT', '6')

    def enter_T_5(self, event):
        TwoKeyCombo('LSHIFT', 'R')

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