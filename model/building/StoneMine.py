

"""
Objects
"""
from model.building.Batiment import *


class StoneMine(Batiment):
    """
    Spawn a Player
    """

    def __init__(self, pos, team):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 40
        self.contenu = {"gold": 0, "stone": 40, "wood": 0, "food": 0}
        self.job = "stonemine"
        self.action = "Neant"

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("building/images/StoneMine.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos, team);
        self.ressource = "stone"
        self.type = "ressource"
