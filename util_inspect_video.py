import sys
import os
import time
import re
import pathlib
import subprocess

# segments.txt formatting
"""
START xx:xx:xx
END xx:xx:xx

START yy:yy:yy
END yy:yy:yy

...

"""

batch_script_path = ''
timestamp_match = re.compile('(\d+:)?(\d{1,2}):(\d{2})')


def remove_empty_lines(line):
    if line is None:
        return False
    line = line.strip()
    if len(line) < 1:
        return False
    return True

def validate_pairs(pair):
    if not pair[0].upper().startswith('START'):
        return False
    if not pair[1].upper().startswith('END'):
        return False
    return True

def group_to_numbers(group):
    if (group[0] is None):
        return int(group[1]) * 60 + int(group[2])
    else:
        return int(group[0].rstrip(':')) * 3600 + int(group[1]) * 60 + int(group[2])

def timestamp_to_seconds(pair):
    start = timestamp_match.search(pair[0]).groups()
    end = timestamp_match.search(pair[1]).groups()
    retStart = group_to_numbers(start)
    endTimingBuffer = 10
    retEnd = group_to_numbers(end) + endTimingBuffer
    return retStart, retEnd

def main(video_file_path):
    vfp = pathlib.Path(video_file_path)
    base_directory_path = vfp.parent
    segments_file_path = vfp.with_name('segments.txt')
    obj = {}
    with segments_file_path.open() as seg_file:
        rawlines = seg_file.readlines()
        lines = filter(remove_empty_lines, rawlines)
        paired = zip(lines, lines)
        validated = filter(validate_pairs, paired)
        seconds = map(timestamp_to_seconds, validated)
        obj['seconds'] = seconds
    
    # find segments.txt file
    # extract time segments
    # create subdirs
    # run batch file with segments
    # wait for the video to finish
    for index, group in enumerate(list(obj['seconds'])):
        print(index)
        print(group)
        target_directory = base_directory_path / str(index)
        target_directory.mkdir()

        subprocess.run(['video.cmd', video_file_path, str(group[0]), str(group[1]), target_directory.as_posix()])
        time.sleep(group[1] - group[0] + 5)

if __name__ == '__main__':
    main(sys.argv[1])