"""This module acts as the display drivers for the terminal graphics"""

import shutil
import objects

class Screen:
	"""This object is an easy way of displaying each screen"""

	border_element = "@"
	content = ""
	# defines what how the user should interact with the screen after it has been displayed
	input_type = "press_any"

	def __init__(self, s=None):
		"""Sets content to whatever s is if s isn't None, otherwise it does nothing"""
		if s is not None:
			self.content = s

	def set_border_element(self, element):
		"""Sets the border element"""
		self.border_element = element
		return

	def make_borders(self):
		"""Makes borders that are the top and bottom of the terminal
Returns a string that is the width of the terminal constructed with the border string"""
		columns, rows = shutil.get_terminal_size()

		# figure out how many border elements are needed to span the column space
		border_element_size = self.border_element.__len__()

		column_span = columns/border_element_size

		return self.border_element*int(column_span)

	def display(self):
		"""Displays the screen. """
		columns, rows = shutil.get_terminal_size()

		border = self.make_borders()

		# display the top border
		print(border)

		# count the # of newlines in the content
		num_newlines = 0
		for char in self.content:
			if char == '\n':
				num_newlines += 1

		print(self.content)

		# fill the rest of the space with blank lines
		for i in range((rows-4)-num_newlines):
			print()

		# display the bottom border
		print(border)

		# get inputs and process it according to the current value of self.input_method
		inputs = input(">")
		if inputs == "press_any":
			# Return as None since we don't care about the input
			inputs = None
		elif inputs == "menu":
			# Return as a char since we care about singular inputs
			inputs = char(inputs)

		return inputs

class SplashScreen(Screen):
	"""This is the class for all static screens that the user hits any button to continue"""
	input_type = "press_any"

class BasicMenu(Screen):
	"""This class builds a simple menu out of a list of strings. Make sure to build the menu before displaying"""

	input_type = "menu"

	def build_menu(self, string_tup=()):
		"""Takes a tuple of strings and generates content based on that"""
		for item in string_tup:
			self.content += item+"\n"

class TownScreen(Screen):
	"""This is the main menu for the game and maybe more if I decide to add more towns"""

	input_type = "menu"

	town_title = "\n\tWillsburg"

	town_image = """
                               ___        ___       T__
                    ________   | |~~~~~~~~| ||~~~~| |||
__|~~~~~~~~|   _/\_ |^^^^^^|  _| |--------| ||    | |##
|_|HHHHHHHH|  _|--| |------|_-#########################"""

	vsep = "\n\n\n\n"


	def update(self, level=1):
		"""Displays specific options based on the player's level and then displays the screen"""

		self.content = self.town_title+self.town_image + self.vsep
		if level >= 1:
			self.content += "[F] Fight\n"
			self.content += "[S] Sleep\n"
			self.content += "[P] Check character\n"

		# always add the quit option
		self.content += "[Q} Quit the game"

		return self.display()

	def set_title(self, new_title):
		"""Sets the town title"""
		self.town_title = new_title

	def set_picture(self, new_picture):
		"""Sets the town picture"""
		self.town_image = new_picture

class PlayerInfo(Screen):
	"""This is the screen for displaying character info"""

	input_type = "press_any"

	def update(self, player):
		"""Updates content based on what is stored in the player object"""
		self.content = ""
		self.content += " Name: "+player.name+"\n"
		self.content += " Role: " + player.role + "\n"
		self.content += " Level: "+str(player.level)+"\n"
		self.content += " Strength: "+str(player.strength)+"\n"
		self.content += " HP: "+str(player.hp)+"\n"
		self.content += " Defense: "+str(player.defense)+"\n"
		self.content += " Dexterity: "+str(player.dexterity)+"\n"
		self.content += " MP: "+str(player.mp)+"\n"
		self.content += " Charisma: "+str(player.charisma)+"\n"
		self.content += " Wisdom: "+str(player.wisdom)+"\n"
		self.content += " Willpower: "+str(player.willpower)+"\n"
		self.content += " Perception: "+str(player.perception)+"\n"
		self.content += " Luck: "+str(player.luck)+"\n"
		self.content += " Gold: "+str(player.gold)
