#!/usr/bin/env python3
import os

from model.Unit.Unit import *


class Champion(Unit):

    def __init__(self, pos, team, board):
        ### Tout ce qui fait un champion ###
        self.pv=20
        self.job="champion"
        self.action="Neant"
        self.spd=100
        self.atk=4
        self.atk_spd=50
        self.rng=1
        self.sight=2

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        self.img = pygame.image.load(os.path.join("model/Unit/"+team+'_square.png')).convert()
        self.images.append(self.img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board)
