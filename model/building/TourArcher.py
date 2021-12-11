from model.building.Batiment import *


class TourArcher(Batiment):

    def __init__(self, pos, team, joueur, board):
        ### Tout ce que fait une Tour d'archer ###
        self.pv = 30
        self.maxpv= 30
        self.team=team
        self.job = "tourarcher"
        self.action = "Neant"
        self.sight = 10
        self.rng = 4
        self.size = 2
        self.needGold = 50
        self.needStone = 120
        self.needWood = 30
        self.needFood = 0
        self.needInhabitant = 0


        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/TourArcher.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board);