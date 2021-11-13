from inputKeys import KeyPress, TwoKeyCombo
from windowManager import WindowMgr
import time
import datetime
import sys
import re
import mss
import mss.tools

getChapter = re.compile(r'(\d+)-\d+')

# TODO: fine-tuning of time (change to sensible minimums for polling)

# Entries:
# (<KEYMAP_PAIR>, <CLEAR_TIME_SECONDS>)

stageMap = {
    '1-4': (('LSHIFT', '1'), 5 * 60),
    '2-2': (('LSHIFT', '1'), 7.5 * 60),
    '2-3': (('LSHIFT', '2'), 7.5 * 60),
    '2-4': (('LSHIFT', '3'), 7.5 * 60),
    '3-2': (('LSHIFT', '4'), 7.5 * 60),
    '3-4': (('LSHIFT', '5'), 7.5 * 60),
    '4-2': (('LSHIFT', '5'), 7.5 * 60),
    '6-3': (('LSHIFT', '6'), 7.5 * 60),
    '6-4': (('LSHIFT', '7'), 9 * 60),
    '7-3': (('LSHIFT', '8'), 10 * 60),
    '7-4': (('LSHIFT', '9'), 9 * 60),
    '8-1': (('LSHIFT', '1'), 10 * 60),
    '8-2': (('LSHIFT', 'Y'), 10 * 60),
    '8-3': (('LSHIFT', '3'), 10 * 60),
    '8-4': (('LSHIFT', '9'), 10 * 60),
    '9-3': (('LSHIFT', 'W'), 10 * 60),
    '10-1': (('LSHIFT', 'Q'), 10 * 60),
    '10-2': (('LSHIFT', '5'), 10 * 60),
    '10-3': (('LSHIFT', 'T'), 10 * 60),
    '10-4': (('LSHIFT', 'W'), 10 * 60),
    '11-1': (('LSHIFT', '6'), 10 * 60),
    '11-2': (('LSHIFT', 'E'), 10 * 60),
    '11-3': (('LSHIFT', '1'), 10 * 60),
    '11-4': (('LSHIFT', '9'), 10 * 60),
    'A1': (('LSHIFT', 'Q'), 5.5 * 60),
    'A2': (('LSHIFT', 'E'), 6.5 * 60),
    'A3': (('LSHIFT', 'W'), 6.5 * 60),
    'B1': (('LSHIFT', 'Y'), 6.5 * 60),
    'B2': (('LSHIFT', 'T'), 7.5 * 60),
    'B3': (('LSHIFT', 'W'), 8 * 60),
    'C1': (('LSHIFT', 'Q'), 8 * 60),
    'C2': (('LSHIFT', 'E'), 8 * 60),
    'C3': (('LSHIFT', 'W'), 10 * 60),
    'D1': (('LSHIFT', 'Q'), 10 * 60),
    'D2': (('LSHIFT', '5'), 12 * 60),
    'D3': (('LSHIFT', 'W'), 12 * 60),
    'SP1': (('LSHIFT', '5'), 6 * 60),
    'SP2': (('LSHIFT', 'U'), 6 * 60),
    'SP3': (('LSHIFT', 'I'), 8 * 60)
}

eventPrefix = ['A', 'B', 'C', 'D']
eventSPPrefix = 'SP'
eventString = 'event'
eventHardString = 'event-hard'

# Need to adjust timing above!
eventNormalModeStages = [
    'A1',
    'A2',
    'A3',
    'B1',
    'B2',
    'B3'
]

eventHardModeStages = [
    'C1', 
    'C2', 
    'C3',
    'D1',
    'D2',
    'D3'
]

def enterCampaignMode():
    # Time it takes to change to the correct window - can remove in future
    time.sleep(3)
    KeyPress('M')
    time.sleep(1)
    TwoKeyCombo('LSHIFT', 'R')
    time.sleep(3)

def goToChapter(chapter):
    for i in range(chapter-1):
        KeyPress('N')

def enterFleetSelection():
    KeyPress('G')

def clearSecondSurfaceFleet():
    KeyPress('2')

def selectFirstSurfaceFleet(fleet):
    KeyPress('C')
    KeyPress(fleet)
    
def selectSecondSurfaceFleet(fleet):
    KeyPress('3')
    newKey = int(fleet) + 3
    KeyPress(str(newKey))

def assignFleetRoles():
    # First fleet is mob fleet
    # Second fleet is boss fleet
    KeyPress('O')

date_to_file_format = '%d-%m-%Y %H_%M_%S'
screenshot_directory = './screenshots/'

def repeatStage(window, sct, iterations, timebox):
    for i in range(iterations):
        time.sleep(timebox)
        now = datetime.datetime.now()
        date_string = now.strftime(date_to_file_format)
        filename = screenshot_directory + date_string + '.png'
        coordinates = window.get_window_coordinates()
        image = sct.grab(coordinates)
        mss.tools.to_png(image.rgb, image.size, output=filename)
        if i != iterations - 1:
            TwoKeyCombo('LCTRL', 'C')

