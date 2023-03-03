import os
import json

systemOS = "macos"
username = "rob"
game = "Hogwarts Legacy"

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

def getDirectory(dictionary, systemOS, username, game):
    file_path = ""
    if systemOS == "windows":
        path = dictionary[game].replace("USERNAME", username)
        try:
            directory = os.listdir(path)[0] + "\\"
            file_path += path + directory
        except:
            file_path = "Not found"
    return file_path

def getPrint():
    print("Test")
        
print(getDirectory(saveDictionary, systemOS, username, game))
file.close()