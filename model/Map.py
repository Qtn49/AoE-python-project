import os

import jsonpickle
from matplotlib import image as mpimg

from model import game_constants
from model.Element import Element
import pygame

from model.environment.GoldMine import GoldMine
from model.environment.StoneMine import StoneMine
from model.environment.Tree import Tree
from resources import ElementsColor


class Map:

    def __init__(self, background=None, x_shift=0, y_shift=0):
        self.elements = {}
        self.background = background
        self.x_shift = x_shift
        self.y_shift = y_shift
        map = self
        self.map_moved = False

    @staticmethod
    def get_map():
        if map:
            return map

    def addElement(self, position, element):
        key = str(position)
        if key[0] == '(':
            key = key[1:-1]
        self.elements[key] = element

    def set_x_shift(self, value_to_add):
        for key in self.elements:
            element = self.elements[key]
            element.rect.x -= self.x_shift
            element.rect.x += self.x_shift + value_to_add
        self.x_shift += value_to_add
        # if self.x_shift < 0:
        #     self.x_shift = 0
        # elif self.x_shift > game_constants.GAME_DIMENSIONS[0]:
        #     self.x_shift = game_constants.GAME_DIMENSIONS[0]

    def set_y_shift(self, value_to_add):
        for key in self.elements:
            element = self.elements[key]
            element.rect.y -= self.y_shift
            element.rect.y += self.y_shift + value_to_add
        self.y_shift += value_to_add
        # if self.y_shift < 0:
        #     self.y_shift = 0
        # elif self.y_shift > game_constants.GAME_DIMENSIONS[0]:
        #     self.y_shift = game_constants.GAME_DIMENSIONS[0]

    def removeElement(self, position):
        key = str(position)
        if key[0] == '(':
            key = key[1:-1]
        del self.elements[key]

    def getElement(self, position):
        return self.elements[position]

    def get_map_from_json(json_file_path):
        json_file = open(json_file_path, 'r')
        json_content = json_file.read()
        json_file.close()
        return jsonpickle.decode(json_content)

    @staticmethod
    def create_map_from_file(file_path):
        if os.path.isfile(json_file_path := 'resources/map/json/' + file_path[0:file_path.rfind('.') + 1] + 'json'):
            return Map.get_map_from_json(json_file_path)

        img_script = mpimg.imread('resources/map/png/' + file_path).tolist()

        game_map = Map()

        for y, line in enumerate(img_script):
            for x, column in enumerate(line):
                if column == ElementsColor.Color.TREE.value:
                    game_map.addElement((x, y), Tree(image_path='resources/environment/tree.png'))
                elif column == ElementsColor.Color.GOLD_MINE.value:
                    game_map.addElement(GoldMine(x,y,image_path='resources/environment/gold.png'))
                elif column == ElementsColor.Color.STONE_MINE.value:
                    game_map.addElement(StoneMine(x,y,image_path='resources/environment/stone.png'))
                elif column == ElementsColor.Color.TOWN_CENTER.value:
                    game_map.addElement(StoneMine(x,y,image_path='resources/building/town_center.webp'))

        Map.create_json_file(game_map, file_path)

        return game_map

    def create_json_file(game_map, file_name):
        file = open('resources/map/json/' + file_name[0:file_name.rfind('.') + 1] + 'json', 'w')
        file.write(jsonpickle.encode(game_map))
        file.close()

    # TODO define this method with the PyGame Library

    def placeBackground(self, screen):
        image = pygame.image.load(self.background)
        screen.blit(image, (self.x_shift, self.y_shift))

    def createInterface(self, screen):

        # image = pygame.image.load("resources/background/grass_tile.png")
        # image = pygame.transform.scale(image, (300, 300))
        # for i in range(5):
        #     for j in range(5):
        #         for k in range(2):
        #             if k % 2 == 0:
        #                 screen.blit(image, (i * image.get_width(), j * image.get_height()))
        #             else:
        #                 screen.blit(image, (i * image.get_width() + image.get_width() * 0.5,
        #                                     j * image.get_height() + image.get_height() * 0.5))
        wrong_positions = []
        add_elements = {}
        for position in self.elements:
            element = self.elements[position]
            if type(position) is not tuple:
                position_tuple = tuple(map(int, position.split(', ')))
            else:
                position_tuple = position
            if element.pos != position_tuple:
                add_elements[element.pos] = element
                wrong_positions.append(position_tuple)
                position_tuple = element.pos
            # image = pygame.image.load(element.image_path)
            # image = pygame.transform.scale(image, (int(game_constants.BACKGROUND_DIMENSIONS[0] /
            #                                            game_constants.MODEL_DIMENSIONS[0]),
            #                                        int(game_constants.BACKGROUND_DIMENSIONS[1] /
            #                                            game_constants.MODEL_DIMENSIONS[1])))
            # screen.blit(image, (position_tuple[0] * game_constants.BASE + element.shift_x, position_tuple[1] * game_constants.BASE + element.shift_y))
            element.draw(screen)

        for i in wrong_positions:
            self.removeElement(i)

        for i in add_elements:
            self.addElement(i, add_elements[i])

    def move(self, direction):
        if direction == game_constants.MOVE_LEFT:
            self.set_x_shift(game_constants.MOVEMENT_VALUE)
        elif direction == game_constants.MOVE_RIGHT:
            self.set_x_shift(-game_constants.MOVEMENT_VALUE)
        elif direction == game_constants.MOVE_UP:
            self.set_y_shift(game_constants.MOVEMENT_VALUE)
        elif direction == game_constants.MOVE_DOWN:
            self.set_y_shift(-game_constants.MOVEMENT_VALUE)
