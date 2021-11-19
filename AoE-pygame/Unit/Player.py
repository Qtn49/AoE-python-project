"""
Import
"""
import os
import pygame
from Variables import *
"""
Objects
"""
class Player(pygame.sprite.Sprite):
	"""
	Possible actions for Buildings
	"""

	def __init__(self):
		"""
		create
		"""
		self.type = "joueur"
		self.wood = 50
		self.stone = 50
		self.gold = 50
		self.inhabitant = 5