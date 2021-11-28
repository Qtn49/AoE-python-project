from Unit.Variables import *
from Unit.Villager import *


def main():

    world = pygame.display.set_mode([WIDTH, HEIGHT])
    backdrop = pygame.image.load(os.path.join('model/Unit/echec.jpg'))
    clock = pygame.time.Clock()
    pygame.init()
    backdropbox = world.get_rect()
    game = True

    vil0 = Villager((0, 4500), 'R')
    vil1 = Villager((0, 4000), 'B')
    vil2 = Villager((0, 3500), 'R')
    vil3 = Villager((0, 3000), 'R')
    vil4 = Villager((0, 2500), 'R')
    vil5 = Villager((0, 2000), 'R')
    vil6 = Villager((0,0),'R')
    board.board.append(vil0)
    board.board.append(vil1)
    board.board.append(vil2)
    board.board.append(vil3)
    board.board.append(vil4)
    board.board.append(vil5)
    board.board.append(vil6)
    board.update_afg()

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
                    vil0.thr=Threadatuer(target=vil0.attack, args=(vil1,)).start()
                if event.key == ord('e'):
                    vil7 = Villager((500, 4500), 'R')
                    board.board.append(vil7)


        board.update_afg()
        world.blit(backdrop, backdropbox)
        board.afg.draw(world)
        pygame.display.flip()
        clock.tick(fps)


if __name__ == '__main__': main()
