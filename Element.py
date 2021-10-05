#!/usr/bin/env python3

import abc

class Element:

	def __init__(self, pos, board, image_path=None):
		self.image_path = image_path
		self.pos = pos
		board.addElement(pos, self)
		super().__init__()

	@abc.abstractmethod
	def removeSelf(self, player):
		pass

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def get_image_path(self):
		return self.image_path
