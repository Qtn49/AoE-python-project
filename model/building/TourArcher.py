from model.building.Batiment import *


class TourArcher(Batiment):

    def __init__(self, pos, team, joueur):
        ### Tout ce que fait une Tour d'archer ###
        self.pv = 700
        self.maxpv=700
        self.job = "tourarcher"
        self.action = "Neant"
        self.sight = 10
        self.rng = 4
        self.needGold = 50
        self.needStone = 120
        if (self.needStone <= joueur.contenu["stone"] & self.needGold <= joueur.contenu["gold"]):
            joueur.contenu["stone"] -= self.needStone
            joueur.contenu["gold"] -= self.needGold
        else:
            print(self.needGold , self.needStone,"<", joueur.contenu["stone"], joueur.contenu["gold"])


        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("building/images/TourArcher.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);