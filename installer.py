import os
import winshell
import requests
import pyuac
from win32com.client import Dispatch
import tkinter as tk
from tkinter import filedialog
import shutil
root = tk.Tk()
root.withdraw()
desktop = winshell.desktop()
startup = winshell.startup()
startmenu = winshell.start_menu()

def OverrideShortcut(path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)

    # Get the existing target path
    existing_target = shortcut.TargetPath

    # Append the new argument
    target = existing_target + " --remote-debugging-port=9222"

    # Set the TargetPath to the desired value and save again
    shortcut.Arguments = target
    shortcut.save()
    return True

def SelectShortcut():
    # Specify the file type to .lnk to prevent resolving the target
    path = filedialog.askopenfilename(filetypes=[("Shortcut files", "*.lnk")])

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)  # Directly use the selected path

    # Get the existing target path
    existing_target = shortcut.TargetPath

    # Append the new argument
    target = existing_target + " --remote-debugging-port=9222"


    # Set the TargetPath to the desired value and save again
    shortcut.Arguments = target
    shortcut.save()


def SelectDirectory():
    path = filedialog.askdirectory()

    return path



def download_github_files(repo_url, filenames, save_folder):
    """
    Download specific files from the GitHub repo and save them as .py files.

    Parameters:
    - repo_url (str): The URL of the GitHub repository (e.g., "https://github.com/username/repo_name")
    - filenames (list): List of filenames to download from the repo
    - save_folder (str): The path to the folder where the files will be saved
    """
    
    # Ensure the save folder exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Base URL for raw content from GitHub
    base_url = repo_url.replace("github.com", "raw.githubusercontent.com")

    for filename in filenames:
        file_url = f"{base_url}/main/{filename}"
        response = requests.get(file_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            with open(os.path.join(save_folder, filename), 'w') as file:
                file.write(response.text)
            print(f"Downloaded {filename} and saved to {save_folder}")
        else:
            print(f"Failed to download {filename}. Status code: {response.status_code}")



print("\n\nTHIS IS NOT CONFIRMED TO WORK ON THE WINDOWS STORE VERSION OF SPOTIFY,\nPLEASE MAKE SURE YOU ARE USING THE DESKTOP APP FROM THE SPOTIFY WEBSITE")
input("ok? (enter to continue)")

print("\nPlease choose a directory for the install folder and files.")
installdir = SelectDirectory()

print("Downloading files...")
if not os.path.exists(installdir):
    print("Warning: Install directory that was selected does not exist, defauting to Desktop installation.")
    installdir = (desktop)
download_github_files("https://github.com/RoCoderXD/Spotify-Customizer/", ["SpotifyCustomizerAutoStart.py", "main.py", "Spotify-Customizer.py", "theme.json"], installdir+"\\Spotify-Customizer")

print(f"\n\nDownloaded Github files and put into: {installdir}")






print("\n\nWould you like to enable autostart? (Y/N) ")
autostart = input()
if str.upper(autostart) == "Y":
    if not pyuac.isUserAdmin():
        print("Getting admin for startup file transfer.")
        pyuac.runAsAdmin()
    else:
        shutil.copy("./SpotifyModderAutoStart.py", winshell.startup())



print("\n\nAutomatically checking for Spotify shortcuts in Desktop and Start Menu")
shortcut_SM = False
shortcut_DSKTP = False

if os.path.isfile(desktop + "\\Spotify.lnk"):
    print("Found Desktop shortcut.")
    OverrideShortcut(desktop + "\\Spotify.lnk")
    shortcut_SM = True
else:
    print("Did not find Desktop Shortcut!")

if os.path.isfile(startmenu + "\\Programs\\Spotify.lnk"):
    print("Found Start Menu shortcut.")
    OverrideShortcut(startmenu + "\\Programs\\Spotify.lnk")
    shortcut_DSKTP = True
else:
    print("Did not find Start Menu shortcut!")



if shortcut_SM == False:
    if str.upper(input("\n\nCouldn't find the Start Menu shortcut, would you like to select it manually? (N = skip) (Y/N) ")) == "Y":
        print("\nSelect Your Spotify Shortcut.")
        SelectShortcut()
        print("Edited shortcut!")

if shortcut_DSKTP == False:
    if str.upper(input("\n\nCouldn't find the Desktop shortcut, would you like to select it manually? (N = skip) (Y/N) ")) == "Y":
        print("\nSelect Your Spotify Shortcut.")
        SelectShortcut()
        print("Edited shortcut!")




input("Done! Press enter to close...")