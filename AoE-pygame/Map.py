from Variables import *

class Map:
	
	def __init__(self, size, sprites):
		self.sprites=sprites
		self.size = size
		self.boxes = {}
		
	def add(self, ob):
		self.sprites.add(ob)
		x = ob.rect.x // base
		y = ob.rect.y // base
		self.boxes[(x,y)]=True
		
	def move(self, ob, pos):
		x = ob.rect.x // base
		y = ob.rect.y // base
		self.boxes[(x,y)]=False
		x = (ob.rect.x + pos[0]) // base
		y = (ob.rect.y + pos[1]) // base		
		self.boxes[(x,y)]=True

