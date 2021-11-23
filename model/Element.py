import abc
import pygame

class Element(pygame.sprite.Sprite):

    def __init__(self, pos, image_path=None):
        self.image_path = image_path
        self.present = True
        self.pos=pos
        super().__init__()

    @abc.abstractmethod
    def removeSelf(self, player):
        pass

    def get_image_path(self):
        return self.image_path
