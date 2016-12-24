"""This module is for the non-display related classes"""

class Character:
	"""This is the class that defines the players and monsters"""

	# attributes for the character
	name = "NULL"
	level = 0
	strength = 0
	vitality = 0
	defense = 0
	dexterity = 0
	intelligence = 0
	charisma = 0
	wisdom = 0
	willpower = 0
	perception = 0
	luck = 0

	def display_stats(self):
		"""Display all stats"""

		print("Name:", self.name)
		print("Level:", self.level)
		print("Strength:", self.strength)
		print("Vitality:", self.vitality)
		print("Defense:", self.defense)
		print("Dexterity:", self.dexterity)
		print("Intelligence:", self.intelligence)
		print("Charisma:", self.charisma)
		print("Wisdom:", self.wisdom)
		print("Willpower:", self.willpower)
		print("Perception:", self.perception)
		print("Luck:", self.luck)

class Player(Character):
	"""Class for the player character"""

	def __init__(self, player_name=None, load= None):
		"""Constructor of the player class, should only be called once, before the main game loop"""

		# will set the player name if no load mode is selected
		if load is None:
			# set player name
			if player_name is None:
				self.name = str(input("Please choose a name for your character:"))
		# if load == "file":
			# TODO: implement save files

	def load_player(self):
		"""Loads all the player data either from a local file or possibly from remote"""

		# TODO: implement load_player function




