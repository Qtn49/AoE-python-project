

"""
Objects
"""
from model.building.Batiment import *


class StoneMine(Batiment):
    """
    Spawn a Player
    """

    def __init__(self, pos, team, board):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 40
        self.contenu = {"gold": 0, "stone": 40, "wood": 0, "food": 0}
        self.job = "stonemine"
        self.action = "Neant"

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/StoneMine.png")).convert()

        N_img = pygame.transform.scale(img, (BASE, BASE))
        self.images.append(N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos, team, board)
        self.ressource = "stone"
        self.type = "ressource"
