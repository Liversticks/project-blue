import mss
import mss.tools
from infra.windowManager import WindowMgr
import datetime

def main():
    with mss.mss() as sct:
        wm = WindowMgr()
        wm.find_window_wildcard("BlueStacks")
        wm.set_foreground()

        date_to_file_format = '%d-%m-%Y %H_%M_%S'
        screenshot_directory = './screenshots/'

        now = datetime.datetime.now()
        date_string = now.strftime(date_to_file_format)
        filename = screenshot_directory + date_string + '.png'
        coordinates = wm.get_window_coordinates()
        image = sct.grab(coordinates)
        mss.tools.to_png(image.rgb, image.size, output=filename)


if __name__ == '__main__':
    main()