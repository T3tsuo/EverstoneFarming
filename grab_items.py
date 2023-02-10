import time
import pyautogui
import pydirectinput
from random import random

# this program grabs items and then fly's to go restore pokemon pp

'''
first pokemon has frisk ability 
second pokemon (Quagsire) has thief in first slot and surf in second slot
sweet scent in fourth key slot

horde of 5 pokemon

takes into account of sturdy and flinch

make game the second window so the program will switch to it

make window small enough so only 2 battle logs are shown at a time (reduce height of application)
ex: window size 765 x 534 (2 battle logs)
you can change this in the main directory of pokemmo:
PokeMMO/config/main.properties client.graphics.height=534
PokeMMO/config/main.properties client.graphics.width=765
'''


def change_pokemon():
    # go to pokemon
    pydirectinput.press('down')
    print("down")
    # human input break
    time.sleep(paying_attention_break())
    pydirectinput.press('z')
    print("z")
    time.sleep(paying_attention_break())
    # following pokemon
    pydirectinput.press('right')
    print("right")
    time.sleep(paying_attention_break())
    # select the pokemon
    pydirectinput.press('z')
    print("z")
    time.sleep(paying_attention_break())
    time.sleep(attack_break())
    print("time to attack")


def thief():
    stole_item = False
    # counter to keep track of which pokemon is currently selected
    select_pokemon = 0
    # while the item is not found and we still have not attacked all 5 pokemons
    while stole_item is False and select_pokemon < 5:
        # press fight
        pydirectinput.press('z')
        print("z")
        time.sleep(paying_attention_break())
        # press thief (first move)
        pydirectinput.press('z')
        print("z")
        time.sleep(paying_attention_break())
        # select and attack specific pokemon
        which_to_attack(select_pokemon)
        # if pokemon flinches
        flinched = False
        # wait for entire attack break while checking if thief took an item
        seconds = attack_break()
        end_time = time.time() + seconds
        while time.time() < end_time:
            # if item is found
            if pyautogui.locateOnScreen('battle_logs/stole.png', grayscale=True, confidence=0.8) is not None:
                stole_item = True
                print("Stole item")
                # if the item is found early then wait the remaining time before exiting
                time.sleep(end_time - time.time())
                break
            if pyautogui.locateOnScreen('battle_logs/flinched.png', grayscale=True, confidence=0.8) is not None:
                flinched = True
                print("Flinched")
                # if the pokemon flinched then wait the remaining time of the turn before exiting
                time.sleep(end_time - time.time())
                break
        if not flinched:
            select_pokemon += 1


def which_to_attack(n):
    print("SELECT #" + str(n + 1))
    if n == 0:
        # go down to select the first pokemon
        pydirectinput.press('down')
        print("down")
        time.sleep(paying_attention_break())
        # select it
        pydirectinput.press("z")
        print("z")
        time.sleep(paying_attention_break())
    elif n == 1:
        # select the second pokemon
        pydirectinput.press("z")
        print("z")
        time.sleep(paying_attention_break())
    elif n == 2:
        # go down to select the third pokemon
        pydirectinput.press('right')
        print("right")
        time.sleep(paying_attention_break())
        # select it
        pydirectinput.press("z")
        print("z")
        time.sleep(paying_attention_break())
    elif n == 3:
        # go down to select the fourth pokemon
        pydirectinput.press('right')
        print("right")
        time.sleep(paying_attention_break())
        pydirectinput.press('right')
        print("right")
        time.sleep(paying_attention_break())
        # select it
        pydirectinput.press("z")
        print("z")
        time.sleep(paying_attention_break())
    elif n == 4:
        # go down to select the fifth pokemon
        pydirectinput.press('right')
        print("right")
        time.sleep(paying_attention_break())
        pydirectinput.press('right')
        print("right")
        time.sleep(paying_attention_break())
        pydirectinput.press('down')
        print("down")
        time.sleep(paying_attention_break())
        # select it
        pydirectinput.press("z")
        print("z")
        time.sleep(paying_attention_break())


