import psutil


for process in psutil.process_iter(['name']):
        if process.info['name'] == "Spotify.exe":
            print("Spotify is running.")