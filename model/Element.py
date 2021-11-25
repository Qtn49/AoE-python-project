import abc
import pygame

class Element(pygame.sprite.Sprite):

    def __init__(self, pos, image_path=None):
        self.image_path = image_path
        self.present = True
        self.pos=pos
        self.shift_x = 0
        self.shift_y = 0
        super().__init__()

    @abc.abstractmethod
    def removeSelf(self, player):
        pass

    def get_image_path(self):
        return self.image_path
