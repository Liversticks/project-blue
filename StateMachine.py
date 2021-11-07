from transitions import Machine, State
from inputKeys import KeyPress, TwoKeyCombo

class StateMachine(Machine):
    # Based on the controls - see bluestacks.md
    def go_to_main_menu(self):
        TwoKeyCombo('LCTRL', 'H')
    
    def main_to_event(self):
        KeyPress('V')

    def main_to_battle(self):
        KeyPress('B')

    def main_to_hq(self):
        KeyPress('H')

    def main_to_build(self):
        TwoKeyCombo('LCTRL', 'C')

    def main_to_quick_access(self):
        TwoKeyCombo('LCTRL', 'Q')

    def battle_to_campaign(self):
        KeyPress()

    def battle_to_event(self):
        KeyPress()

    def battle_to_raids(self):
        KeyPress()
    
    def battle_to_exercises(self):
        KeyPress()

    def to_chapter_1(self):
        currentChapters = 14
        for _ in range(currentChapters):
            KeyPress('LARROW')

    def to_next_chapter(self):
        KeyPress('RARROW')

    def enter_1_1(self):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_1_2(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_1_3(self):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_1_4(self):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_2_1(self):
        TwoKeyCombo('LSHIFT', '5')
    
    def enter_2_2(self):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_2_3(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_2_4(self):
        TwoKeyCombo('LSHIFT', '6')

    def enter_3_1(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_3_2(self):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_3_3(self):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_3_4(self):
        TwoKeyCombo('LSHIFT', '7')

    def enter_4_1(self):
        TwoKeyCombo('LSHIFT', '8')
    
    def enter_4_2(self):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_4_3(self):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_4_4(self):
        TwoKeyCombo('LSHIFT', '7')

    def enter_5_1(self):
        TwoKeyCombo('LSHIFT', '8')
    
    def enter_5_2(self):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_5_3(self):
        TwoKeyCombo('LSHIFT', '7')
    
    def enter_5_4(self):
        # Not actually assigned right now
        TwoKeyCombo('LSHIFT', '')

    def enter_6_1(self):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_6_2(self):
        TwoKeyCombo('LSHIFT', '7')
    
    def enter_6_3(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_6_4(self):
        TwoKeyCombo('LSHIFT', '9')

    def enter_7_1(self):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_7_2(self):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_7_3(self):
        TwoKeyCombo('LSHIFT', '0')
    
    def enter_7_4(self):
        TwoKeyCombo('LSHIFT', '5')

    def enter_8_1(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_8_2(self):
        TwoKeyCombo('LSHIFT', '8')
    
    def enter_8_3(self):
        TwoKeyCombo('LSHIFT', '6')
    
    def enter_8_4(self):
        TwoKeyCombo('LSHIFT', '5')

    def enter_9_1(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_9_2(self):
        TwoKeyCombo('LSHIFT', '1')
    
    def enter_9_3(self):
        TwoKeyCombo('LSHIFT', '0')
    
    def enter_9_4(self):
        TwoKeyCombo('LSHIFT', '3')

    def enter_10_1(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_10_2(self):
        TwoKeyCombo('LSHIFT', '9')
    
    def enter_10_3(self):
        TwoKeyCombo('LSHIFT', '3')
    
    def enter_10_4(self):
        TwoKeyCombo('LSHIFT', '0')

    def enter_11_1(self):
        TwoKeyCombo('LSHIFT', '2')
    
    def enter_11_2(self):
        TwoKeyCombo('LSHIFT', '6')
    
    def enter_11_3(self):
        TwoKeyCombo('LSHIFT', '4')
    
    def enter_11_4(self):
        TwoKeyCombo('LSHIFT', '5')

    def successful_clear(self):
        # TODO: check if the clearing rewards are displayed
        return True
    
    def defeated(self):
        # TODO: check if the defeated screen is displayed
        return False

    def not_clear_yet(self):
        return (not self.successful_clear()) and (not self.defeated()) 
    
    def __init__(self):
        
        states = [
            'disconnected',
            'main-menu',
            'quick-access',
            'hq',
            'dorm',
            'academy',
            'cattery',
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
            # Event "chapters"
            'current-event-*',
            'current-event-A',
            'current-event-B',
            'current-event-C',
            'current-event-D',
            'current-event-SP',
            'current-event-EX',
            # All stages (Clearing mode must be on and Auto-Search must be enabled!)
            'enter-stage',
            'enter-stage-hard',
            # Fleet selection (normal stages only)
            'select-fleet',
            'combat',
            'stage-clear',
            'stage-defeat',
            # Exercises
            'exercises-overview',
            'exercises-opponent',
            'exercises-fleet',
            'exercises-victory',
            'exercises-defeat',
            # Daily raids
            'daily-raids',
            'escort-mission',
            'advance-mission',
            'fierce-assault',
            'supply-line-disruption',
            'tactical-training',
            'tactical-training-aviation',
            'tactical-training-shelling',
            'tactical-training-torpedo',
            'maritime-attack-levels',
            'escort-firepower',
            'escort-air',
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

        # template: { 'trigger': '', 'source': '', 'dest': '' }
        # TODO: add callbacks
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
                'daily-raids',
                ], 'dest': 'main-menu', 'before': 'go_to_main_menu' },
            # Quick access submenu
            { 'trigger': 'collect_coins', 'source': 'quick-access', 'dest': None },
            { 'trigger': 'collect_oil', 'source': 'quick-access', 'dest': None },
            { 'trigger': 'collect_XP_packs', 'source': 'quick-access', 'dest': None },
            # HQ submenu
            { 'trigger': 'to_academy', 'source': 'hq', 'dest': 'academy' },
            { 'trigger': 'to_dorm', 'source': 'hq', 'dest': 'dorm' },
            { 'trigger': 'to_cattery', 'source': 'hq', 'dest': 'cattery' },
            # Battle menu
            { 'trigger': 'to_campaign', 'source': 'battle', 'dest': 'chapter-normal-*', 'before': 'battle_to_campaign' },
            { 'trigger': 'to_event', 'source': 'battle', 'dest': 'current-event-*', 'before': 'battle_to_event' },
            { 'trigger': 'to_exercises', 'source': 'battle', 'dest': 'exercises-overview', 'before': 'battle_to_exercises' },
            { 'trigger': 'to_daily_raids', 'source': 'battle', 'dest': 'daily-raids', 'before': 'battle_to_raids' },
            # Campaign stages
            { 'trigger': 'to_chapter_1', 'source': 'chapter-normal-*', 'dest': 'chapter-normal-1', 'before': 'to_chapter_1' },
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
            { 'trigger': 'enter_1', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-1', 'chapter-hard-1'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-2', 'chapter-hard-2'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-3', 'chapter-hard-3'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-4', 'chapter-hard-4'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-5', 'chapter-hard-5'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-6', 'chapter-hard-6'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-7', 'chapter-hard-7'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-8', 'chapter-hard-8'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-9', 'chapter-hard-9'],'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-9', 'chapter-hard-9'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-10', 'chapter-hard-10'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-10', 'chapter-hard-10'],  'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-10', 'chapter-hard-10'],  'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-10', 'chapter-hard-10'],  'dest': 'enter-stage' },
            { 'trigger': 'enter_1', 'source': ['chapter-normal-11', 'chapter-hard-11'],  'dest': 'enter-stage' },
            { 'trigger': 'enter_2', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_3', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage' },
            { 'trigger': 'enter_4', 'source': ['chapter-normal-11', 'chapter-hard-11'], 'dest': 'enter-stage' },
            # TODO: triggers for entering chapter 12-14 normal stages
            # Normal mode fleet selection
            # Hard mode requires manually pre-selecting the fleets (which are the same for the entire chapter)
            { 'trigger': 'to_select_fleet', 'source': 'enter-stage', 'dest': 'select-fleet' },
            { 'trigger': 'clear_2', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_1_1', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_1_2', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_1_3', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_1_4', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_1_5', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_1_6', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_2_1', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_2_2', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_2_3', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_2_4', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_2_5', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'surface_2_6', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'sub_1_1', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'set_roles', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'set_heclp', 'source': 'select-fleet', 'dest': None },
            { 'trigger': 'enter_combat', 'source': 'select-fleet', 'dest': 'combat' },
            # TODO: some way to detect whether we finish in Normal or Hard Mode
            { 'trigger': 'finish_combat', 'source': 'combat', 'dest': 'stage-clear', 'conditions': 'successful_clear' },
            { 'trigger': 'finish_combat', 'source': 'combat', 'dest': 'stage-defeat', 'conditions': 'defeated' },
            { 'trigger': 'finish_combat', 'source': 'combat', 'dest': None, 'conditions': 'not_clear_yet' },
        ]

        Machine.__init__(self, states=states, transitions=transitions, initial='main-menu', auto_transitions=False)