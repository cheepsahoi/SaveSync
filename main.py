import tkinter as tk
import urllib.request
import os
import re
from tkinter import filedialog
import platform
import getDirectory, ftp

class DownloadGUI:
    def __init__(self, master, names):
        self.master = master
        master.title("Sync Saves")

        # Create list box for games
        self.list_label = tk.Label(master, text="Games")
        self.list_label.grid(row=0, column=1, pady=5)
        self.listbox = tk.Listbox(master, width=50)
        self.listbox.grid(row=1, column=1, padx=5)
        
        # Bind click event to list box
        self.listbox.bind("<Button-1>", self.select_game)
        
        # Initialize game index to -1
        self.game = -1

        # Create status label
        self.status_label = tk.Label(master, text="")
        self.status_label.grid(row=1, column=0, padx=5, pady=5)

        # Create Save location label
        self.save_label = tk.Label(master, text="Local location:")
        self.save_label.grid(row=2, column=1, pady=5)
        self.save_localDir = tk.Label(master, text="")
        self.save_localDir.grid(row=3, column=1, padx=5, pady=5)
        
        # Create Download button
        self.download_button = tk.Button(master, text="Download Saves", state="disabled", command=self.download_files)
        self.download_button.grid(row=4, column=1, padx=5, pady=5)
        
        # Create Upload button
        self.upload_button = tk.Button(master, text="Upload Saves", state="disabled", command=self.upload_files)
        self.upload_button.grid(row=5, column=1, padx=5, pady=5)
        
        # Create status label
        self.status_label = tk.Label(master, text="")
        self.status_label.grid(row=6, column=1, padx=5, pady=5)

        # Debug label
        self.debug_label = tk.Label(master, text="")
        self.debug_label.grid(row=7, column=1, padx=5, pady=5)

        # Get systemOS
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        if platform.system() == "Windows":
            self.platform = "windows"
        elif platform.system() == "Linux":
            self.platform = "linux"
        elif platform.system() == "Darwin":
            self.platform = "macos"
            self.debug_label.config(text="MacOS not supported. Press enter to exit")
            #self.listbox.delete(0, 'end')
            #input("Press enter to exit")
            #exit()
        else:
            self.platform = "unknown"
            self.debug_label.config(text="Operating system not detected.")
        self.debug_label.config(text=self.current_directory)

        # Add games to list box
        for i, name in enumerate(names):
            self.listbox.insert(i+1, f"{i+1}. {name}")


    def select_game(self, event):
        # Get index of selected item
        index = self.listbox.curselection()
        
        # Store index in game variable
        if len(index) > 0:
            self.game = index[0]
            self.status_label.config(text=f"Selected game: {self.listbox.get(self.game)}")
            # Get save location using getDirectory.py script
            self.saveLocation = getDirectory.getDirectory(self.platform, str(os.getenv("USER") or os.getlogin()), self.listbox.get(self.game)[3:])
            self.game = self.listbox.get(self.game)[3:]
            self.save_localDir.config(text=self.saveLocation)
            if self.saveLocation == "Not found":
                self.save_localDir.config(text="Save directory doesn't exist. Play game and save first.")
                self.download_button.config(state="disabled")
                self.upload_button.config(state="disabled")
            else:
                self.save_localDir.config(text="Save directory found")
                self.download_button.config(state="normal")
                self.upload_button.config(state="normal")
        else:
            self.game = -1
            self.status_label.config(text="No game selected")

    def download_files(self):
        save_location = self.saveLocation
        self.status_label.config(text="Downloading saves from remote folder")
        
        # Download files using ftp.py script
        ftp.downloadFiles(self.game, save_location)
        print("Download finished")
        self.status_label.config(text="All files downloaded")

        # # Make request to URL
        # try:
        #     response = urllib.request.urlopen(self.url)
        #     html = response.read().decode('utf-8')
        # except:
        #     self.status_label.config(text="Error connecting to server")
        #     return
        
        # # Find all links on the page
        # links = re.findall(r'href=[\'"]?([^\'" >]+)', html)
        
        # # Delete any existing files in the save location
        # for file_name in os.listdir(save_location):
        #     file_path = os.path.join(save_location, file_name)
        #     try:
        #         if os.path.isfile(file_path):
        #             os.unlink(file_path)
        #     except Exception as e:
        #         print(e)
        
        # # Download each file
        # for link in links:
        #     file_url = self.url + link
        #     file_name = os.path.join(save_location, link)
        #     urllib.request.urlretrieve(file_url, file_name)
        
        # self.status_label.config(text="All files downloaded to " + save_location)
    
    def upload_files(self):
        save_location = self.saveLocation #tmp
        self.status_label.config(text="Uploading files to remote folder")
        
        # Upload files using ftp.py script
        ftp.uploadFiles(self.game, save_location)
        print("Upload finished")
        self.status_label.config(text="All files uploaded")

        # # Upload each file in save location
        # files = []
        # uploadUrl = self.url + 'upload'
        # for file_name in os.listdir(save_location):
        #     file_path = os.path.join(save_location, file_name)
        #     print("Current file: " + file_path) #tmp
        #     if os.path.isfile(file_path):
        #         files.append(str("-F files=@" + file_path))
        # files = " ".join(files)
        # os.system("curl -X POST " + uploadUrl + " " + files)
        # self.status_label.config(text="All files uploaded to " + uploadUrl)

root = tk.Tk()
download_gui = DownloadGUI(root, getDirectory.gameList(platform.system().lower()))
root.geometry("350x420")
root.mainloop()