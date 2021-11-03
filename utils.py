import shutil
import os
import sys
import subprocess

controls_file_name = 'controls.json'

def copyControlsFile(file_path):
    cwd = os.getcwd()
    dest = os.path.join(cwd, controls_file_name)
    shutil.copy(file_path, dest)

def startExecutable(file_path, args):
    in_args = []
    in_args.append(file_path)
    in_args.extend(args)

    subprocess.run(in_args)

def main(task):
    with open('./secrets.txt') as s:
        # Current format:
        # Line 1: path to Bluestacks controls file
        # Line 2: path to Bluestacks executable
        # Lines 3-n: arguments needed for Bluestacks
        lines = s.readlines()

        config_file_path = lines[0]
        executable_path = lines[1]
        executable_args = lines[2:]
        
        if task == 'controls':
            copyControlsFile(config_file_path)
        elif task == 'start':
            startExecutable(executable_path, executable_args)
        else:
            print("Unsupported task.")

if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        print("Usage:")
        print(f"{sys.argv[0]} controls (copies control file to repo)")
        print(f"{sys.argv[0]} start (starts BlueStacks)")