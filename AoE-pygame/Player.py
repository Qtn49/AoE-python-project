import pygame
import os

"""
Variables
"""
BLUE = (25, 25, 200)
BLACK = (23, 23, 23)
WHITE = (254, 254, 254)
ALPHA = (0, 255, 0)

ani=1

"""
Objects
"""
class Player(pygame.sprite.Sprite):
    """
    Spawn a Player
    """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.moveX = 0
        self.moveY = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join('gauche.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self,x,y):
        """
        Control Player
        """
        self.moveX += x
        self.moveY += y

    def update(self):
        """
        update sprite position
        """
        self.rect.x += self.moveX
        self.rect.y += self.moveY

        # moving left
        if self.moveX < 0:
            self.image = self.images[self.frame//ani]

        # moving right
        if self.moveX > 0:
            self.image = pygame.transform.flip(self.images[self.frame // ani], True, False)
