"""This module is for the non-display related classes"""

class Character:
	"""This is the class that defines the players and monsters"""

	# attributes for the character
	name = "NULL"
	level = 0
	strength = 0
	# max hit-points
	vitality = 0
	defense = 0
	dexterity = 0
	# max magic points
	intelligence = 0
	charisma = 0
	wisdom = 0
	willpower = 0
	perception = 0
	luck = 0
	gold = 0

	# current stats
	hp = 0
	mp = 0
	xp = 0

class Player(Character):
	"""Class for the player character"""

	# attributes for a player
	role = "Nullspace Sorcerer"

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
			self.hp = load[14]
			self.mp = load[15]
			self.xp = load[16]


	def load_player(self):
		"""Loads all the player data either from a local file or possibly from remote"""

		# TODO: implement load_player function


	def rest(self):
		"""Called whenever the player rests at an inn or equivalent. Restores hp and mp to full"""

		self.hp = self.vitality
		self.mp = self.intelligence

class Monster(Character):
	"""This is class used to define all monsters in the game: monsters are all objects of this class"""

	# TODO: define a few unique attributes for these monsters
	# TODO: implement an item system first
	loot = ()

	# This replaces the role attribute for the player
	type = "normal"

	def __init__(self, attributes=None):
		"""Similar to player constructor but only loads from the tuple"""

		if isinstance(attributes, tuple):
			self.name = attributes[0]
			self.type = attributes[1]
			self.level = attributes[2]
			self.strength = attributes[3]
			self.vitality = attributes[4]
			self.defense = attributes[5]
			self.dexterity = attributes[6]
			self.intelligence = attributes[7]
			self.charisma = attributes[8]
			self.wisdom = attributes[9]
			self.willpower = attributes[10]
			self.perception = attributes[11]
			self.luck = attributes[12]
			self.gold = attributes[13]
			self.hp = attributes[14]
			self.mp = attributes[15]
			self.xp = attributes[16]
