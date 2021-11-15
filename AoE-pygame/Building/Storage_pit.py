from Batiment import *

class Storage_pit(Batiment):

    def __init__(self, pos, team):
        self.pv=350
        self.job="storage_pit"
        self.action="Neant"
        self.sight=4

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/Storage_pit.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);