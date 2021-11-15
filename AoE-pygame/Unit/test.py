#!/usr/bin/env python3

"""
Import
"""
from Player import *
import sys

"""
Variables
"""
worldX = 500
worldY = 500
fps = 30
world = pygame.display.set_mode([worldX, worldY])

"""
Main
"""
def main() :
    """
    Setup
    """
    backdrop = pygame.image.load(os.path.join('echec.jpg'))
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    game = True

    player = Player()  # spawn player
    player.rect.x = 0  # go to x
    player.rect.y = 700  # go to y
    player_list = pygame.sprite.Group()
    player_list.add(player)
    steps = 10

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
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(-steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(steps, 0)
                if event.key == pygame.K_UP or event.key == ord('w'):
                    print('jump')

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    player.control(steps, 0)
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    player.control(-steps, 0)

        world.blit(backdrop, backdropbox)
        player.update()
        player_list.draw(world)
        pygame.display.flip()
        clock.tick(fps)

"""
launch
"""
if __name__=='__main__': main()
