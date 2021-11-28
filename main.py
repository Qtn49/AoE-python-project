#!/usr/bin/env python3

import sys
from threading import Thread
import pygame
from model import game_constants
from model.Map import Map
from model.Unit.Player import Player
from model.Unit.Villager import Villager
from model.building.Forum import Forum
from model.building.Tree import Tree

from model.game import Game

width = 1920
height = 1080

if __name__ == '__main__':
    pygame.mixer.pre_init()
    pygame.init()
    g = Game()

    if g.running:
        # g.curr_menu.display_menu()
        # g.game_loop()

        file_name = 'map_test.png'
        # game_map = Map.create_map_from_file(file_name)
        game_map = Map()

        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # screen = pygame.display.set_mode((1000,1000))
        clock = pygame.time.Clock()

        pressed = 0

        joueur1 = Player()
        # vilB = Villager((0, 0), 'B', image_path='model/Unit/images/B_villager.png')  # spawn
        vilR = Villager((0, 0), 'R')
        tree = Tree((700, 0), 'Neant')
        tree2 = Tree((700, 499), 'Neant')
        forum = Forum((0, 700), 'Neant', joueur1)

        # game_map.addElement((0, 0), vilB)
        game_map.addElement((0, 0), vilR)
        game_map.addElement((7, 0), tree)
        game_map.addElement((7, 5), tree2)
        game_map.addElement((0, 7), forum)

        while g.running:
            screen.fill((0, 255, 0))
            # game_map.placeBackground(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    g.running = False
                    try:
                        sys.exit()
                    finally:
                        g.running = False
                if event.type == pygame.KEYUP:
                    pressed = 0
                    # if event.key == ord('s'):
                    #     for ob in game_map:
                    #         ob.action = "Neant"

                    if event.key == ord('a'):
                        Thread(target=vilR.move, args=(1000, .0)).start()
                        game_map.addElement((1000 // game_constants.BASE, 0), vilR)

                    # if event.key == ord('e'):
                    #     Thread(target=vilB.attack, args=(vilR,)).start()
                    if event.key == ord('z'):
                        Thread(target=vilR.defend, args=(2000,8000)).start()
                    if event.key == ord('r'):
                        vilB1 = Villager((2, 5), 'B')
                        vilB2 = Villager((2, 0), 'B')
                        vilB3 = Villager((2, 2), 'B')

                        game_map.addElement((2, 5), vilB1)
                        game_map.addElement((2, 0), vilB2)
                        game_map.addElement((2, 2), vilB3)
                    if event.key == ord('p'):
                        m = Thread(target=vilR.fetch, args=(forum,tree,joueur1))
                        m.start()
                    if event.key == ord('m'):
                        print(vilR.contenu)
                        print(joueur1.contenu)
                    elif event.key == ord('c'):
                        m = Thread(target=vilR.move, args=((600, 0)))
                        m.start()

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
            pygame.display.flip()
            clock.tick(game_constants.FPS)
