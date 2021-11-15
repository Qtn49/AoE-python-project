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
    backdrop = pygame.image.load(os.path.join('echec.jpg'))
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    game = True


    board = pygame.sprite.Group()

    vilB = Villager((0,0),'B')  # spawn
    vilR = Villager((900,900),'R')

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

        world.blit(backdrop, backdropbox)
        board.draw(world)
        pygame.display.flip()
        clock.tick(fps)

"""
launch
"""
if __name__=='__main__': main()
