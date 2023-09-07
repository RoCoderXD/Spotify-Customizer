import os
import winshell
from win32com.client import Dispatch
import json
import glob
import pyuac
import sys
user = f"C:\\Users\\{os.getlogin()}"
desktop = winshell.desktop()
startup = winshell.startup()
startmenu = winshell.start_menu()
user = f"C:\\Users\\{os.getlogin()}"



def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)
sys.excepthook = show_exception_and_exit


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


if not pyuac.isUserAdmin() and os.path.isfile(f"{startup}/SpotifyCustomizerAutoStart.pyw"):
    print("Getting UAC to remove Auto Start.")
    pyuac.runAsAdmin()
    if not os.path.isfile(f"{startup}/SpotifyCustomizerAutoStart.pyw"):
        input("Uninstalled! Press Enter to close...")
        quit()
    else:
        input("Error trying to remove the Auto Start file, please try again. Press Enter to quit...")
        quit()

AREYOUSUREABOUTTHAT = input("Are you sure you want to uninstall? (Y/N) ")
if str.upper(AREYOUSUREABOUTTHAT) == "Y":

    if os.path.isfile(desktop + "\\Spotify.lnk"):
        print("Found Desktop shortcut.")
        RestoreShortcuts(desktop + "\\Spotify.lnk")
        print("Restored.\n")

    if os.path.isfile(startmenu + "\\Programs\\Spotify.lnk"):
        print("Found Start Menu shortcut.")
        RestoreShortcuts(startmenu + "\\Programs\\Spotify.lnk")
        print("Restored.\n")

    if os.path.isfile(f"{startup}/SpotifyCustomizerAutoStart.pyw"):
        os.remove(f"{startup}/SpotifyCustomizerAutoStart.pyw")


    #for clean_up in glob.glob(installdir):
        #print(clean_up)
        #if not clean_up.endswith('uninstall.py'):    
            #os.remove(clean_up)
    
    os.remove(f"{user}\\Spotify-Customizer-Config.json")


    input("Uninstalled, you will have to delete this file yourself. Press Enter to close...")
else:
    quit()