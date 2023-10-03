import psutil
import os
import json
from time import sleep
import win32api
import win32con
import win32security

def is_user_logged_in():
    # Get the handle for the current session
    hUser = win32api.OpenProcessToken(win32api.GetCurrentProcess(), win32con.TOKEN_QUERY)
    
    # Get the session ID for the current session
    session_id = win32security.GetTokenInformation(hUser, win32security.TokenSessionId)
    
    # Check if the session is active
    for session in win32api.WTSEnumerateSessions(win32con.WTS_CURRENT_SERVER_HANDLE):
        if session['SessionId'] == session_id:
            return session['State'] == win32con.WTSActive
    return False

while is_user_logged_in() == False:
    sleep(5)

user = f"C:\\Users\\{os.getlogin()}"


# Open config file to read the install path.
configfile = open(f"{user}\\Spotify-Customizer-Config.json", "r")
installdir = json.loads(configfile.read())
configfile.close()

AwareOfRunning = False

while True:
    for process in psutil.process_iter(['name']):
        if process.info['name'] == "Spotify.exe":
            print("Spotify is running.")
            if AwareOfRunning == False:
                AwareOfRunning = True
                exec(open(installdir+"/main.pyw").read())
            break
    else:
        if AwareOfRunning == True:
            AwareOfRunning = False

    sleep(0.5)