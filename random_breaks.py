from random import random


def into_cave():
    # goes into the cave and 1 tile into the cave in between 2.1 seconds to 2.105 seconds
    return random() * 0.005 + 2.1


def below_cave():
    # goes right from 1 seconds to 1.1 seconds, up the stairs until it is aligned with the cave entrance
    return random() * 0.1 + 1


def adjust_to_stairs():
    # move on tile down takes 0.02 seconds to 0.07
    return random() * 0.05 + 0.02


def before_stairs():
    # arrive before stairs takes from 0.3 to 0.5 seconds
    return random() * 0.2 + 0.3


def wait_to_iron_island():
    # talking to sailor and wait from 3.1 to 5 seconds
    return random() * 1.9 + 3.1


def leave_building():
    # 1.8 seconds to 2.1 seconds to leave building
    return random() * 0.3 + 1.8


def left_of_city():
    # go left for between 1.9 seconds to 2
    return random() * 0.1 + 1.9


def south_of_city():
    # go south for between 2.2 seconds to 2.24
    return random() * 0.04 + 2.2


def right_to_sailor():
    # go towards sailor for 0.8 to 0.95 seconds
    return random() * 0.15 + 0.8


def paying_attention_break():
    # timer between 0.20 seconds to 0.45 seconds
    return random() * 0.25 + 0.20


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
