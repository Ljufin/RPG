"""This module is for the non-display related classes"""

class Character:
	"""This is the class that defines the players and monsters"""

	# attributes for the character
	name = "NULL"
	role = "Nullspace Sorcerer"
	level = 0
	strength = 0
	Vitality = 0
	defense = 0
	dexterity = 0
	Intelligence = 0
	charisma = 0
	wisdom = 0
	willpower = 0
	perception = 0
	luck = 0
	gold = 0

class Player(Character):
	"""Class for the player character"""

	def __init__(self, player_name=None, load=None):
		"""Constructor of the player class, should only be called once, before the main game loop"""

		# will set the player name if no load mode is selected
		if load is None:
			# set player name
			if player_name is None:
				self.name = str(input("Please choose a name for your character: "))
		# if load == "file":
			# TODO: implement save files
		# Loads the player data from a tuple, mostly for debug purposes right now
		elif isinstance(load, tuple):
			self.name = load[0]
			self.role = load[1]
			self.level = load[2]
			self.strength = load[3]
			self.vitality = load[4]
			self.defense = load[5]
			self.dexterity = load[6]
			self.intelligence = load[7]
			self.charisma = load[8]
			self.wisdom = load[9]
			self.willpower = load[10]
			self.perception = load[11]
			self.luck = load[12]
			self.gold = load[13]


	def load_player(self):
		"""Loads all the player data either from a local file or possibly from remote"""

		# TODO: implement load_player function


	def rest(self):
		"""Called whenever the player rests at an inn or equivalent. Restores hp and mp to full"""
		# TODO: implement the stats and leveling system before doing this method


