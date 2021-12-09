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
        self.pv = 40
        self.maxpv=40
        self.contenu = {"gold": 40, "stone": 0, "wood": 0, "food": 0, "inhabitant":0}
        self.job = "goldmine"
        self.action = "Neant"

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        self.img = pygame.image.load(os.path.join("building/images/GoldMine.png")).convert()
        self.N_img = pygame.transform.scale(self.img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos, team, board);
        self.ressource = "gold"
        self.type = "ressource"
