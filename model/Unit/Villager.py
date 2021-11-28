#!/usr/bin/env python3

from model.Unit.Unit import *
import os

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
        self.contenu = {"gold": 0, "stone": 0, "wood": 0, "food": 0}

        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("model/Unit/"+team+'_square.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        super().__init__(pos, team)

    def fetch(self, forum, cible, joueur):
        self.but = cible.ressource
        self.action = "fetch"
        while self.action == "fetch":
            self.move(cible.rect.x, cible.rect.y)
            if cible not in board :
                zone = self.scanEuc(self.sight)
                print(zone)
                for ob in zone :
                    print(ob.type)
                    if ob.type == "ressource" and ob.ressource == self.but:
                        cible = ob
                    else:
                        print("non")
                        self.action ="None"


            while cible and cible.contenu[self.but]:
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
                    sleep(10/self.atk_spd)
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
