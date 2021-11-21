#!/usr/bin/env python3
"""
Import
"""

from Variables import *
from Villager import *
from threading import *
from Map import *
from Player import *

import sys
#from model.building.Batiment import *
from model.building.Barracks import Barracks
from model.building.Forum import Forum
from model.building.House import House

"""
Variables
"""
world = pygame.display.set_mode([worldX, worldY])

"""
Main
"""
def main() :
    """
    Setup
    """
    print(legal(749))
    backdrop = pygame.image.load(os.path.join('Unit/echec.jpg'))
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    game = True

    quantity = 50
    type = "gold"
    board = pygame.sprite.Group()

    joueur1 = Player()
    vilB = Villager((0,0),'B')  # spawn
    vilR = Villager((900,900),'R')
    barracks = Barracks((502,502),'B',joueur1)
    b = Forum((520,202),'R')
    board.add(vilB)
    board.add(vilR)
    board.add(barracks)

    """
    Loop
    """
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    game = False

            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        game = False

                if event.key == ord('a'):
                    Thread(target=vilR.move, args=(board,100,100)).start()
                if event.key == ord('e'):
                    Thread(target=vilB.attack, args=(board,vilR)).start()
                if event.key == ord('z'):
                    Thread(target=vilR.defend, args=(board,700,700)).start()
                if event.key == ord('y'):
                    house = House((502, 502), 'B', joueur1)

                    print("Player Ressources : Gold :", joueur1.gold, " Wood : ", joueur1.wood, " Stone : ",
                          joueur1.stone, " Inhabitant : ", joueur1.inhabitant)
                    Thread(target=barracks.generateUnit, args=(board,vilR.job)).start()
                    Thread(target=barracks.stockRessources, args=(vilR.job, joueur1, type, quantity)).start()

        world.blit(backdrop, backdropbox)
        board.draw(world)
        pygame.display.flip()
        clock.tick(fps)

"""
launch
"""
if __name__=='__main__': main()
