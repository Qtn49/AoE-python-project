import pygame
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.START_KEY = False
        self.title = pygame.display.set_caption("Age of Cheap")
        self.DISPLAY_W, self.DISPLAY_H = 1920,1080
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        #self.window = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0,0,0),(255,255,255)
        self.back = pygame.image.load("Logo.png").convert_alpha()
        self.main_menu = MainMenu(self)
        self.quit = QuitMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.running:
            self.check_events()
            if self.START_KEY:
                self.running = False
            self.display.blit(self.back, (0, 0))
            self.window.blit(self.display, (0, 0))
            pygame.display.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                p = pygame.mouse.get_pressed()
                if self.main_menu.startx - 70 <= pos[0] <= self.main_menu.startx + 70 and self.main_menu.starty - 10 <= pos[1] <= self.main_menu.starty + 10:
                    self.curr_menu.run_display = False
                    self.running = True
                if self.main_menu.creditsx - 70 <= pos[0] <= self.main_menu.creditsx + 70 and self.main_menu.creditsy-10 <= pos[1] <= self.main_menu.creditsy+10:
                    self.curr_menu.run_display = False
                    self.credits.display_menu()
                if self.credits.retourx - 70 <= pos[0] <= self.credits.retourx + 70 and self.credits.retoury-10 <= pos[1] <= self.credits.retoury+10:
                    # self.curr_menu.run_display = False
                    # self.main_menu.display_menu()
                    self.credits.run_display = False
                    self.curr_menu.run_display = True
                if self.main_menu.quitx-70 <= pos[0] <= self.main_menu.quitx+70 and self.main_menu.quity-10 <= pos[1] <= self.main_menu.quity+10:
                    self.running, self.curr_menu.run_display = False, False

    def draw_text(self, text, size, x, y):
        #font = pygame.font.SysFont('Corbel', size)
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
