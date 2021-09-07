import os
import sys

def main(directory, append):
    for filename in os.listdir(directory):
        newname = append + filename
        full_path_newname = os.path.join(directory, newname)
        full_path_oldname = os.path.join(directory, filename)
        os.rename(full_path_oldname, full_path_newname)

if __name__ == '__main__':
    try:
        main(sys.argv[1], sys.argv[2])
    except IndexError:
        print(f"Usage: {sys.argv[0]} path_to_directory text_to_append")