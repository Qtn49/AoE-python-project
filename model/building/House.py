from model.building.Batiment import *


class House(Batiment):

    def __init__(self, pos, team, joueur):
        self.ok=True
        self.cstrtime=3
        self.pv=75
        self.maxpv=75
        self.job="house"
        self.action="Neant"
        self.inhabitant=5
        self.sight=2
        self.needWood = 30
        if (self.needWood <= joueur.contenu["wood"]):
            joueur.contenu["wood"] -= self.needWood
            joueur.contenu["inhabitant"] += self.inhabitant
        else:
            print(self.needWood, "<", joueur.contenu["wood"])


        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/House.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);