"""
Import
"""
import pygame
import os
from time import sleep
from Variables import *


"""
Objects
"""
class Unit(pygame.sprite.Sprite):
	"""
	Possible actions for Units (moving, attack...)
	"""

	def __init__(self, pos, team):
		"""
		create
		"""
		self.type="unit"
		self.team=team
		self.rect.x = legal(pos[0])
		self.rect.y = legal(pos[1])
		self.moveX = 0
		self.moveY = 0

