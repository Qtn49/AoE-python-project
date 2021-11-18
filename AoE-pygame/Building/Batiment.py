"""
Import
"""
import pygame
from Variables import *

import os

from unitClass import Villager

"""
Objects
"""
class Batiment(pygame.sprite.Sprite):
	"""
	Possible actions for Buildings
	"""

	def __init__(self, pos, team):
		"""
		create
		"""
		self.type="Batiment"
		self.team=team
		self.rect.x = legal(pos[0])
		self.rect.y = legal(pos[1])

		def scan(self, board, rng):
			"""
			to know what's around you
			"""
			retour = []

			for i in range(-rng, rng + 1):
				x = legal(self.rect.x) + i * base

				for j in range(-rng, rng + 1):
					y = legal(self.rect.y) + j * base

					if (x, y) != (self.rect.x, self.rect.y):
						for ob in board:
							if legal(ob.rect.x) == x and legal(ob.rect.y) == y:
								retour.append(ob)
			return retour

	def selfcheck(self, board):
		"""
		state checking
		"""
		print(self.pv)
		if self.pv <=0:
			if self in board:
				board.remove(self)
				self.action="Neant"

	def generateUnit(self, board, job):
		if job == "villager":
			vilB = Villager((0, 0), 'B')
			board.add(vilB);


	##def attackTower(self, board, job):


