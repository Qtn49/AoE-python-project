from model.building.Batiment import *


class Barracks(Batiment):

    def __init__(self, pos, team, joueur, board):
        ### Tout ce que fait une palissade ###
        self.maxpv=350
        self.cstrtime=3
        self.ok=True
        self.taille=2
        self.pv=350
        self.job="barracks"
        self.sight=6
        self.size=2
        self.needWood = 125
        self.needGold = 0
        self.needStone = 0
        self.needFood = 0
        self.needInhabitant = 0

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Barracks.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board)