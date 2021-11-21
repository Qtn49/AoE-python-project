from model.building.Batiment import *


class Barracks(Batiment):

    def __init__(self, pos, team, joueur):
        ### Tout ce que fait une palissade ###
        self.pv=350
        self.job="barracks"
        self.action="Neant"
        self.sight=6
        self.needWood = 125
        joueur.wood -= self.needWood

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/Barracks.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);