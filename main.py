from inputKeys import KeyPress, TwoKeyCombo
from windowManager import WindowMgr
import time
import sys

stageMap = {
    '1-4': '1',
    '2-2': '2',
    '2-3': '3',
    '2-4': '4'
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
    TwoKeyCombo('LCTRL', 'G')

def repeatStage(iterations, timebox):
    for i in range(iterations):
        TwoKeyCombo('LCTRL', 'C')
        time.sleep(timebox)

def returnToMainMenu():
    KeyPress('X')
    KeyPress('X')
    KeyPress('X')

def repeat_stage_14(fleet, iterations):
    enterCampaignMode()
    TwoKeyCombo('LSHIFT', '1')
    enterFleetSelection()
    selectFirstSurfaceFleet(fleet)
    timebox = 5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

# Chapter 2 maps require 3 battles to make the boss appear
# A fourth escort fleet can spawn before the boss though
# Try and finish within 7.5 mins

def repeat_stage_22(fleet, iterations):
    enterCampaignMode()
    goToChapter(2)
    TwoKeyCombo('LSHIFT', '1')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def repeat_stage_23(fleet, iterations):
    enterCampaignMode()
    goToChapter(2)
    TwoKeyCombo('LSHIFT', '2')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()

def repeat_stage_24(fleet, iterations):
    enterCampaignMode()
    goToChapter(2)
    TwoKeyCombo('LSHIFT', '3')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    timebox = 7.5 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()    

# Stage 3-2 can have up to 6 battles as the boss can be blocked
# by up to 2 escort fleets

def repeat_stage_32(fleet, iterations):
    enterCampaignMode()
    goToChapter(3)
    TwoKeyCombo('LSHIFT', '4')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
    timebox = 9 * 60
    time.sleep(timebox)
    remainingIterations = int(iterations) - 1
    repeatStage(remainingIterations, timebox)
    returnToMainMenu()    

def repeat_stage_34(fleet, iterations):
    enterCampaignMode()
    goToChapter(3)
    TwoKeyCombo('LSHIFT', '5')
    enterFleetSelection()
    clearSecondSurfaceFleet()
    selectFirstSurfaceFleet(fleet)
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
    '3-4'
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
    KeyPress('R')
    time.sleep(25)
    # Collect oil and coins
    KeyPress('H')

def main(stage, fleet, iterations):
    if stage not in supportedStages:
        printSupportedStages()
    else:
        switchToApplication()
        if stage == '1-4':
            repeat_stage_14(fleet, iterations)
        elif stage == '2-2':
            repeat_stage_22(fleet, iterations)
        elif stage == '2-3':
            repeat_stage_23(fleet, iterations)
        elif stage == '2-4':
            repeat_stage_24(fleet, iterations)
        elif stage == '3-2':
            repeat_stage_32(fleet, iterations)
        elif stage == '3-4':
            repeat_stage_34(fleet, iterations)
        endRoutine()
    
if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <Stage> <Fleet number> <Number of times to repeat stage>")