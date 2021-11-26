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
        if (self.needWood <= joueur.contenu["wood"]):
            joueur.contenu["wood"] -= self.needWood
        else:
            print(self.needWood ,"<", joueur.contenu["wood"])

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Barracks.png")).convert()

        N_img = pygame.transform.scale(img, (base, base))
        self.images.append(N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);