from model.building.Batiment import *


class Barracks(Batiment):

    def __init__(self, pos, team, joueur):
        ### Tout ce que fait une palissade ###
        self.cstrtime=3
        self.ok=True
        self.taille=2
        self.pv=350
        self.job="barracks"
        self.action="Neant"
        self.sight=6
        self.needWood = 125
        joueur.contenu["wood"] -= self.needWood

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Barracks.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);