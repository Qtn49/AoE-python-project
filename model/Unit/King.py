#!/usr/bin/env python3

from Unit import *
import os

class King(Unit):

    def __init__(self, pos, team):
        ### Tout ce qui fait un champion ###
        self.pv=10
        self.job="king"
        self.size=2
        self.action="Neant"
        self.spd=100
        self.atk=4
        self.atk_spd=50
        self.rng=1
        self.sight=2

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/images/sheep.png")).convert()
        N_img = pygame.transform.scale(img, (base*self.size, base*self.size))
        self.images.append(N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);
