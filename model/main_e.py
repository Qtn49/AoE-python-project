
from Unit.Villager import *
from model.Map_erle import MapE
from model.Unit.Player import Player
from model.building.Forum import Forum
from model.building.Tree import Tree


def cadrillage(world):
    nb_X = WIDTH // BASE
    nb_Y = HEIGHT // BASE

    for i in range(1,nb_X+1):
        pygame.draw.line(world, (105, 105, 105), (i * BASE, 0), (i * BASE, HEIGHT), width=1)
    for i in range(1, nb_Y + 1):
        pygame.draw.line(world, (105, 105, 105), (0, i * BASE), (WIDTH, i * BASE), width=1)


def main():
    board = MapE()

    world = pygame.display.set_mode([WIDTH, HEIGHT])

    clock = pygame.time.Clock()
    pygame.init()

    game = True
    vil0 = Villager((0, 4500), 'R', board)
    vil1 = Villager((0, 4000), 'B', board)
    # vil2 = Villager((0, 3500), 'R')
    # vil3 = Villager((0, 3000), 'R')
    # vil4 = Villager((0, 2500), 'R')
    # vil5 = Villager((0, 2000), 'R')
    # vil6 = Villager((0,0),'R')
    # board.board.append(vil0)
    # board.board.append(vil1)
    # board.board.append(vil2)
    # board.board.append(vil3)
    # board.board.append(vil4)
    # board.board.append(vil5)
    # board.board.append(vil6)
    king = Villager((4500, 500),'B', board)
    # board.board.append(king)
    tree = Tree((700, 4000), 'Neant', board)
    # board.board.append(tree)

    joueur1 = Player()
    forum = Forum((500,4500),'R',joueur1, board)
    # board.board.append(forum)
    board = board.create_map_from_file('map_test.png', joueur1)
    print(board.board)
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
        world.fill((152, 251, 152))
        cadrillage(world)

        board.update_afg()
        board.afg.draw(world)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__': main()
