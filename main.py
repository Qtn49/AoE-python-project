import pygame

from model.Map import Map
from model.game import Game

width = 1920
height = 1080

if __name__ == '__main__':
    g = Game()

    while g.running:
        g.curr_menu.display_menu()

    file_name = 'map_test.png'
    game_map = Map.create_map_from_file(file_name)
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    while g.playing:
        screen.fill((0, 255, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.playing = False

        game_map.createInterface(screen)
        pygame.display.update()


