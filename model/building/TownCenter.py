from abc import ABC

from model.Building import Building


class TownCenter(Building, ABC):

    def __init__(self, x, y, appearance=None):
        super().__init__(x, y, appearance)
