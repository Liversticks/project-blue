import subprocess
import pathlib
import os
import time
import numpy as np
from skimage import transform, io, util

def compress_directory(in_directory, out_directory):
    with os.scandir(in_directory) as it:
        counter = 0
        for image in it:
            output_path = pathlib.Path(out_directory) / image.name
            # Maximum number of "simultaneous" pngquant instances
            if counter > 500:
                time.sleep(10)
                counter = 0
            subprocess.run(['pngquant_wrapper.cmd', f'{output_path}', f'{image.path}'])
            counter += 1

def remove_files(keep_directory, remove_directory):
    files =  os.listdir(keep_directory)
    for file in files:
        try:
            target = pathlib.Path(remove_directory) / file
            os.remove(target)
        except FileNotFoundError:
            pass

# Widescreen is normally 16:9. Using 2:1 makes it easier to split for a CNN
image_size = (128, 256)
def resize_images(from_directory, to_directory):
    folders = os.listdir(from_directory)
    for folder in folders:
        new_folder = pathlib.Path(to_directory) / folder
        new_folder.mkdir(exist_ok=True)
        with os.scandir(pathlib.Path(from_directory) / folder) as it:
            for image in it:
                original_size = io.imread(image.path)
                resized = transform.resize(original_size, image_size, anti_aliasing=True)
                new_path = new_folder / image.name
                io.imsave(new_path.as_posix(), util.img_as_ubyte(resized))