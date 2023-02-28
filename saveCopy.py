import os
def getGame():
    gameList = ["Hogwarts Legacy", "Spider-Man"]
    index = 1
    for game in gameList:
        print(str(index) + ". " + game)
        index += 1
    while True:
        game = input("\nSelect game: ")
        try:
            game = gameList[int(game) - 1]
            break
        except:
            print("Choose from the provided games.")
    print("Game chosen is " + game)

localLocation = input("Game save location: ")
remoteLocation = "site/upload"
saveFile = "test"

# Download the file #urllib.request.urlretrieve(remote, local)
# wget -r -nH -R html,tmp *link*
# curl -X POST http://127.0.0.1:8000/upload -F 'files=@multiple-example-1.txt' -F 'files=@multiple-example-2.txt'
print("Downloading from: " + remoteLocation + "/download/")
print("Saving to: " + saveFile)

getGame()

