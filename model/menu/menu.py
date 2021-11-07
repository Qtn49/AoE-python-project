import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display = True

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.startx, self.starty = self.mid_w, self.mid_h+30
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        self.quitx, self.quity = self.mid_w, self.mid_h+130

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Age of Cheap Empire", 20, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2.5-20)
            self.game.draw_text("Start a Game", 20, self.startx, self.starty)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text("Quitter", 20, self.quitx, self.quity)
            self.blit_screen()

class CreditsMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self, game)
        self.retourx, self.retoury = self.mid_w, self.mid_h+100

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.curr_menu = self.game.main_menu
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Credits", 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Made by the team of Age of Cheap", 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
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
