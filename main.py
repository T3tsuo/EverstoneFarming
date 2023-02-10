import grab_items

x = int(input("Number of times to use sweet scent: "))
# switch to second window which should be the game
grab_items.switch_tabs()
grab_items.run(x)
