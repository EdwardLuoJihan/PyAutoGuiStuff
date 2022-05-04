# Imports
import pyautogui as pagui
from time import *
import random
import asyncio
import requests

# Initialize variables
screenWidth, screenHeight = pagui.size()
statuses = ["They say if a crush lasts more than", "4 months", "you're in love.", "So what happens when", "I've been infatuated with you", "for 36 months?", "Have I fallen in love with you", "9 times?", "Or have I wasted", "3 years", "36 months", "156 weeks", "1092 days", "craving you?", "j.k."]
n = 0
_status = statuses[n]

# Open discord
def openDiscord():
    left, top, width, height = pagui.locateOnScreen('img/discord.png', confidence=0.7)
    pagui.moveTo(left+width/2, top+height/2)
    pagui.click()
    sleep(0.3)
    if pagui.locateOnScreen('img/discord_open.png', confidence=0.7) == None:
        openDiscord()
    else:
        return
    
# Open status menu
def openStatus():
    pagui.moveTo(105, screenHeight-85)
    pagui.click()
    sleep(0.3)
    if pagui.locateOnScreen('img/states.png', confidence=0.7) == None:
        openStatus()
    else:
        return

# Edit status
def editStatus(status):
    pagui.click(205, screenHeight-192)
    sleep(0.3)
    if pagui.locateOnScreen('img/custom_status.png', confidence=0.7) == None:
        editStatus()
    else:
        pagui.hotkey('ctrl', 'a')
        pagui.press('backspace') 
        pagui.write(status, interval=0.1)

# Open change status screen
def openClearAfter():
    try:
        left, top, width, height = pagui.locateOnScreen('img/status.png', confidence=0.8)
        sleep(0.3)
        pagui.click(left+width/2, top+height/2+45)
    except:
        openClearAfter()

# Change clear after to never
def clearAfterNever():
    try:
        left, top, width, height = pagui.locateOnScreen('img/status.png', confidence=0.8)
        sleep(0.3)
        pagui.click(left+width/2, top+height/2+272)
    except:
        clearAfterNever()

# Save status
def saveStatus():
    try: 
        left, top, width, height = pagui.locateOnScreen('img/save_status.png', confidence=0.8)
        sleep(0.3)
        pagui.moveTo(left+width/2, top+height/2)
        sleep(0.2)
        pagui.click()
    except:
        saveStatus()

# Update discord status
def updateDiscordStatus(status):
    openStatus()
    editStatus(status)
    openClearAfter()
    clearAfterNever()
    saveStatus()
    sleep(0.3)
    try:
        pagui.hotkey("alt", "tab")
        left, top, width, height = pagui.locateOnScreen('img/vscode_run.png', confidence=0.8)
        pagui.moveTo(left+width/2-7, top+height/2)
    except:
        pagui.moveTo(screenWidth/2, screenHeight/2-51) # Move to center of screen
    print()
    print(f"Status changed to: '{status}'")

def editStatusLoop(_status):
    pagui.click(205, screenHeight-192)
    sleep(0.3)
    if pagui.locateOnScreen('img/custom_status.png', confidence=0.7) == None:
        editStatus(_status)
    else:
        pagui.hotkey('ctrl', 'a')
        pagui.press('backspace') 
        pagui.write(_status, interval=0.01)

async def updateDiscordStatusLoop():
    n = 0
    while True:
        global _status
        openStatus()
        editStatusLoop(statuses[n%len(statuses)])
        # openClearAfter()
        # clearAfterNever()
        saveStatus()
        print()
        print(f"Status changed to: '{statuses[n%len(statuses)]}'")
        n+=1
        await asyncio.sleep(1)