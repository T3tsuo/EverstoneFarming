import time
import pyautogui
import pydirectinput
from random import random

import random_breaks


def change_pokemon():
    # go to pokemon
    pydirectinput.press('down')
    # human input break
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.press('z')
    time.sleep(random_breaks.paying_attention_break())
    # following pokemon
    pydirectinput.press('right')
    time.sleep(random_breaks.paying_attention_break())
    # select the pokemon
    pydirectinput.press('z')
    print("Change Pokemon")
    time.sleep(random_breaks.paying_attention_break())
    time.sleep(random_breaks.attack_break())
    print("Time To Attack")


def thief():
    # boolean if horde is dead or not
    is_dead = False
    stole_item = False
    # counter to keep track of which pokemon is currently selected
    select_pokemon = 0
    # while the item is not found, and we still have not attacked all 5 pokemons
    while stole_item is False and select_pokemon < 5 and is_dead is False:
        # press fight
        pydirectinput.press('z')
        print("Fight")
        time.sleep(random_breaks.paying_attention_break())
        # press thief (first move)
        pydirectinput.press('z')
        print("Thief")
        time.sleep(random_breaks.paying_attention_break())
        # select and attack specific pokemon
        which_to_attack(select_pokemon)
        # if pokemon flinches
        flinched = False
        # wait for entire attack break while checking if thief took an item
        seconds = random_breaks.attack_break()
        end_time = time.time() + seconds
        while time.time() < end_time:
            # if item is found
            if pyautogui.locateOnScreen('battle_logs/stole.png', confidence=0.8) is not None:
                stole_item = True
                print("Stole item")
                # if the item is found early then wait the remaining time before exiting
                time.sleep(end_time - time.time())
                break
            if pyautogui.locateOnScreen('battle_logs/flinched.png', confidence=0.8) is not None:
                flinched = True
                print("Flinched")
                # if the pokemon flinched then wait the remaining time of the turn before exiting
                time.sleep(end_time - time.time())
                break
            if pyautogui.locateOnScreen('location/quagsire.png', confidence=0.8) is not None:
                print("Horde is dead")
                is_dead = True
                break
        if not flinched:
            select_pokemon += 1


def which_to_attack(n):
    print("SELECT #" + str(n + 1))
    if n == 0:
        # go down to select the first pokemon
        pydirectinput.press('down')
        time.sleep(random_breaks.paying_attention_break())
        # select it
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())
    elif n == 1:
        # select the second pokemon
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())
    elif n == 2:
        # go down to select the third pokemon
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        # select it
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())
    elif n == 3:
        # go down to select the fourth pokemon
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        # select it
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())
    elif n == 4:
        # go down to select the fifth pokemon
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        pydirectinput.press('down')
        time.sleep(random_breaks.paying_attention_break())
        # select it
        pydirectinput.press("z")
        time.sleep(random_breaks.paying_attention_break())


def kill_all():
    dead = False
    # break from 1.5 - 2 seconds
    time.sleep(random_breaks.inside_cave())
    while not dead:
        # press fight
        pydirectinput.press('z')
        print("Fight")
        time.sleep(random_breaks.paying_attention_break())
        # go to second move
        pydirectinput.press('right')
        time.sleep(random_breaks.paying_attention_break())
        # press surf (second move)
        pydirectinput.press('z')
        print("Surf")
        time.sleep(random_breaks.paying_attention_break())
        # select and attack the second pokemon
        which_to_attack(1)
        # wait for entire attack break while checking if thief took an item
        seconds = random_breaks.attack_break()
        end_time = time.time() + seconds
        while time.time() < end_time:
            # if battle is done
            if pyautogui.locateOnScreen('location/quagsire.png', confidence=0.8) is not None:
                # then they are dead
                dead = True
                break


def run_away():
    pydirectinput.press('right')
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.press('down')
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.press('z')
    print('Run away')
    time.sleep(random_breaks.paying_attention_break())
    time.sleep(random_breaks.run_away_break())


def teleport_away():
    left = False
    while left is False:
        # once left the cave
        if pyautogui.locateOnScreen('location/iron_island_entrance.png', confidence=0.8) is not None:
            # wait for screen to change
            time.sleep(random_breaks.paying_attention_break())
            # press teleport
            pydirectinput.press('5')
            print("Teleport")
            left = True
            time.sleep(random_breaks.paying_attention_break())
            time.sleep(random_breaks.to_nurse())


        else:
            # continue to leave the cave until you leave
            pydirectinput.press('down')


def in_battle():
    while True:
        if pyautogui.locateOnScreen('battle_logs/frisked.png', confidence=0.8) is not None:
            print("Found item")
            # change pokemon
            change_pokemon()
            # switch to attacking stage
            thief()
            # switch to killing all the pokemons if battle isn't done
            if pyautogui.locateOnScreen('location/quagsire.png', confidence=0.8) is None:
                print("Kill All")
                kill_all()
            print("Battle End")
            return True
        else:
            # did not find any items on pokemon
            return False


def take_item():
    item_taken = False
    while item_taken is False:
        if pyautogui.locateOnScreen('location/quagsire.png', confidence=0.8) is not None:
            # grab location of image
            location = pyautogui.locateOnScreen('location/quagsire.png', confidence=0.8)
            # click randomly on the box
            pyautogui.moveTo(location.left + random() * location.width, location.top + random() * location.height)
            pydirectinput.click()
            print("Quagsire Selected")
            # user paying attention reaction time
            time.sleep(random_breaks.paying_attention_break())
            while item_taken is False:
                # do the same thing for everstone
                if pyautogui.locateOnScreen('location/take_everstone.png', confidence=0.8):
                    location = pyautogui.locateOnScreen('location/take_everstone.png',
                                                        confidence=0.8)
                    print("Taking Everstone")
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)
                    pydirectinput.click()
                    item_taken = True
                    time.sleep(random_breaks.paying_attention_break())
                if pyautogui.locateOnScreen('location/take_hard_stone.png', confidence=0.8):
                    # same thing for hard stone
                    location = pyautogui.locateOnScreen('location/take_hard_stone.png',
                                                        confidence=0.8)
                    print("Taking Hard Stone")
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)
                    pydirectinput.click()
                    item_taken = True
                    time.sleep(random_breaks.paying_attention_break())


def switch_tabs():
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')


def run(x):
    for i in range(x):
        # wait for program to switch to game window
        time.sleep(random_breaks.run_away_break())
        # use sweet scent
        pydirectinput.press('4')
        print("Sweet Scent")
        time.sleep(random_breaks.starting_battle_break())
        # check if item was found and if it was it will try to get it
        found_item = in_battle()
        if not found_item:
            print("Not found")
            # run away from battle
            run_away()
        else:
            # if item is stolen then take it off of your pokemon
            take_item()
    # when all of sweet scent is used then leave to pokecenter
    teleport_away()
