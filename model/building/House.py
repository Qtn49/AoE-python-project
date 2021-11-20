from Batiment import *


class House(Batiment):

    def __init__(self, pos, team, joueur):
        self.pv=75
        self.job="house"
        self.action="Neant"
        self.inhabitant=5
        self.sight=2
        self.needWood = 30
        joueur.wood -= self.needWood
        joueur.inhabitant += self.inhabitant

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/House.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);