import subprocess
import re
import glob
import os

# Global Variables
sess_list = []
root_directory = r'H:\yi''\\'
year = "24-"

class session:
    def __init__(self, date, input):
        self.date = year + date
        self.input = input

def convert_time(input_time):
    l = (len(input_time))
    seconds = int(input_time[(l-2):])

    if l < 4: minutes = int(input_time[0])
    else: minutes = int(input_time[:2])

    hours = 0

    time_format = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    return time_format

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

def process_input(sess_list):
    for sess in sess_list:
        newpath = root_directory + sess.date + r'\clips'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        # Get input from sess object
        input_text = sess.input

        # Split the input text into lines
        lines = input_text.split('\n')

        # Regex pattern to extract video index (if applicable), start time, end time, and clip names
        pattern = r'^(\d+)\s?-\s?(.*)$'
        
        # Get a list of input video files in the directory, sorted by name
        input_files = sorted(glob.glob(f"{root_directory + sess.date}/*.mp4"), key=os.path.basename)


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
                output_file = f'{root_directory + sess.date}\\clips\\{files_created}-{clip_name}.mp4'

                # Construct and run the FFmpeg command to clip the video
                command = f'ffmpeg -i {input_files[video_index]} -ss {start_time} -to {end_time} -c copy -vcodec libx265 -crf 16 {output_file}'
                subprocess.call(command, shell=True)

        print("\nDONE\n")

get_input()
process_input(sess_list)

# def text_cleanup():
# # Clean up input for Instagram
#     files_created = 0
#     for line in lines:
#         # Extract clip information using regex
#         match = re.match(pattern, line)

#         # If line contains video index
#         if match:
#             clip_info = match.group(2)
#         # If line doesn't contain video index
#         else:
#             clip_info = line    

#         if clip_info:
#             # Extract clip name
#             clip_parts = clip_info.split(' ')
#             clip_name = ' '.join(clip_parts[2:])
            
#             files_created += 1
#             clip_name = str(files_created) + " - " + clip_name
#             print(clip_name)