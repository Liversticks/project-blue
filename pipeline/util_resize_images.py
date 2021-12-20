import sys
from preprocessing import resize_images


def main(in_directory, out_directory):
    resize_images(in_directory, out_directory)

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} <compressed image directory> <resized image directory>")