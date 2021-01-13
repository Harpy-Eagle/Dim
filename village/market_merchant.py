from classes.player import player
import random
from functions.responses import yes_inputs, no_inputs, leave_inputs
import curses
import time


def merchant():
	screen = curses.initscr()
	screen.refresh()
	merchant = True

	
	while merchant == True:
		merchant2 = True
		while merchant2 == True:
			num_rations = random.randint(2,8)

			if player.region == "Forest":

				wares = ["lockpicks", "rations"]

				ware = {"lockpicks": True, "ration": num_rations}

			if player.lockpicks == True:
				wares.lockpicks = False

			screen.addstr("The beady-eyed merchant eyes your coin purse greedily. He immediately asks if you'd care to browse his wares.\n\n")
			merchant = screen.getstr().lower()
			merchant = merchant.decode("utf-8")

			if merchant not in yes_inputs and merchant not in no_inputs and merchant not in leave_inputs:
				screen.addstr("## Please enter a valid action ##\n\n")
				continue


			if merchant in yes_inputs:
				merchant3 = True
				while merchant3 == True:
					lockpick_cost = 20
					ration_cost = 1
					screen.addstr("\nThe merchant tells you he currently has " + str(ware.get("ration", 0)) + " "+  wares[1]  + ", " + wares[0] + "\nHe asks what you would care to purchase.\n\n")
					ans = screen.getstr().lower()
					ans = ans.decode("utf-8")

					if ans not in wares and ans not in no_inputs and ans != "nothing" and ans not in leave_inputs:
						screen.addstr('\n\n## Please type in the item you would like to purchase; or type "nothing" ##\n\n')
						continue
					

					if ans == wares[0]:

						if player.gold < lockpick_cost:
							screen.addstr("\n\n## You do not have enough gold to purchase the lockpicks ##\n\n")
							continue

						elif player.gold >= lockpick_cost:
							player.gold = player.gold - cost
							player.lockpicks = True
							screen.addstr(f"\n\nYou bought the {wares[0]}! You now have {player.gold} gold left\n\n")
							break

					elif ans == wares[1]:

						screen.addstr(f"How many {wares[1]} would you like to purchase?\n\n")
						rations_num = screen.getstr().lower()
						rations_num = rations_num.decode("utf-8")
						cost = ration_cost * int(rations_num)

						if player.gold < cost:
							screem.addstr(f"\n\n## You don't have enough gold to purchase the {wares[1]} ##\n\n")
							continue

						if int(rations_num) > num_rations:
							screen.addstr("\n\n## The merchant doesnt have that many in stock ##\n\n")
							continue

						else:

							player.gold = player.gold - cost
							player.rations = player.rations + int(rations_num)
							screen.addstr(f"\n\nYou bought {rations_num} {wares[1]}! You now have {player.gold} gold left\n\n")
							break
							

					elif ans in no_inputs or ans == "nothing" or ans in leave_inputs:
						screen.clear()
						screen.addstr("The merchant asks you to consider returning to purchase something later.")
						merchant = False
						merchant2 = False
						merchant3 = False
						time.sleep(1)
						screen.refresh()
						screen.clear()
						time.sleep(3)
						break

			elif merchant in no_inputs or merchant in leave_inputs:
				screen.clear()
				screen.addstr("The merchant asks you to consider returning to purchase something later.")
				merchant = False
				time.sleep(1)
				screen.refresh()
				screen.clear()
				time.sleep(3)
				break
		