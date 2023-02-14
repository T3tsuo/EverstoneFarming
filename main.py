import sys
import os
import time

import grab_items
import heal_return

# this program grabs items and then fly's to go restore pokemon pp

os.environ['REQUESTS_CA_BUNDLE'] = "certifi/cacert.pem"

try:
    # try to grab input from command line for amount of sweet scent
    x = int(sys.argv[1])
    # try to grab how many seconds to run the code
    run_code_time = int(sys.argv[2])
except IndexError:
    # else then ask for amount of times user can use sweet scent before going to pokecenter
    x = int(input("Number of times to use sweet scent: "))
    # ask how long the code should run in seconds
    run_code_time = int(input("How long (in seconds) do you want the code to run for: "))
# this is when the code should stop
end_time = time.time() + run_code_time
# while we have not reached the end time, keep on going
while end_time > time.time():
    heal_return.run()
    grab_items.run(x)
    if end_time > time.time():
        print(str(round(time.time() / end_time * 100)) + "% Done")
    else:
        print("100% Done")
