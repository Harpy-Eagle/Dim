from classes.player import player

def health_potion():
	name = "health potion"
	player.potions = player.potions - 1
	player.hp = player.hp + 5
