#!/usr/bin/env python3

"""
Import
"""
# import os
# from Villager import *
# from model.ThreadManager import *

from model.building.Barracks import *
from model.Unit.Player import Player
from model.building.Forum import Forum
from model.building.House import *
from model.Unit.King import *
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
    backdrop = pygame.image.load(os.path.join('model/Unit/echec.jpg'))
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    game = True

    joueur1 = Player()
    # vilB = Villager((800,800),'B')  # spawn
    # tree = Tree((700,0),'Neant')
    # tree2 = Tree((700, 499), 'Neant')
    print(GenID.__next__())
    king = Villager((800,100),'B')
    forum = Forum((200,800),'R',joueur1)
    vilR = forum.generateUnit(board,'villager')
    # board.add(vilB)
    board.add(vilR)
    # board.add(tree)
    # board.add(tree2)
    board.add(forum)
    board.add(king)

    """
    Loop
    """
    while game:
        if king.pv <=0:
            break
        if forum.pv <=0:
            break

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

                if event.key == ord('a'):
                    # Brk = Barracks((600,850),vilR.team, joueur1)
                    vilR.thr = Threadatuer(target=vilR.attack, args=(king,))
                    vilR.thr.start()
                    # vilR.thr = Threadatuer(target=vilR.move, args=(800,800))
                    # vilR.thr.start()
                    #
                    # Thread(target=vilR.attack, args=(vilB,)).start()
                    # vilB.thr=Threadatuer(target=vilB.move, args=(0,0))
                    # vilB.thr.start()
                if event.key == ord('e'):
                    king.thr = Threadatuer(target=king.attack, args=(forum,))
                    king.thr.start()
                    # Threadatuer(target=vilB.defend, args=((800,800))).start()
                # if event.key == ord('z'):
                #     Threadatuer(target=vilR.defend, args=(2000,8000)).start()
                # if event.key == ord('r'):
                #     vilB1 = Villager((250,500),'B')
                #     vilB2 = Villager((250,0),'B')
                #     vilB3 = Villager((250,250),'B')
                #     board.add(vilB1)
                #     board.add(vilB2)
                #     board.add(vilB3)
                # if event.key == ord('p'):
                #     m = Thread(target=vilR.fetch, args=(forum,tree,joueur1))
                #     m.start()
                # if event.key == ord('m'):
                #     print(vilR.contenu)
                #     print(joueur1.contenu)

        world.blit(backdrop, backdropbox)
        board.draw(world)
        pygame.display.flip()
        clock.tick(fps)

    for ob in board :
        if ob.thr:
            ob.thr.tuer()
    print("t'as gagné chakal")

"""
launch
"""
if __name__=='__main__': main()
