import pygame
from model import game_constants

from model.Map import Map

from model.game import Game

width = 1920
height = 1080

if __name__ == '__main__':
    pygame.mixer.pre_init()
    pygame.init()
    g = Game()

    if g.running:
        g.curr_menu.display_menu()
        g.game_loop()

        file_name = 'map_test.png'
        game_map = Map.create_map_from_file(file_name)

        # screen = pygame.display.set_mode(game_constants.GAME_DIMENSIONS)
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        running = True
        pressed = 0

        while running:
            screen.fill((0, 0, 0))
            # game_map.placeBackground(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.KEYUP:
                    pressed = 0
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
            pygame.display.update()


