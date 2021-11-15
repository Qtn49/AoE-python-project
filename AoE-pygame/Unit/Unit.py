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

	def control(self,x,y):
		"""
		Control Player
		"""
		self.moveX += x
		self.moveY += y
		sleep(1/self.spd)

	def update(self):
		"""
		update sprite position
		"""
		self.rect.x += self.moveX
		self.rect.y += self.moveY

		# moving left
		if self.moveX < 0:
			self.image = self.images[self.frame//ani]

		# moving right
		if self.moveX > 0:
			self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)

		self.moveX = 0
		self.moveY = 0

	def move(self, board, newX, newY):
		"""
		moving without doing anything else
		"""
		newX = legal(newX)
		newY = legal(newY)

		while self.rect.x!=newX or self.rect.y!=newY:

			dir = self.direction(newX,newY)

			if not self.walk(board, dir[0], dir[1]):
				break

		print(self.rect.x," : ", self.rect.y)

	def walk(self, board, dirX, dirY):
		"""
		used to move
		"""
		collide = self.collision(board, dirX, dirY)
		if (collide[0] and collide[1]) or (collide[0] and not dirY) or (collide[1] and not dirX):
			print("BLOCK")
			return False

		self.control(dirX*(1-collide[0]),dirY*(1-collide[1]))
		self.update()

		return True

	def direction(self, newX, newY):
		"""
		defines the direction we need to take for the objective
		"""
		if self.rect.x < newX:      dirX = 1
		elif self.rect.x > newX:    dirX = -1
		else:                       dirX = 0

		if self.rect.y < newY:      dirY = 1
		elif self.rect.y > newY:    dirY = -1
		else :                      dirY = 0
		return (dirX, dirY)

	def march(self, board, target):
		"""
		moving and attacking
		"""
		zone = self.scan(board, self.rng)
		imp = False

		while target not in zone :
			print(zone)
			dir=self.direction(target.rect.x, target.rect.y)

			while self.rect.x!=legal(self.rect.x+dir[0]*base) and self.rect.y!=legal(self.rect.y+dir[1]*base):
				dir=self.direction(target.rect.x, target.rect.y)
				zone = self.scan(board, self.rng)
				if not self.walk(board, dir[0], dir[1]) and target not in zone:
					imp=True
					break


			if imp:
				return False

			zone=self.scan(board, self.rng)

		return True

	def collision(self, board, dirX, dirY):
		"""
		defines wether there is a collision or not
		"""
		box=[True,True,True]
		for sprite in board:
			if sprite!=self:
				print(legal(self.rect.x)+base*dirX, " : ",legal(self.rect.y)+base*dirY)
				if legal(sprite.rect.x)==legal(self.rect.x)+base*dirX and legal(sprite.rect.y)==legal(self.rect.y)+base*dirY:
					box[0]=False
				if sprite.rect.x==legal(self.rect.x)+base and sprite.rect.y==legal(self.rect.y):
					box[1]=False
				if sprite.rect.x==legal(self.rect.x) and sprite.rect.y==legal(self.rect.y)+base:
					box[2]=False

		if box[0]:		return (0,0)
		elif box[1]:	return (0,1)
		elif box[2]:	return (1,0)
		else :			return (1,1)

	def scan(self, board, rng):
		"""
		to know what's around you
		"""
		retour=[]

		for i in range(-rng, rng+1):
			x=legal(self.rect.x)+i*base

			for j in range(-rng, rng+1):
				y=legal(self.rect.y)+j*base

				if (x,y)!=(self.rect.x,self.rect.y):
					for ob in board:
						if legal(ob.rect.x)==x and legal(ob.rect.y)==y:
							retour.append(ob)
		return retour

	def attack(self, board, target):
		"""
		attacking
		"""
		self.action="atk"
		zone=self.scan(board, self.rng)

		while target.pv >0 and self.action=="atk":
			if not self.march(board, target):
				self.action="Neant"
				break
			target.pv-=self.atk
			target.selfcheck(board)
			sleep(100/self.atk_spd)

	def selfcheck(self, board):
		"""
		state checking
		"""
		print(self.pv)
		if self.pv <=0:
			if self in board:
				board.remove(self)
				self.action="Neant"

	def defend(self, board, newX, newY):
		"""
		defend a position
		"""
		self.action="defend"
		while (self.action=="defend"):
			self.move(board, newX, newY)
			zone=self.scan(board,self.sight)
			for ob in zone:
				if ob.team!=self.team:
					self.attack(board, ob);
