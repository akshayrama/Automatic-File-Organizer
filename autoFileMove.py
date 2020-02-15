from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json 
import time
import mimetypes

from autoFileMoveConfiguration import configurationFlag, folder_to_track, folder_destination, programConfigurationDate

from datetime import datetime

if configurationFlag == False:
    print('Please complete configuration before running this file')
    exit()

def modification_date(filename):
    t = os.path.getmtime(filename)
    return datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        for filename in os.listdir(folder_to_track):
            fileType = mimetypes.guess_type(filename)[0] 
            if fileType == 'application/pdf':
                src = folder_to_track + "/" + filename
                if modification_date(src) > programConfigurationDate:
                    new_destination = folder_destination + "/" + filename
                    os.rename(src, new_destination)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()     