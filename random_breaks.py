from random import random


def inside_cave():
    # waits inside of cave for 1.5 second to 2 seconds
    return random() * 0.5 + 1.5

def into_cave():
    # goes into the cave and 1 tile into the cave in between 1.4 seconds to 1.6 seconds
    return random() * 0.2 + 1.4


def below_cave():
    # goes right from 1 seconds to 1.1 seconds, up the stairs until it is aligned with the cave entrance
    return random() * 0.1 + 1


def adjust_to_stairs():
    # move on tile down takes 0.02 seconds to 0.06
    return random() * 0.04 + 0.02


def before_stairs():
    # arrive before stairs takes from 0.3 to 0.5 seconds
    return random() * 0.2 + 0.3


def wait_to_iron_island():
    # talking to sailor and wait from 3.1 to 5 seconds
    return random() * 1.9 + 3.1


def leave_building():
    # 1.8 seconds to 1.9 seconds to leave building
    return random() * 0.1 + 1.8


def to_nurse():
    # run up to nurse time interval 3 seconds to 3.1 seconds
    return random() * 0.1 + 3

def left_of_city():
    # go left for between 1.9 seconds to 1.95
    return random() * 0.05 + 1.9


def south_of_city():
    # go south for between 2.2 seconds to 2.24
    return random() * 0.04 + 2.2


def right_to_sailor():
    # go towards sailor for 1.15 to 1.3 seconds
    return random() * 0.15 + 1.15


def paying_attention_break():
    # timer between 0.25 seconds to 0.50 seconds
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


def heal_up_break():
    # dialogue of nurse healing break from 7 seconds to 12 seconds
    return random() * 5 + 7


def input_break():
    # break for hoping on bike from 0.1 - 0.25 seconds
    return random() * 0.15 + 0.1
