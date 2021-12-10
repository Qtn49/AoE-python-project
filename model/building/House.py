from model.building.Batiment import *


class House(Batiment):

    def __init__(self, pos, team, joueur, board):
        self.ok=True
        self.cstrtime=3
        self.pv=75
        self.maxpv=75
        self.job="house"
        self.action="Neant"

        self.sight=2
        self.size=2
        self.needWood = 30
        self.needGold = 0
        self.needStone = 0
        self.needFood = 0
        self.needInhabitant = -5



        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/House.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board);