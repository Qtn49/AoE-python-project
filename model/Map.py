from model import game_constants
from model.Element import Element
import pygame


class Map:

    def __init__(self, background=None, x_shift=0, y_shift=0):
        self.elements = {}
        self.background = background
        self.x_shift = x_shift
        self.y_shift = y_shift

    def addElement(self, position, element):
        self.elements[str(position)] = element

    def set_x_shift(self, value_to_add):
        self.x_shift += value_to_add
        # if self.x_shift < 0:
        #     self.x_shift = 0
        # elif self.x_shift > game_constants.GAME_DIMENSIONS[0]:
        #     self.x_shift = game_constants.GAME_DIMENSIONS[0]

    def set_y_shift(self, value_to_add):
        self.y_shift += value_to_add
        # if self.y_shift < 0:
        #     self.y_shift = 0
        # elif self.y_shift > game_constants.GAME_DIMENSIONS[0]:
        #     self.y_shift = game_constants.GAME_DIMENSIONS[0]

    def removeElement(self, position):
        del self.elements[position]

    def getElement(self, position):
        return self.elements[position]

    def placeBackground(self, screen):
        image = pygame.image.load(self.background)
        screen.blit(image, (self.x_shift, self.y_shift))

    def createInterface(self, screen):

        image = pygame.image.load("resources/background/grass_tile.png")
        image = pygame.transform.scale(image, (300, 300))
        for i in range(5):
            for j in range(5):
                for k in range(2):
                    if k % 2 == 0:
                        screen.blit(image, (i * image.get_width(), j * image.get_height()))
                    else:
                        screen.blit(image, (i * image.get_width() + image.get_width() * 0.5,
                                            j * image.get_height() + image.get_height() * 0.5))
        # for position in self.elements:
        #     position_tuple = tuple(map(int, position.split(', ')))
        #     image = pygame.image.load(self.elements[position].image_path)
        #     image = pygame.transform.scale(image, (int(game_constants.BACKGROUND_DIMENSIONS[0] /
        #                                                game_constants.MODEL_DIMENSIONS[0]),
        #                                            int(game_constants.BACKGROUND_DIMENSIONS[1] /
        #                                                game_constants.MODEL_DIMENSIONS[1])))
        #     screen.blit(image, (position_tuple[0] * 100 + self.x_shift, position_tuple[1] * 100 + self.y_shift))

    def move(self, direction):
        if direction == game_constants.MOVE_LEFT:
            self.set_x_shift(game_constants.MOVEMENT_VALUE)
        elif direction == game_constants.MOVE_RIGHT:
            self.set_x_shift(-game_constants.MOVEMENT_VALUE)
        elif direction == game_constants.MOVE_UP:
            self.set_y_shift(game_constants.MOVEMENT_VALUE)
        elif direction == game_constants.MOVE_DOWN:
            self.set_y_shift(-game_constants.MOVEMENT_VALUE)
