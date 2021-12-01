"""
Objects
"""
import os

import pygame

from model.building.Batiment import Batiment
from model.game_constants import BASE


class Tree(Batiment):
    """
    Spawn a Player
    """

    def __init__(self, pos, team, board):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 40
        self.contenu = {"gold": 0, "stone": 0, "wood": 40, "food": 0, "inhabitant": 0}
        self.size = 1
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Tree.png")).convert()
        N_img = pygame.transform.scale(img, (BASE*self.size, BASE*self.size))
        self.images.append(N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos, team, board)
        self.ressource = "wood"
        self.type = "ressource"
