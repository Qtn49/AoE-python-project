import json
import pygame
from model import game_constants

import matplotlib.image as mpimg

from model.Element import Element
from model.Map import Map
from model.environment.GoldMine import GoldMine
from model.environment.StoneMine import StoneMine
from model.environment.Tree import Tree
from resources import ElementsColor
import jsonpickle
import os.path


def get_map_from_json(json_file_path):
    json_file = open(json_file_path, 'r')
    json_content = json_file.read()
    json_file.close()
    return jsonpickle.decode(json_content)


def create_map_from_file(file_path):
    if os.path.isfile(json_file_path := 'resources/map/json/' + file_name[0:file_name.rfind('.') + 1] + 'json'):
        return get_map_from_json(json_file_path)

    img_script = mpimg.imread('resources/map/png/' + file_path).tolist()

    game_map = Map("resources/background/background_test.jpg")

    for y, line in enumerate(img_script):
        for x, column in enumerate(line):
            if column == ElementsColor.Color.TREE.value:
                game_map.addElement(str(x) + ', ' + str(y), Tree(image_path='resources/environment/tree.png'))
            elif column == ElementsColor.Color.GOLD_MINE.value:
                game_map.addElement(str(x) + ', ' + str(y), GoldMine(image_path='resources/environment/gold.png'))
            elif column == ElementsColor.Color.STONE_MINE.value:
                game_map.addElement(str(x) + ', ' + str(y), StoneMine(image_path='resources/environment/stone.png'))
            elif column == ElementsColor.Color.TOWN_CENTER.value:
                game_map.addElement(str(x) + ', ' + str(y), StoneMine(image_path='resources/building/town_center.webp'))

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
    # screen = pygame.display.set_mode(game_constants.GAME_DIMENSIONS)
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    running = True
    pressed = 0

    while running:
        screen.fill((0, 0, 0))
        # game_map.placeBackground(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            if event.type == pygame.KEYUP:
                pressed = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    pressed = game_constants.MOVE_RIGHT
                elif event.key == pygame.K_LEFT:
                    pressed = game_constants.MOVE_LEFT
                elif event.key == pygame.K_UP:
                    pressed = game_constants.MOVE_UP
                elif event.key == pygame.K_DOWN:
                    pressed = game_constants.MOVE_DOWN

        if pressed != 0:
            game_map.move(pressed)

        game_map.createInterface(screen)
        pygame.display.update()


