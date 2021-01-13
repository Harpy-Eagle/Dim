import curses
from functions.responses import talk_inputs, yes_inputs, no_inputs
from classes.player import player
import random
import re

decide = random.choice([1,2])

if decide == 1:
	descr = '"Thrust! Turn! Pull! Thats it men!" The captain yells at the soldiers training.\n He sees you walking over.\n"Aye, whaddya want?" He asks.'

elif decide == 2:
	descr = '"Take a break now, men. Youve done well. Head inside and grab some food!"\n"The gods know we need our strength..."\nHe turns to you and makes a gesture as if to bid you to speak'


def training_grounds():
	training_ground = True
	screen = curses.initscr()
	screen.clear()
	screen.addstr(descr + '\nYou may be able to learn a thing or two about the blade from him...Maybe even join his group of soldiers. Or, you could always just chat.\n\nWhat do you do?\n\n')
	
	while training_ground == True:
		ans = screen.getstr().lower()
		ans = ans.decode("utf-8")
		dialogue_regex = re.compile('join')
		mo = dialogue_regex.search(ans)
		if mo == None:
			mo = False
		else:
			mo = True

		if ans in talk_inputs or ans == ["talk with captain", "chat with captain"]:
			screen.addstr('"Well theres not a whole lot to talk about..."\nIm Threbek; of Fakralth, out west by a few hundred miles. Came to find myself in command of this motley crew..."\n"but thats a story for perhaps another time, eh?"')
			screen.addstr('"So...Anything else on yer mind?"')
			continue

		if ans in ["train", "i want to train", "can i train", "id like to train", "training", "train with"]:
			screen.addstr('"Oh ho! Another swordsmen here...Sure, I can train you.\n"Its good to understand that thing yer swinging around huh?"\n"But theres a price; bah, theres a price to everything. Never expect anything for free."')

			if player.sword_skill < 10:
				price = 10

			elif player.sword_skill > 10 and player.sword_skill < 25:
				price = 15


			screen.addstr(f'\n\n"Thatll be {price} gold for now. Whaddya say?"\n\n')
			ans2 = screen.getstr().lower()
			ans2 = ans.decode("utf-8")

			if ans2 in yes_inputs:
				if player.gold >= price:

					player.gold = player.gold - price
					player.sword_skill = player.sword_skill + random.choice([1,2,3])
					screen.clear()
					screen.addstr("You train with captain Threbek for several hours. He is a master at his art, and you learn much from him.")
				else:
					screen.addstr("## You do not have enough gold ##\n\n")
					continue

			elif ans2 in no_inputs:
				screen.addstr('"Well, you know where to find me if you change yer mind."')
				continue

		elif mo == True:
			screen.addstr('\nThrebek pauses for a moment\n"Well, I cant gurantee that you can join us; at least; not right now. Youd have to join us on our journey back to the land we hail from--Fakralth, and then we would see."\n"But its a long journey; took us over a month to get here in the first place."\n\n')
			screen.addstr('"So...Anything else on yer mind?"')
		




