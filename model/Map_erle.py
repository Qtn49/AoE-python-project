import os
from pprint import pprint

import jsonpickle
import pygame
from matplotlib import image as mpimg

from model.Unit.Champion import Champion
from model.Unit.King import King
from model.Unit.Villager import Villager
from model.building.Barracks import Barracks
from model.building.Forum import Forum
from model.building.GoldMine import GoldMine
from model.building.House import House
from model.building.Sheep import Sheep
from model.building.StoneMine import StoneMine
from model.building.TourArcher import TourArcher
from model.game_constants import *
from resources import ElementsColor

from model.building.Tree import *

class MapE():

    def __init__(self):
        self.afg = pygame.sprite.Group()
        self.board = []
        self.screenX = 0
        self.screenY = GAME_DIMENSIONS[1]*BASE-HEIGHT

    def update_afg(self):

        for ob in self.board:
            # print(self.screenX, "<= ", ob.x, "< ", self.screenX + WIDTH)
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

    @staticmethod
    def get_board_from_json(json_file_path):
        json_file = open(json_file_path, 'r')
        json_content = json_file.read()
        json_file.close()
        return jsonpickle.decode(json_content)

    def create_map_from_file(self, file_path, joueur):
        print(file_path[file_path.rfind('.'):])
        # if file_path[file_path.rfind('.'):] == "json":
        #     map = MapE()
        #     map.board = MapE.get_board_from_json(file_path)
        #     self.update_images(map.board)
        #     return map

        img_script = mpimg.imread('resources/map/png/' + file_path).tolist()

        board = MapE()

        for y, line in enumerate(img_script):
            for x, column in enumerate(line):
                if column != [1.0, 1.0, 1.0]:
                    print(column)
                if column == ElementsColor.Color.TREE.value:
                    board.board.append(Tree((x * BASE, y * BASE), None, self.board))
                elif column == ElementsColor.Color.GOLD_MINE.value:
                    board.board.append(GoldMine((x * BASE, y * BASE), None, self.board))
                elif column == ElementsColor.Color.STONE_MINE.value:
                    board.board.append(StoneMine((x * BASE, y * BASE), None, self.board))
                elif column == ElementsColor.Color.TOWN_CENTER.value:
                    board.board.append(Forum((x * BASE, y * BASE), None, joueur, self.board))
                elif column == ElementsColor.Color.KING.value:
                    board.board.append(King((x * BASE, y * BASE), "R", self.board))
                elif column == ElementsColor.Color.CHAMPION.value:
                    board.board.append(Champion((x * BASE, y * BASE), 'R', self.board))
                elif column == ElementsColor.Color.VILLAGEOIS.value:
                    board.board.append(Villager((x * BASE, y * BASE), 'B', self.board))
                elif column == ElementsColor.Color.SHEEP.value:
                    board.board.append(Sheep((x * BASE, y * BASE), None, self.board))

        # board.create_json_file(file_path[0:file_path.rfind('.')])

        return board

    def create_json_file(self, file_name):
        file = open('resources/map/json/' + file_name + '.json', 'w')
        file.write(jsonpickle.encode(self.board))
        file.close()

    def update_images(self, board):
        for el in board:
            image = None
            if type(el) is Tree:
                image = pygame.image.load(os.path.join("model/building/images/Tree.png")).convert()
            elif type(el) is GoldMine:
                image = pygame.image.load(os.path.join("model/building/images/GoldMine.png")).convert()
            elif type(el) is Forum:
                image = pygame.image.load(os.path.join("model/building/images/Towncenter.png")).convert()
            elif type(el) is StoneMine:
                image = pygame.image.load(os.path.join("model/building/images/StoneMine.png")).convert()
            elif type(el) is Villager:
                image = pygame.image.load(os.path.join("model/Unit/" + el.team + '_square.png')).convert()
            elif type(el) is TourArcher:
                image = pygame.image.load(os.path.join("model/building/images/TourArcher.png")).convert()
            elif type(el) is Barracks:
                image = pygame.image.load(os.path.join("model/building/images/Barracks.png")).convert()
            elif type(el) is House:
                image = pygame.image.load(os.path.join("model/building/images/House.png")).convert()
            if type(el) is Forum:
                image = pygame.transform.scale(image, (BASE*el.size, BASE*el.size))
            else:
                print(type(el))

            el.image = image
