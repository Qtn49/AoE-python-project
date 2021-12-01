import pygame

from model.draw.Draw import Draw
from model.menu.menu import MainMenu, QuitMenu, CreditsMenu


class Game():
    def __init__(self):
        self.running = True
        self.running_logo = True
        self.title = pygame.display.set_caption("Age of Cheap")
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.DISPLAY_W, self.DISPLAY_H = pygame.display.Info().current_w, pygame.display.Info().current_h
        Draw.set_display(pygame.Surface((pygame.display.Info().current_w, pygame.display.Info().current_h)))
        self.back = pygame.image.load("model/menu/Logo.png").convert_alpha()
        self.back = pygame.transform.scale(self.back, (self.DISPLAY_W, self.DISPLAY_H))
        self.main_menu = MainMenu(self)
        self.quit = QuitMenu(self)
        # self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        alpha = 255
        while alpha > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running_logo = False
                    self.running = False
            Draw.fill(Draw.BLACK)
            self.back.set_alpha(alpha)
            alpha -= 1
            Draw.DISPLAY.blit(self.back, (0, 0))
            self.window.blit(Draw.DISPLAY, (0, 0))
            pygame.display.flip()
            pygame.display.update()

    def check_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            p = pygame.mouse.get_pressed()
            # if self.main_menu.startx - 70 <= pos[0] <= self.main_menu.startx + 70 and self.main_menu.starty - 10 <= \
            #         pos[1] <= self.main_menu.starty + 10:
            if self.main_menu.collidepoint(pos):
                self.curr_menu.run_display = False
                self.running = True
            if self.main_menu.creditsx - 70 <= pos[
                0] <= self.main_menu.creditsx + 70 and self.main_menu.creditsy - 10 <= pos[
                1] <= self.main_menu.creditsy + 10:
                self.curr_menu.run_display = False
                self.credits.display_menu()
            if self.credits.retourx - 70 <= pos[0] <= self.credits.retourx + 70 and self.credits.retoury - 10 <= \
                    pos[1] <= self.credits.retoury + 10:
                # self.curr_menu.run_display = False
                # self.main_menu.display_menu()
                self.credits.run_display = False
                self.curr_menu.run_display = True
            if self.main_menu.quitx - 70 <= pos[0] <= self.main_menu.quitx + 70 and self.main_menu.quity - 10 <= \
                    pos[1] <= self.main_menu.quity + 10:
                self.running, self.curr_menu.run_display = False, False
