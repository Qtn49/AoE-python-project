import abc

"""

Faire heriter chaque element abstrait de la classe Element

"""

class Element:

    def __init__(self, image_path=None):
        self.image_path = image_path
        self.present = True

    @abc.abstractmethod
    def removeSelf(self, player):
        pass

    def get_image_path(self):
        return self.image_path
