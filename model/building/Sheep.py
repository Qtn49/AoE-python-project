#!/usr/bin/env python
from model.building.Batiment import *

class Sheep(Batiment):

    def __init__(self, pos, team):
        ### Tout ce qui fait un mouton ###
        self.pv=20
        self.job="animal"
        self.action="Neant"
        self.spd=100
        self.atk=2
        self.atk_spd=50
        self.rng=1
        self.sight=2
        self.food = 50

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
