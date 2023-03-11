import sys
import time

import grab_items
import heal_return
import time_to_seconds

try:
    # try to grab input from command line for amount of sweet scent
    x = int(sys.argv[1])
    # try to grab how many seconds to run the code
    run_code_time = time_to_seconds.sum_seconds(sys.argv[2])
except IndexError:
    # else then ask for amount of times user can use sweet scent before going to pokecenter
    x = int(input("Number of times to use sweet scent: "))
    # ask how long the code should run
    print("Time format: hours.minutes\n2.35 = 2 hours and 35 minutes")
    run_code_time = time_to_seconds.sum_seconds(input("How long do you want the code to run for: "))
print("Running for " + str(run_code_time) + " seconds")
time.sleep(2)
# this is when the code started to run
start_time = time.time()
# this is when the code should stop
end_time = time.time() + run_code_time
# while we have not reached the end time, keep on going
while end_time > time.time():
    heal_return.run()
    grab_items.run(x)
    if end_time > time.time():
        print(str(round((time.time() - start_time) / (end_time - start_time) * 100)) + "% Done")
    else:
        print("100% Done")
