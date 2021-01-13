import sys
import time
import random
import curses
from encounters.chest import chest
from encounters.battle2 import battle
from classes.player import player
from village.village_choice import village_verston, village_westeroak
from village.tavern import tavern
from village.market import market
from village.church import church
from functions.inventory import inventory
from functions.camp_functions import rest
from functions.responses import yes_inputs, no_inputs, attack_inputs, n_inputs, e_inputs, s_inputs, w_inputs, dir_inputs, vil_inputs, rest_inputs
from functions.text_functions import slow_print, fast_print


def forest2():
	forest_descr = True
	plains_descr = True
	swamp_descr = True
	mental_check_one = True

	while True:
		screen = curses.initscr()
		screen.refresh()

		while player.hp > 0:

			if player.hp > player.maxhp:
				player.hp = player.maxhp


			if player.n_region_count >= 0 and player.n_region_count < 3:
				player.region == "Forest"

				if forest_descr == True:
					screen.refresh()
					screen.addstr("\n\n## You rest for a short while. ##\nYou have been walking today for hours, but you've been traveling the known world for as long as you remember.\nNearby you see a small village, surrounded by the forest you are currently in.\nFar ahead to the north, you see a range of snow-peaked mountains. To the east and west, everlasting forest. To the south, a gloomy swamp.\nMaybe you will stay in this area a while, and see what is has to offer...")
					forest_descr = False
					swamp_descr = True
					plains_descr = True
			
			if player.n_region_count >= 70 and player.n_region_count < 73:
				player.region == "Plains"	

				if plains_descr == True:
					screen.clear()
					screen.addstr("\n##...The trees slowly dissipate around you...##\nFirm, long grass encompasses the rolling hills around you as far as the eye can see\nAnd yet; further north, you can see the peak of a large mountain\nDark storms surround it's peak...\n\n")
					plains_descr == False
					forest_descr = True

			if player.s_region_count >= 60 and player.s_region_count < 63:
				player.region == "Swamp"

				if swamp_descr == True:
					screen.clear()
					screen.addstr("\n##...The ground beneath you grows wet and muddy...###\nCattails and reeds; great willows and vines begin to replace the forest as the sky becomes as dark and muddied as the stagnant water.\nThis swamp will take it's toll on your body...and your mind...\n\n")
					swamp_descr = False
					forest_descr = True

			if player.mentality < 900:
				if mental_check_one == True:
					
					screen.clear()
					screen.refresh()
					screen.addstr("\n\n##You can feel the stress of adventuring getting to you ##\n        ...Constant headaches...\n\n        ...Strange visions...\n")
					time.sleep(5)
					screen.clear()
					mental_check_one = False

			screen.addstr("\n\nWhat do you do?\n\n")
			onward = screen.getstr().lower()
			onward = onward.decode("utf-8")


				

			if onward not in n_inputs and onward not in e_inputs and onward not in s_inputs and onward not in w_inputs and onward != "a valid action" and onward != "valid action" and onward not in vil_inputs and onward != "cry" and onward != "inventory" and onward not in rest_inputs:

				screen.addstr("\n## Please enter a valid action ##\n")
				continue

			if onward == "cry":
				screen.clear()
				screen.addstr("You collapse on the earth and cry for several hours. Whether this helped or hurt, you do not quite know.")
				player.clock = player.clock + 2
				effect = random.choice(["hurt", "heal"])

				if effect == "hurt":
					player.mentality = player.mentality - 5
				elif effect == "heal":
					player.mentality = player.mentality + 5
				break

			if onward == "a valid action" or onward == "valid action":
				screen.addstr("\n## Don't be smart, just play the game ##\n")
				break

			if onward == "inventory":
				inventory()
				break

			if onward in rest_inputs:
				rest()
				break



			if onward in vil_inputs:
				player.village = "Verston"
				player.region_count = 0
				player.n_region_count = 0
				player.e_region_count = 0
				player.s_region_count = 0
				player.w_region_count = 0
				screen.clear()
				screen.refresh()
				
				village_verston()
				
			if onward in n_inputs or e_inputs or s_inputs or w_inputs:
				if player.region == "Plains":
					player.mentality = player.mentality + 1

				elif player.region == "Forest":
					player.mentality = player.mentality - 1

				elif player.region == "Swamp":
					player.mentality = player.mentality - 2

				miles = random.randint(1,3)
				player.clock = player.clock + 1

				if miles == 1:
					mile = "mile"
				else:
					mile = "miles"

				if player.region_count > 1:
					tot_miles = "miles"

				else:
					tot_miles = "mile"




				window = curses.initscr()
				window.clear()



				for i in range(miles + 1):
					num = 1 + i


					if onward in n_inputs:
						player.n_region_count = player.n_region_count + 1

					elif onward in e_inputs:
						player.e_region_count = player.e_region_count + 1
			
					elif onward in s_inputs:
						player.s_region_count = player.s_region_count + 1
							
					elif onward in w_inputs:
						player.w_region_count = player.w_region_count + 1
		



					player.region_count = player.region_count + 1


					n_miles = (f"{player.n_region_count} miles north, ")
					e_miles = (f"{player.e_region_count} miles east, ")
					s_miles = (f"{player.s_region_count} miles south, ")
					w_miles = (f"and {player.w_region_count} miles west.")

					


					window.addstr(f"\nYou walk {num} {mile} in peace. You have walked {player.region_count} {tot_miles} in total. You have walked {n_miles} {e_miles} {s_miles} {w_miles}\n")
			
					time.sleep(1)
					window.refresh()
					window.clear()
					slow_print("...")

					if player.e_region_count == 20:
						player.village = "Westeroak"
						village_westeroak()



				if player.clock == 10:
					if player.region == "Forest":
						screen.clear()
						screen.addstr("\n##...Night falls upon the forest...##\n")

					elif player.region == "Plains":
						screen.clear()
						screen.addstr("\n##...The sun sets on the rolling hills...##")
					player.time = "Night" 

				if player.clock == 16:
					screen.addstr("\n##...Dawn breaks through the leaves, and the night ends. Having not rested, you grow weary...##\n")
					player.time = "Day"
					player.clock = 0
					player.mentality = player.mentality - 30
					player.hp = player.hp - 3

				encounter = random.randint(1,100)

				if encounter < 0:#10

					if player.time == "Night":
						chest("You stumble across a chest in the darkness of the night...It appears to be locked...Do you want to try and unlock it?", random.randint(2,10))

					elif player.time == "Day":
						chest("You found a chest while out adventuring! It appears to be locked...Do you want to try and unlock it?", random.randint(2,10))

				if encounter >= 100 and encounter < 500:
					rest()

				if encounter >= 0:
					battle()

forest2()


