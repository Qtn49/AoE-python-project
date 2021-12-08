#!/usr/bin/env python3
import os
from model.Unit.Unit import *


class Archer(Unit):

    def __init__(self, pos, team):
        ### Tout ce qui fait un archer ###
        self.pv = 50
        self.maxpv = 50
        self.size=1
        self.job = "archer"
        self.spd = 700
        self.atk = 5
        self.atk_spd = 500
        self.rng = 3
        self.sight = 5

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/images/archer.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);
