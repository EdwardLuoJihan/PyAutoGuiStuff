# Import modules
import pyautogui as pagui
from time import *
import random
import asyncio
import requests

# Initialize variables
screenWidth, screenHeight = pagui.size()
currentMouseX, currentMouseY = pagui.position()
statuses = ["Depressing status #1", "Depressing status #2", "Depressing status #3", "Depressing status #4", "Depressing status #5", "Depressing status #6", "Depressing status #7", "Depressing status #8", "Depressing status #9", "Depressing status #10"]
_status = random.choice(statuses)

# Import functions
from discord import *
from spotify import *
from btd6 import *

# PAG initialize
pagui.moveTo(screenWidth/2, screenHeight/2-51) # Move to center of screen

def main():
    print('''
    -LEGEND-
    1: Update discord status          A: Infinite loop          B: One time
    2: Open Spotify
    3. Play BTD6
    ''')
    operation = input(": ")
    if operation == "1":
        openDiscord()
    elif len(operation) > 1:
        url = "http://www.kite.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            if operation[1].lower() == "a":
                openDiscord()
                sleep(1)
                a = asyncio.get_event_loop()
                a.create_task(updateDiscordStatusLoop())
                a.run_forever()
            else:
                status = input(": ")
                openDiscord()
                sleep(1)
                updateDiscordStatus(status)
        except (requests.ConnectionError, requests.Timeout) as exception:
            pagui.alert(text='Could not preform these actions', title='No Wifi!', button='OK')
    elif operation[0] == "2":
        openSpotify()
    elif operation[0] == "3":
        openBTD()

main()