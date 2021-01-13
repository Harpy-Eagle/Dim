from classes.player import player
from village.tavern_sleep import tavern_sleep
from village.tavern_drink import tavern_drink
from dialogue.inn_chat import innkeeper_dialogue, tavern_dialogue
import curses
from functions.responses import leave_inputs, local_chat



if player.region == "Forest":
	innkeeper_chat = ['talk to innkeeper', 'chat with innkeeper', 'talk with innkeeper']

	descr = ("The tavern is bustling with the local folk. They offer drinks for one gold piece and rooms for two gold pieces.")


def tavern():
	tavern = True
	screen = curses.initscr()
	screen.clear()

	while tavern == True:

		if player.first_time == False:
			choice = ("\nOne of the innkeepers asks how they can help you. (Drink/Sleep)\n\n")

		elif player.first_time == True:
			choice = ('\n"Hey!" The innkeeper yells at you as he sees you open the door.\n"Ye got the look of a new folk; so thats what you must be!"\n"This here is my tavern, good enough place; unless you start trouble, that is."\n"We offer rooms to sleep in and ale to drink, feel free to ask for anything when you need it."\n"Ye can also learn a thing or two from the rifraff that comes round these parts; so its a good idea to chat around with yer fellow travelers here as well."\n"Anyway, how can I be of service?"\n\n')

		player.first_time = False

		screen.addstr(descr)
		screen.addstr(choice)

		tavern_choice = screen.getstr().lower()
		tavern_choice = tavern_choice.decode("utf-8")

		if tavern_choice in leave_inputs:
			screen.clear()
			break

		elif tavern_choice != "sleep" and tavern_choice != "drink" and tavern_choice not in leave_inputs and tavern_choice not in innkeeper_chat:
			screen.addstr("\n\n## Please enter a valid action ##\n\n")
			continue

			
		if tavern_choice == "sleep":
			tavern_sleep()

		elif tavern_choice == "drink":
			tavern_drink()

		elif tavern_choice in innkeeper_chat:
			innkeeper_dialogue()

		elif tavern_choice in local_chat:
			tavern_dialogue()


