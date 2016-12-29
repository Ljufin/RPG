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
player_data = ("Will", "Dev", 100, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 10, 1000, 1000)
user = objects.Player(load=player_data)


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

	os.system("cls")
	return

if __name__ == "__main__":
	game()
