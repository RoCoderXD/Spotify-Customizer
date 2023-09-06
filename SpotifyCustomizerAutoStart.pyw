import psutil
import os
import json
from time import sleep
user = f"C:\\Users\\{os.getlogin()}"

configfile = open(f"{user}\\Spotify-Customizer-Config.json", "r")
installdir = json.loads(configfile.read())

AwareOfRunning = False

while True:
    for process in psutil.process_iter(['name']):
        if process.info['name'] == "Spotify.exe":
            print("Spotify is running.")
            exec(open(installdir+"/main.py").read())
            if AwareOfRunning == False:
                AwareOfRunning = True
            break
    else:
        if AwareOfRunning == True:
            AwareOfRunning = False

    sleep(0.5)