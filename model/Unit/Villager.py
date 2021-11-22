#!/usr/bin/env python3

from Unit import *

class Villager(Unit):

    def __init__(self, pos, team):
        ### Tout ce qui fait un villageois ###
        self.pv=20
        self.job="villager"
        self.action="Neant"
        self.spd=500
        self.atk=2
        self.atk_spd=500
        self.rng=1
        self.sight=4
        self.capa=50
        self.espace=50
        self.contenu={"gold":0,"stone":0,"wood":0, "food":0}

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("Unit/"+team+'_square.png')).convert()
        img.convert_alpha()  # optimise alpha
        img.set_colorkey(ALPHA)  # set alpha
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team);

    def fetch(self, forum, cible, board):
        self.ressource=cible.ressource
        while cible.contenu[self.ressource]:
            # bouger
            self.move(board, cible.rect.x, cible.rect.y)
            zone = self.scan(board, self.rng)

            if cible not in zone:
                print("Pas trouvé")
                break

            # remplir
            while self.espace:
                cible.contenu[self.but]-=1
                self.contenu[self.but]+=1
                self.espace-=1

            # bouger
            #self.move(board, forumX, forumY)

            # décharger
            #while self.espace<self.capa and self.espace>=0:
                #self.contenu[self.but]-=1
                #joueur.contenu[self.but]+=1
                #self.espace-=1
