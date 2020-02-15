from datetime import datetime
import os

configurationFlag = False

print('Enter the source directory you want to track:')
folder_to_track = input()
print('Enter the destination file directory to move your files:')
folder_destination = input()
programConfigurationDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
if os.path.isdir(folder_to_track) == False:
    print('Source folder not available')
else:
    print('Configuration Success')
    configurationFlag = True

