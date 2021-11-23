import pygame

tempo=1
size = 3
ani = 1
base = 250

worldX = size*base
worldY = size*base
fps = 60

BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

board = pygame.sprite.Group()

def legal(value):
	return convert(value)*base

def convert(value):
	return value//base
