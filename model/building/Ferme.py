from model.building.Batiment import *


class Ferme(Batiment):

    def __init__(self, pos, team,joueur):
        ### Tout ce que fait une Ferme ###
        self.pv = 480
        self.job = "ferme"
        self.action = "Neant"
        self.sight = 1
        self.needWood = 75
        if (self.needWood <= joueur.contenu["wood"]):
            joueur.contenu["wood"] -= self.needWood
        else:
            print(self.needWood, "<", joueur.contenu["wood"])

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("building/images/Farm.png")).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);