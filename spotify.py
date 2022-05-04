# Imports
import pyautogui as pagui
from time import *
import random
import asyncio
import requests

# Initialize variables
screenWidth, screenHeight = pagui.size()

def openSpotify():
    left, top, width, height = pagui.locateOnScreen('img/spotify.png', confidence=0.7)
    pagui.moveTo(left+width/2, top+height/2)
    pagui.click()
    sleep(0.3)
    if pagui.locateOnScreen('img/spotify_open.png', confidence=0.7) == None:
        openSpotify()
    else:
        return