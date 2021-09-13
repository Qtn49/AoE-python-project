import json
import pygame

import matplotlib.image as mpimg

from model.Element import Element
from model.Map import Map
from model.environment.GoldMine import GoldMine
from model.environment.StoneMine import StoneMine
from model.environment.Tree import Tree
from resources import ElementsColor
import jsonpickle
import os.path

width = 1000
height = 1000


def get_map_from_json(json_file_path):
    json_file = open(json_file_path, 'r')
    json_content = json_file.read()
    json_file.close()
    return jsonpickle.decode(json_content)


def create_map_from_file(file_path):
    if os.path.isfile(json_file_path := 'resources/map/json/' + file_name[0:file_name.rfind('.') + 1] + 'json'):
        return get_map_from_json(json_file_path)

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

    create_json_file(game_map, file_name)

    return game_map


def create_json_file(game_map, file_name):
    file = open('resources/map/json/' + file_name[0:file_name.rfind('.') + 1] + 'json', 'w')
    file.write(jsonpickle.encode(game_map))
    file.close()


if __name__ == '__main__':
    file_name = 'map_test.png'
    game_map = create_map_from_file(file_name)
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    running = True

    while running:
        screen.fill((0, 255, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game_map.createInterface(screen)
        pygame.display.update()


