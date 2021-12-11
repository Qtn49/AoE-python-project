from time import sleep
import pygame
import os
from resources.Variables import *


class Age():
    buff = 1.2
    toChange = 1000
    agePassed = False

    def changement(self,joueur, forum):
        if (10000 <= joueur.contenu["gold"]):
            joueur.contenu["gold"] -= 10000
        else:
            print(10000 ,"<", joueur.contenu["gold"])
            return
        forum.images = []
        img = pygame.image.load(os.path.join("model/building/images/Towncenter2.png")).convert()
        img = pygame.transform.scale(img, (BASE*forum.size, BASE*forum.size))
        self.agePassed=True
        forum.image= img
        print(forum.images)
        autorisation["archer"] = True
        autorisation["2_TownCenter"] = True


