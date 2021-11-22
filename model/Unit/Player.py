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
		self.wood = 500
		self.stone = 500
		self.gold = 50
		self.food = 50
		self.inhabitant = 5

		self.contenu={"gold":0,"stone":0,"wood":0, "food":0}