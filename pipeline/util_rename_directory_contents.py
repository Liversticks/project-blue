import os
import sys

def append(directory, append):
    for filename in os.listdir(directory):
        newname = append + filename
        full_path_newname = os.path.join(directory, newname)
        full_path_oldname = os.path.join(directory, filename)
        os.rename(full_path_oldname, full_path_newname)

def trim(directory, trim):
    for filename in os.listdir(directory):
        newname = filename.removeprefix(trim)
        full_path_newname = os.path.join(directory, newname)
        full_path_oldname = os.path.join(directory, filename)
        os.rename(full_path_oldname, full_path_newname)

if __name__ == '__main__':
    try:
        if (sys.argv[1] == 'append'):
            append(sys.argv[2], sys.argv[3])
        elif (sys.argv[1] == 'trim'):
            trim(sys.argv[2], sys.argv[3])
        else:
            raise IndexError
    except IndexError:
        print(f"Usage: {sys.argv[0]} <append/trim> <path_to_directory> <text_to_append_or_trim>")