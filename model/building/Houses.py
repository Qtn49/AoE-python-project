from abc import ABC

from model.Building import Building


class TownCenter(Building, ABC):

    def __init__(self, x, y, image_path=None):
        super().__init__(x, y, image_path)