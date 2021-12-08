
"""
Objects
"""
from model.building.Batiment import *

class Bush(Batiment):
    """
    Spawn a Player
    """

    def __init__(self, pos, team):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 40
        self.contenu = {"gold": 0, "stone": 0, "wood": 0, "food": 40, "inhabitant":0}
        self.team = None

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("building/images/Buisson.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos,team);
        self.ressource = "food"
        self.type = "ressource"

