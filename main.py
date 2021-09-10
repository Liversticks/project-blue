from inputKeys import KeyPress, TwoKeyCombo
from windowManager import WindowMgr
import time
import sys
import re

getChapter = re.compile(r'(\d)+-\d+')

# TODO: fine-tuning of time
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
    chapter = int(getChapter.match(stage).group(0))
    goToChapter(chapter)
    # Currently, only support two-key to enter stage
    TwoKeyCombo(stageMetadata[0][0], stageMetadata[0][1])
    enterFleetSelection()
    if stage is not '1-4':
        clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = stageMetadata[1]
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()


def repeat_stage_14(fleet, iterations):
    enterCampaignMode()
    TwoKeyCombo('LSHIFT', '1')
    enterFleetSelection()
    selectFirstSurfaceFleet(fleet)
    TwoKeyCombo('LCTRL', 'G')
    timebox = 5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

# Chapter 2 maps require 3 battles to make the boss appear
# A fourth escort fleet can spawn before the boss though
# Try and finish within 7.5 mins

def repeat_stage_22(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(2)
    TwoKeyCombo('LSHIFT', '1')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def repeat_stage_23(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(2)
    TwoKeyCombo('LSHIFT', '2')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def repeat_stage_24(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(2)
    TwoKeyCombo('LSHIFT', '3')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()    

# Stage 3-2 can have up to 6 battles as the boss can be blocked
# by up to 2 escort fleets

def repeat_stage_32(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(3)
    TwoKeyCombo('LSHIFT', '4')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()    

def repeat_stage_34(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(3)
    TwoKeyCombo('LSHIFT', '5')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 6 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()    

def repeat_stage_42(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(4)
    TwoKeyCombo('LSHIFT', '5')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def repeat_stage_63(fleet, iterations, boss=None):
    enterCampaignMode()
    goToChapter(6)
    TwoKeyCombo('LSHIFT', '6')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    if boss is not None:
        selectSecondSurfaceFleet(boss)
        assignFleetRoles()
    TwoKeyCombo('LCTRL', 'G')
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

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

def switchToApplication():
    wm = WindowMgr()
    wm.find_window_wildcard("BlueStacks")
    wm.set_foreground()

def printSupportedStages():
    print("Supported stages:")
    for stage in supportedStages:
        print(stage)

def endRoutine():
    # Quick Retire
    # Remember to lock your ships!
    KeyPress('R')
    time.sleep(25)
    
    # Collect oil and coins
    KeyPress('H')

def combined(stage, fleet, iterations):
    if stage not in supportedStages:
        printSupportedStages()
    else:
        switchToApplication()
        repeat_stage(fleet, iterations, stage=stage)
        endRoutine()

def two_fleets(stage, mob_fleet, boss_fleet, iterations):
    if stage not in supportedStages:
        printSupportedStages()
    else:
        switchToApplication()
        repeat_stage(mob_fleet, iterations, boss=boss_fleet, stage=stage)
        endRoutine()
    
if __name__ == '__main__':
    if len(sys.argv) == 5:
        try:
            two_fleets(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Mobbing fleet number> <Boss fleet number> <Number of times to repeat stage>")
    elif len(sys.argv) == 4:
        try:
            combined(sys.argv[1], sys.argv[2], sys.argv[3])
        except IndexError:
            print(f"Usage: {sys.argv[0]} <Stage> <Mob/boss fleet number> <Number of times to repeat stage>")
    