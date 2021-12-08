import os

import pygame

from model.draw.Draw import Draw
from model.Unit.Player import Player
from model.Unit.Villager import Villager


class Menu():
    def __init__(self):
        self.title = pygame.display.set_caption("Age of Cheap")
        self.window = pygame.display.set_mode((1500, 800))
        self.DISPLAY_W, self.DISPLAY_H = pygame.display.Info().current_w, pygame.display.Info().current_h
        Draw.set_display(pygame.Surface((pygame.display.Info().current_w, pygame.display.Info().current_h)))
        self.back = pygame.image.load("model/menu/Logo.png").convert_alpha()
        self.back = pygame.transform.scale(self.back, (self.DISPLAY_W, self.DISPLAY_H))
        self.run_display = True
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.game = False
        self.from_saved_game = False

    def blit_screen(self):
        self.window.blit(Draw.DISPLAY, (0, 0))
        pygame.display.flip()


class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.newx, self.newy = self.mid_w, self.mid_h + 30
        self.loadx, self.loady = self.mid_w, self.mid_h + 100
        self.quitx, self.quity = self.mid_w, self.mid_h + 300
        self.retourx, self.retoury = self.mid_w, self.mid_h + 300
        self.load_menu = LoadMenu(self)
        self.joueur = Player()

    def display_menu(self):
        self.new_display = False
        self.texts = {}
        selected_text = None

        while self.run_display:
            Draw.DISPLAY.fill(Draw.BLACK)
            Draw.draw_text("Age of Cheap Empire", 60, self.mid_w, self.DISPLAY_H / 2.5 - 60)
            self.texts['new'] = Draw.draw_text("Nouvelle partie", 40, self.newx, self.newy)
            self.texts['load'] = Draw.draw_text("Charger une partie", 40, self.loadx, self.loady)
            self.texts['quit'] = Draw.draw_text("Quitter", 40, self.quitx, self.quity)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                selected_text = next((self.texts[el] for el in self.texts if self.texts[el].collidepoint(pos)), None)

                if selected_text is not None:
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)

                Draw.select_text(selected_text)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selected_text == self.texts['new']:
                        self.new_display = True
                        self.choose_para()
                    elif selected_text == self.texts['quit']:
                        self.run_display = False
                        pygame.quit()
                    elif selected_text == self.texts['load']:
                        self.load_menu.run_display = True
                        self.load_menu.display_menu()
                        #self.run_display = self.load_menu.new_display

                if event.type == pygame.QUIT:
                    self.run_display = False

            Draw.select_text(selected_text)
            self.blit_screen()

    def choose_para(self):
        self.texts = {}
        selected_text = None

        while self.new_display:
            Draw.fill(Draw.BLACK)
            Draw.draw_text("Choisissez vos paramètres de jeu", 60, self.DISPLAY_W / 2, self.DISPLAY_H / 2.5 - 60)
            Draw.draw_text("Ressources au début de la partie", 40, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 - 60)
            self.texts['pauvre'] = Draw.draw_text("Pauvre (500 de chaque)", 20, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 - 30)
            self.texts['moyen'] = Draw.draw_text("Moyen (1000 de chaque)", 20, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2)
            self.texts['riche'] = Draw.draw_text("Riche (2000 de chaque)", 20, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 30)
            Draw.draw_text("Difficulté de l'adversaire", 40, self.DISPLAY_W / 2 ,
                           self.DISPLAY_H / 2 + 90)
            self.texts['debutant'] = Draw.draw_text("Débutant", 20, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 120)
            self.texts['intermediaire'] = Draw.draw_text("Intermédiaire", 20, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 150)
            self.texts['confirme'] = Draw.draw_text("Confirmé", 20, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 180)
            self.texts['start'] = Draw.draw_text("Démarrer la partie", 40, self.DISPLAY_W / 2,
                                                    self.DISPLAY_H / 2 + 240)
            self.texts['retour'] = Draw.draw_text("Retour", 40, self.retourx, self.retoury)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                selected_text = next((self.texts[el] for el in self.texts if self.texts[el].collidepoint(pos)), None)

                if selected_text is not None:
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selected_text == self.texts['retour']:
                        self.new_display = False
                        self.texts = {}
                        selected_text = None
                    elif selected_text == self.texts['pauvre']:
                        print(self.joueur.contenu)
                        self.joueur.contenu["gold"] = 500
                        self.joueur.contenu["stone"] = 500
                        self.joueur.contenu["wood"] = 500
                        self.joueur.contenu["food"] = 500
                        self.joueur.contenu["inhabitant"] = 5
                        print(self.joueur.contenu)
                    elif selected_text == self.texts['moyen']:
                        print(self.joueur.contenu)
                        self.joueur.contenu["gold"] = 1000
                        self.joueur.contenu["stone"] = 1000
                        self.joueur.contenu["wood"] = 1000
                        self.joueur.contenu["food"] = 1000
                        self.joueur.contenu["inhabitant"] = 5
                        print(self.joueur.contenu)
                    elif selected_text == self.texts['riche']:
                        print(self.joueur.contenu)
                        self.joueur.contenu["gold"] = 2000
                        self.joueur.contenu["stone"] = 2000
                        self.joueur.contenu["wood"] = 2000
                        self.joueur.contenu["food"] = 2000
                        self.joueur.contenu["inhabitant"] = 5
                        print(self.joueur.contenu)
                    elif selected_text == self.texts['debutant']:
                        print("debutant")
                    elif selected_text == self.texts['intermediaire']:
                        print("intermediaire")
                    elif selected_text == self.texts['confirme']:
                        # self.villager.spd = 500
                        # self.villager.atk = 2
                        print("confirme")
                    elif selected_text == self.texts['start']:
                        self.game = True
                        self.run_display = False
                        self.new_display = False

                if event.type == pygame.QUIT:
                    self.run_display = False

            Draw.select_text(selected_text)
            self.blit_screen()


class LoadMenu(Menu):
    def __init__(self, menu):
        Menu.__init__(self)
        self.menu = menu
        self.retourx, self.retoury = self.mid_w, self.mid_h + 300
        self.texts = {}

    def display_menu(self):
        self.run_display = True
        selected_text = None

        while self.run_display:
            Draw.fill(Draw.BLACK)
            Draw.draw_text("Charger une partie", 60, self.DISPLAY_W / 2, self.DISPLAY_H / 2.5 - 20)
            if os.path.isfile("resources/map/json/last_game.json"):
                self.texts['last_game'] = Draw.draw_text("Last Game", 40, self.DISPLAY_W / 2,
                               self.DISPLAY_H / 2 + 10)
            else:
                Draw.draw_text("<Emplacement vide 1>", 40, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 10)
            Draw.draw_text("<Emplacement vide 2>", 40, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 60)
            Draw.draw_text("<Emplacement vide 3>", 40, self.DISPLAY_W / 2,
                           self.DISPLAY_H / 2 + 110)
            self.texts['retour'] = Draw.draw_text("Retour", 40, self.retourx, self.retoury)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                selected_text = next((self.texts[el] for el in self.texts if self.texts[el].collidepoint(pos)), None)

                if selected_text is not None:
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selected_text == self.texts['retour']:
                        self.run_display = False
                    elif selected_text == self.texts['last_game']:
                        self.game = True
                        self.from_saved_game = True
                        self.run_display = False
                        self.new_display = False

                if event.type == pygame.QUIT:
                    self.run_display = False
                    self.menu.run_display = False

            Draw.select_text(selected_text)
            self.blit_screen()
