import pygame
from resources.Generator import *
from resources.game_constants import *

autorisation = {"Archer": False, "2_TownCenter": False}

GenID = first_n(500)
tempo = 1
ani = 1

fps = 60


def legal(value):
	return convert(value)*BASE

def convert(value):
	return value//BASE

