
"""
Objects
"""
from model.building.Batiment import *



class Tree(Batiment):
    """
    Spawn a Player
    """

    def __init__(self, pos, team):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 40
        self.ressource = "wood"
        self.contenu = {"gold": 0, "stone": 0, "wood": 40, "food": 0}

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Building/images/Tree.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos,team);


