import pygame
from menu import *

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True,False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.MOUSE_KEY = False, False, False, False, False
        self.image_icon = pygame.image.load("Logo1.png")
        self.icon = pygame.display.set_icon(self.image_icon)
        self.title = pygame.display.set_caption("Age of Cheap")
        self.DISPLAY_W, self.DISPLAY_H = 1920,1080
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W,self.DISPLAY_H))
        #self.window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.font_name = '8-BIT WONDER.TTF'
        self.BLACK,self.WHITE = (0,0,0,),(255,255,255)
        self.back = pygame.image.load("Logo1.png").convert_alpha()
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.quit = QuitMenu(self)
        self.curr_menu = self.main_menu
        self.width = self.display.get_width()
        self.height = self.display.get_height()

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            self.display.blit(self.back,(0,0))
            self.window.blit(self.display,(0,0))
            pygame.display.update()
            self.reset_keys()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running,self.playing = False,False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                p = pygame.mouse.get_pressed()
                if self.main_menu.quitx-70 <= pos[0] <= self.main_menu.quitx+70 and self.main_menu.quity-10 <= pos[1] <= self.main_menu.quity+10:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                if self.main_menu.creditsx-70 <= pos[0] <= self.main_menu.creditsx+70 and self.main_menu.creditsy-10 <= pos[1] <= self.main_menu.creditsy+10:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False
                if self.main_menu.optionsx-70 <= pos[0] <= self.main_menu.optionsx+70 and self.main_menu.optionsy-10 <= pos[1] <= self.main_menu.optionsy+10:
                    self.running, self.playing = False, False
                    self.curr_menu.run_display = False

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.MOUSE_KEY = False, False, False, False, False

    def draw_text(self, text, size, x, y):
        #font = pygame.font.SysFont('Corbel', 35)
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text,True,self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)
