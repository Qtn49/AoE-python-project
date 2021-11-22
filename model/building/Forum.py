from model.building.Batiment import *


class Forum(Batiment):

    def __init__(self, pos, team, joueur):
        ### Tout ce que fait le Forum ###
        self.pv=600
        self.job="forum"
        self.needWood = 125
        joueur.wood -= self.needWood

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/Towncenter.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);