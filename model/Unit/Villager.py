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

    def fetch(self, forum, cible, joueur):
        self.but=cible.ressource
        while cible.contenu[self.but]:
            print("----")
            # bouger
            self.move(cible.rect.x, cible.rect.y)
            zone = self.scanMan(self.rng)

            if cible not in zone:
                print("Pas trouvé")
                 #break

            # remplir
            while self.espace > 0 and cible.pv>0:
                cible.contenu[self.but]-=1
                self.contenu[self.but]+=1
                self.espace-=1
                sleep(100/self.atk_spd)
                cible.pv -= 1
                cible.selfcheck()
                print(cible.pv)

            # bouger
            self.move(forum.rect.x, forum.rect.y)

            #décharger
            while self.espace<self.capa:
                joueur.contenu[self.but]+=1
                self.espace+=1
                self.contenu[self.but]-=1
