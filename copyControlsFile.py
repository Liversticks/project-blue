import shutil
import os

def main():
    with open('./secrets.txt') as s:
        config_file_path = s.readline()
        cwd = os.getcwd()
        dest = os.path.join(cwd, 'controls.json')
        print(dest)
        shutil.copy(config_file_path, dest)

if __name__ == '__main__':
    main()