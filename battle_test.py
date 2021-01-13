
import random
import sys
import curses
import time
import re
import select
import threading

attack_inputs = ["hit", "a", "strike", "attack", "stab", "slash", "fight"]

screen = curses.initscr()

def battle_loop():
	enemy = goblin()
	enemy_advantage = False
	battle_loop = True
	while battle_loop == True:

		if player.hp <= 0:

			battle = False
			battle_loop = False
			slow_print("...")
			screen.refresh()
			screen.addstr(f"\n## The goblin knocked you out! ## \n\n")
			screen.refresh()
			break
			sys.exit()

		if enemy_advantage == True:
			screen.addstr(f"\nHaving parried your blow, the goblin counter-attacks quickly!\n")
			enemy_advantage = False
			response_time = 2
		else:
			screen.addstr("\nThe goblin readies its blade, and prepares to strike")
			screen.refresh()
			response_time = 5
		
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


		if user_input in attack_inputs:

			if player.sword_skill <= 10:
				player_dmg = random.choice([1,2,3])

			elif player.sword_skill >10 and player.sword_skill <= 25:
				player_dmg = random.choice([3,4,5])

			if enemy.hp <= 0:

				screen.clear()
				screen.addstr('You stab the goblin and it dies\n\n')
				screen.refresh()
				t.cancel()
				battle = False
				battle_loop = False
				break

			else:
				attack = random.choice([1,2,3])
				if attack == 1:
					t.cancel()
					screen.addstr("\nYou slice at the goblin, but it dodges out of the way just in time.\n")
					continue

				if attack == 2:
					t.cancel()
					screen.addstr("\nThe goblin parries your blow and sets you off balance, opening you up for their own counter attack!\n")
					enemy_advantage = True
					continue

				if attack == 3:
					t.cancel()
					screen.clear()
					screen.addstr("\nYou successfully slice the goblin, opening up a deep gash\n")
					enemy.hp = enemy.hp - player_dmg
					continue

		elif run == True:
			screen.clear()
			screen.addstr(f"\n## You run away from the goblin ##\n")
			screen.refresh()
			battle = False
			t.cancel()
			break

		elif block == True:
			t.cancel()
			screen.addstr("\n## You parry the enemies attack ##\n\n")
			screen.refresh()
			continue

		else:
			t.cancel()
			screen.addstr("I dont understand")
			continue


def slow_print(str):
	for letter in str:
		sys.stdout.write(letter)
		sys.stdout.flush()
		time.sleep(1)

def time_ran_out():
	enemy = goblin()
	screen.clear()
	enemy.dmg = enemy.dmg + random.choice([-1, 0, 1]) - player.ac
	screen.refresh()
	screen.addstr(f'\nThe goblin nicks you with their blade!\n')
	screen.refresh()
	player.hp = player.hp - enemy.dmg
	time.sleep(3)
	battle_loop()


class player:
	hp = 10
	sword_skill = 1

class goblin:
	hp = 6
	dmg = 3

def battle():
	enemy = goblin()
	screen = curses.initscr()
	screen.clear()
	battle = True
	enemy_advantage = False


	while battle == True:

		screen.addstr("You encounter a goblin!\n")

		enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])


		while enemy.hp > 0 or player.hp > 0:

			screen.refresh()
			screen.clear()
			slow_print("...")
			battle_loop()	


battle()
