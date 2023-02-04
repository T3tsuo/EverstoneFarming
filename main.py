import time
import pyautogui
import pydirectinput
from random import random

'''
frisked is first pokemon, second pokemon has thief in first slot 
and surf in second slot

make window small enough so only a couple of battle logs are shown at a time (reduce height of application)
'''


def change_pokemon():
    # go to pokemon
    pydirectinput.press('down')
    print("down")
    # human input break
    paying_attention_break()
    pydirectinput.press('z')
    print("z")
    paying_attention_break()
    # following pokemon
    pydirectinput.press('right')
    print("right")
    paying_attention_break()
    # select the pokemon
    pydirectinput.press('z')
    print("z")
    paying_attention_break()
    attack_break()
    print("time to attack")
    # switch to attacking stage
    thief()


def thief():
    stole_item = False
    # counter to keep track of which pokemon is currently selected
    select_pokemon = 0
    # while the item is not found and we still have not attacked all 5 pokemons
    while stole_item is False and select_pokemon < 5:
        # press fight
        pydirectinput.press('z')
        print("z")
        paying_attention_break()
        # press thief (first move)
        pydirectinput.press('z')
        print("z")
        paying_attention_break()
        # select and attack specific pokemon
        which_to_attack(select_pokemon)
        # if pokemon flinches
        flinched = False
        # wait for entire attack break while checking if thief took an item
        seconds = random() * 5 + 34
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
    print("Done")


def which_to_attack(n):
    print("SELECT #" + str(n + 1))
    if n == 0:
        # go down to select the first pokemon
        pydirectinput.press('down')
        print("down")
        paying_attention_break()
        # select it
        pydirectinput.press("z")
        print("z")
        paying_attention_break()
    elif n == 1:
        # select the second pokemon
        pydirectinput.press("z")
        print("z")
        paying_attention_break()
    elif n == 2:
        # go down to select the third pokemon
        pydirectinput.press('right')
        print("right")
        paying_attention_break()
        # select it
        pydirectinput.press("z")
        print("z")
        paying_attention_break()
    elif n == 3:
        # go down to select the fourth pokemon
        pydirectinput.press('right')
        print("right")
        paying_attention_break()
        pydirectinput.press('right')
        print("right")
        paying_attention_break()
        # select it
        pydirectinput.press("z")
        print("z")
        paying_attention_break()
    elif n == 4:
        # go down to select the fifth pokemon
        pydirectinput.press('right')
        print("right")
        paying_attention_break()
        pydirectinput.press('right')
        print("right")
        paying_attention_break()
        pydirectinput.press('down')
        print("down")
        paying_attention_break()
        # select it
        pydirectinput.press("z")
        print("z")
        paying_attention_break()


def paying_attention_break():
    # timer between 0.25 seconds to 0.5 seconds
    time.sleep(random() * 0.25 + 0.25)


def attack_break():
    # timer between 35 and 40 seconds for waiting out a horde attack
    time.sleep(random() * 5 + 35)


while True:
    if pyautogui.locateOnScreen('battle_logs/frisked.png', grayscale=True, confidence=0.8) is not None:
        print("Found item")
        # random number from 3 to 20 seconds
        time.sleep(random() * 12 + 3)
        # change Pokemon
        change_pokemon()
        break
