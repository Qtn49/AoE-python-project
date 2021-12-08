import pygame

from menu import *
from model.Unit.Console import Console
from model.Unit.Horloge import Horloge
from model.Unit.Villager import *
from model.Map_erle import MapE
from model.Unit.Player import Player
from model.building.Barracks import Barracks
from model.building.Forum import Forum
from model.building.House import House
from model.building.TourArcher import TourArcher
from model.building.Tree import Tree
from model.hud.hud import Hud


def cadrillage(world):
    nb_X = WIDTH // BASE
    nb_Y = HEIGHT // BASE

    for i in range(1,nb_X+1):
        pygame.draw.line(world, (105, 105, 105), (i * BASE, 0), (i * BASE, HEIGHT), width=1)
    for i in range(1, nb_Y + 1):
        pygame.draw.line(world, (105, 105, 105), (0, i * BASE), (WIDTH, i * BASE), width=1)


def main():
    pygame.init()



    m = MainMenu()
    m.display_menu()

    joueur1 = m.joueur

    cache_clk = None
    hudsprites = None
    target = [0, 0]
    # world = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    world = pygame.display.set_mode([WIDTH, HEIGHT])
    # DISPLAY_H, DISPLAY_W = pygame.display.Info().current_h, pygame.display.Info().current_w
    clock = pygame.time.Clock()
    game = m.game

    hud = Hud()

    horloge = Horloge()
    console = Console()
    hthr = Threadatuer(target=horloge.horloge, args=())

    hthr.start()
    board = MapE()

    game = True



    forum = Forum((500,4500),'R', joueur1, board)
    board = board.create_map_from_file('ma_daronne.png', joueur1)

    pygame.mouse.set_cursor(pygame.cursors.arrow)

    counter = 0

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
                if event.key == pygame.K_UP:
                    board.move_screen(0, -1)
                if event.key == pygame.K_DOWN:
                    board.move_screen(0, 1)
                if event.key == pygame.K_LEFT:
                    board.move_screen(-1, 0)
                if event.key == pygame.K_RIGHT:
                    board.move_screen(1, 0)
                if event.key == ord('a'):
                    if vil0.thr:
                        vil0.thr.tuer()
                        for i in vil0.action:
                            vil0.action[i]=False
                    vil0.thr = Threadatuer(target=vil0.fetch, args=(forum, tree, joueur1))
                    vil0.thr.start()
                if event.key == ord('e'):
                    vil7 = Villager((500, 4500), 'R', board)
                    board.board.append(vil7)
                if event.key == ord('m'):
                    print(vil0.contenu)
                    print(joueur1.contenu)
                    cthr = Threadatuer(target=console.console, args=(joueur1,horloge))
                    cthr.start()

                keys = pygame.key.get_pressed()
                if keys[pygame.K_s] and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    board.create_json_file("last_game")


            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clk_sprites = [s for s in board.afg if s.rect.collidepoint(pos)]

                target[0]=pos[0]+board.screenX
                target[1]=pos[1]+board.screenY


                if cache_clk:
                    print("MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA BIT")
                    if not clk_sprites:
                        if cache_clk.type == "unit":
                            cache_clk.thr = Threadatuer(target=cache_clk.move, args=(target[0], target[1])).start()
                            cache_clk = None
                    else:
                        if clk_sprites[0].type == "unit":
                            if clk_sprites[0].team != cache_clk.team:
                                cache_clk.thr = Threadatuer(target=cache_clk.attack, args=(clk_sprites[0],)).start()
                                cache_clk = None

                if clk_sprites:
                    hudsprites = clk_sprites[0]
                    if clk_sprites[0].type == "unit":
                        cache_clk = clk_sprites[0]
                    if clk_sprites[0].job == "tree":
                        if cache_clk and cache_clk.job=="villager":
                            print("vindiou")
                            cache_clk.thr = Threadatuer(target=cache_clk.fetch, args=(forum, clk_sprites[0], joueur1)).start()
                            cache_clk = None
                else:
                   hudsprites = None

            if event.type == pygame.KEYDOWN:
                if event.key == ord('t'):
                    m = House((target[0], target[1]), 'Neant',joueur1,board)
                    board.board.append(m)
                if event.key == ord('y'):
                    b = Barracks((target[0], target[1]), 'Neant',joueur1,board)
                    board.board.append(b)
                if event.key == ord('u'):
                    a = TourArcher((target[0], target[1]), 'Neant',joueur1, board)
                    board.board.append(a)

        mouse_pos = pygame.mouse.get_pos()

        if counter == 0:
            if mouse_pos[0] < 30:
                board.move_screen(-1, 0)
            if mouse_pos[1] < 30:
                board.move_screen(0, -1)
            if mouse_pos[0] > WIDTH-30:
                board.move_screen(1, 0)
            if mouse_pos[1] > HEIGHT-30:
                board.move_screen(0, 1)
        counter += 1

        if counter == 3:
            counter = 0

        world.fill((152, 251, 152))
        cadrillage(world)

        hud.hud_joueur(world, joueur1, horloge)

        if hudsprites:
            hud.hud_item(world,hudsprites)


        board.update_afg()
        board.afg.draw(world)
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(fps)

    for ob in board.board :
        if ob.thr:
            ob.thr.tuer()

if __name__ == '__main__': main()
