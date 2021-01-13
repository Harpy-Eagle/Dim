from classes.player import player
from encounters.hunt_battle import HuntBattle
import random
from functions.responses import n_inputs, e_inputs, s_inputs, w_inputs
import sys
import curses

def camp():
	screen = curses.initscr()
	screen.clear()
	screen.addstr("\n## You set up a small shelter and get a fire going for the night. ##")
	player.clock = 0
	player.time = "Day"
	if player.rations < 1:
		screen.addstr("## You do not have any rations, and go hungry as a result. ##")
		player.hp = player.hp - 2
		player.mentality = player.mentality - 50
	else:
		screen.addstr("## You consume a days worth of rations and heal a little. ##")
		player.rations = player.rations - 1
		player.hp = player.hp + 5
		player.mentality = player.mentality + 10



def hunt():
	hunt = random.randint(1,100)
	screen = curses.initscr()
	if hunt < 60: 
		screen.addstr("\n\nUnfortunately, you caught nothing in your traps, and wasted several hours attempting to catch something")
		player.clock = player.clock + 6
		if player.clock >= 10 and player.clock < 16:

			if player.region == "Forest":
				nightdescr = "\n##...Night falls upon the forest...##"
			elif player.region == "Plains":
				nightdescr = "\n##...The sun sets on the rolling hills...##"

			screen.addstr(nightdescr)
			player.time = "Night"

		elif player.clock >= 16:
			screen.addstr("\n##...Dawn breaks through the leaves, and the night ends. Having not rested, you grow weary...##\n")
			player.time = "Day"
			player.clock = 0
			player.mentality = player.mentality - 30
			player.hp = player.hp - 3

		


	if hunt > 60 and hunt <= 80:
		screen.addstr("You managed to set a snare and trap some small game! You got a days worth of rations!")
		player.rations = player.rations + 1
		


	elif hunt > 80:
		screen.addstr("You hear rustling in a nearby bush... It's an ambush!")
		HuntBattle()
		

def rest():
	screen = curses.initscr()
	screen.clear()
	rest = True
	while rest == True:
		screen.addstr("\nYou are in a small clearing. You can hunt, set up camp, or keep walking.\n\n")
		ans = screen.getstr().lower()
		ans = ans.decode("utf-8")
		if ans == "hunt":
			hunt()
			break
		
		elif ans == "camp":
			camp()
			break

		elif ans in n_inputs or e_inputs or s_inputs or w_inputs or ans == "keep walking":
			break
