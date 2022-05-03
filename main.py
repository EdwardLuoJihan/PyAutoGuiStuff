# Import modules
from pyautogui import *
from time import *
import random
import asyncio

# Initialize variables
screenWidth, screenHeight = size()
currentMouseX, currentMouseY = position()
statuses = ["This status was made by PyAutoGUI!", "This status was also made by PyAutoGUI!", "PyAutoGUI is awesome!"]

# PAG initialize
moveTo(screenWidth/2, screenHeight/2-51) # Move to center of screen

# Open discord
def openDiscord():
    left, top, width, height = locateOnScreen('img/discord.png', confidence=0.7)
    moveTo(left+width/2, top+height/2)
    click()
    

# Update discord status
def updateStatus():
    moveTo(105, screenHeight-85)
    click()
    moveTo(205, screenHeight-192)
    click()
    hotkey('ctrl', 'a')
    press('backspace') 
    write(random.choice(statuses))
    sleep(1)
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
    openDiscord()
    # Infinite status update
    # a = asyncio.get_event_loop()
    # a.create_task(updateStatus())
    # a.run_forever()
    # Remember to add proper async and await where needed

    # Single status update
    updateStatus()