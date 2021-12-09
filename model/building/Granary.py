from model.building.Batiment import *


class Granary(Batiment):

    def __init__(self, pos, team,joueur):
        self.pv=350
        self.job="granary"
        self.action="Neant"
        self.sight=4
        self.needWood = 120
        self.size = 1
        if (self.needWood <= joueur.contenu["wood"]):
            joueur.contenu["wood"] -= self.needWood
        else:
            print(self.needWood, "<", joueur.contenu["wood"])

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Granary.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);