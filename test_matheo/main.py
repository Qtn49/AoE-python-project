import pygame
import pytmx
import pyscroll

from game import Game

if __name__ == '__main__':
    # initialisation des composants de pygame
    pygame.init()

    game = Game()  # instanciation de la classe Game()
    game.run()  # on lance la classe et donc la fenêtre
