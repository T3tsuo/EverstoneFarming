import time
import pyautogui
import pydirectinput
from random import random
from PIL import Image
import requests

import random_breaks


stole_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                             "T3tsuo/AllEyes2.0/main/battle_logs/stole.png", stream=True).raw)

flinched_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/battle_logs/flinched.png", stream=True).raw)

quagsire_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/location/quagsire.png", stream=True).raw)

iron_island_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/location/iron_island_entrance.png", stream=True).raw)

frisked_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/battle_logs/frisked.png", stream=True).raw)

everstone_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/location/take_everstone.png", stream=True).raw)

hard_stone_png = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/location/take_hard_stone.png", stream=True).raw)

metal_coat = Image.open(requests.get("https://raw.githubusercontent.com/"
                                       "T3tsuo/AllEyes2.0/main/location/take_metal_coat.png", stream=True).raw)

inside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                          "T3tsuo/AllEyes2.0/main/location/inside_building.png", stream=True).raw)

inside_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                      "T3tsuo/AllEyes2.0/main/location/inside_cave.png", stream=True).raw)


def heal_up():
    at_nurse = False
    # we are not at nurse yet
    while at_nurse is False:
        # once we are at the nurse
        if pyautogui.locateOnScreen(inside_building, confidence=0.8) is not None:
            # then set flag to true, so we can talk to the nurse
            at_nurse = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)

    # talk through dialogue
    print("Talking to Nurse")
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.heal_up_break())
    pydirectinput.keyUp("z")
    print("Healing Done")
    # break
    time.sleep(random_breaks.input_break())


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
    # counter to keep track of which pokemon is currently selected
    select_pokemon = 0
    # while the item is not found, and we still have not attacked all 5 pokemons
    while select_pokemon < 5:
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
            if pyautogui.locateOnScreen(stole_png, confidence=0.8) is not None:
                print("Stole item")
                # if the item is found early then wait the remaining time before exiting
                time.sleep(end_time - time.time())
                # return that item was found
                return True
            if pyautogui.locateOnScreen(flinched_png, confidence=0.8) is not None:
                flinched = True
                print("Flinched")
                # if the pokemon flinched then wait the remaining time of the turn before exiting
                time.sleep(end_time - time.time())
            if pyautogui.locateOnScreen(inside_cave, confidence=0.8) is not None:
                print("Horde is dead")
                # return that item was not found
                return False
        if not flinched:
            select_pokemon += 1
    return False


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
            if pyautogui.locateOnScreen(inside_cave, confidence=0.8) is not None:
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
    # use dig
    pydirectinput.press("6")
    print("Dig")
    time.sleep(random_breaks.paying_attention_break())
    left = False
    while left is False:
        # once left the cave
        if pyautogui.locateOnScreen(iron_island_png, confidence=0.8) is not None:
            # wait for screen to change
            time.sleep(random_breaks.paying_attention_break())
            # press teleport
            pydirectinput.press('5')
            print("Teleport")
            left = True
            time.sleep(random_breaks.paying_attention_break())
            print("At Nurse")
            time.sleep(random_breaks.to_nurse())


def in_battle():
    while True:
        if pyautogui.locateOnScreen(frisked_png, confidence=0.8) is not None:
            print("Found item")
            # change pokemon
            change_pokemon()
            # switch to attacking stage
            took_item = thief()
            # switch to killing all the pokemons if battle isn't done
            if pyautogui.locateOnScreen(quagsire_png, confidence=0.8) is None:
                print("Kill All")
                kill_all()
            print("Battle End")
            # found item but return if we took the item
            return True, took_item
        else:
            # did not find any items on pokemon so did not take it
            return False, False


def take_item():
    item_taken = False
    while item_taken is False:
        if pyautogui.locateOnScreen(quagsire_png, confidence=0.8) is not None:
            # grab location of image
            location = pyautogui.locateOnScreen(quagsire_png, confidence=0.8)
            # click randomly on the box
            pyautogui.moveTo(location.left + random() * location.width, location.top + random() * location.height)
            pydirectinput.click()
            print("Quagsire Selected")
            # user paying attention reaction time
            time.sleep(random_breaks.paying_attention_break())
            while item_taken is False:
                # do the same thing for everstone
                if pyautogui.locateOnScreen(everstone_png, confidence=0.8):
                    location = pyautogui.locateOnScreen(everstone_png,
                                                        confidence=0.8)
                    print("Taking Everstone")
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)
                    pydirectinput.click()
                    item_taken = True
                    time.sleep(random_breaks.paying_attention_break())
                if pyautogui.locateOnScreen(hard_stone_png, confidence=0.8):
                    # same thing for hard stone
                    location = pyautogui.locateOnScreen(hard_stone_png,
                                                        confidence=0.8)
                    print("Taking Hard Stone")
                    pyautogui.moveTo(location.left + random() * location.width,
                                     location.top + random() * location.height)
                    pydirectinput.click()
                    item_taken = True
                    time.sleep(random_breaks.paying_attention_break())
                if pyautogui.locateOnScreen(metal_coat, confidence=0.8):
                    # same thing for hard stone
                    location = pyautogui.locateOnScreen(metal_coat,
                                                        confidence=0.8)
                    print("Taking Metal Coat")
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
        time.sleep(random_breaks.run_away_break())
        # use sweet scent
        pydirectinput.press('4')
        print("Sweet Scent")
        time.sleep(random_breaks.starting_battle_break())
        # check if item was found and if it was it will try to get it and return if it did or didn't
        found_item, took_item = in_battle()
        if not found_item and not took_item:
            print("Not found")
            # run away from battle
            run_away()
        elif found_item and took_item:
            # if item is stolen then take it off of your pokemon
            take_item()
    # when all of sweet scent is used then leave to pokecenter
    teleport_away()
    # then heal up
    heal_up()
