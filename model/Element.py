import abc
import pygame

class Element(pygame.sprite.Sprite):

    def __init__(self, pos):
        self.present = True
        self.pos=pos
        self.shift_x = 0
        self.shift_y = 0
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        super().__init__()

    @abc.abstractmethod
    def removeSelf(self, player):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
