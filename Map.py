#!/usr/bin/env python3

from Element import *

class Map:

	def __init__(self, background=None):
		self.elements = {}
		self.background = background

	def addElement(self, pos, element):
		self.elements[pos] = element

	def removeElement(self, pos):
		del self.elements[pos]

	def getElement(self, pos):
		return self.elements[pos]

    # TODO define this method with the PyGame Library
	def createInterface(self, screen):
		for element in self.elements:
			image = pygame.image.load(element.image_path)
			image = pygame.transform.scale(image, (100, 100))
			screen.blit(image, (element.x * 100, element.y * 100))
