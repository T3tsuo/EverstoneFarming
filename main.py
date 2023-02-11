import grab_items
import heal_return

# this program grabs items and then fly's to go restore pokemon pp

x = int(input("Number of times to use sweet scent: "))
# switch to second window which should be the game
grab_items.switch_tabs()
while True:
    grab_items.run(x)
    heal_return.run()
