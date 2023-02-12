import time
import pyautogui
import pydirectinput

import random_breaks

def go_to_nurse():
    print("Going to Nurse")
    pydirectinput.keyDown("up")
    time.sleep(random_breaks.to_nurse())
    pydirectinput.keyUp("up")
    time.sleep(random_breaks.input_break())



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
    # wait 1.5 - 2 seconds
    time.sleep(random_breaks.inside_cave())


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
    time.sleep(random_breaks.paying_attention_break())


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
    time.sleep(random_breaks.inside_cave())
    print("Inside of Cave")
    time.sleep(random_breaks.paying_attention_break())
    pydirectinput.PAUSE = 0.05
    pydirectinput.press("up")
    pydirectinput.PAUSE = 0.1
    # break
    time.sleep(random_breaks.input_break())


def run():
    go_to_nurse()
    heal_up()
    leave_building()
    go_to_sailor()
    travel_to_island()
    go_into_cave()
