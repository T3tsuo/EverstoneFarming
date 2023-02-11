import grab_items
import heal_return

# this program grabs items and then fly's to go restore pokemon pp

'''
Start at PokeCenter in Canalave City

first pokemon has frisk ability 
second pokemon (Quagsire) has thief in first slot and surf in second slot
pokemon with sweet scent anywhere
bike in 1st key slot, sweet scent in fourth key slot, fly in 5th key slot

best if as many pokemons as you can uses exp. shares to clear battle logs quicker
by gaining exp so program doesn't detect 

make game the second window so the program will switch to it

make battle log as minimized as possible and lock the chat
set: window size 765 x 534 (2 battle logs)
you can change this in the main directory of pokemmo:
PokeMMO/config/main.properties client.graphics.height=534
PokeMMO/config/main.properties client.graphics.width=765
'''

x = int(input("Number of times to use sweet scent: "))
# switch to second window which should be the game
grab_items.switch_tabs()
while True:
    grab_items.run(x)
    heal_return.run()
