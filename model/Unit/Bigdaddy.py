#!/usr/bin/env python3

from model.Unit.Unit import *
import os

class Bigdaddy(Unit):

    def __init__(self, pos, team, board):
        ### Tout ce qui fait un champion ###
        self.pv=5000
        self.maxpv=5000
        self.job="bigdaddy"
        self.size=2
        self.spd=300
        self.atk=100
        self.atk_spd=50
        self.rng=1
        self.sight=2

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/images/voiture.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board);
