import sys
import os

import grab_items
import heal_return

# this program grabs items and then fly's to go restore pokemon pp

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

try:
    # try to grab input from command line
    x = int(sys.argv[1])
except IndexError:
    # else then ask for amount of times user can use sweet scent before going to pokecenter
    x = int(input("Number of times to use sweet scent: "))
while True:
    grab_items.run(x)
    heal_return.run()