def kill_all():
    dead = False
    while not dead:
        # press fight
        pydirectinput.press('z')
        print("z")
        time.sleep(paying_attention_break())
        # go to second move
        pydirectinput.press('right')
        print("right")
        time.sleep(paying_attention_break())
        # press surf (second move)
        pydirectinput.press('z')
        print("z")
        time.sleep(paying_attention_break())
        # select and attack the second pokemon
        which_to_attack(1)
        # no sturdy
        sturdy = False
        # if pokemon flinches
        flinched = False
        # wait for entire attack break while checking if thief took an item
        seconds = attack_break()
        end_time = time.time() + seconds
        while time.time() < end_time:
            # if item is found
            if pyautogui.locateOnScreen('battle_logs/sturdy.png', grayscale=True, confidence=0.8) is not None:
                sturdy = True
                print("Sturdy")
                # if the item is found early then wait the remaining time before exiting
                time.sleep(end_time - time.time())
                break
            if pyautogui.locateOnScreen('battle_logs/flinched.png', grayscale=True, confidence=0.8) is not None:
                flinched = True
                print("Flinched")
                # if the pokemon flinched then wait the remaining time of the turn before exiting
                time.sleep(end_time - time.time())
                break
        if not sturdy and not flinched:
            dead = True


def run():
    pydirectinput.press('right')
    print('right')
    time.sleep(paying_attention_break())
    pydirectinput.press('down')
    print('down')
    time.sleep(paying_attention_break())
    pydirectinput.press('z')
    print('z')
    time.sleep(paying_attention_break())
    time.sleep(run_away_break())


def paying_attention_break():
    # timer between 0.25 seconds to 0.5 seconds
    return random() * 0.25 + 0.25


def attack_break():
    # timer between 32 and 37 seconds for waiting out a horde attack
    return random() * 5 + 32


def starting_battle_break():
    # timer between 15 and 20 seconds before checking item
    return random() * 5 + 15


def run_away_break():
    # timer between 2.25 to 5 seconds before inputting
    return random() * 2.75 + 2.25


def in_battle():
    while True:
        if pyautogui.locateOnScreen('battle_logs/frisked.png', grayscale=True, confidence=0.8) is not None:
            print("Found item")
            # change pokemon
            change_pokemon()
            # switch to attacking stage
            thief()
            # switch to killing all the pokemons
            kill_all()
            print("Done")
            return True
        else:
            # did not find any items on pokemon
            return False


def take_item():
    item_taken = False
    while item_taken is False:
        if pyautogui.locateOnScreen('battle_logs/quagsire.png', grayscale=True, confidence=0.8) is not None:
            # grab location of image
            location = pyautogui.locateOnScreen('battle_logs/quagsire.png', grayscale=True, confidence=0.8)
            # click randomly on the box
            pyautogui.moveTo(location.left + random() * location.width, location.top + random() * location.height)
            pydirectinput.click()
            print("click")
            # user paying attention reaction time
            time.sleep(paying_attention_break())
            while item_taken is False:
                # do the same thing for everstone
                if pyautogui.locateOnScreen('battle_logs/'
                                            'take_everstone.png', grayscale=True, confidence=0.8) is not None:
                    location = pyautogui.locateOnScreen('battle_logs/'
                                                        'take_everstone.png', grayscale=True, confidence=0.8)
                    print("Taking everstone")
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)
                    pydirectinput.click()
                    print("click")
                    item_taken = True
                    time.sleep(paying_attention_break())
                # same thing for hard stone
                elif pyautogui.locateOnScreen('battle_logs/'
                                              'take_hard_stone.png', grayscale=True, confidence=0.8) is not None:
                    location = pyautogui.locateOnScreen('battle_logs/'
                                                        'take_hard_stone.png', grayscale=True, confidence=0.8)
                    print("Taking hard stone")
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)
                    pydirectinput.click()
                    print("click")
                    item_taken = True
                    time.sleep(paying_attention_break())


def switch_tabs():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


x = int(input("Number of times to use sweet scent: "))
# switch to second window which should be the game
switch_tabs()
for i in range(x):
    # wait for user to switch to game window
    time.sleep(2)
    # use sweet scent
    pydirectinput.press('4')
    print("4")
    time.sleep(starting_battle_break())
    # check if item was found and if it was it will try to get it
    found_item = in_battle()
    if not found_item:
        print("Not found")
        # run away from battle
        run()
    else:
        # if item is stolen then take it off of your pokemon
        take_item()