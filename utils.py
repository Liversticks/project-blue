import shutil
import os
import sys
import subprocess

controls_file_name = 'controls.json'

def copyControlsFile(file_path):
    cwd = os.getcwd()
    dest = os.path.join(cwd, controls_file_name)
    shutil.copy(file_path, dest)

def startExecutable(file_path):
    cwd = os.getcwd()
    fp = os.path.join(cwd, file_path)
    in_args = []
    in_args.append(fp)
    # print(in_args)
    subprocess.run(in_args)

def trim_newlines(line):
    if line[-1] == '\n':
        return line[:-1]
    return line

def get_exec_args(raw_lines):
    ret = []
    for item in raw_lines:
        ret.append(trim_newlines(item))
    return ret

def main(task):
    with open('./secrets.txt') as s:
        # Current format:
        # Line 1: path to Bluestacks controls file
        # Line 2: start script
        # Note: no quotations around file paths please
        lines = s.readlines()

        config_file_path = trim_newlines(lines[0])
        start_file_path = trim_newlines(lines[1])

        if task == 'controls':
            copyControlsFile(config_file_path)
        elif task == 'start':
            startExecutable(start_file_path)
        else:
            print("Unsupported task.")

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print("Usage:")
        print(f"{sys.argv[0]} controls (copies control file to repo)")
        print(f"{sys.argv[0]} start (starts BlueStacks)")