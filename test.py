import tkinter as tk
import urllib.request
import os
import re
from tkinter import filedialog

class DownloadGUI:
    def __init__(self, master):
        self.master = master
        master.title("Download and Upload Files")
        
        # Create URL input box
        self.url_label = tk.Label(master, text="Enter URL:")
        self.url_label.grid(row=0, column=0, sticky="w")
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Create Save location input box
        self.save_label = tk.Label(master, text="Enter save location:")
        self.save_label.grid(row=1, column=0, sticky="w")
        self.save_entry = tk.Entry(master, width=50)
        self.save_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Create Download button
        self.download_button = tk.Button(master, text="Download Files", command=self.download_files)
        self.download_button.grid(row=2, column=1, padx=5, pady=5)
        
        # Create Upload button
        self.upload_button = tk.Button(master, text="Upload Files", command=self.upload_files)
        self.upload_button.grid(row=3, column=1, padx=5, pady=5)
        
        # Create status label
        self.status_label = tk.Label(master, text="")
        self.status_label.grid(row=4, column=1, padx=5, pady=5)
    
    # Ask user what game to determine the URL to use
    def getUrl(self):


    def download_files(self):
        url = self.url_entry.get()
        save_location = self.save_entry.get()
        self.status_label.config(text="Downloading files from " + url)
        
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
        #url = self.url_entry.get() + '/upload'
        url = 'http://46.232.211.40:9911/upload' #tmp
        #save_location = self.save_entry.get()
        save_location = '/Users/rob/Downloads/http_download' #tmp
        self.status_label.config(text="Uploading files to " + url)
        
        # Upload each file in save location
        files = []
        for file_name in os.listdir(save_location):
            file_path = os.path.join(save_location, file_name)
            print("Current file: " + file_path) #tmp
            if os.path.isfile(file_path):
                #file_url = os.path.join(url, file_name)
                files.append(str("-F files=@" + file_path)) #tmp
                #print(files) #tmp
                #input("Paused.")#tmp
                #with open(file_path, 'rb') as file:
                #    response = urllib.request.urlopen(file_url, file.read())
        files = " ".join(files)
        os.system("curl -X POST " + url + " " + files)
        self.status_label.config(text="All files uploaded to " + url)

root = tk.Tk()
download_gui = DownloadGUI(root)
root.mainloop()
