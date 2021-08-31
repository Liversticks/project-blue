from inputKeys import *
import sys

stageMap = {
    '1-4': '1',
    '2-2': '2',
    '2-3': '3',
    '2-4': '4'
}

def repeat_stage_24(fleet, iterations):
    KeyPress('M')
    TwoKeyCombo('LSHIFT', 'R')
    KeyPress('N')
    TwoKeyCombo('LSHIFT', '4')
    KeyPress('G')
    KeyPress('C')
    KeyPress(fleet)
    TwoKeyCombo('LCTRL', 'G')
    time.sleep(5 * 120)
    # Try and finish within 7.5 mins
    remainingIterations = int(iterations) - 1
    for i in range(remainingIterations):
        TwoKeyCombo('LCTRL', 'C')
        time.sleep(7.5 * 60)
    KeyPress('X')
    KeyPress('X')
    KeyPress('X')


def main(fleet, iterations):
    repeat_stage_24(fleet, iterations)
    

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <Fleet number> <Number of times to repeat stage>")