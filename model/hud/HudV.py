import pygame
import random

from model.Unit.Variables import *
from model.game_constants import *

class Hud():

    def __init__(self):
        # couleurs utilisées
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.marron = (182, 121, 22)
        self.red = (200, 0, 0)
        self.blue = (0, 0, 200)
        self.bright_red = (255, 0, 0)
        self.bright_blue = (0, 0, 255)

        self.barre2 = pygame.image.load("model/hud/img.png").convert_alpha()
        self.barre2 = pygame.transform.scale(self.barre2, (500,50))


        # font
        self.font3 = pygame.font.SysFont("arial", 18)


        # image de ressources
        self.g_image = pygame.image.load("model/hud/gold_image.png").convert_alpha()
        self.s_image = pygame.image.load("model/hud/stone_image.png").convert_alpha()
        self.m_image = pygame.image.load("model/hud/meat_image.png").convert_alpha()
        self.w_image = pygame.image.load("model/hud/wood_image.png").convert_alpha()
        self.p_image = pygame.image.load("model/hud/people_image.png").convert_alpha()
        self.gold_image = pygame.transform.scale(self.g_image, (29, 29))
        self.stone_image = pygame.transform.scale(self.s_image, (29, 29))
        self.meat_image = pygame.transform.scale(self.m_image, (29, 29))
        self.wood_image = pygame.transform.scale(self.w_image, (29, 29))
        self.people_image = pygame.transform.scale(self.p_image, (29, 29))


    def hud_joueur(self, display, clock,joueur,horloge):

        gold = joueur.contenu["gold"]
        gold_x1, gold_x2 = 0, 30
        stone = joueur.contenu["stone"]
        stone_x1, stone_x2 = 90, 120
        meat = joueur.contenu["food"]
        meat_x1, meat_x2 = 180, 210
        wood = joueur.contenu["wood"]
        wood_x1, wood_x2 = 270, 300
        people = joueur.contenu["inhabitant"]
        people_x1, people_x2 = 360, 390


        display.blit(self.barre2, (0, 0))



        #affichage des données de la barre
        display.blit(self.gold_image, (gold_x1, 10))
        display.blit(self.font3.render(str(gold), True, self.white), (gold_x2 + 2, 13))
        display.blit(self.stone_image, (stone_x1, 10))
        display.blit(self.font3.render(str(stone), True, self.white), (stone_x2 + 2, 13))
        display.blit(self.meat_image, (meat_x1, 10))
        display.blit(self.font3.render(str(meat), True, self.white), (meat_x2 + 2, 13))
        display.blit(self.wood_image, (wood_x1, 10))
        display.blit(self.font3.render(str(wood), True, self.white), (wood_x2 + 2, 13))
        display.blit(self.people_image, (people_x1, 10))
        display.blit(self.font3.render(str(people), True, self.white), (people_x2 + 2, 13))


        horlogeIMG_1 = horloge.minute
        horlogeIMG_2 = horloge.seconde
        horlogeIMG_x1, horlogeIMG_x2 = 430, 425
        display.blit(self.font3.render(str(horlogeIMG_1), True, self.white), (horlogeIMG_x2 + 2, 13))
        display.blit(self.font3.render(str(":"), True, self.white), (horlogeIMG_x2 + 20, 13))
        display.blit(self.font3.render(str(horlogeIMG_2), True, self.white), (horlogeIMG_x2 + 28, 13))





