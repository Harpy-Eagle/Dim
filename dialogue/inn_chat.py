import curses
from functions.responses import leave_inputs, dialogue_direction_inputs
import re


def innkeeper_dialogue():
	screen = curses.initscr()
	screen.clear()
	screen.addstr('"Whats on your mind?" The innkeeper asks.\n"Im not of the very knowledgable type, but I know my way around. You tend to pick up things here and there from those who wander in here, although whether it be true or not, I cannot say..."\n\n')
	dialogue = True 
	while dialogue == True:

		ans = screen.getstr().lower()
		ans = ans.decode("utf-8")
		dialogue_regex = re.compile('directions')
		mo = dialogue_regex.search(ans)
		if mo == None:
			mo = False
		else:
			mo = True

		if ans not in leave_inputs and ans not in (['goodbye', 'exit dialogue', 'nevermind', 'nothing', 'thank you']) and ans not in dialogue_direction_inputs and mo == False:
			screen.addstr('"Sorry, come again?"')
			continue

		if ans in leave_inputs or ans in (['goodbye', 'exit dialogue', 'nevermind', 'nothing', 'thank you']):
			screen.clear()
			screen.addstr('"Dunno why youre asking all these questions...It can get you into trouble, yknow..."\n\n')
			break

		elif ans in dialogue_direction_inputs or mo == True:
			screen.addstr('"Sure, I can give ye the local lay of the land."\n"To the north, say, oh, five or so days north, the forest here opens up and turns into a great wide plains. Grass for miles there. Further I know there be some mountains, although I cant say I know much else besides that."\n"West and east of here is forest for a long, long time. I know it changes scenery eventually, though I cant say when."\n"Theres another village, about a three day hike east from here, smaller vilalge; quite quaint. But the people there are...stranger. Somethings in the air over there."\n"And then, maybe four days or so south, youll find yourself in Mardok; and the swamp it encompasses. Ye dont wanna go there. People go, and never come back. Its stinks of decay and evil..."\n\n')
			screen.addstr('"You know, it may not be a bad idea to walk around the village too, its a decent size; never know what you may not know is here..."\n\n')

def tavern_dialogue():
	screen = curses.initscr()
	screen.clear()
	num = 1

	if num == 1:
		dialogue = True 
		while dialogue == True:

			screen.addstr('You walk up to a group of cheering tavern-goers. They sit around the table chugging large mugs of ale and laughing\nOne of them notices you...\n"Oi! What is it then; speak up!"\n\n')
			ans = screen.getstr().lower()
			ans = ans.decode("utf-8")

			if ans in leave_inputs or ans in (['goodbye', 'exit dialogue', 'nevermind', 'nothing', 'thank you']):
				screen.clear()
				screen.addstr('"Ok then..."\n\n')
				break


