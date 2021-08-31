from inputKeys import KeyPress, TwoKeyCombo
import time, sys

stageMap = {
    '1-4': '1',
    '2-2': '2',
    '2-3': '3',
    '2-4': '4'
}

def enterCampaignMode():
    # Time it takes to change to the correct window - can remove in future
    time.sleep(10)
    KeyPress('M')
    time.sleep(1)
    TwoKeyCombo('LSHIFT', 'R')
    time.sleep(3)

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
    KeyPress('N')
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
    KeyPress('N')
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
    KeyPress('N')
    TwoKeyCombo('LSHIFT', '3')
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
    '2-4'
]

def printSupportedStages():
    print("Supported stages:")
    for stage in supportedStages:
        print(stage)

def main(stage, fleet, iterations):
    if stage not in supportedStages:
        printSupportedStages()
    else:
        # Get control of the right window
        if stage == '1-4':
            repeat_stage_14(fleet, iterations)
        elif stage == '2-2':
            repeat_stage_22(fleet, iterations)
        elif stage == '2-3':
            repeat_stage_23(fleet, iterations)
        elif stage == '2-4':
            repeat_stage_24(fleet, iterations)
    
if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <Stage> <Fleet number> <Number of times to repeat stage>")