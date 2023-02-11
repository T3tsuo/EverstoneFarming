import time
import pyautogui
import pydirectinput

import random_breaks


def go_to_nurse():
    at_nurse = False
    while at_nurse is False:
        if pyautogui.locateOnScreen('location/at_nurse_desk.png', confidence=0.8):
            pydirectinput.keyUp("up")
            print("At Nurse")
            at_nurse = True
            # break
            time.sleep(random_breaks.input_break())
        else:
            # go up until arrived at nurse
            pydirectinput.keyDown("up")


def heal_up():
    # talk through dialogue
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.heal_up_break())
    pydirectinput.keyUp("z")
    print("Healing Done")
    # break
    time.sleep(random_breaks.input_break())


def leave_building():
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.leave_building())
    pydirectinput.keyUp("down")
    print("Left building")
    time.sleep(random_breaks.paying_attention_break())


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
    # break
    time.sleep(random_breaks.input_break())


def travel_to_island():
    pydirectinput.keyDown("z")
    time.sleep(random_breaks.wait_to_iron_island())
    pydirectinput.keyUp("z")
    print("Traveled")
    # break
    time.sleep(random_breaks.input_break())


def go_into_cave():
    # before stairs
    pydirectinput.keyDown("right")
    time.sleep(random_breaks.before_stairs())
    pydirectinput.keyUp("right")
    # break
    time.sleep(random_breaks.input_break())
    # adjust to go upstairs
    pydirectinput.keyDown("down")
    time.sleep(random_breaks.adjust_to_stairs())
    pydirectinput.keyUp("down")
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
    print("Inside of Cave")
    # break
    time.sleep(random_breaks.input_break())


def run():
    go_to_nurse()
    heal_up()
    leave_building()
    go_to_sailor()
    travel_to_island()
    go_into_cave()
