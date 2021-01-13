from classes.player import player
from functions.responses import yes_inputs, no_inputs
import curses
import time


def smith():
	screen = curses.initscr()
	screen.clear()
	smith = True
	
	while smith == True:

		cost = 5

		screen.addstr(f'\n\n"Mmh..." The smith grunts.\n"I sell weapons. Swords. The kind that hurt. Only five coins. Need one?"\n\n')
		upgrade = screen.getstr().lower()
		upgrade = upgrade.decode("utf-8")

		if upgrade not in yes_inputs and upgrade not in no_inputs:
			screen.addstr("## Please enter a valid action ##\n\n")
			continue

		if upgrade in yes_inputs:

			if player.gold < cost:
				screen.clear()
				screen.addstr("\n\n## You do not have enough gold ##\n\n")
				smith = False
				screen.refresh()
				screen.clear()
				time.sleep(3)
				break

			if player.sword == True:
				screen.addstr('\n\n"The smith looks at the sword swinging by your side.\n"That one looks fine to me. Nice and sharp. Go break it and then come back if you really wanna buy one."')
				continue

			elif player.gold >= cost and player.sword == False:
				player.gold = player.gold - cost
				screen.addstr("The blacksmith hands you a standard-looking iron sword.")
				player.sword = True
		
		elif upgrade in no_inputs:
			screen.clear()
			screen.addstr('"Come back when you need one. Something will happen sooner or later."')
			smith = False
			time.sleep(1)
			screen.refresh()
			screen.clear()
			time.sleep(3)
			break
