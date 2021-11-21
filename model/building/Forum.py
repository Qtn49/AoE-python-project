from model.building.Batiment import *


class Forum(Batiment):

    def __init__(self, pos, team):
        ### Tout ce que fait le Forum ###
        self.pv=600
        self.job="forum"
        self.action="Neant"
        self.sight=8

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/Towncenter.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);