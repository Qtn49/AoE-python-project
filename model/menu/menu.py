import pygame

from model.draw.Draw import Draw


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.quitx, self.quity = self.mid_w, self.mid_h + 130
        self.texts = {}

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill(Draw.BLACK)
            self.texts['title'] = Draw.draw_text("Age of Cheap Empire", 20, self.game.DISPLAY_W / 2,
                                             self.game.DISPLAY_H / 2.5 - 20, self.game.display)
            self.texts['start_game'] = Draw.draw_text("Start a Game", 20, self.startx, self.starty, self.game.display)
            self.texts['credits'] = Draw.draw_text("Credits", 20, self.creditsx, self.creditsy, self.game.display)
            self.texts['quit'] = Draw.draw_text("Quitter", 20, self.quitx, self.quity, self.game.display)
            self.blit_screen()

            for event in pygame.event.get():
                self.check_events(event)
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run_display = False
                    self.game.running = False

    def check_events(self, event):
        pos = pygame.mouse.get_pos()

        if True in list(map(lambda el: self.texts[el].collidepoint(pos), self.texts)):
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
            # pygame.mixer.Channel(1).play(pygame.mixer.Sound('resources/sound/menu-click.wav'))
        else:
            pygame.mouse.set_cursor(pygame.cursors.arrow)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.texts['start_game'].collidepoint(pos):
                self.game.running = True
                self.run_display = False



class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.retourx, self.retoury = self.mid_w, self.mid_h + 100

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.curr_menu = self.game.main_menu
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Credits", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Made by the team of Age of Cheap", 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text("Melanie GOY", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text("Quentin GUEZ", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text("Camille HERRERO", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.game.draw_text("Erle GUILLEMOT", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            self.game.draw_text("Matheo LAVENIR", 10, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 70)
            self.game.draw_text("Retour", 20, self.retourx, self.retoury)
            self.blit_screen()


class QuitMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def quit_menu(self):
        self.game.running = False
