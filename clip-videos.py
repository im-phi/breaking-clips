import subprocess
import re
import glob
import os

def convert_time(input_time):
    minutes = int(input_time[0])
    seconds = int(input_time[1:])

    hours = 0

    time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return time_format

# Directory path containing input video files
input_directory = input('Input directory containing video files: ')
newpath = input_directory + r'\clips'
if not os.path.exists(newpath):
    os.makedirs(newpath)

input_text = [] 
line = input("Input prompt ending with an empty line: ")
while line:
    input_text.append(line)
    line = input() 

input_text = "\n".join(input_text)

# input_text = "5 - 151 204 ***Braid
# 515 603 **Pedestrian Step > Tippy Taps > Bingo Steps > 7Step > No Hands 6Step
# 6 - 245 256 ***No Hands 6Step + Back Rolls
# 653 728 **Pedestrian Step > Stompies(?) > Uncrossed Back Shuffle > misc fw
# 7 - 206 227 misc fw > No Hands 6Step > Hand Swipes
# 8 - 230 313 Floor Palms > Telewide"


# Split the input text into lines
lines = input_text.split('\n')

# Regex pattern to extract video index (if applicable), start time, end time, and clip names
pattern = r'^(\d+)\s?-\s?(.*)$'
 
# Get a list of input video files in the directory, sorted by name
input_files = sorted(glob.glob(f"{input_directory}/*.mp4"), key=os.path.basename)


video_index = -1
files_created = 0
# Iterate over the lines
for line in lines:
    # Extract video index and clip information using regex
    match = re.match(pattern, line)

    # If line contains video index
    if match:
        video_index = int(match.group(1)) - 1
        clip_info = match.group(2)
    else:
        clip_info = line    

    # If there is clip information
    if clip_info:
        # Extract start time, end time, and clip names
        clip_parts = clip_info.split(' ')
        start_time = convert_time(clip_parts[0])
        end_time = convert_time(clip_parts[1])
        clip_name = ' '.join(clip_parts[2:]).replace('*', '')
        
        # Construct the output file name
        clip_name = re.sub(r"[\s\W]+", "-", clip_name)
        files_created += 1
        output_file = f'{input_directory}\clips\{files_created}-{clip_name}.mp4'

        # Construct and run the FFmpeg command to clip the video
        command = f'ffmpeg -i {input_files[video_index]} -ss {start_time} -to {end_time} -c copy -vcodec libx265 -crf 16 {output_file}'
        subprocess.call(command, shell=True)

print("\n\n")

# Clean up input for Instagram
files_created = 0
for line in lines:
    # Extract clip information using regex
    match = re.match(pattern, line)

    # If line contains video index
    if match:
        clip_info = match.group(2)
    # If line doesn't contain video index
    else:
        clip_info = line    

    if clip_info:
        # Extract clip name
        clip_parts = clip_info.split(' ')
        clip_name = ' '.join(clip_parts[2:])
        
        files_created += 1
        clip_name = str(files_created) + " - " + clip_name
        print(clip_name)