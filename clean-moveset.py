import subprocess
import re
import glob
import os

input_text = [] 
line = input("Input prompt ending with an empty line: ")
while line:
    input_text.append(line)
    line = input() 

input_text = "\n".join(input_text)

# input_text = """5 - ***151 204 Braid
# **515 603 Pedestrian Step > Tippy Taps > Bingo Steps > 7Step > No Hands 6Step
# 6 - ***245 256 No Hands 6Step + Back Rolls
# **653 728 Pedestrian Step > Stompies(?) > Uncrossed Back Shuffle > misc fw
# 7 - 206 227 misc fw > No Hands 6Step > Hand Swipes
# 8 - 230 313 Floor Palms > Telewide"""

# Remove asterisks
# input_text = input_text.replace('*', '')

# Split the input text into lines
lines = input_text.split('\n')

# Regex pattern to extract video index (if applicable), start time, end time, and clip names
pattern = r'^(\d+)\s?-\s?(.*)$'
 
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

os.system('pause')