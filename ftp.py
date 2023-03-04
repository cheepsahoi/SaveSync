import ftplib
import os

ftp_address = ""
ftp_port = 0

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

    # Change directory to game's remote directory
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
    # Delete extra files in local that's not in remote
    for file in os.listdir():
        try:
            ftp.nlst().index(file)
        except ValueError:
            print(file + " not in remote. Deleting from local")
            os.remove(file)
        except:
            print("Something went wrong. Exiting.")
            exit()

    # Close FTP connection
    print("Closing FTP connection")
    ftp.quit()

def uploadFiles(game, saves_path):
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

    # Change directory to game's remote directory
    print("Opening FTP game directory")
    try:
        ftp.cwd(game)
    except:
        print("Directory do not exist. Create folder in remote location first")
        exit()
    # For each file in local directory, upload it
    print("Upload files from local directory for " + game)
    for file in os.listdir():
        try:
            ftp.storbinary("STOR " + file, open(file, "rb"))
            print(file + " uploaded")
        except:
            print("Failed to upload " + file)
    print("Complete upload")
    # Delete extra save files in remote folder that's not in sync with local
    for file in ftp.nlst():
        try:
            print("Checking if " + file + " also exist in local")
            os.listdir().index(file)
        except ValueError:
            print(file + " not in local. Deleting")
            ftp.delete(file)
        except:
            print("Something went wrong. Exiting.")
            exit()
    # Close FTP connection
    print("Closing FTP connection")
    ftp.quit()