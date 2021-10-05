from abc import ABC

from model.Building import Building


class TownCenter(Building, ABC):

    def __init__(self, image_path=None):
        super().__init__(image_path)
