from abc import ABC
from model.Building import Building


class Barracks(Building, ABC):

    def __init__(self, x, y, image_path='resources/building/Barracks.png'):
        super().__init__(x, y, image_path)