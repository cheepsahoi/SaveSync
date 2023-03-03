import os

systemOS = "windows"
username = "rob"
game = "Test Game"
testDictionary = {"Hogwarts Legacy": "C:\\Users\\USERNAME\\AppData\\Local\\Phoenix\\Saved\\SaveGames\\",
                  "Spider-Man": "/Users/USERNAME/Downloads/http_download",
                  "Test Game": "/Users/USERNAME/Nextcloud/Repos/SaveSync/temp"}

def getDirectory(systemOS, username, game):
    file_path = ""
    if systemOS == "windows":
        path = testDictionary[game].replace("USERNAME", username)
        try:
            directory = os.listdir(path)[0] + "/"
            file_path += path + "/" + directory
            print(file_path)
        except:
            print("Not found")
        
#print(testDictionary[game].replace("USERNAME", username))
#os.listdir(testDictionary[game].replace("USERNAME", username))
getDirectory(systemOS, username, game)