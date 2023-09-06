import os
import winshell
from win32com.client import Dispatch
import json
import glob
user = f"C:\\Users\\{os.getlogin()}"
configfile = open(f"{user}\\Spotify-Customizer-Config.json", "r")
installdir = json.loads(configfile.read())
configfile.close()

def RestoreShortcuts(path):
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)

    # Set the TargetPath to the desired value and save again
    shortcut.Arguments = ""
    shortcut.save()
    return True




AREYOUSUREABOUTTHAT = input("Are you sure you want to uninstall? (Y/N) ")
if str.upper(AREYOUSUREABOUTTHAT) == "Y":
    desktop = winshell.desktop()
    startup = winshell.startup()
    startmenu = winshell.start_menu()
    user = f"C:\\Users\\{os.getlogin()}"


    if os.path.isfile(desktop + "\\Spotify.lnk"):
        print("Found Desktop shortcut.")
        RestoreShortcuts(desktop + "\\Spotify.lnk")
        print("Restored.\n")

    if os.path.isfile(startmenu + "\\Programs\\Spotify.lnk"):
        print("Found Start Menu shortcut.")
        RestoreShortcuts(startmenu + "\\Programs\\Spotify.lnk")
        print("Restored.\n")


    for clean_up in glob.glob(installdir):
        print(clean_up)
        if not clean_up.endswith('./uninstall.py'):    
            os.remove(clean_up)
    
    os.remove(f"{user}\\Spotify-Customizer-Config.json")


    input("Uninstalled, you will have to delete this file yourself. Press Enter to close...")
else:
    quit()