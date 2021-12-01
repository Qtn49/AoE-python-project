import pygame
from model.game_constants import *

class MapE():

    def __init__(self):
        self.afg = pygame.sprite.Group()
        self.board = []
        self.screenX = 0
        self.screenY = GAME_DIMENSIONS[1]*BASE-HEIGHT

    def update_afg(self):

        for ob in self.board:
            # print(self.screenX, " <= ", ob.x, " < ", self.screenX + WIDTH)
            # print(self.screenY, " <= ", ob.y, " < ", self.screenY + WIDTH)
            if self.screenX <= ob.x < self.screenX + WIDTH and self.screenY <= ob.y < self.screenY + HEIGHT:
                ob.rect.x = ob.x - self.screenX
                ob.rect.y = ob.y - self.screenY
                self.afg.add(ob)
            elif ob in self.afg:
                self.afg.remove(ob)

    def move_screen(self, add_x, add_y):
        if self.screenX+add_x*BASE > GAME_DIMENSIONS[0]*BASE-WIDTH or self.screenX+add_x*BASE < 0:
            print("LIMITE DE H")
            return False
        if self.screenY+add_y*BASE < 0 or self.screenY+add_y*BASE > GAME_DIMENSIONS[0]*BASE-HEIGHT:
            print("LIMITE DE V")
            return False

        self.screenX += add_x*BASE
        self.screenY += add_y*BASE

        for ob in self.afg:
            ob.rect.x -= add_x*BASE
            ob.rect.y -= add_y*BASE

        self.update_afg()

        return True
