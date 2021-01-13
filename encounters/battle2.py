from classes.enemies import Goblin, Spider, Orc, Thief
import random
from classes.player import player
from functions.inventory import inventory
from functions.responses import yes_inputs, no_inputs, attack_inputs
import sys
import curses
import time
from functions.text_functions import slow_print
import re
import select
import threading


attack_inputs = ["hit", "a", "strike", "attack", "stab", "slash", "fight"]

screen = curses.initscr()
ex = False

def battle():
	screen = curses.initscr()
	screen.clear()
	battle = True
	enemy_advantage = False


	while battle == True:
		global enemy_class
		global enemy_name

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

		screen.addstr(f"You encounter a {enemy_name}!\n")

		enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

		while enemy.hp > 0 or player.hp > 0:

			if ex == True:
				return

			screen.refresh()
			screen.clear()
			slow_print("...")
			battle_loop()


def time_ran_out():
	enemy = enemy_class()
	screen.clear()
	enemy.dmg = enemy.dmg + random.choice([-1, 0, 1]) - player.ac
	screen.refresh()
	screen.addstr(f'\nThe {enemy_name} nicks you with their blade!\n')
	screen.refresh()
	player.hp = player.hp - enemy.dmg
	time.sleep(3)
	battle_loop()	



def battle_loop():
	enemy = enemy_class()
	enemy_advantage = False
	battle_loop = True
	while battle_loop == True:
		if player.hp <= 0:

			global ex
			ex = True
			enemy.hp == 0
			slow_print("...")
			screen.refresh()
			screen.clear()
			screen.addstr(f"\n## The {enemy_name} knocked you out! ## \n\n")
			screen.refresh()
			return

		if enemy_advantage == True:
			screen.addstr(f"\nHaving parried your blow, the {enemy_name} counter-attacks quickly!\n")
			enemy_advantage = False
			response_time = 2
		else:
			screen.addstr(f"\nThe {enemy_name} readies its blade, and prepares to strike")
			screen.refresh()
			response_time = 5

		if enemy.hp > 0:
		
			screen.refresh()
			slow_print("...")
			screen.addstr("\n\n")
			screen.clear()
			screen.refresh()
			screen.addstr("\nWhat do you do?\n\n")
			screen.refresh()

			t = threading.Timer(response_time, time_ran_out)
			t.start()

			user_input = screen.getstr().lower()
			user_input = user_input.decode("utf-8")

			run_regex = re.compile(r'run')
			run = run_regex.search(user_input)
			if run == None:
				run = False
			else:
				run = True

			block_regex = re.compile(r'block|guard')
			block = block_regex.search(user_input)
			if block == None:
				block = False
			else:
				block = True

			if player.hp <= 0:
				battle_loop()

			if run == True:
				ex = True
				t.cancel()
				enemy.hp == 0
				screen.clear()
				screen.addstr(f"\n## You run away from the {enemy_name} ##\n")
				screen.refresh()
				return

			if user_input in attack_inputs:

				if player.sword_skill <= 10:
					player_dmg = random.choice([1,2,3])

				elif player.sword_skill >10 and player.sword_skill <= 25:
					player_dmg = random.choice([3,4,5])

				if enemy.hp <= 0:

					screen.clear()
					screen.addstr(f'You stab the {enemy_name} and it dies\n\n')
					screen.refresh()
					t.cancel()
					battle = False
					battle_loop = False
					break

				else:
					attack = random.choice([1,2,3])
					if attack == 1:
						t.cancel()
						screen.addstr(f"\nYou slice at the {enemy_name}, but it dodges out of the way just in time.\n")
						continue

					if attack == 2:
						t.cancel()
						screen.addstr(f"\nThe {enemy_name} parries your blow and sets you off balance, opening you up for their own counter attack!\n")
						enemy_advantage = True
						continue

					if attack == 3:
						t.cancel()
						screen.clear()
						screen.addstr(f"\nYou successfully slice the {enemy_name}, opening up a deep gash\n")
						enemy.hp = enemy.hp - player_dmg
						continue


			elif block == True:
				t.cancel()
				screen.addstr("\n## You parry the enemies attack ##\n\n")
				screen.refresh()
				continue

			if block == False and run == False and user_input not in attack_inputs:
				t.cancel()
				screen.addstr("I dont understand")
				screen.refresh()
				continue

			else:
				exit()
