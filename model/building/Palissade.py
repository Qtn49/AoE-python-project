from Batiment import *

class Palissade(Batiment):

    def __init__(self, pos, team):
        ### Tout ce que fait une palissade ###
        self.pv=150
        self.job="palissade"
        self.action="Neant"
        self.sight=2
        self.needWood = 2

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/Woodwall1.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);