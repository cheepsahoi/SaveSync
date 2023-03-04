import ftplib
import os

game = "Hogwarts Legacy"
saves_path = os.getcwd() + "/saves"
ftp_address = "46.232.211.40"
ftp_port = 9991

def downloadFiles(game, saves_path):
    # Go to game's save directory
    print("Opening directory: " + saves_path)
    os.chdir(saves_path)

    # Connect to FTP
    print("Establishing FTP connection")
    try:
        ftp = ftplib.FTP(ftp_address)
        ftp.connect(port=ftp_port)
        ftp.login() # Anonymous login
        print("FTP connected")
    except:
        print("FTP failed")
        exit()

    # Change directory to game's directory
    print("Opening FTP game directory")
    try:
        ftp.cwd(game)
        directoryList = ftp.nlst()
    except:
        print("Directory do not exist. Create folder in remote location first")
        exit()

    # For each file in ftp directory, download it
    print("Downloading files from FTP for " + game)
    for file in directoryList:
        try:
            with open(file, "wb") as fp:
                ftp.retrbinary("RETR " + file, fp.write)
                fp.close()
            print(file + " downloaded")
        except:
            print("Failed to download " + file)
    print("Complete download")
    # Close FTP connection
    print("Closing FTP connection")
    ftp.quit()

downloadFiles(game, saves_path)