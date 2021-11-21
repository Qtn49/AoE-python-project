"""
Import
"""
import pygame

from Variables import *
from model.Unit.Villager import *

import os

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
			vilF = Villager((256, 256), 'B')
			board.add(vilF);
		#if job == "knight":
			#KnightF = Knight((256, 256), 'B')
			#board.add(KnightF);

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

	def stockRessources(self, job, joueur, type, quantity):
		if job == "villager" and type == "wood":
			joueur.wood += quantity
		if job == "villager" and type == "stone":
			joueur.stone += quantity
		if job == "villager" and type == "gold":
			joueur.gold += quantity
		#ramene 10 bois au granary
		#recupere les 10 bois que le villageois a ramané
	    #vider inventaire du villageois
		#stoker ces 10 bois dans linventaire du joueur

	def recupRessources(self, board, typeRessource):
		print()
		#donne du bois à un villageois qui tape larbre
		#stocke dans linventaire du villageois
		#si on lui ordonne darreter la recolte il arrete
		#check action du joueur, si le joueur ne fait rien il stack le bois sinon il arrete de boloss le bois