def returnToMainMenu():
    for _ in range(2):
        TwoKeyCombo('LCTRL', 'H')
        time.sleep(1)

def repeat_stage(window, sct, fleet, iterations, boss=None, normal=True, stage="1-4"):
    stageMetadata = stageMap[stage]
    if stage in eventHardModeStages:
        normal = False
    if stage[0] in eventPrefix:
        goToEvent(normal)
        goToEventChapter(stage[0])
    elif stage[0:2] == eventSPPrefix:
        goToEvent(normal, sp=True)
    else:
        enterCampaignMode()
        chapter = int(getChapter.match(stage).group(1))
        goToChapter(chapter)
    # Currently, only support two-key to enter stage
    TwoKeyCombo(stageMetadata[0][0], stageMetadata[0][1])
    enterFleetSelection()
    if normal:
        if stage != '1-4':
            clearSecondSurfaceFleet()
        selectFirstSurfaceFleet(fleet)
        if boss is not None:
            selectSecondSurfaceFleet(boss)
            assignFleetRoles()
    else:
        # In case something broke when tinkering with Hard Mode fleet composition
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = stageMetadata[1]
    repeatStage(window, sct, int(iterations), timebox)
    returnToMainMenu()

def goToEvent(normal=False, sp=False):
    KeyPress('V')
    time.sleep(1)
    if not sp:
        KeyPress('E')
        KeyPress('E')
        if normal:
            time.sleep(1)
            KeyPress('I')    

def goToEventChapter(prefix):
    KeyPress('P')
    if prefix == 'B' or prefix == 'D':
        KeyPress('N')

def switchToApplication():
    wm = WindowMgr()
    wm.find_window_wildcard("BlueStacks")
    wm.set_foreground()
    return wm

def printSupportedStages():
    print("Supported stages:")
    for stage in stageMap.keys():
        print(stage)

def endRoutine(quick_retire=True):
    # Quick Retire
    # Remember to lock your ships!
    if quick_retire:
        KeyPress('R')
        time.sleep(25)
    # Collect oil and coins
    KeyPress('H')
    time.sleep(10)

def combined(stage, mob_fleet, iterations, boss_fleet=None):
    if int(iterations) < 1:
        print("Must provide a positive number for the number of iterations")
        return
    
    window = switchToApplication()
    with mss.mss() as sct:
        if stage.startswith(eventString):
            if stage == eventHardString:
                clearHardEventStages(window, sct, mob_fleet, iterations=iterations, boss_fleet=boss_fleet)
            else:    
                clearNormalEventStages(window, sct, mob_fleet, iterations=iterations, boss_fleet=boss_fleet)
            endRoutine()
        else:    
            stagesToClear = stage.split()
            for item in stagesToClear:
                if item not in stageMap.keys():
                    printSupportedStages()
                else:
                    repeat_stage(window, sct, mob_fleet, iterations, stage=item, normal=True, boss=boss_fleet)
                    endRoutine()

def clearNormalEventStages(window, sct, mob_fleet, iterations=1, boss_fleet=None):
    for stage in eventNormalModeStages:
        repeat_stage(window, sct, mob_fleet, iterations, boss=boss_fleet, normal=True, stage=stage)

def clearHardEventStages(window, sct, mob_fleet, iterations=1, boss_fleet=None):
    for stage in eventHardModeStages:
        repeat_stage(window, sct, mob_fleet, iterations, boss=boss_fleet, normal=False, stage=stage)

def catLodgeTasks():
    switchToApplication()
    # Do everything
    KeyPress('F')
    time.sleep(60)

# TODO: revise for calling
"""
def discord_entry(stage, mob_fleet, iterations, boss_fleet=None):
    if stage not in supportedStages:
        return supportedStages
    else:
        switchToApplication()
        repeat_stage(mob_fleet, iterations, stage=stage, boss=boss_fleet)
        endRoutine()
"""

if __name__ == '__main__':    
    
    # TODO: documenting "event" (callable only on its own)
    if len(sys.argv) >= 5:
        try:
            combined(sys.argv[1], sys.argv[2], sys.argv[4], boss_fleet=sys.argv[3])                
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage or whitespace-separated list of stages> <Mobbing fleet number> <Boss fleet number> <Number of times to repeat stage>")
    elif len(sys.argv) >= 4:
        try:
            combined(sys.argv[1], sys.argv[2], sys.argv[3])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage or whitespace-separated list of stages> <Mob/boss fleet number> <Number of times to repeat stage>")
    else:
        try:
            if (sys.argv[1] == 'cat'):
                catLodgeTasks()
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Command>")
            print("Currently supported commands:")
            print("cat")
    