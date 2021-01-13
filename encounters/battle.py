from classes.enemies import Goblin, Spider, Orc, Thief
import random
from classes.player import player
from functions.inventory import inventory
from functions.responses import yes_inputs, no_inputs, attack_inputs
import sys
import curses
import time
from functions.text_functions import slow_print

def battle():
	screen = curses.initscr()
	screen.clear()
	battle = True

	while battle == True:

		if player.time == "Night":
			enemy_class = random.choice([Goblin, Orc, Thief])

		if player.upg == 0:
			enemy_class = random.choice([Goblin, Spider])

		elif player.upg == 1 or player.upg == 2:
			enemy_class = random.choice([Goblin, Spider, Orc])

		elif player.upg > 2:
			enemy_class = random.choice([Goblin, Spider, Orc, Thief])

		enemy = enemy_class()
		enemy_name = enemy_class.__name__

		screen.addstr(f"You encounter a {enemy_name}!")

		enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2]) 


		while enemy.hp > 0 or player.hp > 0:
			screen.addstr("\n\nWhat do you do?\n\n")
			attack = screen.getstr().lower()
			attack = attack.decode("utf-8")

			if attack == "inventory":
				inventory()
			

			if attack not in attack_inputs and attack != "inventory":
				screen.addstr("\n\n## Please enter a valid action ##\n\n")
				continue

			if attack in attack_inputs:
				if player.sword_skill <= 10:
					player_dmg = random.choice([1,2,3])

				elif player.sword_skill >10 and player.sword_skill <= 25:
					player_dmg = random.choice([2,3,4,5])

				enemy.hp = enemy.hp - player_dmg
				screen.addstr(f"You dealt {player_dmg} damage to the {enemy_name}!\n")

			if enemy.hp <= 0:
				screen.clear()

				if enemy.race == "Human":
					screen.addstr(f"The {enemy_name} cowers on the floor, bleeding...He begs you to spare him. He swears a life of purity if you do...\nWhat do you do?")
					ans = screen.getstr().lower()
					ans = ans.decode("utf-8")

					if ans == "spare" or ans == "live":
						screen.addstr(f"You spare the {enemy_name}. and walk onwards.")
						spare = True
						battle = False
						break

					elif ans == "kill" or ans in attack_inputs:
						screen.addstr(f"You stab the {enemy_name}, ending their pleas for life forever.")
						player.mentality = player.mentality -30
						spare = False
						battle = False
				else:

					screen.addstr("\n\n## The enemy is slain ##\n\n")
					screen.refresh()
					spare = False
					battle = False

				if spare == False:

					loot = random.randint(1,100)
					screen.refresh()
					slow_print("...")


					if loot >= 90:
						screen.refresh()
						screen.addstr("\n\nWhats this...? You found a health potion on the corpse! You place it in your backpack")
						player.potions = player.potions + 1
						break
						
					else:
						gold = random.randint(1, 4)
						player.gold = player.gold + gold
						screen.refresh()
						screen.addstr(f"\n\nWhats this..? You found {gold} gold on the corpse!\nYou now have {player.gold} gold!")
						break
	

			if attack in attack_inputs:
				enemy.dmg = enemy.dmg + random.choice([0, 1]) - player.ac
				player.hp = player.hp - enemy.dmg

				if enemy.dmg > 0:
					screen.addstr(f"The {enemy_name} hits back! it deals {enemy.dmg} damage to you!")
				elif enemy.dmg <= 0:
					screen.addstr(f"The {enemy_name}'s blow was completely deflected by your {player.armor}!")
			
			if player.hp <= 0:

				battle = False
				screen.clear()
				screen.addstr(f"\n\n## The {enemy_name} knocked you out! ## \n\n")
				screen.refresh()
				slow_print("...")

				encounter = random.choice([1, 2])

				if encounter == 1:
					screen.refresh()
					screen.addstr("\n\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
					player.gold = 0
					screen.addstr(f"\n\nYou now have {player.gold} gold")
					player.hp = 6
					screen.refresh()
					break


				elif encounter == 2:
					screen.refresh()
					screen.addstr("...You open your eyes to discover wooden walls and a roaring fireplace. A man sits in front of the fire, smoking his pipe.\nYou are resting on an assortment of pelts, on a small bed. The man says nothing, but nods his head towards you and opens the door.\nYou walk out, somewhat confused but overall healed.")
					player.hp = player.maxhp
					screen.refresh()
					time.sleep(6)
					break
