#!/usr/bin/env python3

from model.Unit.Unit import *
import os

class King(Unit):

    def __init__(self, pos, team, board):
        ### Tout ce qui fait un champion ###
        self.pv=100
        self.maxpv=100
        self.job="king"
        self.size=2
        self.spd=100
        self.atk=4
        self.atk_spd=50
        self.rng=1
        self.sight=2
        self.vague = 20

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/images/king.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board);
