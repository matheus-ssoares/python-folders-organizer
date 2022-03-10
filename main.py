from pathlib import Path
import shutil
import os

downloads_path = str(Path.home() / "Downloads")

path = downloads_path + '/'


def listFiles(files):
    filesList = []
    for file in files:
        if os.path.isfile(os.path.join(path, file)) == True:
            filesList.append(file)
    return filesList


class format:
    def __init__(self, name, roll):
        self.name = name
        self.extension = roll


formats = [
    format('images', '.png'),
    format('images', '.jpeg'),
    format('videos', '.mp4'),
    format('images', '.svg'),
    format('files', '.pdf'),
    format('apps', '.exe'),
    format('text', '.txt'),
    format('text', '.docx')
]

generalFolder = listFiles(os.listdir(path))

for obj in formats:

    for file in listFiles(os.listdir(path)):
        fileFormat = os.path.splitext(file)[1]

        if obj.extension == fileFormat:
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
