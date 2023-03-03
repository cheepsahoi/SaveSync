import tkinter as tk
import urllib.request
import os
import re
from tkinter import filedialog
import platform
import getDirectory

class DownloadGUI:
    def __init__(self, master, names):
        self.master = master
        master.title("Sync Saves")

        # Create list box for games
        self.list_label = tk.Label(master, text="Games")
        self.list_label.grid(row=0, column=1, pady=5)
        self.listbox = tk.Listbox(master)
        self.listbox.grid(row=1, column=1, padx=5)
        
        # Add games to list box
        for i, name in enumerate(names):
            self.listbox.insert(i+1, f"{i+1}. {name}")
        
        # Bind click event to list box
        self.listbox.bind("<Button-1>", self.select_game)
        
        # Initialize game index to -1
        self.game = -1

        # Create status label
        self.status_label = tk.Label(master, text="")
        self.status_label.grid(row=1, column=0, padx=5, pady=5)

        # Create Save location input box
        self.save_label = tk.Label(master, text="Enter save location:")
        self.save_label.grid(row=2, column=1, pady=5)
        self.save_entry = tk.Entry(master, width=50)
        self.save_entry.grid(row=3, column=1, padx=5, pady=5)
        
        # Create Download button
        self.download_button = tk.Button(master, text="Download Saves", command=self.download_files)
        self.download_button.grid(row=4, column=1, padx=5, pady=5)
        
        # Create Upload button
        self.upload_button = tk.Button(master, text="Upload Saves", command=self.upload_files)
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
            self.debug_label.config(text="MacOS not supported.")
        else:
            self.platform = "unknown"
            self.debug_label.config(text="Operating system not detected.")
        self.debug_label.config(text=self.current_directory)

    def select_game(self, event):
        # Get index of selected item
        index = self.listbox.curselection()
        
        # Store index in game variable
        if len(index) > 0:
            self.game = index[0]
            self.status_label.config(text=f"Selected game: {self.listbox.get(self.game)}")
        else:
            self.game = -1
            self.status_label.config(text="No game selected")

    def get_saveLocation(self):
        pass

    def download_files(self):
        save_location = self.save_entry.get()
        self.status_label.config(text="Downloading saves from " + url)
        
        # Make request to URL
        try:
            response = urllib.request.urlopen(url)
            html = response.read().decode('utf-8')
        except:
            self.status_label.config(text="Error connecting to server")
            return
        
        # Find all links on the page
        links = re.findall(r'href=[\'"]?([^\'" >]+)', html)
        
        # Delete any existing files in the save location
        for file_name in os.listdir(save_location):
            file_path = os.path.join(save_location, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)
        
        # Download each file
        for link in links:
            file_url = url + link
            file_name = os.path.join(save_location, link)
            urllib.request.urlretrieve(file_url, file_name)
        
        self.status_label.config(text="All files downloaded to " + save_location)
    
    def upload_files(self):
        save_location = self.save_entry.get()
        save_location = '/Users/rob/Downloads/http_download' #tmp
        self.status_label.config(text="Uploading files to " + url)
        
        # Upload each file in save location
        files = []
        uploadUrl = url + '/upload'
        for file_name in os.listdir(save_location):
            file_path = os.path.join(save_location, file_name)
            print("Current file: " + file_path) #tmp
            if os.path.isfile(file_path):
                files.append(str("-F files=@" + file_path))
        files = " ".join(files)
        os.system("curl -X POST " + uploadUrl + " " + files)
        self.status_label.config(text="All files uploaded to " + uploadUrl)

root = tk.Tk()
names = ["Hogwarts Legacy", "Spider-Man", "Red Dead Redemption", "David"]
download_gui = DownloadGUI(root, names)
root.mainloop()
print(getDirectory.getPrint())
