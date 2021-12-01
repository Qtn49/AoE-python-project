from model.building.Batiment import *


class Forum(Batiment):

    def __init__(self, pos, team, joueur, board):
        ### Tout ce que fait le Forum ###
        self.pv=10
        self.cstrtime=3
        self.size = 2
        self.ok=True
        self.job="forum"
        self.needWood = 125

        if (self.needWood <= joueur.contenu["wood"]):
            joueur.contenu["wood"] -= self.needWood
        else:
            print(self.needWood, "<", joueur.contenu["wood"])

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/building/images/Towncenter.png")).convert()
        N_img = pygame.transform.scale(img, (BASE*self.size, BASE*self.size))
        self.images.append(N_img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team, board)