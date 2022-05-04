# Import modules
import pyautogui as pagui
from time import *
import random
import asyncio
import requests

# Initialize variables
screenWidth, screenHeight = pagui.size()

# Open home screen
def BtdHomeScreen():
    pagui.press("win")
    sleep(0.2)
    left, top, width, height = pagui.locateOnScreen('img/windowsSearch.png', confidence=0.8)
    pagui.moveTo(left+width/2, top+height/2)
    pagui.click()
    sleep(0.2)
    pagui.write("Bloons TD 6", interval=0.1)
    pagui.press("enter")
    btn = pagui.locateOnScreen("img/BTD6Button.png")
    while btn == None:
        btn = pagui.locateOnScreen("img/BTD6Button.png")
    left, top, width, height = pagui.locateOnScreen('img/BTD6Button.png', confidence=0.8)
    pagui.moveTo(left+width/2, top+height/2)
    pagui.click()
    statue = pagui.locateOnScreen("img/BTD6HomeStatue.png")
    while statue == None:
        statue = pagui.locateOnScreen("img/BTD6HomeStatue.png")

# Daily Chest
def checkDailyChest():
    try:
        left, top, width, height = pagui.locateOnScreen('img/BTD6DailyChestOpen.png', confidence=0.8)
    except:
        left, top, width, height = pagui.locateOnScreen('img/BTD6DailyChestOpen.png', confidence=0.8)
        pagui.moveTo(left+width/2, top+height/2)
        pagui.click()
        pagui.moveTo(width/2, height/2)
        pagui.click()
        pagui.click()

# Open map select
def openPlayScreen():
    left, top, width, height = pagui.locateOnScreen('img/BTD6PlayButton.png', confidence=0.8)
    pagui.moveTo(left+width/2, top+height/2)
    pagui.click()

# Randomly Choose difficulty
def chooseDifficulty():
    d = ["Beginner", "Intermediate", "Advanced", "Expert"]
    coords = {
        "Beginner":[575,screenHeight-100],
        "Intermediate":[830,screenHeight-100],
        "Advanced":[1085,screenHeight-100],
        "Expert":[1340,screenHeight-100]
    }
    difficulty = str(random.choice(d))
    x, y = coords[difficulty][0], coords[difficulty][1]
    sleep(0.3)
    pagui.click(x, y)
    for i in range(random.randint(0, 4)):
        sleep(0.5)
        pagui.click()
    return difficulty

# Randomly choose map
def chooseMap(difficulty):
    maps = {
        1:['Monkey Meadow', 'Tree Stump', 'Town Center', 'Scrapyard', 'The Cabin', 'Resort'],
        2: ['Skates', 'Lotus Island', 'Candy Falls', 'Winter Park', 'Carved', 'Park Path'],
        3: ['Alpine Run', 'Frozen Over', 'In The Loop', 'Cubism', 'Four Circles', 'Hedge'],
        4: ['End Of The Road', 'Logs'],
        5: ['Quiet Street', 'Bloonarius Prime', 'Balance', 'Encrypted', 'Bazaar', "Adora's Temple"],
        6: ['Spring Spring', 'KartsNDarts', 'Moon Landing', 'Haunted', 'Downstream', 'Firing Range'],
        7: ['Cracked', 'Streambed', 'Chutes', 'Rake', 'Spice Islands'],
        8: ['Sunken Columns', 'X Factor', 'Mesa', 'Geared', 'Spillway', 'Cargo'],
        9: ["Pat's Pond", 'Peninsula', 'High Finance', 'Another Brick', 'Off The Coast', 'Cornfield'],
        10: ['Underground'],
        11: ['Sanctuary', 'Ravine', 'Flooded Valley', 'Infernal', 'Bloody Puddles', 'Workshop'],
        12: ['Quad', 'Dark Castle', 'Muddy Puddles', '#Ouch'],
    }
    #page = position of dot based off math
    #take screenshot of the bar of dots and determine which one is filled in
    
    # possible_choices = maps[page]

# Open BTD
def openBTD():
    BtdHomeScreen()
    checkDailyChest()
    openPlayScreen()
    difficulty = chooseDifficulty()
    chooseMap(difficulty)