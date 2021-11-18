from Batiment import *

class TourArcher(Batiment):

    def __init__(self, pos, team):
        ### Tout ce que fait une Tour d'archer ###
        self.pv = 700
        self.job = "tourarcher"
        self.action = "Neant"
        self.sight = 10
        self.needGold = 50
        self.needStone = 120

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/TourArcher.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);