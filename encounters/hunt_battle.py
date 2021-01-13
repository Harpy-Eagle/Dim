from classes.enemies import Goblin, Spider, Orc, Thief
import random
from classes.player import player
from functions.inventory import inventory
from functions.responses import yes_inputs, no_inputs, attack_inputs

def HuntBattle():
	battle = True

	while battle == True:

		if player.upg == 0:
			enemy_class = random.choice([Goblin, Spider])

		elif player.upg == 1 or player.upg == 2:
			enemy_class = random.choice([Goblin, Spider, Orc])

		elif player.upg > 2:
			enemy_class = random.choice([Goblin, Spider, Orc, Thief])

		enemy = enemy_class()
		enemy_name = enemy_class.__name__

		print(f"You encounter a {enemy_name}!")

		enemy.hp = enemy.hp + random.choice([-2, -1, 0, 1, 2])

		while enemy.hp > 0 or player.hp > 0:
			print("What do you do?")
			attack = input().lower()

			if attack == "inventory":
				inventory()
			

			if attack not in attack_inputs and attack != "inventory":
				print("Please enter a valid action")
				continue

			if attack in attack_inputs:
				enemy.hp = enemy.hp - player.dmg
				print(f"You dealt {player.dmg} damage to the {enemy_name}!")

			if enemy.hp <= 0:
				print("The enemy is slain!")
				battle = False

				loot = random.randint(1,100)

				if loot >= 0:
					print("Whats this...? You found a health potion on the corpse! You place it in your backpack")
					player.potions = player.potions + 1
				else:
					gold = random.randint(1, 4)
					player.gold = player.gold + gold

					print(f"Whats this..? You found {gold} gold on the corpse!\nYou now have {player.gold} gold!")
				break

			if attack in attack_inputs:
				enemy.dmg = enemy.dmg + random.choice([0, 1]) - player.ac
				player.hp = player.hp - enemy.dmg

				if enemy.dmg > 0:
					print(f"The {enemy_name} hits back! it deals {enemy.dmg} damage to you!")
				elif enemy.dmg <= 0:
					print(f"The {enemy_name}'s blow was completely deflected by your {player.armor}!")
			if player.hp <= 0:

				print(f"The {enemy_name} knocked you out!\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
				player.gold = 0
				print(f"You now have {player.gold} gold")
				player.hp = 6
				battle = False
				break