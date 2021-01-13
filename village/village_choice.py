from classes.player import player
import curses
from village.tavern import tavern
from village.market import market
from village.church import church
from functions.responses import look_village_inputs
from village.training_grounds import training_grounds


verst_descr = ("\nYou walk to the local village to stop at and rest for a while.\nThe local tavern costs 2 gold pieces to stay the night in,\nor you could go to the local marketplace and browse the various shops.\nYou can also see the steeple of a local church nearby, with it's high towers easily being the most noticeable object in the near vicinity.")

wester_descr = ("\nAs you walk, you can see a small village ahead of you. You walk into the village, and find yourself in what seems to be the town square. You see no one here.\nIt may be a good idea to look around...")	

def village_verston():
	screen = curses.initscr()
	screen.refresh()
	vill = True
	while vill == True:

		#screen.addstr(f"\n{player.hp} is your current health. {player.maxhp} is your maximum health currently. {player.gold} is your current gold")
		screen.addstr(verst_descr)
		screen.addstr("\n\nWhere will you go?\n\n")
		vil_choice = screen.getstr().lower()
		vil_choice = vil_choice.decode("utf-8")

		if vil_choice != "church" and vil_choice !="market" and vil_choice != "tavern" and vil_choice != "inventory" and vil_choice != "leave" and vil_choice != "grounds" and vil_choice not in look_village_inputs:
			screen.addstr("\n\n## Please enter a valid action ##\n\n")
			screen.clear()

		if vil_choice == "leave":
			screen.clear()
			screen.addstr("You walk to the outskirts of the village.")
			vill = False
			break

		if vil_choice == "grounds":
			training_grounds()

		if vil_choice in look_village_inputs:
			screen.clear()
			screen.addstr("You walk around the village. While quaint; it is of decent size. The people here look generally well-fed and happy.\nCrime rates are low, and the people tend to help oneanother out.\nThe surrounding land is farmed for grains. You continue walking and discover what seems to be a small dirt training ground...soldiers in chain armor thrust and stab on the count of three by what appears to be their captain...\n\nWhat do you do?")
			continue

		if vil_choice == "inventory":
			screen.clear()
			inventory()


		elif vil_choice == "tavern":
			screen.clear()
			tavern()


		elif vil_choice == "market":
			screen.clear()
			market("The marketplace is booming with activity. The smell of milled grain and spices surrounds you. You can hear\nmetal-workers and craftsmen beating their hammers on their anvils.", "\nWhere will you go? (Armorer/Smith/Merchant)\n\n")

		elif vil_choice == "church":
			screen.clear()
			church()


def village_westeroak():
	screen = curses.initscr()
	screen.refresh()
	vill = True

	while vill == True:
		screen.addstr(wester_descr)
		screen.addstr("\n\nWhere will you go?\n\n")
		vil_choice = screen.getstr().lower()
		vil_choice = vil_choice.decode("utf-8")

