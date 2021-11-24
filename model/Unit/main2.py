#!/usr/bin/env python3
"""
Import
"""
from Variables import *
from Villager import *
from threading import *
import sys

from model.Unit.Player import Player
from model.building.Forum import Forum
from model.building.Tree import Tree

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
    backdrop = pygame.image.load(os.path.join('Unit/echec.jpg'))
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    game = True

    joueur1 = Player()
    vilB = Villager((800,800),'B')  # spawn
    vilR = Villager((0,0),'R')
    tree = Tree((700,0),'Neant')
    tree2 = Tree((700, 499), 'Neant')
    forum = Forum((0,700),'Neant',joueur1)


    board.add(vilB)
    board.add(vilR)
 

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
                    for ob in board:
                        ob.action="Neant"
                    pygame.quit()
                    try:
                        sys.exit()
                    finally:
                        game = False

                if event.key == ord('s'):
                    for ob in board:
                        ob.action="Neant"
                if event.key == ord('a'):
                    Thread(target=vilR.attack, args=(vilB,)).start()
                if event.key == ord('e'):
                    Thread(target=vilB.move, args=((0,0))).start()
                if event.key == ord('z'):
                    Thread(target=vilR.defend, args=(2000,8000)).start()
                if event.key == ord('r'):
                    vilB1 = Villager((250,500),'B')
                    vilB2 = Villager((250,0),'B')
                    vilB3 = Villager((250,250),'B')
                    board.add(vilB1)
                    board.add(vilB2)
                    board.add(vilB3)
                if event.key == ord('p'):
                    m = Thread(target=vilR.fetch, args=(forum,tree,joueur1))
                    m.start()
                if event.key == ord('m'):
                    print(vilR.contenu)
                    print(joueur1.contenu)

        world.blit(backdrop, backdropbox)
        board.draw(world)
        pygame.display.flip()
        clock.tick(fps)

"""
launch
"""
if __name__=='__main__': main()
