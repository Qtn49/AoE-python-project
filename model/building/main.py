from abc import ABC
from model.Building import Building
import pygame

pygame.init()


class Houses(Building, ABC):

    def __init__(self, x, y, image_path='resources/building/House.png'):
        super().__init__(x, y, image_path)


class Barracks(Building, ABC):

    def __init__(self, x, y, image_path='resources/building/Barracks.png'):
        super().__init__(x, y, image_path)


class TownCenter(Building, ABC):

    def __init__(self, x, y, image_path='resources/building/Towncenter.png'):
        super().__init__(x, y, image_path)
