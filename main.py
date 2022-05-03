# Import modules
from pyautogui import *
from time import *
import random
import asyncio
import requests

# Initialize variables
screenWidth, screenHeight = size()
currentMouseX, currentMouseY = position()
statuses = ["This status was made by PyAutoGUI!", "This status was also made by PyAutoGUI!", "PyAutoGUI is awesome!"]
_status = random.choice(statuses)

# PAG initialize
moveTo(screenWidth/2, screenHeight/2-51) # Move to center of screen

# Open discord
def openDiscord():
    left, top, width, height = locateOnScreen('img/discord.png', confidence=0.7)
    moveTo(left+width/2, top+height/2)
    click()
    sleep(0.5)
    if locateOnScreen('img/discord_open.png', confidence=0.7) == None:
        openDiscord()
    else:
        return
    
# Open status menu
def openStatus():
    moveTo(105, screenHeight-85)
    click()
    sleep(0.5)
    if locateOnScreen('img/states.png', confidence=0.7) == None:
        openStatus()
    else:
        return

# Edit status
def editStatus():
    global _status
    click(205, screenHeight-192)
    sleep(0.5)
    if locateOnScreen('img/custom_status.png', confidence=0.7) == None:
        editStatus()
    else:
        hotkey('ctrl', 'a')
        press('backspace') 
        write(_status, interval=0.1)

# Open change status screen
def openClearAfter():
    try:
        left, top, width, height = locateOnScreen('img/status.png', confidence=0.8)
        sleep(0.5)
        click(left+width/2, top+height/2+45)
    except:
        openClearAfter()

# Change clear after to never
def clearAfterNever():
    try:
        left, top, width, height = locateOnScreen('img/status.png', confidence=0.8)
        sleep(0.5)
        click(left+width/2, top+height/2+272)
    except:
        clearAfterNever()

# Save status
def saveStatus():
    try: 
        left, top, width, height = locateOnScreen('img/save_status.png', confidence=0.8)
        sleep(0.5)
        moveTo(left+width/2, top+height/2)
        sleep(0.2)
        click()
    except:
        saveStatus()

# Update discord status
def updateStatus():
    global _status
    openStatus()
    editStatus()
    openClearAfter()
    clearAfterNever()
    saveStatus()
    sleep(0.5)
    try:
        hotkey("alt", "tab")
        left, top, width, height = locateOnScreen('img/vscode_run.png', confidence=0.8)
        moveTo(left+width/2-7, top+height/2)
    except:
        moveTo(screenWidth/2, screenHeight/2-51) # Move to center of screen
    print()
    print(f"Status changed to {_status}!")

async def updateStatusLoop():
    moveTo(105, screenHeight-85)
    click()
    moveTo(205, screenHeight-192)
    click()
    hotkey('ctrl', 'a')
    press('backspace') 
    write(random.choice(statuses))
    await asyncio.sleep(1)
    left, top, width, height = locateOnScreen('img/status.png', confidence=0.8)
    moveTo(left+width/2, top+height/2+45)
    click()
    moveTo(left+width/2, top+height/2+272)
    click()
    left, top, width, height = locateOnScreen('img/save_status.png', confidence=0.8)
    moveTo(left+width/2, top+height/2)
    click()
    moveTo(screenWidth/2, screenHeight/2-51) # Move to center of screen

# Open spotify
def openSpotify():
    left, top, width, height = locateOnScreen('img/spotify.png', confidence=0.7)
    moveTo(left+width/2, top+height/2)
    click()
    

if __name__ == "__main__":
    print('''
    -LEGEND-
    1: Open Discord          a: Update status
    2: Open Spotify
    ''')
    operation = input(": ")
    if operation[0] == "1":
        url = "http://www.kite.com"
        timeout = 5
        try:
            request = requests.get(url, timeout=timeout)
            openDiscord()
            if operation[1] == "a":
                updateStatus()
        except (requests.ConnectionError, requests.Timeout) as exception:
            alert(text='Could not preform these actions', title='No Wifi!', button='OK')
    elif operation[0] == "2":
        openSpotify()