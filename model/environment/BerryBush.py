from model.Environment import Environment
import pygame


class BerryBush(Environment):

    def __init__(self, x, y, resources=10, image_path=None):
        super().__init__(x, y, resources, image_path)
