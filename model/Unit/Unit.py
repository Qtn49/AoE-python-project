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
base =2

class Unit(pygame.sprite.Sprite):
	"""
	Possible actions for Units (moving, attack...)
	"""

	def __init__(self, pos, team, board):
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
		self.x = pos[0]
		self.y = pos[1]
		self.board = board
		super().__init__()
		print(self.board)

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
		self.x += self.moveX
		self.y += self.moveY

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
		while self.x != newX or self.y != newY:
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

		butX = legal(self.x) + BASE * dirX * (1 - collide[0])
		butY = legal(self.y) + BASE * dirY * (1 - collide[1])

		while self.x != butX or self.y != butY:
			self.control(dirX * (1 - collide[0]), dirY * (1 - collide[1]))
			self.update()

		return True

	def direction(self, newX, newY):
		"""
		defines the direction we need to take for the objective
		"""
		if self.x < newX:
			dirX = 1
		elif self.x > newX:
			dirX = -1
		else:
			dirX = 0

		if self.y < newY:
			dirY = 1
		elif self.y > newY:
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
			dir = self.direction(target.x, target.y)
			newX = legal(self.x) + dir[0] * BASE
			newY = legal(self.y) + dir[1] * BASE

			if not self.move(newX, newY) and target not in zone:
				return False

			zone = self.scanEuc(self.rng)


		return True

	def collision(self, cX, cY):

		# limites de la map
		if (cX < 0 or cX >= (GAME_DIMENSIONS[0] - self.size + 1) * BASE) or (cY < 0 or cY >= (GAME_DIMENSIONS[1] - self.size + 1) * BASE):
			return True

		print(self.board)
		# collision avec les sprites
		for sprite in self.board.board:
			if sprite != self:
				if legal(sprite.x) <= cX <= legal(sprite.x) + (sprite.size - 1) * BASE or legal(
						sprite.rect.x) <= cX + (self.size - 1) * BASE <= legal(sprite.x) + (
						sprite.size - 1) * BASE:
					if legal(sprite.y) <= cY <= legal(sprite.y) + (sprite.size - 1) * BASE or legal(
							sprite.y) <= cY + (self.size - 1) * BASE <= legal(sprite.y) + (
							sprite.size - 1) * BASE:
						return True

		return False

	def choice(self, dirX, dirY):

		box = [False for i in range(3)]

		if dirX != 0:

			cX = legal(self.x) + BASE * dirX
			cY = legal(self.y)

			if not self.collision(cX, cY):
				box[0] = True
			# print("H")

			if dirY != 0:
				cY = legal(self.y) + BASE * dirY

				if not self.collision(cX, cY):
					box[2] = True
				# print("D")

				cX = legal(self.x)

				if not self.collision(cX, cY):
					box[1] = True
		# print("V")

		elif dirY != 0:
			cX = legal(self.x)
			cY = legal(self.y) + BASE * dirY
			print(self.x," : ", self.y)
			print(cX, " : ", cY)
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
			x = legal(self.x) + i * BASE

			for j in range(-rng, rng + 1):
				y = legal(self.y) + j * BASE

				for ob in self.board.board:
					if legal(ob.x) == x and legal(ob.y) == y and ob != self:
						retour.append(ob)
		return retour

	def scanMan(self, rang):
		"""
		to know what's around you
		"""
		retour = []

		for i in range(-rang, rang + 1):
			x = legal(self.rect.x) + i * BASE

			for j in range(-rang, rang + 1):
				y = legal(self.rect.y) + j * BASE

				if abs(i) + abs(j) <= rang:
					for ob in self.board.board:
						if legal(ob.x) == x and legal(ob.y) == y and ob != self:
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
				self.action = None
				self.thr.tuer()
				break

			# frapper
			target.pv -= self.atk
			print(target.team, " : ", target.pv)
			# attendre
			sleep(100 / self.atk_spd)

			check(target, self.board)
		self.action = self.cache

	def defend(self, newX, newY):
		"""
		defend a position
		"""
		self.action = "defend"
		self.move(newX, newY)

		while self.action == "defend":
			sleep(1)
			zone = self.scanMan(self.sight)
			for ob in zone:
				if ob.team != self.team and ob.team != "Neant":
					self.attack(ob)

			if self.pv <= 0:
				if self in self.board.board:
					self.board.board.remove(self)
					self.board.afg.remove(self)
				self.action = None
				if self.thr:
					self.thr.tuer()
			sleep(1)

def check(target, board):
	"""
	state checking
	"""
	if target.pv <= 0:
		print(board.board)
		for i in board.board:
			print(i.team)
		for i in board.afg:
			print(i)
		if target in board.board:
			board.board.remove(target)
			board.afg.remove(target)
			print(target.team)
		target.action = None
		if target.thr:
			target.thr.tuer()

	elif target.action!="atk":
		# if target.thr:
		# 	target.thr.tuer()
		target.thr = Threadatuer(target=target.defend, args=(target.x, target.y))
		target.thr.start()
