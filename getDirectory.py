import os

systemOS = "windows"
username = "rob"
game = "Spider-Man"
testDictionary = {"Hogwarts Legacy": "C:\\Users\\USERNAME\\AppData\\Local\\Phoenix\\Saved\\SaveGames\\",
                  "Spider-Man": "/Users/USERNAME/Downloads/http_download/"}

def getDirectory(systemOS, username, game):
    file_path = ""
    if systemOS == "windows":
        pass
        
print(testDictionary[game].replace("USERNAME", username))
os.listdir()
#getDirectory(systemOS, username)