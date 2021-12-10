"""
Import
"""
import pygame
from resources.Variables import *
from model.Unit.Archer import Archer
from model.Unit.Knight import Knight
from model.Unit.Villager import *
import os

"""
Objects
"""
class Batiment(pygame.sprite.Sprite):
	"""
	Possible actions for Buildings
	"""

	def __init__(self, pos, team,board):
		"""
		create
		"""
		self.action = {"atk": False, "defend": False, "Construction": False, "fetch": False}
		self.thr=None
		self.type="Batiment"
		self.team=team
		self.rect.x = legal(pos[0])
		self.rect.y = legal(pos[1])
		self.x = pos[0]
		self.y = pos[1]

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
			if self in board.board:
				board.board.remove(self)
				self.action="Neant"

	def generateUnit(self, board, job, joueur):
		ID = GenID.__next__()
		print(ID)
		if job == "villager" and joueur.contenu["food"]>=50:
			gen = Villager((self.x-base, self.y), self.team)
			joueur.contenu["food"] -= 50
		if job == "knight" and joueur.contenu["food"]>=100:
			gen = Knight((self.x-base, self.y), self.team)
			joueur.contenu["food"] -= 100
		if job == "archer" and joueur.contenu["food"]>=150:
			gen = Archer((self.x-base, self.y), self.team)
			joueur.contenu["food"] -= 150
		board.add(gen)
		return gen

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

	def defend(self, bla,blo):
		pass
