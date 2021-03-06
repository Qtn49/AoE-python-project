
"""
Objects
"""
from model.building.Batiment import *



class Sheep(Batiment):

    def __init__(self, pos, team, board):
        ### Tout ce qui fait un mouton ###
        self.pv = 50
        self.maxpv= 50
        self.contenu = {"gold": 0, "stone": 0, "wood": 0, "food": 50, "inhabitant":0}
        self.job="animal"
        self.action="Neant"
        self.team=None
        self.spd=100
        self.atk=2
        self.atk_spd=50
        self.rng=1
        self.sight=2
        self.size = 1

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/sheep.png")).convert()
        self.N_img = pygame.transform.scale(img, (BASE * self.size, BASE * self.size))
        self.images.append(self.N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        super().__init__(pos, team, board);
        self.ressource = "food"
        self.type = "ressource"

