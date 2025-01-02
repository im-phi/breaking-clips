import subprocess
import re
import glob
import os

sess_list = []

class session:
    def __init__(self, date, input):
        self.date = date
        self.input = input

def get_input():
    sess_date = ''
    input_text = []
    line = input('Input data ending with an empty line: ')
    date_pattern = r'\d\d-\d\d'

    while line:
        match = re.match(date_pattern, line)
        if sess_date == '' and match: 
            sess_date = line
        elif sess_date and match: 
            input_text = "\n".join(input_text)
            sess = session(sess_date, input_text)
            sess_list.append(sess)

            input_text = []
            sess_date = line
        else:
            input_text.append(line)

        line = input()

        if not line: 
            input_text = "\n".join(input_text)
            sess = session(sess_date, input_text)
            sess_list.append(sess)

# input_text = "11-26
# 2 - 151 220 Literal Kick 
# 908 920 Elbow Flare 
# 1915 1945 Angled Thread Lab
# 3 - 1714 1746 2hr Layover > Ringaround > 180 Pulley > Yaks Transfer > Decou Portals
# 4 - 118 141 2hr Layover > Ringaround > 180 Pulley > Yaks Transfer
# 12-02
# 4 - 143 205 2hr Layover > Ringaround > 180 Pulley > Yaks Transfer
# 550 615 2hr Layover > Ringaround > 180 Pulley > Yaks Transfer > Decou Portals
# 5 - 618 640 FW FS -- Shuffle > Kickstall > Stutter Step
# 7 - 707 731 FS Pretzel and Sweep Lab"

# Remove asterisks
# input_text = input_text.replace('*', '')

def create_text(sess_list):
    files_created = 0
    for sess in sess_list:
    # Split the input text into lines
        lines = sess.input.split('\n')

        # Regex pattern to extract video index (if applicable), start time, end time, and clip names
        pattern = r'^(\d+)\s?-\s?(.*)$'
        
        # Clean up input for Instagram
        print(sess.date)
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
        print("\n")

    os.system('pause')

get_input()
create_text(sess_list)