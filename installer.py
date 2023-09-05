import os, winshell
import pyuac
import win32com
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



print("\n\nTHIS IS NOT CONFIRMED TO WORK ON THE WINDOWS STORE VERSION OF SPOTIFY,\nPLEASE MAKE SURE YOU ARE USING THE DESKTOP APP FROM THE SPOTIFY WEBSITE")
input("ok? (enter to continue)")




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