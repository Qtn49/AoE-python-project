"""
Import
"""
# import pygame
from time import sleep
from model.ThreadManager import *
from model.Unit.Variables import *

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
		self.thr = None
		self.action = None
		self.type = "unit"
		self.team = team
		self.rect.x = legal(pos[0])
		self.rect.y = legal(pos[1])
		self.moveX = 0
		self.moveY = 0
		super().__init__()

	def control(self, x, y):
		"""
		Control Player
		"""
		self.moveX += x
		self.moveY += y
		sleep(1 / self.spd)

	def update(self):
		"""
		update sprite position
		"""
		self.rect.x += self.moveX
		self.rect.y += self.moveY

		# moving left
		if self.moveX < 0:
			self.image = self.images[self.frame // ani]

		# moving right
		if self.moveX > 0:
			self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

		self.moveX = 0
		self.moveY = 0

	def move(self, newX, newY):
		"""
		moving without doing anything else
		"""
		# définir la case d'arrivée
		newX = legal(newX)
		newY = legal(newY)

		# bouger tant que le lieu d'arrivée n'est pas le bon
		while self.rect.x != newX or self.rect.y != newY:
			dir = self.direction(newX, newY)

			if not self.walk(dir[0], dir[1]):
				return False
		return True

	def walk(self, dirX, dirY):
		"""
		used to move
		"""
		collide = self.choice(dirX, dirY)

		if not collide or (collide[0] and not dirY) or (collide[1] and not dirX):
			print("BLOCK")
			return False

		butX = legal(self.rect.x) + base * dirX * (1 - collide[0])
		butY = legal(self.rect.y) + base * dirY * (1 - collide[1])

		while self.rect.x != butX or self.rect.y != butY:
			"""
			if (collide[1] and collide[1]) or (collide[0] and not dirY) or (collide[1] and not dirX):
				print("BLOCK")
				return False
			"""
			self.control(dirX * (1 - collide[0]), dirY * (1 - collide[1]))
			self.update()

		return True

	def direction(self, newX, newY):
		"""
		defines the direction we need to take for the objective
		"""
		if self.rect.x < newX:
			dirX = 1
		elif self.rect.x > newX:
			dirX = -1
		else:
			dirX = 0

		if self.rect.y < newY:
			dirY = 1
		elif self.rect.y > newY:
			dirY = -1
		else:
			dirY = 0
		return (dirX, dirY)

	def march(self, target):
		"""
		moving and attacking
		"""
		zone = self.scanEuc(self.rng)
		imp = False

		while target not in zone:
			dir = self.direction(target.rect.x, target.rect.y)
			newX = legal(self.rect.x) + dir[0] * base
			newY = legal(self.rect.y) + dir[1] * base

			if not self.move(newX, newY) and target not in zone:
				return False

			zone = self.scanEuc(self.rng)

			"""
			while self.rect.x!=legal(self.rect.x)+dir[0]*base and self.rect.y!=legal(self.rect.y)+abs(dir[1])*base:
				zone = self.scanEuc(board, self.rng)
				if not self.walk(board, dir[0], dir[1]) and target not in zone:
					imp=True
					break

			if imp:
				return False
			"""

		return True

	def collision(self, cX, cY):

		# limites de la map
		if (cX < 0 or cX >= (size - self.size + 1) * base) or (cY < 0 or cY >= (size - self.size + 1) * base):
			return True

		# collision avec les sprites
		for sprite in board:
			if sprite != self:
				if legal(sprite.rect.x) <= cX <= legal(sprite.rect.x) + (sprite.size - 1) * base or legal(
						sprite.rect.x) <= cX + (self.size - 1) * base <= legal(sprite.rect.x) + (
						sprite.size - 1) * base:
					if legal(sprite.rect.y) <= cY <= legal(sprite.rect.y) + (sprite.size - 1) * base or legal(
							sprite.rect.y) <= cY + (self.size - 1) * base <= legal(sprite.rect.y) + (
							sprite.size - 1) * base:
						return True

		return False

	def choice(self, dirX, dirY):

		box = [False for i in range(3)]
		if dirX != 0:

			cX = legal(self.rect.x) + base * dirX
			cY = legal(self.rect.y)

			if not self.collision(cX, cY):
				box[0] = True
			# print("H")

			if dirY != 0:
				cY = legal(self.rect.y) + base * dirY

				if not self.collision(cX, cY):
					box[2] = True
				# print("D")

				cX = legal(self.rect.x)

				if not self.collision(cX, cY):
					box[1] = True
		# print("V")

		elif dirY != 0:
			cX = legal(self.rect.x)
			cY = legal(self.rect.y) + base * dirY

			if not self.collision(cX, cY):
				box[1] = True
				print("V")

		if not box[0] and not box[1] and not box[2]:
			return False

		if box[2]:
			return (0, 0)
		elif box[0]:
			return (0, 1)
		elif box[1]:
			return (1, 0)
		else:
			return (1, 1)

	def scanEuc(self, rng):
		"""
		to know what's around you
		"""
		retour = []

		for i in range(-rng, rng + 1):
			x = legal(self.rect.x) + i * base

			for j in range(-rng, rng + 1):
				y = legal(self.rect.y) + j * base

				for ob in board:
					if legal(ob.rect.x) == x and legal(ob.rect.y) == y and ob != self:
						retour.append(ob)
		return retour

	def scanMan(self, rang):
		"""
		to know what's around you
		"""
		retour = []

		for i in range(-rang, rang + 1):
			x = legal(self.rect.x) + i * base

			for j in range(-rang, rang + 1):
				y = legal(self.rect.y) + j * base

				if abs(i) + abs(j) <= rang:
					for ob in board:
						if legal(ob.rect.x) == x and legal(ob.rect.y) == y and ob != self:
							retour.append(ob)
		return retour

	def attack(self, target):
		"""
		attacking
		"""
		# sauvegarder
		self.cache = self.action
		self.action = "atk"

		while target.pv > 0 and self.action == "atk":

			# se déplacer
			if not self.march(target):
				self.action = "Neant"
				self.thr.tuer()
				break

			# frapper
			target.pv -= self.atk
			print(target.team, " : ", target.pv)
			# attendre
			sleep(100 / self.atk_spd)

			check(target)
		self.action = self.cache

	def defend(self, newX, newY):
		"""
		defend a position
		"""
		self.action = "defend"
		self.move(newX, newY)

		while self.action == "defend":
			sleep(1)
			check(self)
			print("WOULA jdefend")
			zone = self.scanMan(self.sight)
			for ob in zone:
				if ob.team != self.team and ob.team != "Neant":
					self.attack(ob)


def check(target):
	"""
	state checking
	"""
	if target.pv <= 0:
		if target in board:
			board.remove(target)
		target.action = None
		if target.thr:
			target.thr.tuer()
	elif target.action!="atk":
		if target.thr:
			target.thr.tuer()
		target.thr = Threadatuer(target=target.defend, args=(target.rect.x, target.rect.y))
		target.thr.start()
