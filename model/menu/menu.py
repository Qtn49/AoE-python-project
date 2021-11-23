import pygame

from model.draw.Draw import Draw


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(Draw.DISPLAY, (0, 0))
        pygame.display.update()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.quitx, self.quity = self.mid_w, self.mid_h + 130
        self.texts = {}
        self.credits_menu = CreditsMenu(self)

    def display_menu(self):
        self.run_display = True
        selected_text = None

        while self.run_display:
            Draw.DISPLAY.fill(Draw.BLACK)
            Draw.draw_text("Age of Cheap Empire", 20, self.mid_w, self.game.DISPLAY_H / 2.5 - 20)
            self.texts['start_game'] = Draw.draw_text("Start a Game", 20, self.startx, self.starty)
            self.texts['credits'] = Draw.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.texts['quit'] = Draw.draw_text("Quitter", 20, self.quitx, self.quity)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                selected_text = next((self.texts[el] for el in self.texts if self.texts[el].collidepoint(pos)), None)

                if selected_text is not None:
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                    # pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sound/menu-click.wav'))
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)

                Draw.select_text(selected_text)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)
                    if self.texts['start_game'].collidepoint(pos):
                        self.game.running_logo = True
                        self.game.running = True
                        self.run_display = False
                    elif self.texts['quit'].collidepoint(pos):
                        self.run_display = False
                        self.game.running_logo = False
                        self.game.running = False
                    elif self.texts['credits'].collidepoint(pos):
                        self.credits_menu.run_display = True
                        self.credits_menu.display_menu()

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run_display = False
                    self.game.running_logo = False
                    self.game.running = False

            Draw.select_text(selected_text)
            self.blit_screen()


class CreditsMenu(Menu):
    def __init__(self, menu):
        Menu.__init__(self, menu.game)
        self.menu = menu
        self.retourx, self.retoury = self.mid_w, self.mid_h + 100
        self.texts = {}

    def display_menu(self):
        self.run_display = True
        selected_text = None

        while self.run_display:
            self.game.curr_menu = self.game.main_menu
            Draw.fill(Draw.BLACK)
            Draw.draw_text("Credits", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            Draw.draw_text("Made by the team of Age of Cheap", 15, self.game.DISPLAY_W / 2,
                           self.game.DISPLAY_H / 2 + 10)
            Draw.draw_text("Melanie GOY", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            Draw.draw_text("Quentin GUEZ", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
            Draw.draw_text("Camille HERRERO", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            Draw.draw_text("Erle GUILLEMOT", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            Draw.draw_text("Matheo LAVENIR", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.texts['retour'] = Draw.draw_text("Retour", 20, self.retourx, self.retoury)

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                selected_text = next((self.texts[el] for el in self.texts if self.texts[el].collidepoint(pos)), None)

                if selected_text is not None:
                    pygame.mouse.set_cursor(pygame.cursors.broken_x)
                    # pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sound/menu-click.wav'))
                else:
                    pygame.mouse.set_cursor(pygame.cursors.arrow)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if selected_text == self.texts['retour']:
                        self.run_display = False
                        self.game.running = False

                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run_display = False
                    self.game.running = False
                    self.menu.run_display = False

            Draw.select_text(selected_text)
            self.blit_screen()


class QuitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def quit_menu(self):
        self.game.running = False
