from inputKeys import KeyPress, TwoKeyCombo
from windowManager import WindowMgr
import time
import sys
import re

getChapter = re.compile(r'(\d+)-\d+')

# TODO: fine-tuning of time
# Chapter 2 maps require 3 battles to make the boss appear
# A fourth escort fleet can spawn before the boss though
# Try and finish within 7.5 mins
stageMap = {
    '1-4': (('LSHIFT', '1'), 5 * 60),
    '2-2': (('LSHIFT', '1'), 7.5 * 60),
    '2-3': (('LSHIFT', '2'), 7.5 * 60),
    '2-4': (('LSHIFT', '3'), 7.5 * 60),
    '3-2': (('LSHIFT', '4'), 7.5 * 60),
    '3-4': (('LSHIFT', '5'), 7.5 * 60),
    '4-2': (('LSHIFT', '5'), 7.5 * 60),
    '6-3': (('LSHIFT', '6'), 7.5 * 60)
}

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
    KeyPress('X')
    KeyPress('X')
    KeyPress('X')

def repeat_stage(fleet, iterations, boss=None, stage="1-4"):
    enterCampaignMode()
    stageMetadata = stageMap[stage]
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

"""
supportedStages = [
    '1-4',
    '2-2',
    '2-3',
    '2-4',
    '3-2',
    '3-4',
    '4-2',
    '6-3'
]
"""

def switchToApplication():
    wm = WindowMgr()
    wm.find_window_wildcard("BlueStacks")
    wm.set_foreground()

def printSupportedStages():
    print("Supported stages:")
    for stage in stageMap.keys():
        print(stage)

def endRoutine():
    # Quick Retire
    # Remember to lock your ships!
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
    if len(sys.argv) >= 4:
        try:
            combined(sys.argv[1], sys.argv[2], sys.argv[4], boss_fleet=sys.argv[3])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Mobbing fleet number> <Boss fleet number> <Number of times to repeat stage>")
    elif len(sys.argv) == 4:
        try:
            combined(sys.argv[1], sys.argv[2], sys.argv[3])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Mob/boss fleet number> <Number of times to repeat stage>")
    