from classes.player import player
import curses

def tavern_sleep():


	screen = curses.initscr()
	screen.clear()

	if player.gold < 2:
		screen.addstr("\n\n## You do not have enough gold to sleep at the tavern ##\n\n")
		tavern = False

	elif player.gold >= 2:
		cost = 2
		player.gold = player.gold - cost
		screen.addstr(f"You stay the night at the Tavern and rest.\nYou now have {player.gold} gold left in your pockets, and your health returns to {player.maxhp} health.")
		player.hp = player.maxhp
		tavern = False

