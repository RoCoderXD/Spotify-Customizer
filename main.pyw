import asyncio
import websockets
import aiohttp
import json
import winshell
import sys
import psutil
import subprocess
import os
from time import sleep
user = f"C:\\Users\\{os.getlogin()}"


async def execute_script(script):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get('http://localhost:9222/json') as response:
                tabs = await response.json()
                # Assuming the first tab is the one you want to control
                ws_url = tabs[0]['webSocketDebuggerUrl']
        except:
            for proc in psutil.process_iter():
                # check whether the process name matches
                if proc.name() == "Spotify.exe":
                    proc.kill()
            sleep(0.25)
            subprocess.run([f"{winshell.application_data()}/Spotify/Spotify.exe", "-remote-debugging-port=9222"], timeout=1)

            async with session.get('http://localhost:9222/json') as response:
                tabs = await response.json()
                # Assuming the first tab is the one you want to control
                ws_url = tabs[0]['webSocketDebuggerUrl']

        print(ws_url)
        async with websockets.connect(ws_url) as ws:
            # Create a message to evaluate a script
            message = json.dumps({
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": script
                }
            })
            await ws.send(message)
            response = await ws.recv()
            print(response)


# THIS IS THE SELECTOR FOR THE PLAY BUTTON: document.querySelector('#main > div > div.ZQftYELq0aOsg6tPbVbV > div.JG5J9NWJkaUO9fiKECMA > footer > div > div.P4eSEARM2h24PZxMHz1T > div > div.player-controls__buttons.player-controls__buttons--new-icons > button').click()
js_script = """

function main() {

    document.querySelector("#main > div > div.ZQftYELq0aOsg6tPbVbV").classList.add('backgroundClass');


    var style = document.createElement('style');
    style.type = 'text/css';
    style.innerHTML = `.backgroundClass {
        background-image: url('https://media.discordapp.net/attachments/758081788861087794/1148096212529053766/wallpapersden.com_dragon-artwork-4k_3840x2160.jpg');
        background-size: cover;
        background-repeat: no-repeat;
    }`;
    document.head.appendChild(style);
}

var readyStateCheckInterval = setInterval(function() {
    if (document.readyState === "complete") {
        clearInterval(readyStateCheckInterval);
        main();
    }
}, 10);


"""
asyncio.get_event_loop().run_until_complete(execute_script(js_script))

# filter: brightness(50%); for making an element darker.

