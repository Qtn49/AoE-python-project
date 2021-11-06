from model.Environment import Environment
import pygame


class Tree(Environment):

    def __init__(self, resources=10, image_path=None):
        super().__init__(resources, image_path)

