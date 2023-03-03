import os
import json

with open(os.getcwd() + "/save_locs/windows") as file:
    tempDictionary = file.read()

saveDictionary = json.loads(tempDictionary)

systemOS = "windows"
username = "rob"
game = "Hogwarts Legacy"

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
        
print(getDirectory(saveDictionary, systemOS, username, game))