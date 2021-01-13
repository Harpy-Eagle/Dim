from classes.player import player
from functions.actions import consume_actions, actions, pray_actions, bury_actions
from functions.items import health_potion
from functions.player_functions import bones_bury, potion_bury
import sys
import curses
import time

items = [""]

def inventory():
	inventory = True
	while inventory == True:
		screen = curses.initscr()

		screen.clear()
		screen.addstr("#" * 40)
		screen.addstr("\n    	     INVENTORY    \n")
		screen.addstr(f"Current health: {player.hp} Max health: {player.maxhp}")
		screen.addstr(f"\n\nCurrent gold: {player.gold}")
		screen.addstr("\n\nSword")
		screen.addstr(f"\n\nArmor: {player.armor}")
		if player.potions > 0:
			items.extend(["health potion", "potion"])
			screen.addstr(f"\n\n{player.potions} Health Potions")
		if player.lockpicks == True:
			screen.addstr("\n\nLockpicks")
		if player.rations > 0:
			screen.addstr(f"\n\n{player.rations} days worth of rations")
		screen.addstr("\n#" + "#" * 40)

		screen.addstr("\n\n")

		action = screen.getstr().lower()
		action = action.decode("utf-8")

		if action == "back":
			inventory = False
			screen.clear()

		elif action in actions:
			screen.addstr(f"\n\nWhat would you like to {action}?\n\n")
			ingest = screen.getstr().lower()
			ingest = ingest.decode("utf-8")
			if ingest not in items:
				screen.addstr("\n\nYou do not have any of that")
				continue
			elif ingest in items:
				if action in consume_actions:
					health_potion()
					screen.addstr(f"\n\nYou have consumed the {ingest}")
					time.sleep(3)
					screen.clear()
				elif action in bury_actions:
					if ingest == "bones":
						bones_bury()
						screen.addstr(f"You have buried the {ingest}")

					elif ingest == "health potion" or ingest == "potion":
						potion_bury()
						screen.addstr(f"You have buried the {ingest}")
				elif action in pray_actions:
					screen.addstr(f"You have prayed over the {ingest}")
					screen.clear()
				break


