from model.building.Batiment import *


class Granary(Batiment):

    def __init__(self, pos, team):
        self.pv=350
        self.job="granary"
        self.action="Neant"
        self.sight=4
        self.needWood = 120

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("building/images/Granary.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);