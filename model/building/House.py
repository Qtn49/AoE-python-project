from abc import ABC
from model.Building import Building


class Houses(Building, ABC):

    def __init__(self, x, y, image_path='resources/building/House.png'):
        super().__init__(x, y, image_path)
