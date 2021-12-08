from model.building.Barracks import Barracks
from model.building.House import House
from model.building.TourArcher import TourArcher
from resources.Console import *
from resources.Horloge import *
from model.Unit.Villager import *
from model.Unit.Player import *
from model.building.Forum import *
from model.building.Tree import *
from view.hud.hud import *
from resources.game_constants import *
from model.Unit.Champion import *
from model.Unit.King import *
from model.age.Age import *
from view.menu import MainMenu


def cadrillage(world):
    nb_X = WIDTH // BASE
    nb_Y = HEIGHT // BASE

    for i in range(1,nb_X+1):
        pygame.draw.line(world, (105, 105, 105), (i * BASE, 0), (i * BASE, HEIGHT), width=1)
    for i in range(1, nb_Y + 1):
        pygame.draw.line(world, (105, 105, 105), (0, i * BASE), (WIDTH, i * BASE), width=1)


def main():
    counter = 0
    vague = {10:True, 20:True, 25:True, 30:True}

    age = Age()
    cache_clk = None
    hudsprites = None
    target = [0, 0]
    world = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()
    pygame.init()

    m = MainMenu()
    m.display_menu()
    joueur1 = m.joueur

    hud = Hud()
    console = Console()

    horloge = Horloge()
    hthr = Threadatuer(target=horloge.horloge, args=())
    hthr.start()

    # if m.from_saved_game:
    #     board = board.create_map_from_file('last_game.json', joueur1)
    # else:
    #     board = board.create_map_from_file('map.png', joueur1)

    game = True
    vil0 = Villager((0, 4500), 'R', board)
    vil1 = Champion((0, 4000), 'B', board)
    board.board.append(vil0)
    board.board.append(vil1)
    king = King((4500, 500), 'B', board)
    board.board.append(king)
    tree = Tree((700, 4000), 'Neant', board)
    board.board.append(tree)


    forum = Forum((500,4500),'R',joueur1, board)
    board.board.append(forum)
    board.update_afg()

    for i in range(5):
        champ = Champion((4450, 450+i*BASE),board,'B')
        board.board.append(champ)

    for i in range(5):
        champ = Champion((4500+i*BASE, 650),board,'B')
        board.board.append(champ)

    for i in range(5):
        champ = Knight((100, 4000+i*BASE),board,'R')
        board.board.append(champ)

    for i in range(5):
        champ = Knight((600+i*2*BASE, 4050),'R',board)
        board.board.append(champ)

    for i in range(4):
        champ = Champion((4300, 300+i*3*BASE),'B',board,10)
        board.board.append(champ)

    for i in range(3):
        champ = Champion((4400+i*3*BASE, 800),'B',board,10)
        board.board.append(champ)
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
                    game=False

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
                            vil0.action[i] = False
                    vil0.thr = Threadatuer(target=vil0.fetch, args=(forum, tree, joueur1))
                    vil0.thr.start()
                if event.key == ord('e'):
                    vil7 = Villager((450, 4500), 'R')
                    board.board.append(vil7)
                if event.key == ord('z'):
                    age.changement(joueur1, forum)

                if event.key == ord('m'):
                    cthr = Threadatuer(target=console.console, args=(joueur1, horloge))
                    cthr.start()


            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clk_sprites = [s for s in board.afg if s.rect.collidepoint(pos)]

                target[0]=pos[0]+board.screenX
                target[1]=pos[1]+board.screenY

                # click_manager(clk_sprites, target)
                if cache_clk:
                    if not clk_sprites:
                        if cache_clk.type == "unit":
                            if cache_clk.thr:
                                cache_clk.thr.tuer()
                                for i in cache_clk.action:
                                    cache_clk.action[i] = False
                            cache_clk.thr = Threadatuer(target=cache_clk.move, args=(target[0], target[1])).start()
                            cache_clk = None
                    else:
                        if clk_sprites[0].type == "unit":
                            if clk_sprites[0].team != cache_clk.team:
                                if cache_clk.thr:
                                    cache_clk.thr.tuer()
                                    for i in cache_clk.action:
                                        cache_clk.action[i] = False
                                cache_clk.thr = Threadatuer(target=cache_clk.attack, args=(clk_sprites[0],)).start()
                                cache_clk = None

                if clk_sprites:
                    hudsprites = clk_sprites[0]
                    if clk_sprites[0].type == "unit":
                        cache_clk = clk_sprites[0]
                    if clk_sprites[0].job == "tree":
                        if cache_clk and cache_clk.job=="villager":
                            if cache_clk.thr:
                                cache_clk.thr.tuer()
                                for i in cache_clk.action:
                                    cache_clk.action[i] = False
                            cache_clk.thr = Threadatuer(target=cache_clk.fetch, args=(forum, clk_sprites[0], joueur1)).start()
                            cache_clk = None
                else:
                    hudsprites = None

            if event.type == pygame.KEYDOWN:
                if event.key == ord('t'):
                    m = House((legal(target[0]), legal(target[1])), 'Neant', joueur1, board)
                    board.board.append(m)
                if event.key == ord('y'):
                    b = Barracks((legal(target[0]), legal(target[1])),'R', joueur1, board)
                    board.board.append(b)
                if event.key == ord('u'):
                    a = TourArcher((legal(target[0]), legal(target[1])), 'Neant', joueur1, board)
                    board.board.append(a)

        if vague[10] and horloge.minute==10:
            for ob in board.board :
                if ob.job=="champion" and ob.vague==10:
                    ob.thr = Threadatuer(target=ob.attack, args=(forum,)).start()
            vague[10]=False

        mouse_pos = pygame.mouse.get_pos()



        if counter == 0:
            if mouse_pos[0] < 30:
                board.move_screen(-1, 0)
            if mouse_pos[1] < 30:
                board.move_screen(0, -1)
            if mouse_pos[0] > WIDTH - 30:
                board.move_screen(1, 0)
            if mouse_pos[1] > HEIGHT - 30:
                board.move_screen(0, 1)
        counter += 1

        if counter == 2:
            counter = 0

        world.fill((152, 251, 152))
        cadrillage(world)
        hud.hud_joueur(world, joueur1, horloge)

        if hudsprites:
            hud.hud_item(world, hudsprites)

        board.update_afg()
        board.afg.draw(world)

        if king.pv <= 0:
            img = pygame.image.load(os.path.join("resources/gagner.png")).convert()
            world.blit(img, (500, 500))
            pygame.display.update()
            game=False
            sleep(2)
            pygame.quit()
            hthr.tuer()
            for ob in board.board:
                if ob.thr:
                    ob.thr.tuer()
        if forum.pv <= 0:
            img = pygame.image.load(os.path.join("resources/perdu.png")).convert()
            world.blit(img, (500, 500))
            pygame.display.update()
            game=False
            sleep(2)
            pygame.quit()
            hthr.tuer()
            for ob in board.board:
                if ob.thr:
                    ob.thr.tuer()
        pygame.display.update()
        # pygame.display.flip()
        clock.tick(fps)

    pygame.quit()
    hthr.tuer()
    for ob in board.board:
        if ob.thr:
            ob.thr.tuer()

if __name__ == '__main__': main()
