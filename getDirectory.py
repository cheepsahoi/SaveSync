import os
import json
import platform

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
    file.close()
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
            print(systemOS)
            print(username)
            print(game)
            print(saveDictionary)
            print("Game: " + game + " directory not found")
            file_path = "Not found"

    return file_path

def gameList(systemOS):
    if systemOS == "windows":
        with open(os.getcwd() + "\\save_locs\\windows") as file:
            tempDictionary = file.read()
    elif systemOS == "linux":
        with open(os.getcwd() + "/save_locs/windows") as file:
            tempDictionary = file.read()
    elif systemOS == "macos" or systemOS == "darwin":
        with open(os.getcwd() + "/save_locs/windows") as file:
            tempDictionary = file.read()
            print(tempDictionary)
    saveDictionary = json.loads(tempDictionary)
    file.close()
    return list(saveDictionary)

#path, list = getDirectory("macos", "rob", "Spider-Man")
#print(path, list)
#print(getDirectory("windows", "rob", "Hogwarts Legacy"))