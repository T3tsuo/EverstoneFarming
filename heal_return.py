import time

import pyautogui
import pydirectinput
import requests
from PIL import Image

import random_breaks


outside_building = Image.open(requests.get("https://raw.githubusercontent.com/"
                                           "T3tsuo/EverstoneFarming/main/location/outside_building.png", stream=True).raw)

at_island = Image.open(requests.get("https://raw.githubusercontent.com/"
                                    "T3tsuo/EverstoneFarming/main/location/at_island.png", stream=True).raw)

inside_cave = Image.open(requests.get("https://raw.githubusercontent.com/"
                                      "T3tsuo/EverstoneFarming/main/location/inside_cave.png", stream=True).raw)


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    print(outside_building)
    print("Left building")
    # while cannot find outside, keep on waiting
    is_outside = False
    while is_outside is False:
        print("while loop confidence 0.8", pyautogui.locateOnScreen(outside_building, confidence=0.8))
        # if image recognition detects that we left the building
        if pyautogui.locateOnScreen(outside_building, confidence=0.8) is not None:
            # then we are outside
            is_outside = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)


def go_to_sailor():
    # hop on bike
    pydirectinput.press("1")
    print("Bicycle")
    time.sleep(random_breaks.input_break())
    # go left
    pydirectinput.keyDown("left")
    time.sleep(random_breaks.left_of_city())
    pydirectinput.keyUp("left")
    # break
    time.sleep(random_breaks.input_break())
    # keep ongoing down until at south-end of the city
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.south_of_city())
    pydirectinput.keyUp("down")
    # input break
    time.sleep(random_breaks.input_break())
    # turn right and head towards sailor
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.right_to_sailor())
    pydirectinput.keyUp("right")
    print("At the Sailor")
    # break 1.5 - 2 seconds
    time.sleep(random_breaks.inside_cave())


def travel_to_island():
    pydirectinput.keyDown("z")
    # while cannot island, keep on talking
    arrived = False
    while arrived is False:
        # if image recognition detects that we are at the island
        if pyautogui.locateOnScreen(at_island, confidence=0.8) is not None:
            # then we are at island
            arrived = True
            pydirectinput.keyUp("z")
            time.sleep(0.5)
            print("Traveled")


def go_into_cave():
    # before stairs
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.before_stairs())
    pydirectinput.keyUp("right")
    # break
    time.sleep(random_breaks.input_break())
    # adjust to go upstairs
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("down")
    time.sleep(random_breaks.input_break())
    pydirectinput.press("down")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.below_cave())
    pydirectinput.keyUp("right")
    # break
    time.sleep(random_breaks.input_break())
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.into_cave())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.inside_cave())
    in_cave = False
    while in_cave is False:
        # use image detection to make sure we are inside the cave
        if pyautogui.locateOnScreen(inside_cave, confidence=0.8) is not None:
            in_cave = True
            time.sleep(0.5)
        else:
            time.sleep(0.5)
    print("Inside of Cave")
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.PAUSE = 0.03
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())


def run():
    leave_building()
    go_to_sailor()
    travel_to_island()
    go_into_cave()
