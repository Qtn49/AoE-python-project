"""
Import
"""
import os
import pygame
from resources.Variables import *
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

		self.contenu={"gold":500,"stone":500,"wood":500, "food":500, "inhabitant":5}