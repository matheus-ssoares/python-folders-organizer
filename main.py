from pathlib import Path
import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

downloads_path = str(Path.home() / "Downloads")

path = downloads_path + '/'

class format:
    def __init__(self, name, roll):
        self.name = name
        self.extension = roll
        
formats = [
    format('Pictures', '.png'),
    format('Pictures', '.jpeg'),
    format('Pictures', '.jpg'),
    format('Videos', '.mp4'),
    format('Pictures', '.svg'),
    format('Files', '.pdf'),
    format('Apps', '.exe'),
    format('Text', '.txt'),
    format('Text', '.docx')
]        

def list_files(files):
    filesList = []
    for file in files:
        if os.path.isfile(os.path.join(path, file)) == True:
            filesList.append(file)
    return filesList

def organize_files():
    generalFolder = list_files(os.listdir(path))

    for obj in formats:
    
        for file in list_files(os.listdir(path)):
            fileFormat = os.path.splitext(file)[1]
    
            if obj.extension == fileFormat.lower():
                pathToFile = path + obj.name + '/'
    
                oldPath = path + file
                destination = pathToFile + file
                if os.path.isdir(pathToFile) == False:
                    os.mkdir(pathToFile)
                    shutil.move(oldPath, destination)
                    generalFolder.remove(file)
                else:
                   
                    shutil.move(oldPath, destination)
                    generalFolder.remove(file)
            elif fileFormat == '.tmp':
                 
                try:
                    generalFolder.remove(file)
                except Exception:
                    pass
                continue
    
    if len(generalFolder) > 0:
        for file in generalFolder:
            otherFilesPath = path + 'others/'
            oldPath = path + file
            destination = otherFilesPath + file
            if os.path.isdir(otherFilesPath) == False:
                os.mkdir(otherFilesPath)
                shutil.move(oldPath, destination)
            else:
                shutil.move(oldPath, destination)

def on_created(event):
   organize_files()

def on_modified(event):
   organize_files()
   
organize_files()   

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(
        patterns,
        ignore_patterns,
        ignore_directories,
        case_sensitive
    )

    my_event_handler.on_created = on_created
    my_event_handler.on_modified = on_modified

    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
