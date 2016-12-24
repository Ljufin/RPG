"""The main game loop is here"""

"""ASCII art by http://www.ascii-code.com/ascii-art/"""

import terminal
import os

os.system("cls")

mainTown = terminal.TownScreen()

# main game loop
while 1:
	os.system("cls")

	# display the main menu
	choice = mainTown.update()
	if choice is 'q':
		break

