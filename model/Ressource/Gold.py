
from Ressource import *

"""
Objects
"""
class Gold(Ressource):

    """
    Spawn a Player
    """

    def __init__(self, pos, team):
        ### Tout ce qui fait une batiment ressource ###
        self.pv = 20
        self.gold = 40
        self.job = "gold"
        self.action = "Neant"

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Unit/" + team + '_square.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);