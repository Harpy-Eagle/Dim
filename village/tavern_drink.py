from classes.player import player
from functions.responses import attack_inputs
from classes.enemies import Goblin
import random
import curses

def tavern_drink():

	screen = curses.initscr()
	screen.clear()

	if player.gold < 1:
		screen.addstr("\n\n## You do not have enough gold to buy a drink ##\n\n")
		drink = False



	elif player.gold >= 1:
		cost = 1
		player.gold = player.gold - cost
		screen.addstr(f"You stop at the bar and grab yourself a mug of grog to drink.\nYou now have {player.gold} gold left in your pockets.")

		drink = True
		while drink == True:
			drinking_event = random.randint(1,100)

			if drinking_event > 10 and drinking_event <= 30:
				screen.addstr(f"The grog is especially good tonight. Warmth fills your veins and you feel renewed with energy and vigor.")
				player.hp = player.hp + 5
				screen.addstr(f"{player.hp} is your current health. {player.maxhp} is your maximum health currently.")
				drink = False

			elif drinking_event >30 and drinking_event <=80:

				if player.gold >= 5:
					bad_bet = random.randint(1,5)
				elif player.gold >= 2 and player.gold < 5:
					bad_bet = random.randint(1,2)
				elif player. gold < 2:
					continue
				player.gold = player.gold - bad_bet
				screen.addstr(f"Drinking was not such a good idea after all...while drunk, someone snatched {bad_bet} gold from your pockets...\nYou now have only {player.gold} gold left.")
				drink = False

			elif drinking_event >80:
				good_bet= random.randint(1,5)
				player.gold = player.gold + good_bet
				screen.addstr(f"The night was filled with laughter and many bets! You won multiple bets, totaling in {good_bet} gold.\nYou now have {player.gold} gold!")
				drink = False



			elif drinking_event <= 10:
				battle = True
				while battle == True:

					print(f"While drunk, a tavern wench convinces you to join her in her room upstairs.\nWhen alone, she proceeds to demand all your gold and takes out a dagger.\nIt's no wench--it's a goblin in disguise!")
					enemy = Goblin()
					while enemy.hp > 0 or player.hp > 0:
						screen.addstr("What do you do?\n\n")
						user = screen.getstr().lower()
						user = user.decode("utf-8")

						if user not in attack_inputs:
							screen.addstr("Please enter a valid action")
							continue

						if user in attack_inputs:
							enemy.hp = enemy.hp - player.dmg
							screen.addstr(f"You dealt {player.dmg} damage to the goblin wench!")

						if enemy.hp <= 0:
							screen.addstr("The enemy is slain!")

							gold = random.randint(2,8)
							player.gold = player.gold + gold

							screen.addstr(f"Whats this..? You found {gold} gold on the corpse!")
							battle = False
							drink = False
							break

						if user == "a":
							player.hp = player.hp - enemy.dmg
							screen.addstr(f"The goblin wench strikes back! it deals {enemy.dmg} damage to you!")

						if player.hp <= 0:

							screen.addstr(f"The wench knocked you out!\nYou wake up several hours later, and discover that while you were out someone stole your gold...")
							player.gold = 0
							screen.addstr(f"You now have {player.gold} gold")
							player.hp = 5
							battle = False
							drink = False
							break