import glob
import os
import datetime
import shutil

# TODO: ERROR HANDLING, OPTION TO ADD YOUTUBE FUNCTIONALITY

# input_directory = os.path.join("C:\\", "Users", "Phi", "Videos", "test")

input_directory = os.path.join("I:\\", "DCIM", "100MEDIA")

# Get a list of input video files in the directory, sorted by name
input_files = sorted(glob.glob(f"{input_directory}/*.mp4"), key=os.path.basename)

# Get date modified of first file in sorted list and parse with datetime
time_modified = datetime.date.fromtimestamp(os.path.getmtime(input_files[0]))

# Reformat full date with year, short ver, without century
target_directory = os.path.join("H:\\", "yi", time_modified.strftime("%y-%m-%d"))

backup_directory = os.path.join("Z:\\", time_modified.strftime("%y-%m-%d"))

if not os.path.exists(target_directory):
    os.makedirs(target_directory)

# Copy files to target directory
for file in input_files:
    if os.path.isfile(file):
        if os.path.basename(file) not in os.listdir(target_directory): 
            print("Copying " + file + " to " + target_directory)
            shutil.copy(file, target_directory)
        else:
            print(file + " already exists in " + target_directory)

# Copy to backup drive
print("Copying files to backup drive...")
shutil.copytree(target_directory, backup_directory)

# Delete from input directory
answer = input("Delete items from " + input_directory + " ? y/n: ")
if answer.lower() in ["y","yes"]:
    for file in os.listdir(input_directory):
        print("Deleting " + file)
        os.remove(os.path.join(input_directory, file))
    print("Files deleted")
else:
    print("Files not deleted")
      
os.system('pause')