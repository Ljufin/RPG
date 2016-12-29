"""The main game loop is here"""

"""ASCII art by http://www.ascii-code.com/ascii-art/"""


import os

# internal project modules
import terminal
import objects


"""Define the content and screens for the game
This stuff will eventually be moved to a different file to make creating content more easily"""
# create screens and specify info
main_town = terminal.TownScreen()
player_info = terminal.PlayerInfo()
player_info.set_border_element("#")
inn_screen = terminal.BasicMenu()
inn_screen.build_menu(("Sleep?", "[Y]: Stay the night (10 gold)", "[N]: No"))
inn_screen.set_border_element("~")
too_poor_screen = terminal.SplashScreen("You are too poor, go away")
too_poor_screen.set_border_element("$")
resting_screen = terminal.SplashScreen("You feel completely rested, your hp and mp is restored to full")
resting_screen.set_border_element("Z")

# create a player object
player_data = ("Will", "Dev", 100, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 10, 1000, 1000, 1000)
user = objects.Player(load=player_data)


def battle(player=objects.Player):
	"""Function holds all the logic for the battle system. Treat this as a separate game"""



	# TODO: generate a random monster based on the player's level
	# for now we use a placeholder monster
	monster_data = ("Punching bag", "Sandbag", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 2000, 0, 20)
	monster = objects.Monster(monster_data)


	# show a splash screen that introduces the battle
	intro_splash = terminal.SplashScreen("A %s has appeared!" % monster.name)
	intro_splash.display()

	# battle loop
	while 1:

		# check hp
		if (player.hp <= 0) and (monster.hp <= 0):
			break

		# display battle menu
		battle = terminal.BattleMenu(player, monster)
		battle.update()
		c = ''
		while c not in ('a', 'd', 'i', 'r'):
			c = battle.display()

		# TODO: implement choice system


def game():
	"""Function to hold all the game logic. Call to start the game"""

	os.system("cls")

	# main game loop
	while 1:
		os.system("cls")

		# display the main menu
		choice = main_town.update()
		if choice is 'q':
			break
		elif choice is 'p':
			player_info.update(user)
			# display the screen
			player_info.display()
		elif choice is 's':
			inn_choice = inn_screen.display()
			if inn_choice is "y":
				if user.gold < 10:
					too_poor_screen.display()
				else:
					resting_screen.display()
					user.gold -= 10
		# TODO: implement the battle system once implemented

	os.system("cls")
	return

if __name__ == "__main__":
	game()
