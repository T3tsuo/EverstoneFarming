import time
import pydirectinput

def run():
  input("Hit enter to toggle run and tab into game immediately: ")
  # time to switch to game
  time.sleep(2)
  # toggle run
  pydirectinput.press("x")
