
"""
Objects
"""
from model.building.Batiment import *



class Tree(Batiment):
    """
    Spawn a Player
    """

    def __init__(self, pos, team, image_path=None):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 40
        self.contenu = {"gold": 0, "stone": 0, "wood": 40, "food": 0, "inhabitant":0}


        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Tree.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos,team, image_path)
        self.ressource = "wood"
        self.type = "ressource"

