"""
Import
"""
import pygame
from model.Unit.Variables import *
from model.Unit.Archer import Archer
from model.Unit.Knight import Knight
from model.Unit.Villager import *
import os

"""
Objects
"""
class Batiment(Element):
	"""
	Possible actions for Buildings
	"""

	def __init__(self, pos, team, image_path=None):
		"""
		create
		"""
		self.type="Batiment"
		self.team=team
		self.rect.x = legal(pos[0])
		self.rect.y = legal(pos[1])

		super().__init__(pos, image_path)

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

	def selfcheck(self):
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
			vilF = Villager((256, 256), 'B')
			board.add(vilF);
		if job == "knight":
			knightF = Knight((256, 256), 'B')
			board.add(knightF);
		if job == "archer":
			archerF = Archer((256, 256), 'B')
			board.add(archerF);

	def attackTower(self, board, target):
		"""
				attacking
				"""
		self.action = "atk"
		zone = self.scan(board, self.rng)

		while target.pv > 0 and self.action == "atk":
			if not self.march(board, target):
				self.action = "Neant"
				break
			target.pv -= self.atk
			target.selfcheck(board)
			sleep(100 / self.atk_spd)

