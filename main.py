from model.Unit.Console import *
from model.Unit.Horloge import *
from model.Unit.Villager import *
from model.Unit.Player import Player
from model.building.Forum import Forum
from model.building.Tree import Tree
from model.hud.Hud import Hud


# def click_manager(sprite,pos):
#     if sprite :
#         if sprite[0].type == "unit":
#             cache_clk = sprite[0]
#     else:
#         if cache_clk.type == "unit":
#             cache_clk.thr = Threadatuer(target=cache_clk.move, args=(pos[0], pos[1]))



def cadrillage(world):
    nb_X = WIDTH // BASE
    nb_Y = HEIGHT // BASE

    for i in range(1,nb_X+1):
        pygame.draw.line(world, (105, 105, 105), (i * BASE, 0), (i * BASE, HEIGHT), width=1)
    for i in range(1, nb_Y + 1):
        pygame.draw.line(world, (105, 105, 105), (0, i * BASE), (WIDTH, i * BASE), width=1)


def main():
    cache_clk = None
    target = [0, 0]
    # world = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    world = pygame.display.set_mode([WIDTH, HEIGHT])
    # DISPLAY_H, DISPLAY_W = pygame.display.Info().current_h, pygame.display.Info().current_w
    clock = pygame.time.Clock()
    pygame.init()

    hud = Hud()

    horloge = Horloge()
    console = Console()
    hthr = Threadatuer(target=horloge.horloge, args=())
    hthr.start()

    game = True
    vil0 = Villager((0, 4500), 'R')
    vil1 = Villager((0, 4000), 'B')
    # vil2 = Villager((0, 3500), 'R')
    # vil3 = Villager((0, 3000), 'R')
    # vil4 = Villager((0, 2500), 'R')
    # vil5 = Villager((0, 2000), 'R')
    # vil6 = Villager((0,0),'R')
    board.board.append(vil0)
    board.board.append(vil1)
    # board.board.append(vil2)
    # board.board.append(vil3)
    # board.board.append(vil4)
    # board.board.append(vil5)
    # board.board.append(vil6)
    king = Villager((4500, 500),'B')
    board.board.append(king)
    tree = Tree((700, 4000), 'Neant')
    board.board.append(tree)

    joueur1 = Player()
    forum = Forum((500,4500),'R',joueur1)
    board.board.append(forum)
    board.update_afg()
    """
    Loop
    """
    while game:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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
                    vil7 = Villager((500, 4500), 'R')
                    board.board.append(vil7)
                if event.key == ord('m'):
                    print(vil0.contenu)
                    print(joueur1.contenu)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clk_sprites = [s for s in board.afg if s.rect.collidepoint(pos)]

                target[0]=pos[0]+board.screenX
                target[1]=pos[1]+board.screenY

                # click_manager(clk_sprites, target)
                if cache_clk:
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
                    if clk_sprites[0].type == "unit":
                        cache_clk = clk_sprites[0]
                    if clk_sprites[0].job == "tree":
                        if cache_clk and cache_clk.job=="villager":
                            print("vindiou")
                            cache_clk.thr = Threadatuer(target=cache_clk.fetch, args=(forum, clk_sprites[0], joueur1)).start()
                            cache_clk = None


        mouse_pos = pygame.mouse.get_pos()

        if mouse_pos[0] < 30:
            board.move_screen(-1, 0)
        if mouse_pos[1] < 30:
            board.move_screen(0, -1)
        if mouse_pos[0] > WIDTH-30:
            board.move_screen(1, 0)
        if mouse_pos[1] > HEIGHT-30:
            board.move_screen(0, 1)

        world.fill((152, 251, 152))
        cadrillage(world)
        hud.hud_joueur(world, clock, joueur1, horloge)

        board.update_afg()
        board.afg.draw(world)
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(fps)

    for ob in board.board :
        if ob.thr:
            ob.thr.tuer()

if __name__ == '__main__': main()
