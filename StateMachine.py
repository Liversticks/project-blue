from transitions import Machine, State
from inputKeys import KeyPress, TwoKeyCombo

class StateMachine():
    # Based on the controls - see bluestacks.md
    def go_to_main_menu():
        TwoKeyCombo('LCTRL', 'H')
    
    def go_to_event():
        KeyPress('V')

    
    
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
        # Event stages
        'enter-A-1',
        'enter-A-2',
        'enter-A-3',
        'enter-B-1',
        'enter-B-2',
        'enter-B-3',
        'enter-C-1',
        'enter-C-2',
        'enter-C-3',
        'enter-D-1',
        'enter-D-2',
        'enter-D-3',
        # SP and EX should be done manually...for now
        # Normal mode stages
        'enter-1-1-N',
        'enter-1-2-N',
        'enter-1-3-N',
        'enter-1-4-N',
        'enter-2-1-N',
        'enter-2-2-N',
        'enter-2-3-N',
        'enter-2-4-N',
        'enter-3-1-N',
        'enter-3-2-N',
        'enter-3-3-N',
        'enter-3-4-N',
        'enter-4-1-N',
        'enter-4-2-N',
        'enter-4-3-N',
        'enter-4-4-N',
        'enter-5-1-N',
        'enter-5-2-N',
        'enter-5-3-N',
        'enter-5-4-N',
        'enter-6-1-N',
        'enter-6-2-N',
        'enter-6-3-N',
        'enter-6-4-N',
        'enter-7-1-N',
        'enter-7-2-N',
        'enter-7-3-N',
        'enter-7-4-N',
        'enter-8-1-N',
        'enter-8-2-N',
        'enter-8-3-N',
        'enter-8-4-N',
        'enter-9-1-N',
        'enter-9-2-N',
        'enter-9-3-N',
        'enter-9-4-N',
        'enter-10-1-N',
        'enter-10-2-N',
        'enter-10-3-N',
        'enter-10-4-N',
        'enter-11-1-N',
        'enter-11-2-N',
        'enter-11-3-N',
        'enter-11-4-N',
        'enter-12-1-N',
        'enter-12-2-N',
        'enter-12-3-N',
        'enter-12-4-N',
        'enter-13-1-N',
        'enter-13-2-N',
        'enter-13-3-N',
        'enter-13-4-N',
        'enter-14-1-N',
        'enter-14-2-N',
        'enter-14-3-N',
        'enter-14-4-N',
        # Hard mode stages
        'enter-1-1-H',
        'enter-1-2-H',
        'enter-1-3-H',
        'enter-1-4-H',
        'enter-2-1-H',
        'enter-2-2-H',
        'enter-2-3-H',
        'enter-2-4-H',
        'enter-3-1-H',
        'enter-3-2-H',
        'enter-3-3-H',
        'enter-3-4-H',
        'enter-4-1-H',
        'enter-4-2-H',
        'enter-4-3-H',
        'enter-4-4-H',
        'enter-5-1-H',
        'enter-5-2-H',
        'enter-5-3-H',
        'enter-5-4-H',
        'enter-6-1-H',
        'enter-6-2-H',
        'enter-6-3-H',
        'enter-6-4-H',
        'enter-7-1-H',
        'enter-7-2-H',
        'enter-7-3-H',
        'enter-7-4-H',
        'enter-8-1-H',
        'enter-8-2-H',
        'enter-8-3-H',
        'enter-8-4-H',
        'enter-9-1-H',
        'enter-9-2-H',
        'enter-9-3-H',
        'enter-9-4-H',
        'enter-10-1-H',
        'enter-10-2-H',
        'enter-10-3-H',
        'enter-10-4-H',
        'enter-11-1-H',
        'enter-11-2-H',
        'enter-11-3-H',
        'enter-11-4-H',
        # Fleet selection
        'select-1-surface',
        'select-2-surface',
        'select-all',
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
        { 'trigger': 'to_battle', 'source': 'main-menu', 'dest': 'battle' },
        { 'trigger': 'to_event', 'source': 'main-menu', 'dest': 'current-event-*' },
        { 'trigger': 'to_build', 'source': 'main-menu', 'dest': 'build-*' },
        { 'trigger': 'to_hq', 'source': 'main-menu', 'dest': 'hq' },
        { 'trigger': 'to_quick_access', 'source': 'main-menu', 'dest': 'quick-access' },
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
            ], 'dest': 'main-menu' },
        # Quick access submenu
        { 'trigger': 'collect_coins', 'source': 'quick-access', 'dest': None },
        { 'trigger': 'collect_oil', 'source': 'quick-access', 'dest': None },
        { 'trigger': 'collect_XP_packs', 'source': 'quick-access', 'dest': None },
        # HQ submenu
        { 'trigger': 'to_academy', 'source': 'hq', 'dest': 'academy' },
        { 'trigger': 'to_dorm', 'source': 'hq', 'dest': 'dorm' },
        { 'trigger': 'to_cattery', 'source': 'hq', 'dest': 'cattery' },
        # Battle menu
        { 'trigger': 'to_campaign', 'source': 'battle', 'dest': 'chapter-normal-*' },
        { 'trigger': 'to_event', 'source': 'battle', 'dest': 'current-event-*' },
        { 'trigger': 'to_exercises', 'source': 'battle', 'dest': 'exercises-overview' },
        { 'trigger': 'to_daily_raids', 'source': 'battle', 'dest': 'daily-raids' },
        # Campaign stages
        { 'trigger': 'to_chapter_1', 'source': 'chapter-normal-*', 'dest': 'chapter-normal-1' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-1', 'dest': 'chapter-normal-2' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-2', 'dest': 'chapter-normal-3' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-3', 'dest': 'chapter-normal-4' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-4', 'dest': 'chapter-normal-5' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-5', 'dest': 'chapter-normal-6' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-6', 'dest': 'chapter-normal-7' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-7', 'dest': 'chapter-normal-8' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-8', 'dest': 'chapter-normal-9' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-9', 'dest': 'chapter-normal-10' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-10', 'dest': 'chapter-normal-11' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-11', 'dest': 'chapter-normal-12' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-12', 'dest': 'chapter-normal-13' },
        { 'trigger': 'next_chapter', 'source': 'chapter-normal-13', 'dest': 'chapter-normal-14' },
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
        { 'trigger': 'enter_1', 'source': 'chapter-normal-1', 'dest': 'enter-1-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-1', 'dest': 'enter-1-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-1', 'dest': 'enter-1-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-1', 'dest': 'enter-1-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-2', 'dest': 'enter-2-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-2', 'dest': 'enter-2-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-2', 'dest': 'enter-2-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-2', 'dest': 'enter-2-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-3', 'dest': 'enter-3-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-3', 'dest': 'enter-3-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-3', 'dest': 'enter-3-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-3', 'dest': 'enter-3-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-4', 'dest': 'enter-4-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-4', 'dest': 'enter-4-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-4', 'dest': 'enter-4-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-4', 'dest': 'enter-4-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-5', 'dest': 'enter-5-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-5', 'dest': 'enter-5-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-5', 'dest': 'enter-5-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-5', 'dest': 'enter-5-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-6', 'dest': 'enter-6-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-6', 'dest': 'enter-6-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-6', 'dest': 'enter-6-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-6', 'dest': 'enter-6-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-7', 'dest': 'enter-7-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-7', 'dest': 'enter-7-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-7', 'dest': 'enter-7-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-7', 'dest': 'enter-7-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-8', 'dest': 'enter-8-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-8', 'dest': 'enter-8-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-8', 'dest': 'enter-8-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-8', 'dest': 'enter-8-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-9', 'dest': 'enter-9-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-9', 'dest': 'enter-9-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-9', 'dest': 'enter-9-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-9', 'dest': 'enter-9-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-10', 'dest': 'enter-10-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-10', 'dest': 'enter-10-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-10', 'dest': 'enter-10-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-10', 'dest': 'enter-10-4-N' },
        { 'trigger': 'enter_1', 'source': 'chapter-normal-11', 'dest': 'enter-11-1-N' },
        { 'trigger': 'enter_2', 'source': 'chapter-normal-11', 'dest': 'enter-11-2-N' },
        { 'trigger': 'enter_3', 'source': 'chapter-normal-11', 'dest': 'enter-11-3-N' },
        { 'trigger': 'enter_4', 'source': 'chapter-normal-11', 'dest': 'enter-11-4-N' },
        # TODO: triggers for entering chapter 12-14 normal stages
        { 'trigger': 'enter_1', 'source': 'chapter-hard-1', 'dest': 'enter-1-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-1', 'dest': 'enter-1-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-1', 'dest': 'enter-1-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-1', 'dest': 'enter-1-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-2', 'dest': 'enter-2-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-2', 'dest': 'enter-2-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-2', 'dest': 'enter-2-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-2', 'dest': 'enter-2-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-3', 'dest': 'enter-3-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-3', 'dest': 'enter-3-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-3', 'dest': 'enter-3-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-3', 'dest': 'enter-3-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-4', 'dest': 'enter-4-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-4', 'dest': 'enter-4-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-4', 'dest': 'enter-4-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-4', 'dest': 'enter-4-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-5', 'dest': 'enter-5-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-5', 'dest': 'enter-5-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-5', 'dest': 'enter-5-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-5', 'dest': 'enter-5-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-6', 'dest': 'enter-6-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-6', 'dest': 'enter-6-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-6', 'dest': 'enter-6-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-6', 'dest': 'enter-6-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-7', 'dest': 'enter-7-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-7', 'dest': 'enter-7-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-7', 'dest': 'enter-7-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-7', 'dest': 'enter-7-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-8', 'dest': 'enter-8-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-8', 'dest': 'enter-8-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-8', 'dest': 'enter-8-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-8', 'dest': 'enter-8-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-9', 'dest': 'enter-9-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-9', 'dest': 'enter-9-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-9', 'dest': 'enter-9-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-9', 'dest': 'enter-9-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-10', 'dest': 'enter-10-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-10', 'dest': 'enter-10-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-10', 'dest': 'enter-10-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-10', 'dest': 'enter-10-4-H' },
        { 'trigger': 'enter_1', 'source': 'chapter-hard-11', 'dest': 'enter-11-1-H' },
        { 'trigger': 'enter_2', 'source': 'chapter-hard-11', 'dest': 'enter-11-2-H' },
        { 'trigger': 'enter_3', 'source': 'chapter-hard-11', 'dest': 'enter-11-3-H' },
        { 'trigger': 'enter_4', 'source': 'chapter-hard-11', 'dest': 'enter-11-4-H' },

    ]