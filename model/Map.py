import os

import jsonpickle
from matplotlib import image as mpimg

from model.Element import Element
import pygame

from model.environment.GoldMine import GoldMine
from model.environment.StoneMine import StoneMine
from model.environment.Tree import Tree
from resources import ElementsColor


class Map:

    def __init__(self, background=None):
        self.elements = []
        self.background = background

    def addElement(self, position, element):
        self.elements[position] = element

    def removeElement(self, position):
        del self.elements[position]

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
                    game_map.addElement(Tree(x, y, image_path='resources/environment/tree.png'))
                elif column == ElementsColor.Color.GOLD_MINE.value:
                    game_map.addElement(GoldMine(x, y, image_path='resources/environment/gold.png'))
                elif column == ElementsColor.Color.STONE_MINE.value:
                    game_map.addElement(StoneMine(x, y, image_path='resources/environment/stone.png'))
                elif column == ElementsColor.Color.TOWN_CENTER.value:
                    game_map.addElement(StoneMine(x, y, image_path='resources/building/town_center.webp'))

        self.create_json_file(game_map, file_path)

        return game_map

    def create_json_file(game_map, file_name):
        file = open('resources/map/json/' + file_name[0:file_name.rfind('.') + 1] + 'json', 'w')
        file.write(jsonpickle.encode(game_map))
        file.close()

    # TODO define this method with the PyGame Library
    def createInterface(self, screen):
        for element in self.elements:
            image = pygame.image.load(element.image_path)
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (element.x * 100, element.y * 100))
