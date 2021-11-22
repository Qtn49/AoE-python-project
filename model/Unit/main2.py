#!/usr/bin/env python3
"""
Import
"""
from Variables import *
from Villager import *
from threading import *
from Map import *
import sys

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


    vilB = Villager((0,0),'B')  # spawn
    vilR = Villager((0,0),'R')

    board.add(vilB)
    board.add(vilR)

    print(vilR.rect.right)
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
                    Thread(target=vilB.move, args=(750,750)).start()
                if event.key == ord('e'):
                    Thread(target=vilB.attack, args=(vilR,)).start()
                if event.key == ord('z'):
                    Thread(target=vilR.defend, args=(2000,8000)).start()
                if event.key == ord('r'):
                    vilB1 = Villager((250,500),'B')
                    vilB2 = Villager((250,0),'B')
                    vilB3 = Villager((250,250),'B')
                    board.add(vilB1)
                    board.add(vilB2)
                    board.add(vilB3)


        world.blit(backdrop, backdropbox)
        board.draw(world)
        pygame.display.flip()
        clock.tick(fps)

"""
launch
"""
if __name__=='__main__': main()
