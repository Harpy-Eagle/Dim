from classes.player import player
from functions.responses import yes_inputs, no_inputs
import curses
import time

def church():
	screen = curses.initscr()
	screen.refresh()

	screen.addstr('You enter the modest village church, with a few small wooden benches and stools scattered around.\nYou see an elderly man in dark robes kneeling before an altar to a god unbeknownst to you.\nWithout turning around, he asks what you seek here.\n"Health?" He asks.\n\n')

	church = True
	while church == True:

		if player.hpupg == 2:
			screen.addstr("The church is abandoned. The floor is covered in dust, the windows boarded up, and there is no evidence of anyone having been there in years.")
			church = False


		else:			
			church_choice = screen.getstr().lower()
			church_choice = church_choice.decode("utf-8")

			if player.hpupg == 0:
				cost = 15
			elif player.hpupg == 1:
				cost = 50

			if church_choice not in yes_inputs and church_choice not in no_inputs:
				screen.addstr('"What was that?"\n\n')
				continue

			if church_choice in yes_inputs:
				screen.addstr(f'"I can aid you in that, with powers deemed unnatural by some."\n"But this does not come without a price. {cost} gold will do for now."\n"Do you agree to this?"\n\n')
				church_choice_2 = screen.getstr().lower()
				church_choice_2 = church_choice_2.decode("utf-8")

				if church_choice_2 not in yes_inputs and church_choice_2 not in no_inputs:
					screen.addstr('"What was that?"\n\n')
					continue

				if church_choice_2 in yes_inputs:
						if player.gold < cost:
							screen.clear()
							screen.addstr('"My my my... not enough gold..."')
							church = False
							time.sleep(1)
							screen.refresh()
							screen.clear()
							time.sleep(3)



						elif player.gold >= cost:                                                                                       
							player.gold = player.gold - cost
							player.maxhp = player.maxhp + 5
							player.hpupg = player.hpupg + 1
							player.mentality = player.mentality - 75
							screen.addstr(f'"Mmhm...There you are. Go now; and reap the benefits of your increased fortitude". You now have {player.gold} gold and {player.maxhp} maximum health')
							church = False
							time.sleep(1)
							screen.refresh()
							screen.clear()
							time.sleep(3)




				elif church_choice_2 in no_inputs:
					screen.clear()
					screen.addstr('"Then please, leave me to my work."')
					church = False
					time.sleep(1)
					screen.refresh()
					screen.clear()
					time.sleep(3)



			elif church_choice in no_inputs:
				screen.clear()
				screen.addstr('"Then please, leave me to my work."')
				church = False
				time.sleep(1)
				screen.refresh()
				screen.clear()
				time.sleep(3)

