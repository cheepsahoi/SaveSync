import os
import json

def getDirectory(systemOS, username, game):
    if systemOS == "windows":
        with open(os.getcwd() + "\\save_locs\\windows") as file:
            tempDictionary = file.read()
    elif systemOS == "linux":
        with open(os.getcwd() + "/save_locs/linux") as file:
            tempDictionary = file.read()
    elif systemOS == "macos":
        with open(os.getcwd() + "/save_locs/windows") as file:
            tempDictionary = file.read()
    saveDictionary = json.loads(tempDictionary)
    directory = findFilePath(systemOS, username, game, saveDictionary)
    return directory

def findFilePath(systemOS, username, game, saveDictionary):
    file_path = ""
    if systemOS == "windows":
        path = saveDictionary[game].replace("USERNAME", username)
        try:
            directory = os.listdir(path)[0] + "\\"
            file_path += path + directory
        except:
            file_path = "Not found"
    elif systemOS == "macos":
        path = saveDictionary[game].replace("USERNAME", username)
        try:
            directory = os.listdir(path)[0] + "/"
            file_path += path + directory
        except:
            print("Game: " + game)
            file_path = "Not found"

    return file_path

print(getDirectory("macos", "rob", "Test Game"))