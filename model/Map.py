from model.Element import Element
import pygame


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

    # TODO define this method with the PyGame Library
    def createInterface(self, screen):
        for element in self.elements:
            image = pygame.image.load(element.image_path)
            image = pygame.transform.scale(image, (100, 100))
            screen.blit(image, (element.x * 100, element.y * 100))
