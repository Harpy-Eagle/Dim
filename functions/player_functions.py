from classes.player import player


def bones_bury():
	player.bones = player.bones - 1
	player.mentality = player.mentality + 10


def potion_bury():
	player.potions = player.potions - 1
