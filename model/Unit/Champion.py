#!/usr/bin/env python3

from model.Unit.Unit import *

class Champion(Unit):

    def __init__(self, pos, team, board, vague=0):
        ### Tout ce qui fait un champion ###
        self.pv=30
        self.maxpv=30
        self.vague=vague
        self.size=1
        self.job="champion"
        self.spd=300
        self.atk=6
        self.atk_spd=50
        self.rng=1
        self.sight=2

        self.needFood = 0
        self.needWood = 0
        self.needGold = 0
        self.needStone = 0
        self.needInhabitant = 0

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/images/champion.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team,board);
