import sys
import time
from preprocessing import compress_directory, remove_files


def main(in_directory, out_directory):
    compress_directory(in_directory, out_directory)
    time.sleep(30)
    remove_files(out_directory, in_directory)

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <pre-compressed image directory> <post=compressed image directory>")