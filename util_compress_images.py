import subprocess
import pathlib
import sys
import os
import time

def compress_directory(in_directory, out_directory):
    with os.scandir(in_directory) as it:
        counter = 0
        for image in it:
            output_path = pathlib.Path(out_directory) / image.name
            #print(output_path)
            #print(image.path)
            #print(f'-o "{output_path}"')
            if counter > 500:
                time.sleep(10)
                counter = 0
            subprocess.run(['pngquant_wrapper.cmd', f'{output_path}', f'{image.path}'])
            counter += 1
            #time.sleep(1)
            # os.remove(image.path)

def remove_files(keep_directory, remove_directory):
    files =  os.listdir(keep_directory)
    for file in files:
        try:
            target = pathlib.Path(remove_directory) / file
            os.remove(target)
        except FileNotFoundError:
            pass

def main(in_directory, out_directory):
    compress_directory(in_directory, out_directory)
    time.sleep(30)
    remove_files(out_directory, in_directory)

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <input image directory> <output image directory>")