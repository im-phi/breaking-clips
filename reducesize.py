import subprocess
import re
import glob
import os

# Directory path containing input video files
input_directory = input('Input directory containing video files: ')
newpath = input_directory + r'\clips'
if not os.path.exists(newpath):
    os.makedirs(newpath)

input_files = sorted(glob.glob(f"{input_directory}/*.mp4"), key=os.path.basename)

pattern = r'\\([^\\]+\.mp4)$'

# Iterate over the lines
for path in input_files:
    file = re.search(pattern, path).group(1)
    output_file = f'{input_directory}\clips\{file}'

    # Construct and run the FFmpeg command to clip the video
    command = f'ffmpeg -i {path} -c copy -vcodec libx265 -crf 16 {output_file}'
    subprocess.call(command, shell=True)

print("\n\n")