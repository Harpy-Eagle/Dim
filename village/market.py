from classes.player import player
from village.market_armorer import armory
from village.market_smith import smith
from village.market_merchant import merchant
import curses

def market(descr, choice):
	screen = curses.initscr()
	market = True
	while market == True:

		screen.addstr(descr)
		screen.addstr(choice)

		market_choice = screen.getstr().lower()
		market_choice = market_choice.decode("utf-8")

		if market_choice == "leave":
			market = False

		if market_choice == "armory" or market_choice == "armorer":
			screen.clear()
			armory("The Armory is stocked with all sorts of armors and shields.", "\nThe smith procuring these wares asks if you'd care to examine any.\n\n")


		elif market_choice == "smith" or market == "blacksmith":
			screen.clear()
			smith()


		elif market_choice == "merchant":
			screen.clear()
			merchant()

			


