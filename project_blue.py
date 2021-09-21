from inputKeys import KeyPress, TwoKeyCombo
from windowManager import WindowMgr
import time
import sys
import re

getChapter = re.compile(r'(\d+)-\d+')

# TODO: fine-tuning of time
# Chapter 2 maps require 3 battles to make the boss appear
# A fourth escort fleet can spawn before the boss though

stageMap = {
    '1-4': (('LSHIFT', '1'), 5 * 60),
    '2-2': (('LSHIFT', '1'), 7.5 * 60),
    '2-3': (('LSHIFT', '2'), 7.5 * 60),
    '2-4': (('LSHIFT', '3'), 7.5 * 60),
    '3-2': (('LSHIFT', '4'), 7.5 * 60),
    '3-4': (('LSHIFT', '5'), 7.5 * 60),
    '4-2': (('LSHIFT', '5'), 7.5 * 60),
    '6-3': (('LSHIFT', '6'), 7.5 * 60),
    'A1': (('LSHIFT', 'Q'), 5.5 * 60),
    'A2': (('LSHIFT', 'E'), 6 * 60),
    'A3': (('LSHIFT', 'W'), 6 * 60),
    'B1': (('LSHIFT', 'Y'), 6.5 * 60),
    'B2': (('LSHIFT', 'T'), 6.5 * 60),
    'B3': (('LSHIFT', 'W'), 7.5 * 60),
    'C1': (('LSHIFT', 'Q'), 7.5 * 60)
}

# Normal mode only!
eventPrefix = ['A', 'B']

# Need to adjust timing above!
eventNormalModeStages = [
    'A1',
    'A2',
    'A3',
    'B1',
    'B2',
    'B3'
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

def repeatStage(iterations, timebox):
    for i in range(iterations):
        TwoKeyCombo('LCTRL', 'C')
        time.sleep(timebox)

def returnToMainMenu():
    for _ in range(2):
        TwoKeyCombo('LCTRL', 'H')
        time.sleep(1)

def repeat_stage(fleet, iterations, boss=None, stage="1-4"):
    stageMetadata = stageMap[stage]
    if stage[0] in eventPrefix:
        goToEvent()
        goToEventChapter(stage[0])
    else:
        enterCampaignMode()
        chapter = int(getChapter.match(stage).group(1))
        goToChapter(chapter)
    # Currently, only support two-key to enter stage
    TwoKeyCombo(stageMetadata[0][0], stageMetadata[0][1])
    enterFleetSelection()
    if stage != '1-4':
        clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = stageMetadata[1]
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    # TODO: check status of stage attempt and emit somewhere

    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def goToEvent():
    KeyPress('E')

def goToEventChapter(prefix):
    KeyPress('P')
    if prefix == 'B':
        KeyPress('N')

def repeat_event_hard_stage(iterations, stage="C1"):
    goToEvent()
    time.sleep(2)
    KeyPress('P')
    if stage[0] == 'D':
        KeyPress('N')
    stageMetadata = stageMap[stage]
    TwoKeyCombo(stageMetadata[0][0], stageMetadata[0][1])
    KeyPress('G')
    time.sleep(1)
    TwoKeyCombo('LCTRL', 'G')
    timebox = stageMetadata[1]
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    # TODO: check status of stage attempt and emit somewhere
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def switchToApplication():
    wm = WindowMgr()
    wm.find_window_wildcard("BlueStacks")
    wm.set_foreground()

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

def combined(stage, mob_fleet, iterations, boss_fleet=None):
    if stage not in stageMap.keys():
        printSupportedStages()
    elif int(iterations) < 1:
        print("Must provide a positive number for the number of iterations")
    else:
        switchToApplication()
        repeat_stage(mob_fleet, iterations, stage=stage, boss=boss_fleet)
        endRoutine()

def clearNormalEventStages(mob_fleet, iterations=1, boss_fleet=None):
    if int(iterations) < 1:
        print("Must provide a positive number for the number of iterations")
    else:
        switchToApplication()
        for stage in eventNormalModeStages:
            repeat_stage(mob_fleet, iterations, boss=boss_fleet, stage=stage)
        endRoutine()

def specialHardMode(stage, iterations):
    if stage not in stageMap.keys():
        printSupportedStages()
    elif int(iterations) < 1:
        print("Must provide a positive number for the number of iterations")
    else:
        switchToApplication()
        repeat_event_hard_stage(iterations, stage=stage)
        endRoutine(quick_retire=False)


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
    if len(sys.argv) >= 5:
        try:
            if (sys.argv[1] == 'event'):
                clearNormalEventStages(sys.argv[2], sys.argv[4], boss_fleet=sys.argv[3])
            else:
                combined(sys.argv[1], sys.argv[2], sys.argv[4], boss_fleet=sys.argv[3])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Mobbing fleet number> <Boss fleet number> <Number of times to repeat stage>")
    elif len(sys.argv) >= 4:
        try:
            combined(sys.argv[1], sys.argv[2], sys.argv[3])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Mob/boss fleet number> <Number of times to repeat stage>")
    elif len(sys.argv) >= 3:
        try:
            specialHardMode(sys.argv[1], sys.argv[2])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Number of times to repeat stage>")
    