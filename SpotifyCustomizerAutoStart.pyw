import psutil
import os
import json
from time import sleep
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