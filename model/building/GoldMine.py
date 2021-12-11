"""
Objects
"""
from model.building.Batiment import *


class GoldMine(Batiment):

    """
    Spawn a Player
    """

    def __init__(self, pos, team,board):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 90
        self.maxpv=90
        self.contenu = {"gold": 40, "stone": 0, "wood": 0, "food": 0, "inhabitant":0}
        self.job = "goldmine"
        self.action = "Neant"
        self.size = 1

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        self.img = pygame.image.load(os.path.join("model/building/images/GoldMine.png")).convert()
        self.N_img = pygame.transform.scale(self.img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos, team, board);
        self.ressource = "gold"
        self.type = "ressource"
