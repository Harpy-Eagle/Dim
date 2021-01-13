import random
from classes.player import player
from functions.responses import yes_inputs, no_inputs
import curses

def chest(descr,loot):
	screen = curses.initscr()
	locked = True
	while locked == True:
		screen.clear()
		screen.addstr(descr)
		chest = screen.getstr().lower()

		if chest not in yes_inputs and chest not in no_inputs:
			screen.addstr("\n\n## Please enter a valid action ##\n\n")
			continue

		elif chest in yes_inputs:
			unlock = random.randint(1,100)

			if player.lockpicks == True:
				if unlock <= 80:
					gold = loot
					player.gold = player.gold + gold
					screen.addstr(f"You opened the chest with your lockpicks! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
					locked = False
				elif unlock > 80:
					screen.addstr("Unfortunately, you were not able to open the chest")
					locked = False

			elif unlock > 80:
				gold = loot
				player.gold = player.gold + gold
				screen.addstr(f"You opened the chest! You found {gold} gold inside of it!\nYou now have {player.gold} gold.")
				locked = False

			elif unlock <= 80:
				screen.addstr("Unfortunately, you were not able to open the chest")
				locked = False

		elif chest in no_inputs:
			screen.addstr("You leave the chest be, and return to the trail.")
			locked = False
