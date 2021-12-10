#!/usr/bin/env python3
import os
from model.Unit.Unit import *

class Knight(Unit):

    def __init__(self, pos, team, board, joueur):
        ### Tout ce qui fait un chevalier ###
        self.pv=30
        self.maxpv=30
        self.job="knight"
        self.spd=100
        self.size=1
        self.atk=6
        self.atk_spd=50
        self.rng=1
        self.sight=3
        self.needWood = 0
        self.needGold = 0
        self.needStone = 0
        self.needFood = 50
        self.needInhabitant = 2



        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/images/soldat.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board);
