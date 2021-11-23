#!/usr/bin/env python3

from model.Unit.Unit import *

class Archer(Unit):

    def __init__(self, pos, team):
        ### Tout ce qui fait un archer ###
        self.pv=20
        self.job="archer"
        self.action="Neant"
        self.spd=100
        self.atk=3
        self.atk_spd=50
        self.rng=4
        self.sight=2

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Unit/"+team+'_square.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);
