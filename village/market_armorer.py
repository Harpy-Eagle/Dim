from classes.player import player 
from functions.responses import yes_inputs, no_inputs, leave_inputs
import curses
import time

def armory(descr, choice):
	screen = curses.initscr()
	screen.clear()
	armory = True

	if player.region == "Forest":

		wares = ["Leather armor", "Chainmail armor"]
		price_0 = 10
		price_1 = 25

		ware = {"leather_armor": True, "chain_armor": False}


	while armory == True:
		screen.addstr(descr)
		screen.addstr(choice)
		armory_choice = screen.getstr().lower()
		armory_choice = armory_choice.decode("utf-8")

		if armory_choice not in yes_inputs and armory_choice not in no_inputs:
			screen.addstr("\n\n## Please enter a valid action ##\n\n")
			continue

		if armory_choice in leave_inputs:
			break

		if armory_choice in yes_inputs:
			screen.addstr("The smith says he currently has " + ", ".join(wares) + " in stock. Would you care to purchase one?\n\n")
			ans2 = screen.getstr().lower()
			ans2 = ans2.decode("utf-8")

			if ans2 in yes_inputs:
				screen.addstr(f"Which armor would you care to buy? The {wares[0]} costs {price_0} and the {wares[1]} costs {price_1}.\n{wares[0]} or {wares[1]}?\n\n")
				ans3 = screen.getstr().lower()
				ans3 = ans3.decode("utf-8")

				if ans3 =="leather" or ans3 == "leather armor":
					if player.gold < price_0:
						screen.clear()
						screen.addstr("## ou do not have enough gold to purchase the armor ##\n\n")
						screen.refresh()
						screen.clear()
						time.sleep(3)
						continue

					elif player.gold >= leather_price:
						player.gold = player.gold - price_0
						screen.clear()
						screen.addstr(f"The smith hands you the leather armor. You feel agile!\nYou now have {player.gold} gold.")
						player.dmg = player.dmg + 1
						wares.remove("Leather armor")
						player.armor = "Leather armor"
						screen.refresh()
						screen.clear()
						time.sleep(3)
						continue

				if ans3 =="chain":
					if player.gold < price_1:
						screen.clear()
						screen.addstr("\n\n## You do not have enough gold to purchase the armor ##\n\n")
						screen.refresh()
						screen.clear()
						time.sleep(3)
						continue

					elif player.gold >= price_1:
						player.gold = player.gold - price_1
						screen.clear()
						screen.addstr(f"The smith hands you the chain armor. Your armor level has increased!\nYou now have {player.gold} gold.")
						player.ac = 1
						player.upg = player.upg + 1
						player.armor = "Chain armor"
						screen.refresh()
						screen.clear()
						time.sleep(3)
						continue

			elif ans2 in no_inputs:	
				screen.clear()
				screen.addstr("The smith nods and asks you to come back if you change your mind.")
				screen.refresh()
				screen.clear()
				time.sleep(3)
				armory = False
				break

		elif armory_choice in no_inputs:
			screen.clear()
			screen.addstr("The smith nods and asks you to come back if you change your mind.")
			screen.refresh()
			screen.clear()
			time.sleep(3)
			armory = False
			break

